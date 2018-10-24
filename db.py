#!/usr/bin/env python

# "Database code" for the DB Forum.

import psycopg2

DBNAME = "news"


questions = [
'What are the most popular three articles of all time?',
'Who are the most popular article authors of all time?',
'On which days did more than 1% of requests lead to errors?'
]
#define SQL query
queries = [
"""
SELECT title,
       count(*) AS num
FROM articles,
     log
WHERE log.path = CONCAT('/article/', articles.slug)
  AND status = '200 OK'
GROUP BY title,
         slug,
         PATH
ORDER BY num DESC
LIMIT 3;
""",
"""
SELECT name,
       count(*) AS num
FROM authors,
     articles,
     log
WHERE log.path = CONCAT('/article/', articles.slug)
  AND author = authors.id
  AND status = '200 OK'
GROUP BY author,
         name
ORDER BY num DESC;
""",
"SELECT day, error_rate FROM error_rates WHERE error_rate >1;"
]

def report(questions, queries):
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    for question, query in zip(questions, queries):
        c.execute(query)
        results= c.fetchall()
        print(question)
        for result in results:
            try:
                print(result[0] + ': ' + str(result[1]) + ' views')
            except TypeError:
                print(result[0].strftime("%B %d, %Y") + ': ' + str(result[1])+'%')
        print()
    return

if __name__ == '__main__':
    report(questions, queries)

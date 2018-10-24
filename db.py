#!/usr/bin/env python

# "Database code" for the DB Forum.

import psycopg2

DBNAME = "news"

#connect to DB
db = psycopg2.connect(dbname=DBNAME)
c = db.cursor()

# 1st question:
#What are the most popular three articles of all time?

#define SQL query
query1 = """
SELECT title,
       count(*) AS num
FROM articles,
     log
WHERE PATH LIKE '%'||slug||'%'
  AND status NOT LIKE '400%'
GROUP BY title,
         slug,
         PATH
ORDER BY num DESC
LIMIT 3;
"""

#execute query
c.execute(query1)
results= c.fetchall()

#print results
print('Most popular 3 articles of all time:')
for result in results:
    print(result[0]+': '+str(result[1])+' views')

print()

# 2nd question:
# Who are the most popular article authors of all time?
query2 = """
SELECT name,
       count(*) AS num
FROM authors,
     articles,
     log
WHERE PATH LIKE '%'||slug||'%'
  AND author = authors.id
  AND status NOT LIKE '400%'
GROUP BY author,
         name
ORDER BY num DESC;
"""

c.execute(query2)
results= c.fetchall()
print('Most popular articles of all time:')
for result in results:
    print(result[0]+': '+str(result[1])+' views')

print()

# 3rd question:
# On which days did more than 1% of requests
# lead to errors?
query3 = "SELECT day FROM error_rates WHERE error_rate >1;"

c.execute(query3)
results = c.fetchall()
print(r'Day where more than 1% of requets lead to errors')
print(results[0][0].strftime("%B %d, %Y"))

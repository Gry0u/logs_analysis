# Logs Analysis
Given a database containing newspaper articles as well as web server log, the aim of this project is to write a reporting tool to get some insights e.g on the articles popularity.  
## Getting Started
1. Set up virtual machine:
  - Install [Virtual Box](https://www.virtualbox.org/)
  - Install [Vagrant](https://www.vagrantup.com/)
  - [Download or clone](https://github.com/udacity/fullstack-nanodegree-vm) the virtual machine configuration files
  - Change to the `\vagrant` directory
  - Start the virtual machine: `vagrant up` then `vagrant ssh`
2. [Download newsdata database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and place it in the `\vagrant` directory.
4. Load the data: `psql -d news -f newsdata.sql`
5. Connect to the database: `psql -d news`
6. Create the views:
  - **Requests per day**  
  `create view requests_per_day as select date(time) as day, count(*) as total from log group by date(time);`
  - **Errors per day**  
  `create view errors_per_day as select date(time) as day, count(*) as total from log
  where status != '200 OK'
  group by day;`
  - **Error rates**  
  `create view error_rates as select requests_per_day.day, round(100*errors_per_day.total/requests_per_day.total,2)
  as error_rate from errors_per_day, requests_per_day where errors_per_day.day = requests_per_day.day;`
## Resources
The database uses the [PostgreSQL](https://www.postgresql.org/) system.  
The tool is written in [Python](https://www.python.org/).

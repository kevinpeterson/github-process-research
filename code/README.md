# Code

Python code for data analytics and LaTex image/table generation.

## Source Files
* __get_summary_data.py__ - Builds the data summary table (_Table 1: GitHub summary statistics_).
* __plots.py__ - Creates all graphs and tables used in the manuscript.
* __plotter.py__ - A helper class for creating Scatterplots and Histographs.
* __research.py__ - Gathers and stores data using the [GitHub REST API](https://developer.github.com/v3/).
* __research.sql__ - SQL analytical queries used to analyze data from the data gathering process.

## Prerequisites
* [MySQL](http://www.mysql.com/) version 5.5+
* [Python](https://www.python.org/) version 2.7+ with the following extra modules:
    * [matplotlib](http://matplotlib.org/)
    * [NumPy](http://www.numpy.org/)
    * [MySQL-Python](http://mysql-python.sourceforge.net/)
    * [SQLAlchemy](http://www.sqlalchemy.org/)
    * [Requests](http://docs.python-requests.org/)
* A valid GitHub user account

## Configuration
A file called ```config.py``` must be added to the ```code``` directory. This file will contain database and GitHub credentials. The structure of this file will be as follows:

```
#Database Config
db_username='your_db_username'
db_password='xxxxx'
db_host='127.0.0.1'
db_port=3306
db_database='github'

#GitHub API Config
github_username='your_github_id'
github_password='xxxxx'
```

## Gather Data
Data gathing is done by examining random repositories via the [GitHub REST API](https://developer.github.com/v3/). To start the data gathering process, execute:

    python research.py
    
__Note:__ The data gathering process may take several hours (or longer, depending on desired sample size). Modifying the ```crawl(5000)``` statement (at the bottom of ```research.py```) will control sample size.

__Note:__ Because of GitHub API [rate limiting](https://developer.github.com/v3/#rate-limiting), the data gathering process will automatically pause when the alloted number of requests has been reached. Data gathering will automatically resume after an hour of waiting to allow for re-allocation of hourly requests.
    
## Analyze Data
Once the data has been gathered, data analytics are provided via combination of SQL queries and Python [SciPy](http://www.scipy.org/) and [NumPy](http://www.numpy.org/). This process will generate all graphs, tables, and images needed by the manuscript. To start the data analytics process, execute:

    python plots.py

Data summary analytics are gathered using SQL queries, and transformed into LaTeX table format. To execute the SQL summary analytics, execute:

    python get_summary_data.py > ../paper/summary_statistics.tex

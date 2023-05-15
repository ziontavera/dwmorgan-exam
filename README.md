## DW Morgan Exam
- Running on Django and PostreSQL

## Description
1. Download the COVID-19 data set (covid_19_data.csv) from this link.
2. On startup of the web application, parse the CSV file and store the relevant data in a table
named covid_observations.
3. Create an endpoint GET /top/confirmed that returns a list of the top N countries with confirmed
cases for a given observation date where N is the maximum number of results. Include the total
number of deaths and recoveries per country in the response for that day.
4. Include a README file with instructions on how to run the application.

# Testing Tool
 - Postman

## Setup
1. Create virtual environment
 - `python -m venv {venv_name}`
    - make sure python and pip is installed

2. Install Dependencies
 - `pip install django`
 - `pip install djangorestframework`
 - `pip install psycopg2`
 
3. Run server
 - `python manage.py runserver`


## Route http://127.0.0.1:8000/top/confirmed/ (Tested with Postman)
- 1 route with 3 methods
1. Method: POST
   - Parse csv file and save to Database
3. Method: GET
   - Get data from `covid_observations` table based on parameters
   - parameters:
      - observation_date: YYYY/DD/MM
      - max_results: Int n
4. Method: DELETE
   - Delete all data in `covid_observations` table

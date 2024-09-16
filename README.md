# Data Engineering Tasks ONU

This project contains two main tasks:
1. A dbt (data build tool) task 
2. A Python script for fetching data from an API and inserting it into PostgreSQL

Create a .env file to store the credentials and edit them before running scripts

TOKEN= "xxxxxxx" 
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=xxxxx
DBT_USER=postgres
DBT_PASSWORD=mysecretpassword

Created an venv for virtual environmnet purpose 
"requirement.txt" was done via "pip freeze"

And .gitignore used which was suggesged during repo initilization

Some suggetsion for improvemnts would be 
Use "Github" for verison conrtrol and then can use "Github actions" for CI\CD,
Can use "airflow" for orchestration and all the setup could be hosted on "AWS cloud" using "Terraform" for IaC. 
These all updates could be provided on "Slack" for visisbility.


## Task 1: dbt Data Transformation

### Prerequisites
- dbt installed
- Docker installed
- Access to local postgres

### Setup
1. Clone this repository
2. Navigate to the project repo:
3. run the command "docker compose up -d"

### DBT Part
1. Run "dbt debug", To check helath of dbt
2. Run "dbt run", To build models
3. Run "dbt test", To test the model or seed 

## Task 1: API Data Transformation using Python

### Prerequisites
- Docker Installed
- requirement.txt gets loaded 
- evnironment variables fed into docker container

### Steps to run the script
- Open terminal in "de-student-task-python"
- Script takes in 1 argument i.e one date in format YYYY-MM-DD
- run the script this way "python3 fetch_n_insert.py 2020-1-1"
- This would fetch project ids updated after 2020-1-1

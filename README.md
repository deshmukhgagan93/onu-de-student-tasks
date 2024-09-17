# Data Engineering Tasks ONU

This project contains two main tasks:
1. A dbt (data build tool) task 
2. A Python script for fetching data from an API and inserting it into PostgreSQL

General Info
1. Create a .env file to store the credentials and edit them before running scripts

```env
TOKEN= "xxxxxxx"
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=xxxxx
DBT_USER=postgres
DBT_PASSWORD=xxxxx
```
2. Token could be obtained from this url "https://techport.nasa.gov/help/articles/api"
3. Create an venv for virtual environmnet purpose
4. "requirement.txt" was done via "pip freeze" 
5. And ".gitignore" used which was suggesged during repo initilization

Improvemnets Suggestion
1. Some suggetsion for improvemnts would be 
2. Use "Github" for verison conrtrol
3. And then can use "Github actions" for CI\CD
4. There are lot od "web hooks" in guthub actions, which could help the process of CI\CD
5. Can use "airflow" for orchestration and automation of script
6. And all the setup could be hosted on "AWS cloud"
7. Using "Terraform" for IaC
8. These all updates could be provided on "Slack" for visisbility


## Task 1: dbt Data Transformation

### Prerequisites
- dbt installed
- Docker installed
- Access to local postgres

### Setup
1. Clone this repository
2. Navigate to the project repo
3. Run the command
4. `docker compose up -d`
5. Open terminal in 'de-student-task-main'
6. Then enter below commands

### DBT Part
1. Run `dbt seed` to seed the data
   
2. Run `dbt debug`, To check helath of dbt
   
3. <img width="701" alt="image" src="https://github.com/user-attachments/assets/2af2be2b-4afd-4509-a8c5-bd4d69186b1b">

4. Run `dbt run`, To build models
  
6.   <img width="972" alt="image" src="https://github.com/user-attachments/assets/3fc88df5-dbb8-4c7f-b703-87df1e0bd2be">

7. Run `dbt test`, To test the model or seed
   
9. <img width="994" alt="image" src="https://github.com/user-attachments/assets/82555b28-cd6b-499f-aaea-a0643ba36826">

10. Overall database snippet
    
12. <img width="1138" alt="image" src="https://github.com/user-attachments/assets/4ff12758-8cf0-4172-86be-dd6855ddacc5">


## Task 2: API Data Transformation using Python

### Prerequisites
- Docker Installed
- requirement.txt gets loaded 
- evnironment variables fed into docker container

### Steps to run the script
- Open terminal in "de-student-task-python"
- Script takes in 1 argument i.e one date in format "YYYY-MM-DD"
- Run the script this way
- `python3 fetch_n_insert.py 2020-1-1`
- This would fetch "project ids" updated after "2020-1-1"
- This script fetches data from NASA API and has lots of empty fileds
- URL "https://techport.nasa.gov/help/articles/api"
- Above script ignores the columns which were empty
- And takes only "project_id" and "last_updated" and fed them into postgres database

# Data Engineering Student Assignment - Onu.Energy

Welcome to the data engineering student assignment for Onu.Energy! 

## Time Limit

Please take no more than **90-120 minutes** to complete this assignment. We understand that time is limited, so focus on delivering a functional and correct solution within the given timeframe. Definitely don't do ALL of the optional tasks. We want to see what you can do in a short amount of time.

## Submission

Please submit your work as a private GitHub repository. Add the following users as collaborators to the repository:

- <ds@onu.energy>
- <ar@onu.energy>

## Evaluation Criteria

- **It runs:** Does the code run without error?
- **We can read it:** Is the code well-organized, readable, and made for humans?

## Task 1 (Required, 30-120 minutes)

In this task, you will be working with a dbt (data build tool) project. Your primary objectives are to add dbt models, write tests for these models, and set up a local PostgreSQL database using Docker.

### Prerequisites

Before starting, ensure you have the following installed on your machine:

- Docker
- Python and `pip`

### DBT Tasks

1. **Set Up Local PostgreSQL Database:**
   Use [Docker](https://www.docker.com/products/docker-desktop/) to create a local postgres database. Provide instructions on how to run the database below. You will use this database to run your dbt models. Make sure the database has a user `postgres` with password `mysecretpassword` and a database `postgres`. It should be available at `http://localhost:5432`.

      ```sh
      # TODO: Add instructions for running dockerized postgres here.
      ```

2. **Install dbt:**

      ```sh
      python -m venv .venv
      source .venv/bin/activate
      pip install -r requirements.txt
      ```

3. **Modify dbt Models:**
   Navigate to the `./models/` directory and open the SQL files. You need to fill in the commented-out sections of the [models.](https://docs.getdbt.com/docs/build/sql-models)

4. **Write Tests:**
   Navigate to the `./tests/` directory and [create SQL files to test your models](https://docs.getdbt.com/docs/build/data-tests#singular-data-tests). Ensure that your tests cover the functionality of the models you modified. Optionally, how might you [add 'generic' tests to the project?](https://docs.getdbt.com/docs/build/data-tests#generic-data-tests). Optionally, can you replace some of the tests with out-of-the-box dbt functionality? 

5. **Run dbt Commands:**

   - **Seed:** Load the seed data into your PostgreSQL database.

     ```sh
     dbt seed
     ```

   - **Run:** Execute the models defined in your dbt project.

     ```sh
     dbt run
     ```

   - **Test:** Run tests on your dbt models.

     ```sh
     dbt test
     ```

6. (Optional) The password for our dev database is hardcoded into a file stored in git. This is a security risk. Fix it! Include instructions on how to run the project with better secret management below:

      ```sh
      # TODO: Add instructions for running `dbt` here
      ```

### Other Optional Enhancements

- **Additional Models & Tests:** Feel free to add more models and tests to showcase your skills.
- **CI/CD Implementation:** You can suggest or implement a CI/CD pipeline for automated testing and deployment.
- **Configure dbt:** Modify the `dbt_project.yml` file to optimize your analytics.

## Task 2 (Optional, 60-90 minutes)

This task is designed to assess your ability to pull data from a public API using Python and write the results to a storage solution of your choice:

1. Select a public API of your choice.
2. Use Python to fetch data from the chosen API.
3. Write the fetched data to a storage solution (e.g., local file, database, cloud storage).

### API Task Steps

1. **Select a Public API:**
   - Choose any public API that provides data you find interesting or relevant. Some examples include:
     - [OpenWeatherMap API](https://openweathermap.org/api)
     - [NASA API](https://api.nasa.gov/)
     - [COVID-19 API](https://covid19api.com/)
     - [GitHub API](https://docs.github.com/en/rest)

2. **Fetch Data Using Python:**
   - Write a Python script to make a request to the chosen API.
   - Parse the response and extract the necessary data.

3. **Store the Data:**
   - Choose a storage solution to store the fetched data. Examples include:
     - Writing to a local file (CSV, JSON, etc.)
     - Inserting into a database (SQLite, PostgreSQL, etc.)

4. **Document Your Work:**
   Tell us how to run your script and check the output data with code here:
   
      ```sh
      # TODO: Add instructions to run API pull and check data output here.
      ```

### Example Answer

Here is an example to help you get started:

#### Step 1: Install Required Libraries

```bash
pip install requests
```

#### Step 2: Write the Script (`fetch_data.py`)

```python
import requests
import json

def fetch_weather_data(city):
    api_key = 'your_api_key' # Maybe don't hardcode secrets in your code!
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    return response.json()

def save_to_file(data, filename='output_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    city = 'London'
    weather_data = fetch_weather_data(city)
    save_to_file(weather_data)
```

#### Step 3: Document Your Work

```sh
# 1. Install the required libraries:
pip install requests

# 2. Replace `'your_api_key'` in `fetch_data.py` with your OpenWeatherMap API key.
vi fetch_data.py # Edit the file

# 3. Run the script:
python fetch_data.py

# 4. The output will be saved to `output_data.json`.
head -n 10 output_data.json
```

---

Thank you for participating in this assignment. If you have any questions or need further assistance, feel free to reach out. Good luck!

Best regards,

The Onu.Energy Team

# PYTHON VERSION : 3.12.7
Run the following commands to set up the project:

```bash
# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # For macOS/Linux
.\venv\Scripts\activate   # For Windows

# Install Apache Airflow with constraints
pip install "apache-airflow==2.10.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.12.txt"

# Install additional dependencies from requirements.txt
pip install -r requirements.txt


# Set the AIRFLOW_HOME environment variable
export AIRFLOW_HOME=~/airflow

# Initialize the Airflow database
airflow db init

In terminal 1, start the Airflow webserver:
    airflow webserver
In terminal 2, start the Airflow scheduler:
    airflow scheduler

## create a user for airflow
airflow users create [-h] -e EMAIL -f FIRSTNAME -l LASTNAME [-p PASSWORD] -r
                     ROLE [--use-random-password] -u USERNAME
                     
### put the pipeline_airflow.py file in the dags directory or airflow





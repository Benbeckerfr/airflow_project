from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import pandas as pd
from selenium import webdriver


# Define directories
source = "source"
cible = "cible"
html_dir = "html_output"
os.makedirs(source, exist_ok=True)
os.makedirs(cible, exist_ok=True)
os.makedirs(html_dir, exist_ok=True)

# Extract data from CSV, transform to JSON, and load to output directory
def etl_csv_to_json():
    input_file = os.path.join(source, "sample_data.csv")
    output_file = os.path.join(cible, "transformed_data.json")

    df = pd.read_csv(input_file)
    df.to_json(output_file)
    


# Fetch HTML from group.bnpparibas and save to a file
def fetch_html():

    # Set up the browser in headless mode (no UI)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # Open the page
    driver.get("https://coinmarketcap.com/fr/")

    # Get the HTML after JavaScript execution
    html_content = driver.page_source

    # Save the HTML to a file
    with open("./html_output/response.html", "w") as f:
        f.write(html_content)

    # Close the browser
    driver.quit()


# Define Airflow DAG
default_args = {
    "start_date": datetime(2024, 12, 1),
}

dag = DAG(
    "simple_etl_pipeline",
    default_args=default_args,
    schedule_interval=None,
)


etl_task = PythonOperator(
    task_id="etl_csv_to_json",
    python_callable=etl_csv_to_json,
    dag=dag,
)

fetch_html_task = PythonOperator(
    task_id="fetch_html",
    python_callable=fetch_html,
    dag=dag,
)

# Set task dependencies
[etl_task, fetch_html_task]


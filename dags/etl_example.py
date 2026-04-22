from airflow import DAG
from airflow.decorators import task
from datetime import datetime


with DAG(
    dag_id="etl_pipeline",
    start_date=datetime(year=2026, month=3, day=13),
    schedule = "@weekly"
):
    @task
    def extract_data():
        print("Invoked extract_data()")
        return ["record-01","record-02","record-03"]


    @task
    def transform_data(data):
        print(f"Invoked transform_data {data}")
        transformed_data = [record.upper() for record in data]
        return transformed_data

    @task
    def load_data(data):
        print("Loading Data ")
        for record in data:
            print(f"Loaded= {record}")


    data = extract_data()
    tranformed_data = transform_data(data)
    load_data(tranformed_data)
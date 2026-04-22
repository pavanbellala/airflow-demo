from airflow import DAG
from airflow.decorators import task

from datetime import datetime

with DAG(
    dag_id="ml_pipeline",
    start_date=datetime(year=2026,month=3,day=13),
    schedule = "@weekly"
):
    @task
    def preproces_data():
        print("Preprocessing data...")

    @task
    def train_model():
        print("Training model...")

    @task
    def evaluate_model():
        print("Evaluating model")


    preproces_data() >> train_model() >> evaluate_model()


from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def preprocess_data():
    print("Preprocessing data...")


def train_model():
    print("Training model...")

def evaluate_model():
    print("Evaluating model")


with DAG(
    dag_id="ml_pipeline_02",
    start_date=datetime(year=2026,month=3,day=13),
    schedule = "@weekly"
) as dag:

    preprocess = PythonOperator(
        task_id="preprocess_task",
        python_callable=preprocess_data
    )

    train = PythonOperator(
        task_id="train_task",
        python_callable=train_model
    )

    evaluate = PythonOperator(
        task_id="evaluate_task",
        python_callable=evaluate_model
    )

    preprocess >> train >> evaluate
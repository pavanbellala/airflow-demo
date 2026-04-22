from airflow import DAG
from airflow.decorators import task
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime


with DAG(
    dag_id="failure_branch_example_taskflow",
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False
):

    @task
    def task1():
        print("Running Task 1")
        # raise Exception("Failing Task1")  # Uncomment to simulate failure


    @task
    def task2():
        print("Running Task 2")


    @task
    def task3():
        print("Running Task 3")


    @task
    def task4():
        print("Task1 failed. Running recovery task.")


    t1 = task1()
    t2 = task2()
    t3 = task3()

    t4 = task4.override(trigger_rule=TriggerRule.ONE_FAILED)()

    t1 >> t2 >> t3

    t1 >> t4
from airflow import DAG
from airflow.decorators import task
from datetime import datetime
from airflow.utils.trigger_rule import TriggerRule

with DAG(
    dag_id="failed_job",
    start_date=datetime(year=2026,month=3,day=13),
    schedule = "@weekly"
):
    @task
    def task1():
        print("Executing Task1")
        raise Exception("Failing Task 01")

    @task
    def task2():
        print("Executing Task2")

    @task
    def task3():
        print("Executing Task3")


    @task(trigger_rule=TriggerRule.ONE_FAILED)
    def task4():
        print("Executing task4")

    t1 = task1()
    t2 = task2()
    t3 = task3()
    t4 = task4()


    t1 >> t2 >> t3

    t1 >> t4
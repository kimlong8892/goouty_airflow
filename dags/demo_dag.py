from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Optional: Print sys.path to verify seeing the services folder in logs
# print(sys.path)

# Import from the custom service module
# This works because we added /opt/airflow/services to PYTHONPATH in docker-compose
from demo_service.logic import hello_from_service

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG('demo_service_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    task_call_service = PythonOperator(
        task_id='call_service_logic',
        python_callable=hello_from_service
    )

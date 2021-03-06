from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook
from airflow.utils.dates import days_ago
from datetime import timedelta
import os
import json
import pendulum

# Generate timezone
local_tz = pendulum.timezone("Asia/Tokyo")

# Default arguments
default_args = {
    'start_date': days_ago(0),
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
    'wait_for_downstream': True,
}

# Instantiate a DAG
dag = DAG(
    'create_and_load_file_to_gcs',
    default_args=default_args,
    description='create a local file and upload to google cloud storage periodically',
    schedule_interval=timedelta(minutes=1),
    catchup=False) 

# Functions used for tasks
def write_file_func(**context):
    task_id = context['task'].task_id
    execution_date = local_tz.convert(context['execution_date']).strftime('%Y-%m-%d_%H:%M:%S')
    filename = '_'.join([task_id, execution_date]) + '.json'
    filepath = '/home/airflow/gcs/data/{}'.format(filename)
    with open(filepath, 'w') as f:
        f.write(json.dumps('{"name":"demo-luzhuzhu", "age":"1"}'))
    return [filename, filepath]

def upload_file_func(**context):
    filename, filepath = context['task_instance'].xcom_pull(task_ids='create_file')
    conn = GoogleCloudStorageHook()
    target_bucket = os.getenv('UPLOAD_GCS_BUCKET_NAME')
    target_object = 'uploaded/' + filename
    conn.upload(target_bucket, target_object, filepath)

# Create tasks
create_file	= PythonOperator(task_id='create_file', python_callable=write_file_func, dag=dag, provide_context=True)
copy_file = PythonOperator(task_id='copy_file', python_callable=upload_file_func, dag=dag, provide_context=True)

# Decide the task dependencies
create_file >> copy_file

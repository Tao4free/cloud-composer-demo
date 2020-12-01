import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook
from airflow.contrib.operators.file_to_gcs import FileToGoogleCloudStorageOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import json

def write_file_func():
    file = f'/home/airflow/gcs/data/test.json'
    with open(file, 'w') as f:
        f.write(json.dumps('{"name":"aaa", "age":"10"}'))

def upload_file_func():
    conn = GoogleCloudStorageHook()
    target_bucket = 'composer_wills_xy'
    target_object = 'test.json'
    conn.upload(target_bucket, target_object, "/home/airflow/gcs/data/test.json")
    #conn.delete(source_bucket, source_object)
    #return -1

default_args = {
    'start_date': days_ago(0),
    'retries': 0,
    'retry_delay': timedelta(seconds=3)
}

dag = DAG(
    'load_gcs_file_error',
    default_args=default_args,
    description='test dag',
    #schedule_interval=None,
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=20))
    #schedule_interval=timedelta(hours=5),
    
create_file	= PythonOperator(task_id='create_file', python_callable=write_file_func, dag=dag)
copy_file	= PythonOperator(task_id='copy_file', python_callable=upload_file_func, dag=dag)

error_copy_command="gcloud logging write gcs_copy_Job_failed \
    '{\"message\": \"GCS copy job failed: unknown, check about the error.}\"}' \
     --payload-type=json  --severity=ERROR"
error_copy =BashOperator(
    task_id="error_copy",
    bash_command=error_copy_command,
    dag=dag,
    trigger_rule='one_failed'
)
    
create_file >> copy_file >> error_copy

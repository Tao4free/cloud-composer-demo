from airflow import DAG
from airflow import AirflowException
from airflow.operators.bash_operator import BashOperator
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

}

# Instantiate a DAG
dag = DAG(
    'create_and_load_file_to_gcs_failed_handling',
    default_args=default_args,
    description='move file to another folder in GCS when first upload failed',
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
    raise AirflowException
    # filename, filepath = context['task_instance'].xcom_pull(task_ids='create_file')
    # conn = GoogleCloudStorageHook()
    # target_bucket = None
    # target_object = 'uploaded/' + filename
    # conn.upload(target_bucket, target_object, filepath)

def move_error_file_func(**context):
    filename, filepath = context['ti'].xcom_pull(task_ids='create_file')
    conn = GoogleCloudStorageHook()
    target_bucket = os.getenv('UPLOAD_GCS_BUCKET_NAME')
    target_object = 'moved/' + filename
    conn.upload(target_bucket, target_object, filepath)

# Logging command
create_failed_command="gcloud logging write airflow_create_file_task_failed \
    '{\"message\": \"Failed to create the file in /home/airflow/gcs/data/: check about the error.}\"}' \
     --payload-type=json  --severity=ERROR"

# Create tasks
create_file	= PythonOperator(
        task_id='create_file',
        python_callable=write_file_func,
        dag=dag,
        provide_context=True)

create_failed_handler =BashOperator(
    task_id="create_failed_handler",
    bash_command=create_failed_command,
    dag=dag,
    trigger_rule='one_failed')

copy_file = PythonOperator(
        task_id='copy_file',
        python_callable=upload_file_func,
        dag=dag,
        provide_context=True)

copy_failed_handler = PythonOperator(
        task_id="copy_failed_handler",
        python_callable=move_error_file_func,
        dag=dag,
        provide_context=True,
        trigger_rule='one_failed')

# Decide the task dependencies
create_file >> [copy_file, create_failed_handler]
copy_file >> copy_failed_handler

# cloud-composer-demo
A demo set for Cloud Composer.
Use this demo for quick deployment of some simple tasks to understand Cloud Composer(Apache Airflow) better.

## Source Tree
```bash
cloud-composer-demo
├── 01_create_composer_environment
│   └── prepare_composer_environment.sh
├── 02_create_upload_gcs
│   ├── create_upload_gcs.py
│   ├── create_upload_gcs_failed_handling.py
│   ├── pendulum
│   ├── prepare_create_upload_gce.sh
│   └── prepare_create_upload_gce_failed_handling.sh
├── 03_trigger_reponse_dag
│   ├── gcs-dag-trigger-function
│   ├── get_client_id.py
│   ├── prepare_trigger_reponse_dag.sh
│   └── trigger_reponse_dag.py
├── 04_clean_demo_set
│   └── clean_demo_set.sh
├── LICENSE
├── README.md
├── config.sh
├── config_local.sh
└── images
    ├── create_upload_gcs.png
    ├── create_upload_gcs_failed_handling.png
    └── trigger_reponse_dag.png
```

## Instructions
This demo use the **cloud shell** to show how composer works.

### Modify the config.sh
You have to modify the config's parameter for your environment.
`xxx` need to be modified.

```bash
PROJECT_ID=xxx
LOCATION=asia-northeast1
ZONE=asia-northeast1-b
UPLOAD_GCS_BUCKET_NAME=xxx
COMPOSER_ENV_NAME=xxx
```

### Create composer environment
```bash
cd 01_create_composer_environment
bash prepare_composer_environment.sh
cd ../
```

### Prepare create upload gcs
Workflow:
Create json file and upload to google cloud storage, every minute.
The file name is based on excution datetime.

![create upload gcs](images/create_upload_gcs.png)

```bash
cd 02_create_upload_gcs
bash prepare_create_upload_gce.sh
cd ../
```

### Prepare create upload gcs failed handling
Workflow:
Create json file, if succeeded then upload to gcs, if failed send log to Cloud Logging.
If upload to gcs failed then move the file to another gcs path.

![create upload gcs failed handling](images/create_upload_gcs_failed_handling.png)

```bash
cd 02_create_upload_gcs
bash prepare_create_upload_gce_failed_handling.sh
cd ../
```

### Prepare trigger reponse dag
Workflow:
When the files are uploaded to gcs, then trigger anthoer DAG to print gcs info.
Cloud Functions will be used for sensing gcs and triggering DAG

![trigger reponse dag](images/trigger_reponse_dag.png)

```bash
cd 03_trigger_reponse_dag
bash prepare_trigger_reponse_dag.sh
cd ../
```

### Clean composer demo set resource
```bash
cd 04_clean_demo_set
bash clean_demo_set.sh
cd ../
```

## More dags examples
https://github.com/apache/airflow/tree/master/airflow/example_dags

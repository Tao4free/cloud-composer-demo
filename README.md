# cloud-composer-demo

# Source Tree
```
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
└── config.sh
```

# Instructions
This demo use the **cloud shell** to show how composer works.

## Create composer environment
```bash
cd 01_create_composer_environment
bash prepare_composer_environment.sh
cd ../
```

## Prepare create upload gcs
Workflow:
Create json file and upload to google cloud storage, every minute.
The file name is based on excution datetime.

![create upload gcs](images/create_upload_gcs.png =300x)

```bash
cd 02_create_upload_gcs
bash prepare_create_upload_gce.sh
cd ../
```

## Prepare create upload gcs failed handling
Workflow:
Create json file, if succeeded then upload to gcs, if failed send log to Cloud Logging.
If upload to gcs failed then move the file to another gcs path.

![create upload gcs failed handling](images/create_upload_gcs_failed_handling.png =300x)

```bash
cd 02_create_upload_gcs
bash prepare_create_upload_gce_failed_handling.sh
cd ../
```

## Prepare trigger reponse dag
Workflow:
When the files are uploaded to gcs, then trigger anthoer DAG to print gcs info.
Cloud Functions will be used for sensing gcs and triggering DAG

![trigger reponse dag](images/trigger_reponse_dag.png =300x)

```bash
cd 03_trigger_reponse_dag
bash prepare_trigger_reponse_dag.sh
cd ../
```

## Clean composer demo set resource
```bash
cd 04_clean_demo_set
bash clean_demo_set.sh
cd ../
```

# More dags examples
https://github.com/apache/airflow/tree/master/airflow/example_dags

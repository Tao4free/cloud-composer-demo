# cloud-composer-demo

# Source Tree
```
cloud-composer-demo/
├── 01_create_composer_environment
│   └── prepare_composer_environment.sh
├── 02_create_upload_gcs
│   ├── create_upload_gcs.py
│   ├── create_upload_gcs_failed_handling.py
│   ├── prepare_create_upload_gce.sh
│   ├── prepare_create_upload_gce_failed_handling.sh
│   └── requirements.txt
├── 03_trigger_reponse_dag
│   ├── gcs-dag-trigger-function
│   │   ├── main.py
│   │   └── requirements.txt
│   ├── get_client_id.py
│   ├── prepare_trigger_reponse_dag.sh
│   └── trigger_reponse_dag.py
├── LICENSE
├── README.md
└── config.sh
```

# How to run
This demo use the **cloud shell** to show how composer works.

## Create composer environment
```bash
cd 01_create_composer_environment
bash prepare_composer_environment.sh
cd ../
```

## Prepare create_upload_gcs
```bash
cd 02_create_upload_gcs
bash prepare_create_upload_gce.sh
cd ../
```

## Prepare create_upload_gcs_failed_handling
```bash
cd 02_create_upload_gcs
bash prepare_create_upload_gce_failed_handling.sh
cd ../
```

## Prepare trigger_reponse_dag
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

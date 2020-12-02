#!/usr/bin/env bash
source ../config.sh

webserver_res=`gcloud composer environments describe ${COMPOSER_ENV_NAME} --location ${LOCATION} | grep airflowUri`
webserver_id=${webserver_res##*' '}
client_id=`python3 get_client_id.py ${PROJECT_ID} ${LOCATION} ${COMPOSER_ENV_NAME}`

gcloud functions deploy my_function \
    --source=gcs-dag-trigger-function \
    --runtime=python38 \ 
    --trigger-bucket=${UPLOAD_GCS_BUCKET_NAME} \
    --trigger-event=google.storage.object.finalize \
    --set-env-vars=CLIENT_ID=${client_id},TENANT_PROJECT=${webserver_id}

gcloud composer environments storage dags import \
  --environment ${COMPOSER_ENV_NAME} \
  --location ${LOCATION} \
  --source trigger_reponse_dag.py

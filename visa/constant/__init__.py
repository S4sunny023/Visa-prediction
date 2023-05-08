import os
from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_time_stamp()


ROOT_DIR = os.getcwd()
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)




DATA_INGESTION_CONFIG_KEY = 'data_ingestion_config'
DATA_INGESTED_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_KEY= "ingested_data"
DATA_INGESTION_TRAIN_DATA_DIR_KEY="ingested_train_dir"
DATA_INGESTION_TEST_DATA_DIR_KEY="ingested_test_dir"
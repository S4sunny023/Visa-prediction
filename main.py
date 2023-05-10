import os, sys
from visa.constant import *
from visa.logger import logging
from visa.entity.config_entity import DataIngestionConfig
from visa.entity.artifact_entity import DataIngestionArtifact
from visa.exception import CustomException
from datetime import date
from collections import namedtuple
from visa.config.configuration import Configuration
from visa.components.data_ingestion import DataIngestion
from visa.pipeline.pipeline import Pipeline


def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        raise CustomException(e,sys)
    

if __name__ == "__main__":
    main()    
    
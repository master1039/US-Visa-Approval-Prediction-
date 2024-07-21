import sys

from us_visa.exception import USVisaException
from us_visa.constants import DATABASE_NAME,MONGODB_URL_KEY
from us_visa.logger import logging
#import certifi
import os
import pymongo

#ca = certifi.where()

class MongoDBClient:
    """
    CLASS NAME : export_data_into_feature_store
    Description : This method is used to export the dataframe from mongodb to a feature store as dataframe

    Output : connection to mongodb database
    On Failure : Raise an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f'Environment key: {mongo_db_url} is not set.')
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info(f'Connected to MongoDB database: {database_name}')
        except Exception as e:
            raise USVisaException(e,sys)
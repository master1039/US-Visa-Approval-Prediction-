# from us_visa.logger import logging
# from us_visa.exception import USVisaException
# import sys
# from us_visa.constants import *
from us_visa.pipeline.training_pipeline import TrainPipeline
# try:
#     a = 1/"10"
# except Exception as e:
#     logging.info(e)
#     raise USVisaException(e,sys) from e

pipeline = TrainPipeline()
pipeline.run_pipeline()
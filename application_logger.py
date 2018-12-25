import logging

logging_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename = "application.Log", level = logging.DEBUG, 
							format = logging_format, datefmt ='%d.%m - %H:%M')
logger = logging.getLogger()
logger.info("Program running.")

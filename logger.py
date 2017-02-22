import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s  - %(message)s')
Logger = logging.getLogger()
Logger.setLevel(logging.INFO)

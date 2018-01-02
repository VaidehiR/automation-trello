from selenium import  webdriver
import unittest
import logging
from trello_setting import DETAILED_LOG_FILE_PATH


logging.basicConfig(filename=DETAILED_LOG_FILE_PATH,
                    level=logging.INFO, format='%(asctime)s : %(message)s')
log = logging.getLogger('trello-logger # ')	


# class TrelloSetup(unittest.TestCase) :

# 	def wait_for_element(self, method, element_key, wait_time):
# 			pass
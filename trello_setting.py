from selenium import webdriver
import datetime
log_date = datetime.datetime.now().date().isoformat()
import unittest

import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




DETAILED_LOG_FILE_PATH = '/home/alqama/workspace/autotest-englishduniya/trello/trello_testcase-logger___{}__.log'.format(log_date)


logging.basicConfig(filename=DETAILED_LOG_FILE_PATH,
                    level=logging.INFO, format='%(asctime)s : %(message)s')
log = logging.getLogger('trello-logger # ')	


browser = webdriver.Chrome(executable_path='/home/alqama/workspace/chromedriver')
# browser = webdriver.Firefox(executable_path='/home/alqama/workspace/geckodriver') 

class TrelloSetUp(unittest.TestCase) :

	@classmethod
	def setUpClass(inst) :
		
		browser.get('https://trello.com/')
		log.info('login started')

		login_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".global-header-section-button")))
		login_button.click()

		email = browser.find_element_by_id('user')
		password = browser.find_element_by_id('password')
		login = browser.find_element_by_id('login')

		email.send_keys('vaidehi@zaya.in')
		password.send_keys('qazxswedc')
		login.click()
		log.info('login successful')

	@classmethod
	def tearDownClass(inst) :
		browser.quit()
import unittest
from trello_setting import browser
import pdb
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from trello_config import log


class Board(unittest.TestCase):

    def login_correct_credentials(self):

        

        email = browser.find_element_by_id('user')
        password = browser.find_element_by_id('password')
        login = browser.find_element_by_id('login')

        email.send_keys('vaidehi@zaya.in')
        password.send_keys('qazxswedc')
        login.click()

    def login_wrong_credentials(self) :
        browser.get('https://trello.com/')
        # login_button = browser.find_element_by_css_selector('.global-header-section-button')
        login_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".global-header-section-button")))
        
        login_button.click()

        email = browser.find_element_by_id('user')
        password = browser.find_element_by_id('password')
        login = browser.find_element_by_id('login')

        email.send_keys('qazxswedc')
        password.send_keys('vaidehi@zaya.in')
        login.click()

        credential_error = browser.find_element_by_css_selector(
            '.error-message')
       
        self.assertEqual(credential_error.text,
                         "Invalid password" , "not matching") 
       

        print('this is invalid password')


    def test_01(self):

        self.login_wrong_credentials()
        self.login_correct_credentials()
        
      


if __name__ == '__main__':
    unittest.main()

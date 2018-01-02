
import unittest
from trello_setting import browser
import pdb
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SignUp(unittest.TestCase):


    def test_01_precondition(self) :

        browser.get('https://trello.com/')
        
        sleep(10)
        sign_up = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".global-header-section-button.mod-primary")))
        sign_up.click()
        
    @unittest.skip('google_signUp')
    def test_02_google_signUp(self):

        browser.find_element_by_id('google').click()
        google_login = browser.find_element_by_id('identifierId')

        try:
            google_login
            print('redirected to google sign up')
            return True
            
        except NoSuchElementException:
            print('notredirected to google sign up')
            return False

    def test_03_blank_field_signUp(self):

        name = browser.find_element_by_id('name')
        email = browser.find_element_by_id('email')
        password = browser.find_element_by_id('password')
        create_ac = browser.find_element_by_id('signup')

        name.send_keys('')
        email.send_keys('vaidehi@zaya.in')
        password.send_keys('password')
        # self.precondition()

        # check create account button is enabled
        result = create_ac.is_enabled()
        self.assertFalse(result , True)

    # @unittest.skip('invalid_mail_signUP')
    def test_04_invalid_mail_signUP(self):

        name = browser.find_element_by_id('name')
        email = browser.find_element_by_id('email')
        password = browser.find_element_by_id('password')
        create_ac = browser.find_element_by_id('signup')

        name.clear()
        email.clear()
        password.clear()

        name.send_keys('vaidehi')
        email.send_keys('vaidehi.zaya@in')
        password.send_keys('password')

        email_error = browser.find_element_by_id('email-error')
        self.assertEqual(email_error.text,
                         "That doesn't look like an email address…")

    # @unittest.skip('invalid_password_signU')
    def test_05_invalid_password_signUP(self):

        name = browser.find_element_by_id('name')
        email = browser.find_element_by_id('email')
        password = browser.find_element_by_id('password')
        create_ac = browser.find_element_by_id('signup')

        name.clear()
        email.clear()
        password.clear()

        name.send_keys('vaidehi')
        email.send_keys('vaidehi.zaya@in')
        password.send_keys('pass')

        common_error = browser.find_element_by_css_selector('.error-message')
        self.assertEqual(common_error.text,
                         'Password must be at least 8 characters.')
  
    def test_06_valid_password_signUP(self):
        name = browser.find_element_by_id('name')
        email = browser.find_element_by_id('email')
        password = browser.find_element_by_id('password')
        create_ac = browser.find_element_by_id('signup')

        name.clear()
        email.clear()
        password.clear()       

        name.send_keys('vaidehi')
        email.send_keys('zayatest14@gmail.com')
        password.send_keys('password')
        # checkbox = browser.find_element_by_id('accept-tos').click()
        create_ac.click()
        pdb.set_trace()


if __name__ == '__main__':
    unittest.main()

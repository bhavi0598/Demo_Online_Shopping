import keyring
from selenium.webdriver.common.by import By
import time
import os
from datetime import datetime
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pageObjects.Universal import Universal
from Configurations.customLogger import LoggerFactory

class Loginpage:
    # Objects for Login page
    Login_link_xpath = "// *[text() = 'Log in']"
    Login_page_title_xpath = "// *[text() = 'Welcome, Please Sign In!']"
    username_xpath = "// *[ @ id = 'Email']"
    password_xpath = "// *[ @ id = 'Password']"
    login_button_xpath = "// *[ @ value" \
                         " = 'Log in']"
    Shoptitle_xpath = "// title[text() = 'Demo Web Shop']"
    searchbox_xpath = "// *[ @ id = 'small-searchterms']"
    valid_Login_xpath = "(// *[@class ='account'])[1]"
    Invalid_login_error_message_xpath= "// *[text()='The credentials provided are incorrect']"
    logut_xpath= "// *[text()='Log out']"

    @staticmethod
    def valid_login():
        logger = LoggerFactory.get_logger("valid_login")
        try:
            driver=Universal.driver
            logger.info("***************Started:Test script valid login******************")
            valid_username = keyring.get_password('universal_username', 'valid_username')
            print("username=", valid_username)
            valid_password = keyring.get_password('universal_pasword', 'valid_password')
            print("password=", valid_password)
            driver.find_element(By.XPATH, Loginpage.Login_link_xpath).click()
            Login_page_title = driver.find_element(By.XPATH, Loginpage.Login_page_title_xpath).text
            # if Login_page_title == "Welcome, Please Sign In!":
            assert "Welcome, Please Sign In!" in Login_page_title
            logger.info("***************Passed:Login page title is verified******************")
            driver.find_element(By.XPATH, Loginpage.username_xpath).clear()
            driver.find_element(By.XPATH, Loginpage.username_xpath).send_keys(valid_username)
            driver.find_element(By.XPATH, Loginpage.password_xpath).clear()
            driver.find_element(By.XPATH, Loginpage.password_xpath).send_keys(valid_password)
            driver.find_element(By.XPATH, Loginpage.login_button_xpath).click()
            valid_Login_name =driver.find_element(By.XPATH, Loginpage.valid_Login_xpath).text
            valid_user_logout = driver.find_element(By.XPATH, Loginpage.logut_xpath).text
            assert valid_Login_name == valid_username and valid_user_logout == "Log out", "Either valid user name or Logout link not verified"
            logger.info("******************Passed:Log in successful for valid user name*************************")
            logger.info("***************Completed::Passed-Test script valid login******************")
            #if valid_Login_name == valid_username and valid_user_logout == "Log out":
            #print("Log in successful for valid user name=", valid_Login_name)
            #assert True
            #else:
            #print("Log in is not successful for valid user name=", valid_Login_name)
            #assert False
        except Exception as e:
            path = Universal.take_screenshot("test_valid_login")
            logger.error(f"Test Failed: {e}")
            logger.error(f"Screenshot saved at: {path}")
            assert False, f"valid login test failed: {e}"

    @staticmethod
    def invalid_password_login():
        logger = LoggerFactory.get_logger("Invalid_login_script")
        try:
            driver = Universal.driver
            logger.info("***************Started:Test script Invalid login******************")
            driver.find_element(By.XPATH, Loginpage.Login_link_xpath).click()
            Login_page_title = driver.find_element(By.XPATH, Loginpage.Login_page_title_xpath).text
            #if Login_page_title == "Welcome, Please Sign In!":
            assert "Welcome, Please Sign In!" in Login_page_title
            logger.info("***************Passed:Login page title is verified******************")
            driver.find_element(By.XPATH, Loginpage.username_xpath).clear()
            driver.find_element(By.XPATH, Loginpage.username_xpath).send_keys("FirstName.Lastame@tricentis.test")
            driver.find_element(By.XPATH, Loginpage.password_xpath).clear()
            driver.find_element(By.XPATH, Loginpage.password_xpath).send_keys("Test@12")
            driver.find_element(By.XPATH, Loginpage.login_button_xpath).click()
            Invalid_Login_err_msg = driver.find_element(By.XPATH,Loginpage.Invalid_login_error_message_xpath).text
            assert "The credentials provided are incorrect" in Invalid_Login_err_msg
            logger.info("******************Passed:Verified error message for providing invalid password *************************")
            logger.info("***************Completed::Passed-Test script Invalid login******************")
            # if Invalid_Login_err_msg == "The credentials provided are incorrect":
            #else:
        except Exception as e:
            path = Universal.take_screenshot("test_invalid_login")
            logger.error(f" Test Failed: {e}")
            logger.error(f"Screenshot saved at: {path}")
            assert False, f"Invalid login test failed: {e}"







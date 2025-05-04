import os
import time
import xml.etree.ElementTree as ET

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from configparser import ConfigParser
from builtins import staticmethod
import configparser
import os
from datetime import datetime
import inspect
import sys
import traceback

class Universal:
    global driver
    @staticmethod
    def inittest():
        try:
            #driver=Universal.driver
            # Parse the XML file
            tree = ET.parse('C:\\PycharmProjects\\Demo_Online_Shopping\\Configurations\\settings.xml')
            root = tree.getroot()
            # Get the UAT URL from the XML file
            uat_url_element = root.find('UAT')
            if uat_url_element is not None:
                uat_url = uat_url_element.text
                print("url=",uat_url)# Get the text inside the 'UAT' tag
                if not uat_url:
                    raise ValueError("UAT URL is empty in settings.xml")
                return uat_url  # Return the UAT URL
            else:
                raise ValueError("UAT tag not found in settings.xml")
        except Exception as e:
            print(f"Error in inittest: {e}")
            return None  # Return None if there's any issue
                # You can now use uat_url to launch the application or perform further actions

    @staticmethod
    def test_launch_application():

        Universal.driver= webdriver.Chrome()
        driver=Universal.driver

        # Get the UAT URL from the settings.xml
        uat_url = Universal.inittest()
        # Open the application URL
        driver.get(uat_url)
        driver.maximize_window()
        driver.implicitly_wait(5)
        # Verify the page title
        expected_title = "Demo Web Shop"
        actual_title = driver.title
        if actual_title == expected_title:
            print("Title is verified")
        else:
            print("Title is not verified")
            error_message=traceback.format_exc()
        return driver
    @staticmethod
    def close_driver():
        driver=Universal.driver
        driver.close()

    @staticmethod
    def take_screenshot(test_name):
        driver=Universal.driver
        current_date = datetime.now().strftime("%Y-%m-%d")
        screenshots_dir = 'C:\\PycharmProjects\\Demo_Online_Shopping\\Screenshots\\'+current_date+'\\'+test_name
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        path = os.path.join(screenshots_dir, f"{test_name}.png")
        driver.save_screenshot(path)
        return path

    @staticmethod
    def get_object_locator(section, key):
        config = configparser.ConfigParser()
        config.read('C:\\PycharmProjects\\Demo_Online_Shopping\\Objects\\objectlocators.ini')
        return config.get(section, key)



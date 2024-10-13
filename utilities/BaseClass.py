import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import inspect
import logging
import os
from datetime import datetime

@pytest.mark.usefixtures("setup")
class BaseClass:
    
    script_path = os.path.abspath(__file__)
    folder_name = os.path.dirname(os.path.dirname(script_path))

    # Set the download path to a subfolder within the current script's folder
    log_path = os.path.join(folder_name, "logs/logfile.log")
    
    def explicit_wait(self, locator, text, time=10 ):
        wait = WebDriverWait(self.driver,time)
        return wait.until(EC.presence_of_element_located((locator, text)))
        
    def iframe_explicit_wait(self, locator, text, time=10 ):
        wait = WebDriverWait(self.driver,time)
        return wait.until(EC.presence_of_element_located((locator, text)))
        
    def select_dropdown(self, locator, text):
        dropdown = Select(self.driver.find_element(*locator))
        dropdown.select_by_visible_text(text)
        
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(BaseClass.log_path)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
    
    def wait_for_element_to_be_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        
    def wait_for_element_to_be_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_and_click(self, locator, timeout=10):
        element = self.wait_for_element_to_be_visible(locator, timeout)
        element.click()

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def capture_screenshot(self, name="screenshot"):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.driver.save_screenshot(f"{name}_{timestamp}.png")

    def accept_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def is_element_present(self, locator):
        try: 
            if locator:
                # self.driver.find_element(*locator)
                print("present: ", True)
                return True
            else:
                return False
        except NoSuchElementException as e:
            print("Error ", e)
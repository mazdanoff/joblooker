from abc import ABCMeta

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIMEOUT = 20


class PageObject(metaclass=ABCMeta):

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def is_element_located_present(self, how, what):
        try:
            return bool(self.driver.find_element(how, what))
        except NoSuchElementException:
            return False

    def is_element_located_displayed(self, how, what):
        try:
            return self.driver.find_element(how, what).is_displayed()
        except NoSuchElementException:
            return False

    def wait_for_presence_of_element_located(self, how, what, timeout=0):
        timeout = timeout or WAIT_TIMEOUT
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

    def wait_for_visibility_of_element_located(self, how, what, timeout=0):
        timeout = timeout or WAIT_TIMEOUT
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False

    def wait_for_ajax(self, timeout=0):
        timeout = timeout or WAIT_TIMEOUT
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(lambda dr: dr.execute_script("return jQuery.active == 0"))
        except TimeoutException:
            return False

    def wait_for_javascript(self, timeout=0):
        timeout = timeout or WAIT_TIMEOUT
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(lambda dr: dr.execute_script('return document.readyState === "complete"'))
        except TimeoutException:
            return False

from selenium.webdriver.remote.webelement import WebElement

from page_objects.abstract.page_object import PageObject


class FrameObject(PageObject):

    def __init__(self, driver, frame: WebElement):
        super().__init__(driver)
        self._frame = frame

    def __enter__(self):
        self.driver.switch_to.frame(self._frame)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.switch_to.parent_frame()

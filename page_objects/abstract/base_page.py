from abc import ABCMeta

from page_objects.abstract.page_object import PageObject


class BasePage(PageObject, metaclass=ABCMeta):

    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url

    def open(self):
        self.driver.get(self.url)
        return self

    def get_page_source(self):
        return self.driver.page_source

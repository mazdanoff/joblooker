from selenium.webdriver.common.by import By
from selenium_datatable import DataTable, Column


class JoobleOfferList(DataTable):

    def __init__(self, how: str, what: str):
        super().__init__(how, what)
        self.index_fix = 2

    def __getitem__(self, index):
        return super().__getitem__(index+self.index_fix)

    def __next__(self):
        if self.current_row > len(self)+self.index_fix:
            self.__current_row = 0
            raise StopIteration()
        item = self.__getitem__(self.__current_row)
        self.__current_row += 1
        return item

    rows_locator = (By.CSS_SELECTOR, "div.vacancy_wrapper.vacancy-js.vacancy_wrapper-js")
    name = Column(By.CSS_SELECTOR,
                  "div.vacancy_wrapper.vacancy-js.vacancy_wrapper-js:nth-of-type({row}) .position")
    location = Column(By.CSS_SELECTOR,
                      "div.vacancy_wrapper.vacancy-js.vacancy_wrapper-js:nth-of-type({row}) span.serp_location__region")
    link = Column(By.CSS_SELECTOR,
                  "div.vacancy_wrapper.vacancy-js.vacancy_wrapper-js:nth-of-type({row}) a.link-position.job-marker-js")

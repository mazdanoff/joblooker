from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium_datatable import DataTable, Column


class IndeedOfferList(DataTable):

    def __init__(self, how: str, what: str):
        super().__init__(how, what)
        self.index_fix = 3

    def __getitem__(self, index):
        try:
            _ = self._table.find_element_by_css_selector(".jobsearch-SerpJobCard.unifiedRow.row.result.clickcard:nth-of-type(5)")
            return super().__getitem__(2 * index + self.index_fix + 1)
        except NoSuchElementException:
            return super().__getitem__(2*index + self.index_fix)

    def __next__(self):
        if self.current_row > 2*len(self) + self.index_fix:
            self.__current_row = 0
            raise StopIteration()
        item = self.__getitem__(self.__current_row)
        self.__current_row += 1
        return item

    rows_locator = (By.CSS_SELECTOR, ".jobsearch-SerpJobCard.unifiedRow.row.result.clickcard")
    name = Column(By.CSS_SELECTOR,
                  ".jobsearch-SerpJobCard.unifiedRow.row.result.clickcard:nth-of-type({row}) a.jobtitle.turnstileLink")
    location = Column(By.CSS_SELECTOR,
                      ".jobsearch-SerpJobCard.unifiedRow.row.result.clickcard:nth-of-type({row}) .location.accessible-contrast-color-location")
    link = Column(By.CSS_SELECTOR,
                  ".jobsearch-SerpJobCard.unifiedRow.row.result.clickcard:nth-of-type({row}) a.jobtitle.turnstileLink")
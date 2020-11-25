from selenium.webdriver.common.by import By
from selenium_datatable import DataTable, Column


class AplikujPLOfferList(DataTable):

    rows_locator = (By.CSS_SELECTOR, "div.row")
    name = Column(By.CSS_SELECTOR, "div.row:nth-of-type({row}) a.st")
    location = Column(By.CSS_SELECTOR, "div.row:nth-of-type({row}) span.loc > span")
    link = Column(By.CSS_SELECTOR, "div.row:nth-of-type({row}) a.st")

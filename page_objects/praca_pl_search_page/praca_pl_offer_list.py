from selenium.webdriver.common.by import By
from selenium_datatable import DataTable, Column


class PracaPLOfferList(DataTable):

    rows_locator = (By.CSS_SELECTOR, "li.listing__item")
    name = Column(By.CSS_SELECTOR, "li.listing__item:nth-of-type({row}) a.listing__offer-title.job-id")
    location = Column(By.CSS_SELECTOR, "li.listing__item:nth-of-type({row}) div.listing__location")
    link = Column(By.CSS_SELECTOR, "li.listing__item:nth-of-type({row}) a.listing__offer-title.job-id")

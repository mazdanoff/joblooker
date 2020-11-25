from selenium.webdriver.common.by import By
from selenium_datatable import DataTable, Column


class GumtreeOfferList(DataTable):

    rows_locator = (By.CSS_SELECTOR, "div.tileV1")
    name = Column(By.CSS_SELECTOR, "div.tileV1:nth-of-type({row}) > div.title > a.href-link.tile-title-text")
    location = Column(By.CSS_SELECTOR, "div.tileV1:nth-of-type({row}) > div.category-location > span")
    link = Column(By.CSS_SELECTOR, "div.tileV1:nth-of-type({row}) > div.title > a.href-link.tile-title-text")
    date = Column(By.CSS_SELECTOR, "div.tileV1:nth-of-type({row}) > div.info > div.creation-date > span")

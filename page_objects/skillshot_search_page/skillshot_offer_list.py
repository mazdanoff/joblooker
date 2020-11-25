from selenium.webdriver.common.by import By
from selenium_datatable import DataTable, Column


class SkillshotOfferList(DataTable):

    rows_locator = (By.TAG_NAME, "tr")
    name = Column(By.CSS_SELECTOR, "tr:nth-of-type({row}) td:nth-of-type(2) > a")
    location = Column(By.CSS_SELECTOR, "tr:nth-of-type({row}) td:nth-of-type(2)")
    link = Column(By.CSS_SELECTOR, "tr:nth-of-type({row}) td:nth-of-type(2) > a")
    date = Column(By.CSS_SELECTOR, "tr:nth-of-type({row}) td:nth-of-type(3)")

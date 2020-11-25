from selenium.webdriver.common.by import By
from selenium_datatable import DataTable, Column


class OLXOfferList(DataTable):

    rows_locator = (By.CSS_SELECTOR, "tbody > tr")
    name = Column(By.CSS_SELECTOR, "tbody > tr:nth-of-type({row}) strong")
    location = Column(By.CSS_SELECTOR, "tbody > tr:nth-of-type({row}) td.bottom-cell small:nth-of-type(1)")
    link = Column(By.XPATH, "//tbody/tr[@class='wrap']//strong/parent::a")
    date = Column(By.CSS_SELECTOR, "tbody > tr:nth-of-type({row}) td.bottom-cell small:nth-of-type(2)")

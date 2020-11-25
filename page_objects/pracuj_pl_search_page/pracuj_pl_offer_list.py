from selenium.webdriver.common.by import By
from selenium_datatable import DataTable, Column


class PracujPLOfferList(DataTable):

    rows_locator = (By.CSS_SELECTOR, "li.results__list-container-item")
    name = Column(By.CSS_SELECTOR, "li:nth-of-type({row}) h3.offer-details__title > .offer-details__title-link")
    location = Column(By.CSS_SELECTOR, "li:nth-of-type({row}) li.offer-labels__item.offer-labels__item--location")
    link = Column(By.CSS_SELECTOR, "li:nth-of-type({row}) a.offer-details__title-link")
    region_link = Column(By.CSS_SELECTOR, "li:nth-of-type({row}) a.offer-regions__label")

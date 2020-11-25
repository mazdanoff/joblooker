from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from page_elements import Element
from selenium.webdriver.support.wait import WebDriverWait

from ..base_search_page import BaseSearchPage
from .jooble_offer_list import JoobleOfferList


class JoobleSearchPageLocators:
    OFFER_LIST = (By.ID, "jobs_list__page")
    DECLINE_BUTTON = (By.CSS_SELECTOR, "span.button.disagree_button.disagree_button-js")
    ACTIVE_DATE_FILTER = (By.CSS_SELECTOR, "ul.newitem-list.date-filter-js span.newitem-list_item__active")
    TODAY_DATE_FILTER = (By.XPATH, "//li[@class='newitem-list_item']/a[contains(text(), 'zisiaj')]")


class JoobleSearchPage(BaseSearchPage):

    offer_list = JoobleOfferList(*JoobleSearchPageLocators.OFFER_LIST)
    decline_button = Element(*JoobleSearchPageLocators.DECLINE_BUTTON)  # I don't need a job :)
    active_date_filter = Element(*JoobleSearchPageLocators.ACTIVE_DATE_FILTER)  # .text must be "Dzisiaj"
    today_date_filter = Element(*JoobleSearchPageLocators.TODAY_DATE_FILTER)
    
    def handle_decline_button(self):
        if self.is_element_located_present(*JoobleSearchPageLocators.DECLINE_BUTTON):
            self.decline_button.click()

    def wait_for_today_filter_to_activate(self):
        wait = WebDriverWait(self.driver, timeout=10)
        try:
            wait.until(lambda driver_: driver_.find_element(*JoobleSearchPageLocators.ACTIVE_DATE_FILTER).text == "Dzisiaj")
        except TimeoutException:
            return False
        return True

    def offer_list_info(self):
        if (self.is_element_located_present(*JoobleSearchPageLocators.ACTIVE_DATE_FILTER)
                and self.active_date_filter.text != "Dzisiaj"):
            self.today_date_filter.click()
            self.wait_for_today_filter_to_activate()
        info_list = list()
        for offer in self.offer_list:
            info = [offer.name.text,
                    offer.location.text,
                    offer.link.get_attribute("href")]
            info_list.append(tuple(info))
        return info_list

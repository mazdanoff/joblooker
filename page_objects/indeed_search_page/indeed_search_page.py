from selenium.webdriver.common.by import By

from ..base_search_page import BaseSearchPage
from .indeed_offer_list import IndeedOfferList


class IndeedSearchPageLocators:
    OFFER_LIST = (By.CSS_SELECTOR, "td#resultsCol")


class IndeedSearchPage(BaseSearchPage):

    offer_list = IndeedOfferList(*IndeedSearchPageLocators.OFFER_LIST)

    def offer_list_info(self):
        info_list = list()
        for offer in self.offer_list:
            info = [offer.name.text,
                    offer.location.text,
                    offer.link.get_attribute("href")]
            info_list.append(tuple(info))
        return info_list

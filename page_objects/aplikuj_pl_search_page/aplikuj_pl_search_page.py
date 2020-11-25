from selenium.webdriver.common.by import By

from ..base_search_page import BaseSearchPage
from .aplikuj_pl_offer_list import AplikujPLOfferList


class AplikujPLSearchPageLocators:
    OFFER_LIST = (By.CLASS_NAME, "oferty")


class AplikujPLSearchPage(BaseSearchPage):

    offer_list = AplikujPLOfferList(*AplikujPLSearchPageLocators.OFFER_LIST)

    def offer_list_info(self):
        info_list = list()
        for offer in self.offer_list:
            info = [offer.name.text,
                    offer.location.text,
                    offer.link.get_attribute("href")]
            info_list.append(tuple(info))
        return info_list

from selenium.webdriver.common.by import By

from ..base_search_page import BaseSearchPage
from .praca_pl_offer_list import PracaPLOfferList


class PracaPLSearchPageLocators:
    OFFER_LIST = (By.CSS_SELECTOR, ".listing.listing--with-blocks")


class PracaPLSearchPage(BaseSearchPage):

    offer_list = PracaPLOfferList(*PracaPLSearchPageLocators.OFFER_LIST)

    def offer_list_info(self):
        info_list = list()
        if not self.is_element_located_present(*PracaPLSearchPageLocators.OFFER_LIST):
            return info_list
        for offer in self.offer_list:
            try:
                info = [offer.name.text,
                        offer.location.text,
                        offer.link.get_attribute("href")]
            except AttributeError:
                continue
            info_list.append(tuple(info))
        return info_list

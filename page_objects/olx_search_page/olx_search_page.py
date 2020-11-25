from selenium.webdriver.common.by import By

from ..base_search_page import BaseSearchPage
from .olx_offer_list import OLXOfferList


class OLXSearchPageLocators:
    OFFER_LIST = (By.CSS_SELECTOR, "table#offers_table[summary='Ogłoszenia']")
    TOP_OFFER_LIST = (By.CSS_SELECTOR, "table.fixed.offers.breakword.offers--top.redesigned")


class OLXSearchPage(BaseSearchPage):

    offer_list = OLXOfferList(*OLXSearchPageLocators.OFFER_LIST)
    top_offer_list = OLXOfferList(*OLXSearchPageLocators.TOP_OFFER_LIST)

    def offer_list_info(self):
        info_list = list()
        info_list.extend(self.get_regular_offers())
        info_list.extend(self.get_top_offers())
        return info_list

    def get_regular_offers(self):
        info_list = list()
        if not self.is_element_located_present(*OLXSearchPageLocators.OFFER_LIST):
            return info_list
        for offer in self.offer_list:
            if not offer.name or not offer.date or "dzisiaj" not in offer.date.text:
                continue
            info = [offer.name.text,
                    offer.location.text,
                    offer.link.get_attribute("href")]
            info_list.append(tuple(info))
        return info_list

    def get_top_offers(self):
        info_list = list()
        if not self.is_element_located_present(*OLXSearchPageLocators.TOP_OFFER_LIST):
            return info_list
        for offer in self.top_offer_list:
            if not offer.name or not offer.date or "dzisiaj" not in offer.date.text:
                continue
            info = [offer.name.text,
                    offer.location.text,
                    offer.link.get_attribute("href")]
            info_list.append(tuple(info))
        return info_list

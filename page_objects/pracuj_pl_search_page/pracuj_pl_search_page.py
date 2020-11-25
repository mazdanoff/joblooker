from selenium.webdriver.common.by import By

from ..base_search_page import BaseSearchPage
from .pracuj_pl_offer_list import PracujPLOfferList


class PracujPLSearchPageLocators:
    OFFER_LIST = (By.CSS_SELECTOR, "div#results ul.results__list-container")


class PracujPLSearchPage(BaseSearchPage):

    offer_list = PracujPLOfferList(*PracujPLSearchPageLocators.OFFER_LIST)

    def offer_list_info(self):
        info_list = list()
        for offer in self.offer_list:
            try:
                info = [offer.name.text, ]
            except AttributeError:
                continue

            if "lokalizacji" not in offer.location.text:
                info.append(offer.location.text)
            else:
                info.append("zdalnie")

            if offer.link:
                info.append(offer.link.get_attribute("href"))
            else:
                info.append(offer.region_link.get_attribute("href"))

            info_list.append(tuple(info))
        return info_list

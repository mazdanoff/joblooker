from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from page_objects.base_search_page import BaseSearchPage
from page_objects.gumtree_search_page.gumtree_offer_list import GumtreeOfferList


class GumtreeSearchPageLocators:
    OFFER_LIST = (By.CSS_SELECTOR, "div.results.list-view > div.view")


class GumtreeSearchPage(BaseSearchPage):

    offer_list = GumtreeOfferList(*GumtreeSearchPageLocators.OFFER_LIST)

    def offer_list_info(self):
        info_list = list()
        try:
            for offer in self.offer_list:
                if "minut" not in offer.date.text or "godzin" not in offer.date.text:
                    continue
                info = [offer.name.text,
                        offer.location.text,
                        offer.link.get_attribute("href")]
                info_list.append(tuple(info))
            return info_list
        except NoSuchElementException:
            return []

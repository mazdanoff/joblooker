from selenium.webdriver.common.by import By

from utils import today
from ..base_search_page import BaseSearchPage
from .skillshot_offer_list import SkillshotOfferList


class SkillshotSearchPageLocators:
    OFFER_LIST = (By.CSS_SELECTOR, "table.table-striped.table-sm")


class SkillshotSearchPage(BaseSearchPage):

    offer_list = SkillshotOfferList(*SkillshotSearchPageLocators.OFFER_LIST)

    def offer_list_info(self):
        info_list = list()
        for offer in self.offer_list:
            if offer.date.text != today():
                continue
            info = [offer.name.text,
                    offer.location.text.split(' w ')[1],
                    offer.link.get_attribute("href")]
            info_list.append(tuple(info))
        return info_list

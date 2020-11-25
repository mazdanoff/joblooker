from abc import ABCMeta, abstractmethod

from page_objects.abstract.base_page import BasePage


class BaseSearchPage(BasePage, metaclass=ABCMeta):

    @property
    @abstractmethod
    def offer_list(self):
        raise NotImplementedError("offer_list not implemented, no clue how you got this, tho")

    @abstractmethod
    def offer_list_info(self):
        raise NotImplementedError("offer_list_info not implemented, please stop breaking my code, thank you")

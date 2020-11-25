from decorators import tags
from page_objects.aplikuj_pl_search_page import AplikujPLSearchPage
from page_objects.gumtree_search_page import GumtreeSearchPage
from page_objects.indeed_search_page import IndeedSearchPage
from page_objects.jooble_search_page import JoobleSearchPage
from page_objects.olx_search_page import OLXSearchPage
from page_objects.praca_pl_search_page import PracaPLSearchPage
from page_objects.pracuj_pl_search_page import PracujPLSearchPage
from page_objects.skillshot_search_page import SkillshotSearchPage

default_tags = ("photoshop", "artist", "grafik", "graphic")


@tags(*default_tags)
def search_pracuj_pl(context):
    page = PracujPLSearchPage(context.driver, url=context.url).open()
    context.offers.update(page.offer_list_info())


@tags(*default_tags)
def search_jooble(context):
    page = JoobleSearchPage(context.driver, url=context.url).open()
    page.handle_decline_button()
    context.offers.update(page.offer_list_info())


@tags(*default_tags)
def search_indeed(context):
    page = IndeedSearchPage(context.driver, url=context.url).open()
    context.offers.update(page.offer_list_info())


@tags(*default_tags)
def search_aplikuj_pl(context):
    page = AplikujPLSearchPage(context.driver, url=context.url).open()
    context.offers.update(page.offer_list_info())


@tags(*default_tags)
def search_praca_pl(context):
    page = PracaPLSearchPage(context.driver, url=context.url).open()
    context.offers.update(page.offer_list_info())


@tags("photoshop", "artist", "graphic")
def search_olx(context):
    page = OLXSearchPage(context.driver, url=context.url).open()
    context.offers.update(page.offer_list_info())


def search_skillshot(context):
    page = SkillshotSearchPage(context.driver, url=context.url).open()
    context.offers.update(page.offer_list_info())


def search_gumtree(context):
    page = GumtreeSearchPage(context.driver, url=context.url).open()
    context.offers.update(page.offer_list_info())

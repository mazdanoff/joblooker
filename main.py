from fixtures import driver
from search_pages import search_page_functions
from save_as_html import save_as_html
from url_templates import CASE_URLS, WROCLAW_URLS
from runner.context_object import ContextObject

placeholder_tags = ("photoshop", )


search_page_cases = tuple(
    [getattr(search_page_functions, case)
     for case in dir(search_page_functions)
     if case.startswith("search")]
)

if __name__ == '__main__':
    context = ContextObject()
    with driver() as driver_:
        context.driver = driver_
        for search_func in search_page_cases:
            if not getattr(search_func, "tags", False):
                search_func.tags = placeholder_tags
            for tag in search_func.tags:
                for url in WROCLAW_URLS[search_func.__name__]:
                    context.url = url.format(tag)
                    search_func(context)
    print(f"=============== ZEBRANYCH OFERT PRACY: {len(context.offer_list)} ===============")
    # sorted_offer_list =
    # sorted(context.offer_list, key=lambda offer_: re.search(pattern=r'://(.*)', string=offer_).group(1))
    sorted_offer_list_data = sorted(context.offer_list_data(), key=lambda offer_: offer_[2])
    # for offer in sorted_offer_list:
    #     print(offer)
    save_as_html(sorted_offer_list_data)

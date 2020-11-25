from fixtures import driver
from .context_object import ContextObject
from search_pages import search_page_functions


def null_func(context):
    print(context)


class RunnerObject:

    def __init__(self):
        self.context = ContextObject()
        self.func_list = list()

    def collect_func_list(self):
        for case in dir(search_page_functions):
            if case.startswith("search"):
                self.func_list.append(getattr(search_page_functions, case, null_func))

    def run_with_driver(self, func):
        with driver() as driver_:
            self.context.driver = driver_
            func(self.context)

    def run(self):
        pass

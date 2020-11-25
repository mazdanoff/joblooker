import os
from contextlib import contextmanager

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from conf.path_conf import FIREFOX_DRIVER, SCREENSHOT_DIR, LOG_PATH


@contextmanager
def driver():
    options = Options()
    options.headless = True
    firefox = Firefox(executable_path=FIREFOX_DRIVER, options=options, service_log_path=LOG_PATH)
    firefox.maximize_window()
    try:
        yield firefox
    finally:
        firefox.save_screenshot(os.path.join(SCREENSHOT_DIR, "1.png"))
        firefox.close()
        firefox.quit()

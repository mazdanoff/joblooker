import os


PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DRIVER_DIR = os.path.join(PROJECT_DIR, "drivers")
FIREFOX_DRIVER = os.path.join(DRIVER_DIR, "geckodriver")
SCREENSHOT_DIR = os.path.join(PROJECT_DIR, "screenshots")
REPORT_DIR = os.path.join(PROJECT_DIR, "reports")
LOG_PATH = os.path.join(PROJECT_DIR, "logs/geckodriver.log")

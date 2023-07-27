import os #to remote only!
from selenium import webdriver #to remote only!
from selenium.webdriver.chrome.options import Options #to remote only!
from selene import Browser, Config #для локального запуска #to remote only!
from selene.support.shared import browser #to remote only!
from dotenv import load_dotenv #to remote only!
import pytest
from selene import browser, be, have
from urllib import request

# from webdriver_manager.core.os_manager import ChromeType

from webdriver_manager.chrome import ChromeDriverManager

from utils import attach

def URL_LINK_ALLURE():
     URL_LINK_ALLURE = 'https://landesarchiv-berlin.de'

# -----------------------------------------------------------------------

@pytest.fixture(scope="session", autouse=True)
def browser_management():
    browser.config.timeout = 10
    browser.config.base_url = 'https://landesarchiv-berlin.de'
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1280
    browser.config.window_height = 1300
    browser.config.hold_browser_open = True

    yield


# ----------------------------------------------------------------------
# '''
DEFAULT_BROWSER_VERSION = "100.0"
'''
def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )
'''

'''
 # Selenium3:
    driver = webdriver.Chrome(ChromeDriverManager(version="114.0.5735.90").install(), options=options)

    #Selenium4:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
        version="114.0.5735.90").install()), options=options)
'''

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

# фикстура удаленного запуска:
@pytest.fixture(scope='function')
def setup_browser():
#def setup_browser(request):
    browser.config.timeout = 10
    browser.config.base_url = 'https://landesarchiv-berlin.de'
    browser.config.window_width = 1280
    browser.config.window_height = 1400
    browser.config.browser_name = 'chrome'

    # browser.config.browser_version = '100.0'
    # browser_version = request.config.getoption('--browser_version')
    # browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    # browser_version = "100.0"

    # это capabilites Selenoid!:
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome", #!
        # "browserVersion": browser_version,
        "browserVersion": "100.0", #! new
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True #!
        }
}

    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        # command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",  # see params here
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub", #see file .env
        options=options
    )

    # browser = Browser(Config(driver)) #это ЛОКАЛЬНЫЙ запуск драйвера Хром
    browser.config.driver = driver  # это УДАЛЕННЫЙ запуск драйвера Хром

    yield browser

# '''
# -----------------------------------------------------------------------
# ATTACHs
attach.add_html(browser)
attach.add_screenshot(browser)
attach.add_logs(browser)
attach.add_video(browser)

browser.quit()


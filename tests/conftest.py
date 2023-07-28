import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from utils import attach
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    
    options.add_experimental_option("prefs", {"intl.accept_languages": "de,de-DE"}) #!
    
    options.capabilities.update(selenoid_capabilities)
    
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    
    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options)

    browser.config.driver = driver
    browser.config.window_width = 1200
    browser.config.window_height = 800

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit() 



#---------LOCAL------
'''
@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'http://landesarchiv-berlin.de'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless') #!
    browser.config.driver_options = driver_options
    
    driver_options.add_experimental_option("prefs", {"intl.accept_languages": "de,de-DE"}) #!
    # options.add_experimental_option("prefs", {"intl.accept_languages": "en,en_US"})
    # options.add_experimental_option("prefs", {"intl.accept_languages": "de,de-DE"})
    # chrome_options.add_argument("--lang=en")
    #         OR
    # chrome_options.add_argument("--lang=en-US")    
   
    yield

    browser.quit()
'''

import allure
from allure_commons.types import Severity
from selene import browser, be, by, have
from selene.support.shared import browser
from selene.support.conditions import be

from tests.conftest import URL_LINK_ALLURE

URL_LINK_ALLURE = 'https://landesarchiv-berlin.de'

# Строка sys.path.append добавляет родительский каталог каталога тестов в путь поиска модулей Python, 
# что позволяет импортировать модули из корневой папки.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(file)))
                
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga')
@allure.feature(f'Проверка1')
@allure.story('Стори1')
@allure.link(URL_LINK_ALLURE, name="Link to Home Page")
def test1rem(setup_browser):

    value = 'Das Landesarchiv Berlin'

    with allure.step("Open home page"):
        browser.open('/')
    with allure.step("Кнопка лупа"):
        browser.element('.search-toggle').click()
    with allure.step("В поле ввода пусто"):
        browser.element('.search-field').should(be.blank)


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga')
@allure.feature(f'Проверка1')
@allure.story('Стори1')
@allure.link(URL_LINK_ALLURE, name="Link to Home Page")
def test2loc():

    value = 'Das Landesarchiv Berlin'

    with allure.step("Open home page2"):
        browser.open('/')
    with allure.step("Кнопка лупа2"):
        browser.element('.search-toggle').click()
    with allure.step("В поле ввода пусто2"):
        browser.element('.search-field').should(be.blank)

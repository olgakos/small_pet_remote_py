import allure
from allure_commons.types import Severity
from selene import browser, be, by, have
from selene.support.shared import browser
from selene.support.conditions import be
import pytest
from allure_commons._allure import step


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga')
@allure.feature(f'Проверка1')
@allure.story('Стори1')
@allure.link('https://landesarchiv-berlin.de', name="Link to Home Page")
def test1():

    value = 'Standesamt I in Berlin'

    with allure.step("Open home page"):
        browser.open('http://landesarchiv-berlin.de')
    with allure.step("Нажать кнопку лупа"):
        browser.element('.search-toggle').click()
    with allure.step("Ввести запрос"):
        browser.element('.search-field').should(be.blank).type(value).press_enter()


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga')
@allure.feature(f'Проверка1')
@allure.story('Стори1')
@allure.link('https://landesarchiv-berlin.de', name="Link to Home Page")
def test2():
    with allure.step("Open home page2"):
        browser.open('http://landesarchiv-berlin.de')
    # with allure.step("Перейти на английский"):
        # browser.open('/en/the-landesarchiv-berlin')
    with allure.step("Заголовок"):
        browser.element('h1.post-title').should(have.text("The Landesarchiv Ber­lin"))
    with allure.step("Cсылка"):
        browser.element(by.link_text("Appointment reservation reading room")).should(be.visible)

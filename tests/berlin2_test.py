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
def test1rem():
    value = 'Das Landesarchiv Berlin'
    with allure.step("Open home page"):
        browser.open('http://landesarchiv-berlin.de')
    with allure.step("Кнопка лупа"):
        browser.element('.search-toggle').click()
    with allure.step("В поле ввода пусто"):
        browser.element('.search-field').should(be.blank)


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga')
@allure.feature(f'Проверка1')
@allure.story('Стори1')
@allure.link('https://landesarchiv-berlin.de', name="Link to Home Page")
def test2loc():
    value = 'Das Landesarchiv Berlin'
    with allure.step("Open home page2"):
        browser.open('http://landesarchiv-berlin.de')
    with allure.step("Кнопка лупа2"):
        browser.element('.search-toggle').click()
    with allure.step("В поле ввода пусто2"):
        browser.element('.search-field').should(be.blank)

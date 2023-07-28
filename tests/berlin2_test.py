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
@allure.feature(f'Поисковая строка')
@allure.story('Стори1')
@allure.link('https://landesarchiv-berlin.de', name="Link to Home Page")
def test_easy_search():
    
    data1 = 'Standesamt I in Berlin'

    with allure.step("Open home page"):
        browser.open('http://landesarchiv-berlin.de')
    with allure.step("Нажать кнопку лупа"):
        browser.element('.search-toggle').click()
    with allure.step("Ввести запрос"):
        browser.element('.search-field').should(be.blank).type(data1).press_enter()

@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga')
@allure.feature(f'Англоязычная версия')
@allure.story('Story1')
@allure.link('https://landesarchiv-berlin.de', name="Link to Home Page")
def test_move_to_english():
    with allure.step("Open home page2"):
        browser.open('http://landesarchiv-berlin.de')
    with allure.step("Переключититься на английский"):
        browser.open('/en/the-landesarchiv-berlin')
    with allure.step("Проверить заголовок на английском"):
        browser.element('h1.post-title').should(have.text("The Landesarchiv Ber­lin"))
    with allure.step("Проверить название ссылки на английском"):
        browser.element(by.link_text("Appointment reservation reading room")).should(be.visible)

@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga')
@allure.feature(f'Texts')
@allure.story('Story1')
@allure.link('https://landesarchiv-berlin.de', name="Link to Home Page")
def test_check_text_deutch():
    
    data1 = 'Standesamt I in Berlin'
    data2 = 'Oze­an­damp­fer Im­pe­ra­tor, 1919'
    data3 = 'Quel­le: Lan­des­ar­chiv Ber­lin, F Rep. 290 Nr. II118201, Fo­to­graf: keine An­ga­be'

    with allure.step("Open home page"):
        browser.open('http://landesarchiv-berlin.de')
    with allure.step("Нажать кнопку лупа"):
        browser.element('.search-toggle').click()
    with allure.step("Ввести запрос"):
        browser.element('.search-field').should(be.blank).type(data1).press_enter()
    with allure.step("Перейти по ссылке"):
        browser.element('a[href="https://landesarchiv-berlin.de/standesamt-i-in-berlin"]').click()
    with allure.step("Проверить подпись к фото"):
        # browser.element(".media-caption").should(have.text("Ozeandampfer Imperator, 1919"))
        browser.element(".media-caption").should(have.text(data2))
        browser.element(".media-caption").should(have.text(data3))

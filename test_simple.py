import time
import random
import pytest
from selene import be, have
from selene.support.shared import browser

base_url = 'https://demoqa.com/automation-practice-form'


@pytest.fixture
def config_browser():
    browser.config.window_height = 1024
    browser.config.window_width = 768
    return browser

def test_google():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene is the personification of the Moon'))

def test_good(config_browser):
    browser.open(base_url)
    browser.element('#firstName').type('Denis')
    browser.element('#lastName').type('Denisov')
    browser.element('#userEmail').type('qa@guru.ru')
    browser.element(f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']").click()
    browser.element('#userNumber').type('79776665544')
    browser.element('#dateOfBirthInput').press_enter()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element(f"div[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1, 3)}']").click()
    browser.element('#submit').submit()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    time.sleep(3)


def test_bad(config_browser):
    browser.open(base_url)
    browser.element('#firstName').type('Denis')
    browser.element('#lastName').type('Denisov')
    browser.element('#userEmail').type('qa@guru.ru')
    browser.element(f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']").click()
    browser.element('#userNumber').type('79776665544')
    browser.element('#dateOfBirthInput').press_enter()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element(f"div[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1, 3)}']").click()
    browser.element('#submit').submit()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the FORM'))
    time.sleep(3)

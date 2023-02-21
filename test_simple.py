import time

import pytest
from selene import be, have
from selene.support.shared import browser

base_url = 'https://www.saucedemo.com/'


@pytest.fixture
def config_browser():
    browser.config.window_height = 960
    browser.config.window_width = 720
    return browser


def test_good(config_browser):
    browser.open(base_url)
    browser.element('#user-name').should(be.blank).type('standard_user')
    browser.element('#password').should(be.blank).type('secret_sauce')
    browser.element('#login-button').should(be.clickable).click()
    assert browser.element('.title').should(have.text('PRODUCTS'))
    time.sleep(3)


def test_bad(config_browser):
    browser.open(base_url)
    browser.element('#user-name').should(be.blank).type('standard_user')
    browser.element('#password').should(be.blank).type('secret_sauce')
    browser.element('#login-button').should(be.clickable).click()
    assert browser.element('.title').should(have.text('Products'))
    time.sleep(3)

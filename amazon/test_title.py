import pytest
from selenium import webdriver

expected_title = 'Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more'
base_url = 'https://www.amazon.com'
search_title = 'Amazon.com: nike air max'


@pytest.fixture()
def env_setup():
    global driver
    global baseUrl
    # we will use Google Chrome in this test. Specify the location of your chromedriver.exe
    driver = webdriver.Chrome("../chromedriver_mac_83")
    # wait 10 seconds till the website will open
    driver.implicitly_wait(10)
    # maximize browser window to full screen
    driver.maximize_window()
    yield
    # when test is done, close ALL windows of the browser
    driver.quit()


def test_title(env_setup):
    # navigate to Amazon.com home page
    driver.get(base_url)
    # verify that website title is Amazon.com
    assert driver.title == expected_title
import pytest
import time
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_youtube_flow(driver):
    # Go to youtube.com
    channel_name = '@ClassicMrBean'
    driver.get("https://www.youtube.com/" + channel_name)
    time.sleep(10)

    # Click the subscribe button
    subscribe_container = driver.find_element("id", "subscribe-button")
    subscribe_button = subscribe_container.find_element("xpath", ".//button")
    subscribe_button.click()
    time.sleep(10)

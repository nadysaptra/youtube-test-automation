import pytest
from selenium import webdriver

# @pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_youtube_flow(driver):
    # Go to youtube.com
    driver.get("https://www.youtube.com/")
    
    # Click the search bar
    search_bar = driver.find_element("xpath", "//input[@id='search']")
    search_bar.click()
    
    # Enter keywords
    keywords = "pytest automation"
    search_bar.send_keys(keywords)
    search_bar.submit()
    
    # Click the first video that appears
    first_video = driver.find_element("xpath", "(//a[@id='video-title'])[1]")
    first_video.click()
    
    # give a wait time / delay of 1 minute
    time.sleep(60)
    
    # Click the like button
    like_button = driver.find_element("xpath", "//button[@aria-label='Like']")
    like_button.click()
    
    # Click the subscribe button
    subscribe_button = driver.find_element("xpath", "//button[contains(@aria-label,'Subscribe')]")
    subscribe_button.click()

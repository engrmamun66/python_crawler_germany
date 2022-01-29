from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=e-scooter");
assert "Chrome" in driver.title
elem = driver.find_elements_by_name("h1")

print(len(elem))

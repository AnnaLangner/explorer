from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import namedtuple
from collections import Counter
from main import find_links


LinkInfo  = namedtuple('LinkInfo', 'name href')


def test_find_links(driver):
  find_links(driver)


def test_count_links(links):
  found_number_of_links = Counter(links)
  expected_number_of_links = 98
  assert found_number_of_links == expected_number_of_links


def top():  
  driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get("https://annalangner.github.io/Projekt-1/")
  links = test_find_links(driver)
  test_count_links(links)
  driver.close()


top()

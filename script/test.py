from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import namedtuple
from collections import Counter
from main import find_links


LinkInfo  = namedtuple('LinkInfo', 'name href')


def test_find_links(driver):
  lists_of_tuples = find_links(driver)
  for LinkInfo.href in lists_of_tuples:
    if "href" == None:
      assert Error in lists_of_tuples      
    else:
      assert "All tests done."  
  return lists_of_tuples


def test_count_links(links):
  found_number_of_links = len(links)
  expected_number_of_links = 87
  assert found_number_of_links == expected_number_of_links


def top():  
  driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get("https://annalangner.github.io/Projekt-1/")
  links = test_find_links(driver)
  test_count_links(links)
  driver.close()


top()

import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import namedtuple
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



LinkInfo  = namedtuple('LinkInfo', 'name href')


def find_links(driver):  
  links_elem = driver.find_elements_by_tag_name("a")    
  return [LinkInfo(elem.text, elem.get_attribute('href')) for elem in links_elem]


def print_link_info(links):
  for value in links:    
    print(value.name, value.href)


def test_find_links(links):
  for elem in links:
    if 'href' == None:
      assert Error in find_links      
    else:
      assert "All tests done."
      


def main():  
  driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get("https://wikipedia.org")
  WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(By.TAG_NAME, "a"))
  links = find_links(driver)
  print_link_info(links)
  test_find_links(links)
  driver.close()


main()

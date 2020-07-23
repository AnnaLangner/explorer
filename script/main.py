import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import namedtuple


def fetch_argument():
  parser = argparse.ArgumentParser()   
  parser.add_argument('--driver', help='entry driver')
  parser.add_argument("url", help="entry page url")
  args = parser.parse_args()     
  return args.driver, args.url


def create_driver(name):
  if name  == 'chrome':
    driver = webdriver.Chrome(executable_path="bin/chromedriver")
  else:
    driver = webdriver.Firefox(executable_path="bin/geckodriver.exe")
  return driver


def find_links(driver):  
  links_elem = driver.find_elements_by_tag_name("a")  
  LinkInfo  = namedtuple('LinkInfo ', 'name href')
  return [LinkInfo(name, name.get_attribute('href')) for name in links_elem]


# def print_list_of_all_links(links_elem):
#   for value in links_elem:
#     link_value = value.get_attribute('href')    
#     print("name: " + value.text + ", target location: " + link_value)


def main():  
  driver, url = fetch_argument()
  driver = create_driver(driver)
  driver.get(url)
  links_elem = find_links(driver)
  # print_list_of_all_links(links_elem)
  driver.close()

main()

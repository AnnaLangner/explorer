import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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


def list_of_all_links(driver):
  links_elem = driver.find_elements_by_tag_name("a")
  return links_elem  


def print_list_of_all_links(driver):
  for value in list_of_all_links(driver):
    link_value = value.get_attribute('href')    
    print("name: " + value.text + ", target location: " + link_value)


def main():  
  driver, url = fetch_argument()
  driver = create_driver(driver)
  driver.get(url)
  list_of_all_links(driver)
  print_list_of_all_links(driver)
  driver.close()

main()

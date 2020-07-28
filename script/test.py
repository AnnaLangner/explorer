from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import namedtuple
from collections import Counter


LinkInfo  = namedtuple('LinkInfo', 'name href')


def test_find_links(driver):
  links = driver.find_elements_by_tag_name("a")
  return [LinkInfo(elem.text, elem.get_attribute('href')) for elem in links]


def print_links(links):
  counter_link = Counter(links)
  print(counter_link)


def main():  
  driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get("https://annalangner.github.io/Projekt-1/")
  links = test_find_links(driver)
  print_links(links)
  driver.close()


main()

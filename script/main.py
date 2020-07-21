import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def fetch_argument():
  parser = argparse.ArgumentParser()   
  parser.add_argument('--driver', help='entry driver')
  parser.add_argument("url", help="entry page url")
  args = parser.parse_args()   
  if args.driver  == 'chrome':
    driver = webdriver.Chrome(executable_path="bin/chromedriver")
  else:
    driver = webdriver.Firefox(executable_path="bin/geckodriver.exe")
  return(driver, args.url)


def main():  
  (driver, url) = fetch_argument()
  driver.get(url)
  driver.close()

main()

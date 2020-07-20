import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def fetch_argument():
  parser = argparse.ArgumentParser()
  parser.add_argument("url", help="entry page url")
  args = parser.parse_args()
  return(args.url)


def main():
  driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get(fetch_argument())


main()

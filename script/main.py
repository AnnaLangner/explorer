import argparse
from selenium import webdriver
from collections import namedtuple
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LinkInfo = namedtuple('LinkInfo', 'name href')


def fetch_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('--driver', help='entry driver')
    parser.add_argument("url", help="entry page url")
    args = parser.parse_args()
    return args.driver, args.url


def create_driver(name):
    if name == 'chrome':
        driver = webdriver.Chrome(executable_path="bin/chromedriver")
    else:
        driver = webdriver.Firefox(executable_path="bin/geckodriver.exe")
    return driver


def find_links(driver):
    links_elem = driver.find_elements_by_tag_name("a")
    return [LinkInfo(elem.text, elem.get_attribute('href')) for elem in links_elem]


def print_link_info(links):
    for value in links:
        print(value.name, value.href)


def main():
    driver, url = fetch_argument()
    driver = create_driver(driver)
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(By.TAG_NAME, "a"))
    links = find_links(driver)
    print_link_info(links)
    driver.close()


if __name__ == "__main__":
    main()

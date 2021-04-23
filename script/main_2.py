import argparse
import re
from selenium import webdriver


def fetch_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('--driver', help='entry driver')
    parser.add_argument("url", help="entry page url, like: https://www.google.com")
    args = parser.parse_args()
    return args.driver, args.url


def create_driver(name):
    if name == 'chrome':
        driver = webdriver.Chrome(executable_path="bin/chromedriver.exe")
    else:
        driver = webdriver.Firefox(executable_path="bin/geckodriver.exe")
    return driver


def find_input(driver):
    input_elements = driver.find_elements_by_tag_name("input")
    return input_elements


def find_attribute(input_elements):
    item_list = []
    for item in input_elements:
        attribute = item.get_attribute("placeholder")
        print(attribute)
        item_list.append(attribute)
    return item_list


def find_search(attribute):
    search_elem = []
    for elem in attribute:
        pattern = re.compile('Search')
        search_pattern = pattern.search(elem)
        if search_pattern:
            search_elem.append(elem)
    if search_elem:
        print('There is a search box on the page')
    else:
        print('There is no a search box on the page')


def main():
    driver, url = fetch_argument()
    driver = create_driver(driver)
    driver.get(url)
    input_elements = find_input(driver)
    attribute = find_attribute(input_elements)
    find_search(attribute)
    driver.close()


if __name__ == "__main__":
    main()

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


def find_search_box(input_elements):
    item_list = []
    for item in input_elements:
        attribute = item.get_attribute("placeholder")
        print(attribute)
        item_list.append(attribute)
    for elem in item_list:
        pattern = re.compile('Search')
        search_pattern = pattern.search(elem)
        if search_pattern:
            print('There is a search box on the page')


def main():
    driver, url = fetch_argument()
    driver = create_driver(driver)
    driver.get(url)
    input_elements = find_input(driver)
    find_search_box(input_elements)
    driver.close()


if __name__ == "__main__":
    main()
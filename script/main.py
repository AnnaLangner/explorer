import argparse
from selenium import webdriver
from collections import namedtuple
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

LinkInfo = namedtuple('LinkInfo', 'name href')


def fetch_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('--driver', help='entry driver')
    parser.add_argument("url", help="entry page url, like: https://www.google.com")
    parser.add_argument('--depth', type=int, help='entry how long to follow page links')
    args = parser.parse_args()
    return args.driver, args.url, args.depth


def create_driver(name):
    if name == 'chrome':
        driver = webdriver.Chrome(executable_path="bin/chromedriver.exe")
    else:
        driver = webdriver.Firefox(executable_path="bin/geckodriver.exe")
    return driver


def find_links(driver):
    links_elem = driver.find_elements_by_tag_name("a")
    return [LinkInfo(elem.text, elem.get_attribute('href')) for elem in links_elem]


def print_urls_info(urls):
    for item in urls:
        print(item[0], item[1])


def main():
    driver, url, depth = fetch_argument()
    driver = create_driver(driver)
    links_info = {LinkInfo(url, url)}
    for elem in range(depth + 1):
        new_urls = set()
        for link_info in links_info:
            driver.get(link_info[1])
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
            links = find_links(driver)
            for item in links:
                new_urls.add((item[0], item[1]))
        links_info = new_urls
        print_urls_info(links_info)
    driver.close()


if __name__ == "__main__":
    main()

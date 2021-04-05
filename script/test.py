from selenium import webdriver
from collections import namedtuple
from main import find_links

LinkInfo = namedtuple('LinkInfo', 'name href')


def get_the_page(driver):
    driver.get("https://annalangner.github.io/Projekt-1/")


def find_list_of_tuples(driver):
    lists_of_tuples = find_links(driver)
    print(lists_of_tuples)
    return lists_of_tuples


def verify_list_of_tuples(lists_of_tuples):
    for LinkInfo.href in lists_of_tuples:
        if LinkInfo.href is None:
            assert False
        else:
            assert "All tests done."


def verify_number_of_links(lists_of_tuples):
    found_number_of_links = len(lists_of_tuples)
    assert found_number_of_links == 87


def test_find_links(driver):
    get_the_page(driver)
    list_of_tuples = find_list_of_tuples(driver)
    verify_list_of_tuples(list_of_tuples)


def test_count_links(driver):
    get_the_page(driver)
    list_of_tuples = find_list_of_tuples(driver)
    verify_number_of_links(list_of_tuples)


def test():
    driver = webdriver.Chrome(executable_path="../bin/chromedriver.exe")
    test_find_links(driver)
    test_count_links(driver)
    driver.close()


test()

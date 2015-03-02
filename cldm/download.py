#!/usr/bin/env python
# encoding: utf-8

import sys
import json
from selenium import webdriver


def main(fp, driver="/home/daipeng/Downloads/chromedriver"):

    data = json.load(open(fp))

    for obj in data[:20]:
        if len(obj['url']) == 0:
            continue

        chrome = webdriver.Chrome(driver)
        chrome.get(obj['url'][0])
        sub = chrome.find_element_by_name('submit')
        sub.click()

        chrome.quit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'useage: python download.py <data.json>'
        sys.exit(-1)
    main(sys.argv[1])

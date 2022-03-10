#!/usr/bin/env python3


from selenium import webdriver
from selenium.webdriver import ChromeOptions


def html2img(url):
    """ html to image
    """
    # init chrome
    option = ChromeOptions()
    option.add_argument('headless')
    option.add_argument("--hide-scrollbars")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)
    driver.set_window_size(750, 10000)
    driver.implicitly_wait(1)
    
    driver.get(url)
    height = driver.execute_script("return document.body.scrollHeight")
    #print(height)
    driver.set_window_size(750, height + 15)

    # get screenshot
    name = url.split("/")[-1].split(".")[0]
    print(name)
    driver.get_screenshot_as_file("%s.png" % name)
    driver.quit()


if __name__ == "__main__":
    url = "https://12ff806.github.io/tree/learning_list"
    html2img(url)


from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import TouchActions
from selenium.webdriver.remote.webdriver import WebDriver

class Base():
    driver = None
    base_url = ''

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('w3c', False)
            self.driver = webdriver.Chrome(options=options)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.action=TouchActions(self.driver)
        else:
            self.driver = driver
            self.action = TouchActions(self.driver)

        # if self.base_url != '':
        #     self.driver.get(self.base_url)


    def find(self,tip):
        return self.driver.find_element(*tip)

    def finds(self,tips):
        return self.driver.find_elements(*tips)

    def wait_by_fun(self,func,time=60):
        return WebDriverWait(self.driver,time).until(func)

    def wait_by_excepted_ele(self,tips,time=60):
        '''显式等待官方的用法'''
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(tips))

    def wait_ele_located(self,tips,time=60):
        WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(tips))

    def wait_ele_visibilit(self,tips,time=60):
        WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(tips))
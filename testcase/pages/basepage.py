import yaml
from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_ele(self, by, locator):
        self.driver.find_element(by, locator)

    def find_ele_click(self, by, locator):
        self.driver.find_element(by, locator).click()

    def find_ele_sendkey(self, by, locator, text):
        self.driver.find_element(by, locator).send_keys(text)

    def wait_ele_click(self, by, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((by, locator)))

    def yaml_duqu(self, path):
        with open(path, "r", encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
        for step in steps:
            if step["action"] == "find_ele":
                self.find_ele(step["by"], step["locator"]);
            elif step["action"] == "find_ele_click":
                self.find_ele_click(step["by"], step["locator"]);
            elif step["action"] == "find_ele_sendkey":
                self.find_ele_sendkey(step["by"], step["locator"], step["text"], );
            elif step["action"] == "wait_ele_click":
                self.wait_ele_click(step["by"], step["locator"]);

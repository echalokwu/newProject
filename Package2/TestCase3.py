import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import HtmlTestRunner


class TestCase3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="/Users/echalo/newProject/drivers/geckodriver")
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_case_1(self):
        """Build a Prototype"""
        self.driver.get("https://www.oursky.com/")
        self.driver.find_element_by_class_name('btn-header').click()
        print(self.driver.title)
        self.driver.find_element_by_id("prototype-switch").click()
        self.driver.execute_script("window.scrollBy(0, 300)", "")
        contact = self.driver.find_element_by_xpath("//form[@id='prototype-enquiry-form']//input[@id='contact']")
        contact.send_keys("Michael Smith")
        email = self.driver.find_element_by_xpath("//form[@id='prototype-enquiry-form']//input[@id='email']")
        email.send_keys("abc@gmail.com")
        employees = Select(self.driver.find_element_by_id("noOfEmployees"))
        employees.select_by_value("25-100")
        role = Select(self.driver.find_element_by_id("role"))
        role.select_by_value("Director")
        self.driver.find_element_by_xpath("//div[9]//div[1]").click()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/echalo/newProject/Package2/package2Reports'))

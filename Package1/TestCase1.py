import unittest
from selenium import webdriver
import time
import HtmlTestRunner


class TestCase1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="/Users/echalo/newProject/drivers/geckodriver")
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_case_1(self):
        """Find and click top-right button"""
        self.driver.get('https://www.oursky.com/')
        self.driver.find_element_by_class_name('btn-header').click()
        self.assertEqual("Oursky - Web & mobile application development company based in Hong Kong", self.driver.title,
                         "webpage title is not matching")
        print(self.driver.title)

    def test_case_2(self):
        """Find and click Learn more button"""
        self.driver.get('https://www.oursky.com/')
        self.driver.find_element_by_xpath(".//*[@id='tag-line-wrap']/span/a").click()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/echalo/newProject/Package1/package1Reports'))

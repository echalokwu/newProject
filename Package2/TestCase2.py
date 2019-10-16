import unittest
from selenium import webdriver
import time
import HtmlTestRunner


class TestCase2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="/Users/echalo/newProject/drivers/geckodriver")
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_case_1(self):
        """Fill Other Enquiries"""
        self.driver.get("https://www.oursky.com/")
        self.driver.find_element_by_class_name('btn-header').click()
        print(self.driver.title)
        self.driver.execute_script("window.scrollBy(0, 500)", "")
        contact = self.driver.find_element_by_xpath("//form[@id='general-enquiry-form']//input[@id='contact']")
        contact.send_keys("Michael Smith")
        email = self.driver.find_element_by_xpath("//form[@id='general-enquiry-form']//input[@id='email']")
        email.send_keys("abc@gmail.com")
        checkbox = self.driver.find_element_by_id("checkbox4")
        checkbox.click()
        projectSummary = self.driver.find_element_by_xpath("//textarea[@id='summary']")
        projectSummary.send_keys("testing your nice wibsite")
        upload = self.driver.find_element_by_id('generalFile')
        # upload = self.driver.find_element_by_xpath("//form[@id='general-enquiry-form']//button[@class='btn large-btn submitForm'][contains(text(),'Submit')]")
        upload.send_keys("/Users/echalo/PythonUnitTestProject_POMBased/Downloads/info.pdf")
        time.sleep(7)
        submit = self.driver.find_element_by_xpath("//form[@id='general-enquiry-form']//button[@class='btn large-btn "
                                                   "submitForm'][contains(text(),'Submit')]")
        submit.click()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/echalo/newProject/Package2/package2Reports'))

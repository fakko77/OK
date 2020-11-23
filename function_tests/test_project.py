from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time


class TestProject(StaticLiveServerTestCase):
    def test_search_no_log(self):
        self.browser = webdriver.Chrome('function_tests/driver.exe')
        self.browser.get(self.live_server_url)
        search = self.browser.find_element_by_class_name("form-control")
        search.send_keys("test")
        search.send_keys(Keys.RETURN)
        page = self.browser.find_element_by_class_name("text-uppercase")
        self.assertEqual(page.text, "DU GRAS, OUI, MAIS DE QUALITÉ!")
        time.sleep(2)

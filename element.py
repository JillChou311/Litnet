from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time

class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        try:
            driver = obj.driver
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element_by_name(self.locator))
            driver.find_element_by_name(self.locator).send_keys(value)

        except NoSuchElementException:
            timestr2 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            self.driver.get_screenshot_as_file("screen" + timestr2 + ".png")
            print "Pic record on" + "screen" + timestr2 + ".png"
            return False

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")

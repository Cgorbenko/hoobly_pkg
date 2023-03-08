from .browser import Browser
import time

class Hoobly():
    """Controls Hoobly website"""
    
    def open_home_page(self):
        browser = Browser()
        browser.driver.get(browser.base_url)
        time.sleep(4)

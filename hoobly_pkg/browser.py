from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Browser:
    """Controls the hoobly browser"""
    def __init__(
    self, base_url: str="https://www.hoobly.com/s", retry_timeout: int = 10
    ) -> None:
        self.base_url: str = base_url
        self.retry_timeout = retry_timeout

        # Creates the browser
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        self.driver.implicit_wait(5)

    def close(self):
        """Closes the browser"""
        self.driver.close()
        self.driver.quit()


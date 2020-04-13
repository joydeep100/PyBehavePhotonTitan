from selenium import webdriver
from helpers.selenium_api_wrappers import SeleniumAPIWrapper
from common.variables import *

class Browser(SeleniumAPIWrapper):

	def __init__(self):
		
		if browser_type == 'chrome':

			chromeOptions = webdriver.ChromeOptions()
			chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
			chromeOptions.add_argument("--no-sandbox")
			#Other optional args 
			# --disable-setuid-sandbox, --remote-debugging-port=9222,  --disable-dev-shm-using
			# --disable-extensions, --disable-gpu, start-maximized, disable-infobars, --headless
	
			self.driver = webdriver.Chrome(chrome_options=chromeOptions)
	

		elif browser_type == 'firefox':
			self.driver = webdriver.Firefox()
		
		super().__init__(self.driver) 

		# context.driver = self.driver

	def close_browser(self):
		self.driver.quit()

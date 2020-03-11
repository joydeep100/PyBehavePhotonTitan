from selenium import webdriver
from helpers.selenium_api_wrappers import SeleniumAPIWrapper
from common.variables import *

class Browser(SeleniumAPIWrapper):

	def __init__(self):
		
		if browser_type == 'chrome':
			self.driver = webdriver.Chrome()
		elif browser_type == 'firefox':
			self.driver = webdriver.Firefox()
		
		super().__init__(self.driver) 


	def close_browser(self):
		self.driver.quit()
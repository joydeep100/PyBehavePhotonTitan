from selenium import webdriver
from helpers.selenium_api_wrappers import SeleniumAPIWrapper


class Browser(SeleniumAPIWrapper):

	def __init__(self,browser):

		if browser == 'chrome':
			self.driver = webdriver.Chrome()
		elif browser == 'firefox':
			self.driver = webdriver.Firefox()
		
		super().__init__(self.driver) 
		#initalize the driver for super class 'SeleniumAPIWrapper'
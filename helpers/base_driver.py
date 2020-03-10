from selenium import webdriver
from selenium.webdriver.common.by import By

class Browser():

	def __init__(self,browser):
		if browser == 'chrome':
			self.driver = webdriver.Chrome()
		elif browser == 'firefox':
			self.driver = webdriver.Firefox()
	
	def close_browser(self):
		self.driver.close()

	#Using css selector as default locator strategy
	def get_element(self,selector):
		return self.driver.find_element(By.CSS_SELECTOR,selector)

	#for returning multiple elements as a list
	def get_elements(self,selector):
		return self.driver.find_elements(By.CSS_SELECTOR,selector)

	#Keeping xpath as secondary locator strategy
	def get_element_xpath(self,selector):
		return self.driver.find_element(By.CSS_SELECTOR,selector)

	def get_elements_xpath(self,selector):
		return self.driver.find_elements(By.CSS_SELECTOR,selector)
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class SeleniumAPIWrapper():

	def __init__(self,driver_config):
		self.driver = driver_config

	def close_browser(self):
		self.driver.quit()

	#Using css selector as default locator strategy
	def get_element(self,selector):
		return self.driver.find_element(By.CSS_SELECTOR,selector)

	def get_elements(self,selector):
		return self.driver.find_elements(By.CSS_SELECTOR,selector)

	#Keeping xpath as secondary locator strategy
	def get_element_xpath(self,selector):
		return self.driver.find_element(By.XPATH,selector)

	def get_elements_xpath(self,selector):
		return self.driver.find_elements(By.XPATH,selector)

	def get_element_by_text(self,text,parent_element=''):
		parent_element = parent_element if (parent_element != '') else '*'
		selector = '//{}[text()="{}"]'.format(parent_element,text)
		return self.driver.find_element(By.XPATH,selector)

	def get(self,locator):
		return self.driver.get(locator)

	def drag_n_drop(self,src_ele,target_ele):
		action_chains = ActionChains(self.driver)
		action_chains.drag_and_drop(src_ele, target_ele).perform()
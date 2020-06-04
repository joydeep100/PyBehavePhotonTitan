from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class SeleniumAPIWrapper():

	def __init__(self,driver):
		self.driver = driver

	# to navigate to any url
	def get(self,url):
		return self.driver.get(url)

	# using css selector as default locator strategy
	def get_element(self,selector):
		return self.driver.find_element(By.CSS_SELECTOR,selector)

	def get_elements(self,selector):
		return self.driver.find_elements(By.CSS_SELECTOR,selector)

	# keeping xpath as secondary locator strategy
	def get_element_xpath(self,selector):
		return self.driver.find_element(By.XPATH,selector)

	def get_elements_xpath(self,selector):
		return self.driver.find_elements(By.XPATH,selector)

	def get_element_by_text(self,text,parent_element='*'):
		selector = '//{}[text()="{}"]'.format(parent_element,text)
		return self.driver.find_element(By.XPATH,selector)

	def drag_n_drop(self,src_ele,target_ele):
		action_chains = ActionChains(self.driver)
		action_chains.drag_and_drop(src_ele, target_ele).perform()

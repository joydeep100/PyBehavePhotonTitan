from selenium import webdriver
from common.variables import browser_type

class Browser():

	def __init__(self,context):
		
		if browser_type == 'chrome':
			
			chromeOptions = webdriver.ChromeOptions()
			chromeOptions.add_argument('--headless')		#comment this line to see browser
			self.driver = webdriver.Chrome(chrome_options=chromeOptions)

		elif browser_type == 'firefox':
			self.driver = webdriver.Firefox()

		self.driver.maximize_window()
	
	def close_browser(self):
		self.driver.quit()

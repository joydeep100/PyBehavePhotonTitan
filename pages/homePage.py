from helpers.base_driver import Browser
from common.variables import base_url, home_page_locators

class HomePage(Browser):

	def __init__(self,browser):
		super().__init__(browser)

	def gotoHomepage(self):
		self.driver.get(base_url)

	def validateHomePageIsLoaded(self):
		home_title = self.get_element(home_page_locators['home_label'])
		assert 'Home' in home_title.text;

	def gotoLink(self,link_name):
		links = self.get_elements('li > a')
		HomePage.clickLinkBasedOnTitle(links,link_name)

	@staticmethod
	def clickLinkBasedOnTitle(common_selector,title):

		for i in common_selector:
			if i.text == title:
				i.click();
				break

x = HomePage('chrome')
x.gotoHomepage();
x.validateHomePageIsLoaded()
x.gotoLink('Selectable')
x.close_browser()
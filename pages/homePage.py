from helpers.base_driver import Browser
from common.variables import base_url, home_page_locators

class HomePage(Browser):

	def __init__(self,browser):
		super().__init__(browser)

	def gotoHomepage(self):
		self.get(base_url)

	def validateHomePageIsLoaded(self):
		home_title = self.get_element(home_page_locators['home_label'])
		assert 'Home' in home_title.text, 'Home label is not visible';

	def selectItemInSelectableWindown(self,item):
		items = self.get_elements(home_page_locators['selectable_items'])
		for i in items:
			if i.text == item:
				i.click()

	def checkIfItemIsSelected(self):
		selected_item = self.get_element(home_page_locators['selected_item'])
		assertion_class = str(home_page_locators['selected_item']).strip('.')
		assert assertion_class in str(selected_item.get_attribute('class')), 'Class {} not \
				seen in selected_item'.format(assertion_class)

	def dragItemToDroppableArea(self):
		src_ele = self.get_element(home_page_locators['drag_item'])
		dest_ele = self.get_element(home_page_locators['drop_area'])
		self.drag_n_drop(src_ele,dest_ele)

	def checkIfItemIsDropped(self):
		post_drop_element = self.get_element(home_page_locators['drop_area'])
		assert 'Dropped' in post_drop_element.text, 'Src element is not dropped properly!'

	def gotoLink(self,link_name):
		links = self.get_elements(home_page_locators['home_page_links'])
		HomePage.clickLinkBasedOnTitle(links,link_name)
		window_title = self.get_element(home_page_locators['window_title_txt'])
		assert link_name in window_title.text, 'Window title text is not {}'.format(link_name)

	@staticmethod
	def clickLinkBasedOnTitle(common_selector,title):
		for i in common_selector:
			if i.text == title:
				i.click();
				break

x = HomePage('chrome')
x.gotoHomepage();
x.validateHomePageIsLoaded()
x.gotoLink('Droppable')
x.dragItemToDroppableArea()
x.checkIfItemIsDropped()
x.close_browser()
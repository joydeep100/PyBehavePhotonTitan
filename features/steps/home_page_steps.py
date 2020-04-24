from pages.home_page import HomePage
from common.variables import home_url

@given('I go to the home page')
def step_impl(context):
	home_page =  HomePage(context)
	home_page.gotoPage(home_url)
	   
@given('I verify if the "{label_text}" page is loaded sucessfully')
def step_impl(context,label_text):
	home_page =  HomePage(context)
	home_page.validateHomePageIsLoaded(label_text)

@given('I go to the "{link_name}" link')
def step_impl(context,link_name):
	home_page =  HomePage(context)
	home_page.gotoLink(link_name)

@given('I select "{item}" from the list of items')
def step_impl(context,item):
	home_page =  HomePage(context)
	home_page.selectItemInSelectableWindown(item)

@given('I check if the item is selected')
def step_impl(context):
	home_page =  HomePage(context)
	home_page.checkIfItemIsSelected()

@given('I select the item to be dropped')
def step_impl(context):
	home_page =  HomePage(context)
	home_page.dragItemToDroppableArea()

@given('I verify if the item is sucessfully dropped')
def step_impl(context):
	home_page =  HomePage(context)
	home_page.checkIfItemIsDropped()
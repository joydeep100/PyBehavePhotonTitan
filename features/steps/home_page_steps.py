from behave import *
from pages.home_page import *
from common.variables import *
from helpers.base_driver import *

@given('I go to the home page')
def step_impl(context):
	x = HomePage(context)
	x.gotoPage(home_url)
	   
@given('I verify if the "{label_text}" page is loaded sucessfully')
def step_impl(context,label_text):
	x = HomePage(context)
	x.validateHomePageIsLoaded(label_text)

@given('I go to the "{link_name}" link')
def step_impl(context,link_name):
	x = HomePage(context)
	x.gotoLink(link_name)

@given('I select "{item}" from the list of items')
def step_impl(context,item):
	x = HomePage(context)
	x.selectItemInSelectableWindown(item)

@given('I check if the item is selected')
def step_impl(context):
	x = HomePage(context)
	x.checkIfItemIsSelected()

@given('I select the item to be dropped')
def step_impl(context):
	x = HomePage(context)
	x.dragItemToDroppableArea()

@given('I verify if the item is sucessfully dropped')
def step_impl(context):
	x = HomePage(context)
	x.checkIfItemIsDropped()
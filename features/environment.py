from helpers.base_driver import *

def before_all(context):
	browser_obj = Browser()
	context.driver = browser_obj.driver

def before_scenario(feature,context):
	browser_obj = Browser()
	context.driver = browser_obj.driver

def after_scenario(feature,context):
	context.driver.close()
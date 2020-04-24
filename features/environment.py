from utils.base_driver import Browser

def before_all(context):
	pass
	'''add conditions to run before all features are run'''

def before_scenario(context,feature):
	browser = Browser(context)
	context.driver = browser.driver

def after_scenario(context,feature):
	context.driver.quit()

def after_all(context):
	pass
	'''add conditions to run after all features are run'''
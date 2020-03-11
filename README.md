# PySel
Selenium implementation with Python, POM &amp; Behave!

This is purely a Sample Selenium Framework, attempted to keep it as simple as possible and also by making use of some of best know practices of Test Automation.

Libraries Used.
- Selenium
- Behave (BDD)

- Python version used 3.8

## Behave techniques used

- Tags
- Fixtures (Setup and Teardown)
- Features
- Scenarios

## Python techniques used

- Page Object Model (using classes and objects)
- Multi level Inheritance
- Static methods
- Assertions

## Selenium techinques used

- Action chains
- Navigations
- Locating elements (css - default, xpath as secondary locator strategy and custom locator method based on text of the element)


## How to run

Pre-Requisites.
1. Python3
2. Webdriver's should be installed
3. Install the libraries mentioned in requirement.txt

`pip install -r requirements.txt'

Use any of the below commands to run
1. Go to the parent directory (ie. pysel)
2. behave                                     // To run all the scenarios
  or
3. behave --tags='regression' -k              // To run only tests which are using @regression tag

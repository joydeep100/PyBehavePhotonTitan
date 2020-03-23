# PySel
Selenium3 implementation with Python, POM &amp; BDD!

This is purely a Selenium Framework, attempted to keep it as simple as possible and also by making use of some of best know practices of Test Automation.

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

- Page Object Model
- Multi level Inheritance
- Static methods

## Selenium techinques used

- Action chains
- Writing wrapper functions for cumbersome selnium API's :(
- Added a custom locating method using text of the element (used xpath internally)

## How to run

Pre-Requisites.
1. Python3
2. Webdriver's should be installed
3. Define the browser type in `common/variables.py`file (chrome / firefox)
3. Install the libraries mentioned in requirement.txt using the command`pip install -r requirements.txt`

Use any of the below commands to run
1. Go to the parent directory (ie. pysel)
2. type `behave` and hit enter.                                     // To run all the scenarios
  or
3. type `behave --tags='regression' -k` and hit enter               // To run only tests which are using @regression tag

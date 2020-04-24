Feature: To test various scenarios on the home page of the test website!

@smoke @regression
Scenario: To check if the home page is loading sucessfully
	Given I go to the home page
	And I verify if the "Home" page is loaded sucessfully

@smoke
Scenario: To check if we are able to select and highlight an item (item3)
	Given I go to the home page
	And I go to the "Selectable" link
	And I select "Item 3" from the list of items
	And I check if the item is selected

@smoke
Scenario: To check if we are able to select and highlight an item (item4)
	Given I go to the home page
	And I go to the "Selectable" link
	And I select "Item 4" from the list of items
	And I check if the item is selected

@smoke
Scenario: Testing drag and drop functionality
	Given I go to the home page
	And I go to the "Droppable" link
	And I select the item to be dropped
	And I verify if the item is sucessfully dropped
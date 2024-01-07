@EndToEndRegression
Feature: Customer Search and Purchase item from the application

In this feature a customer will come to my application, login, Search do payment and logout

	Background:
		Given  User open browser, enter URL and navigate to Login page
		
	@Smoke
	Scenario: Test email functionality of application
		When	User enters username "Hello"
		And		User enters password "abcd123"
		And		User clicks on signin button
		And 	User click on Compose button
		And 	User enter address "asdf@gmail.com" enter body text
				"""
				This is line 1
				this is line 2
				this is line 3
				
				Regards
				Testing World
				"""
	
	
	@Sanity @Regression
	Scenario Outline: Verify login and logout functionality with multiple user data
		When	User enters username "<Username>"
		And		User enters password "<Password>"
		And		User clicks on signin button
		Then	User should be logged In
		When 	Clicks on Signout link
		Then	User should be loggedout
	Examples:
		|Username|Password|
		|  User1 | Pass1  |
		|  User2 | Pass2  |
		|  User3 | Pass3  |
		|  User4 | Pass4  |
		|  User5 | Pass5  |
		
	@Performance
	Scenario: New User (unregistered User) comes to application, Search, Register and Purchase		
		When   User enter data in search field
		And    User click on search button
		And    User click on Add to cart for the first test result
		#And    User click on my Cart button
		Then   User could get added item in Cart
		And    User could get price of item in front of Item name
		When   User click on Purchase button
		And    User select Payment mode is Credit Card

	Scenario: Registered User, Search Item, Add to cart and Purchas		
		When   User enter "Mobile Phone" in search field
		And    User click on search button
		And    User click on Add to cart for the first test result

	Scenario: Registered User, search add to cart, change address and payment
		When   User enter "Smart TV" in search field
		And    User click on search button
		And    User click on Add to cart for the first test result

# Created by johannyinfante at 11/5/24
Feature: Test for Reelly App Filter Functionality
# Enter feature name here
  # Enter feature description here

  Scenario:User can use filters in Reelly App
    Given Open the Reelly main page
    When  Log in and enter email
    And   Enter password
    And   Click Continue Button
    And   Click Secondary on menu
    And   Click on Filters
    And   Filter the products by price range from 1200000
    And   Filter the products by price range to 2000000
    And   Click Apply Filters
    Then  Verify all products are within the specified price range
#    # Enter scenario name here
#    # Enter steps here
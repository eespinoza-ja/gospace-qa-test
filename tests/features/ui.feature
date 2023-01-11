@ui
Feature: Testing endpoints from GitHub APIs
  As a qa,
  I want to test GitHub UI,
  So that I can verify and check the user interface of GitHub web page

  Scenario: Login to GitHub
    Given I am on the login page
    When I enter the correct email and password
    Then I see the user home page


  Scenario: Get the list of repositories in GitHub
    Given I am in the the home page
    When I go to the repos page
    Then I see the repos


  Scenario: Create a repository in GitHub
    Given I am in the the home page
    When I go to the new repo page
    And I create a repo
    Then I am in the new repo page

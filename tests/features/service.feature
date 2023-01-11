@api
Feature: Testing endpoints from GitHub APIs
  As a qa,
  I want to test GitHub REST API,
  So that I can verify and check the response of the targeted API

  Scenario Outline: Create a new repository in a GitHub organization
    Given I send to create an org repository <name>
    When the response status code is "201"
    Then the response contains results for <name>

    Examples: Names
      | name        |
      | go-space-qa |
      | test-repo   |
      | new-repo    |


  Scenario Outline: Get the list of repositories in a GitHub organization
    Given I send the request to get repositories list
    When the response has a list of repositories
    Then the response contains repositories <name>

    Examples: Names
      | name        |
      | go-space-qa |
      | test-repo   |
      | new-repo    |


  Scenario Outline: Delete a repository in a GitHub organization
    Given I send to delete the org repository <name>
    Then the response code is "204"

    Examples: Names
      | name        |
      | go-space-qa |
      | test-repo   |
      | new-repo    |
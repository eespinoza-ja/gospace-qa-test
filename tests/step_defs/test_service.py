import os
import requests
from dotenv import load_dotenv
from requests.structures import CaseInsensitiveDict
from pytest_bdd import scenarios, given, when, then, parsers

# Shared Variables
load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
GITHUB_REPOS = os.getenv('GITHUB_REPOS')
GITHUB_REPO = os.getenv('GITHUB_REPO')

# Scenarios Path
scenarios('../features/service.feature')


# Create a new repository in a GitHub organization
# Given Steps
@given(parsers.parse("I send to create an org repository {name}"), target_fixture="cr_response")
def create_repo_response(name):
    """ Send the info in order to create the repo """
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer " + API_TOKEN
    params = {"name": name, "description": "This is a testing repository",
              "homepage": "https://github.com", "private": False, "has_issues": True,
              "has_projects": True, "has_wiki": True, 'format': 'json'}
    response = requests.post(GITHUB_REPOS, headers=headers, params=params)
    return response


# When Steps
@when(parsers.parse('the response status code is "{code:d}"'))
def cr_response_code(cr_response, code):
    """ Assert the status response to be 201 """
    assert cr_response.status_code == code


# Then Steps
@then(parsers.parse('the response contains results for {name}'))
def cr_response_contents(cr_response, name):
    """ Assert the response to has the repo name """
    assert name.lower() == cr_response.json()['name'].lower()


# Get the list of repositories in a GitHub organization
# Given Steps
@given(parsers.parse("I send the request to get repositories list"), target_fixture="gr_response")
def get_repos():
    """ Send the request to get a repos list """
    response = requests.get(GITHUB_REPOS)
    return response


# When Steps
@when(parsers.parse('the response has a list of repositories'))
def repos_response(gr_response):
    """ Assert repos quantity """
    assert (len(gr_response.json())) >= 1


# Then Steps
@then(parsers.parse('the response contains repositories {name}'))
def repos_names(gr_response, name):
    """ Assert the response has the repo names """
    count_names = False
    for i in range(0, len(gr_response.json())):
        if gr_response.json()[0]['name'] == name:
            count_names = True

    assert count_names


# Delete a repository in a GitHub organization
# Given Steps
@given(parsers.parse("I send to delete the org repository {name}"), target_fixture="dr_response")
def get_repos(name):
    """ Send the request to delete a repo """
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer " + API_TOKEN
    response = requests.delete(GITHUB_REPO + name, headers=headers)
    return response


# Then Steps
@then(parsers.parse('the response code is "{code:d}"'))
def repos_names(dr_response, code):
    """ Assert the status response to be 204 """
    assert dr_response.status_code == code

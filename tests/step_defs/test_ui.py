import os
import time
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenarios, given, when, then

# Scenarios
scenarios('../features/ui.feature')

# Shared Variables
load_dotenv()
GITHUB_LOGIN_PAGE = os.getenv('GITHUB_LOGIN_PAGE')
HOME_PAGE_URL = os.getenv('HOME_PAGE_URL')
REPOS_PAGE_URL = os.getenv('REPOS_PAGE_URL')
NEW_REPO_URL = os.getenv('NEW_REPO_URL')
NEW_REPO_PAGE = os.getenv('NEW_REPO_PAGE')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
REPOSITORY_NAME = os.getenv('REPOSITORY_NAME')
REPOSITORY_DESCRIPTION = os.getenv('REPOSITORY_DESCRIPTION')


# Fixtures
@pytest.fixture
def browser_simple():
    """ The fixture without the login steps """
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()


@pytest.fixture
def browser():
    """ The fixture including the login steps """
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    b.get(GITHUB_LOGIN_PAGE)
    email_input = b.find_element(By.ID, 'login_field')
    password_input = b.find_element(By.ID, 'password')
    login_button = b.find_element(By.XPATH, '//*[@value="Sign in"]')
    email_input.send_keys(EMAIL)
    password_input.send_keys(PASSWORD)
    login_button.click()
    yield b
    b.quit()


# Login to GitHub
# Given Steps
@given('I am on the login page', target_fixture='gh_login')
def gh_login_page(browser_simple):
    browser_simple.get(GITHUB_LOGIN_PAGE)


# When Steps
@when('I enter the correct email and password')
def login(browser_simple):
    email_input = browser_simple.find_element(By.ID, 'login_field')
    password_input = browser_simple.find_element(By.ID, 'password')
    login_button = browser_simple.find_element(By.XPATH, '//*[@value="Sign in"]')

    email_input.send_keys(EMAIL)
    password_input.send_keys(PASSWORD)
    login_button.click()


# Then Steps
@then('I see the user home page')
def home_page(browser_simple):
    get_url = browser_simple.current_url
    assert get_url == HOME_PAGE_URL


# Get the list of repositories in GitHub
# Given Steps
@given('I am in the the home page')
def get_repos_page(browser):
    get_url = browser.current_url
    assert get_url == HOME_PAGE_URL


# When Steps
@when('I go to the repos page')
def get_repos_page(browser):
    browser.get(REPOS_PAGE_URL)


# Then Steps
@then('I see the repos')
def repos_page(browser):
    get_url = browser.current_url
    assert get_url == REPOS_PAGE_URL
    repos_list = browser.find_elements(By.CSS_SELECTOR, 'div#user-repositories-list > ul > li > div');
    assert len(repos_list) >= 1


# Create a repository in GitHub
# When Steps
@when('I go to the new repo page')
def get_new_repo_page(browser):
    browser.get(NEW_REPO_URL)


@when('I create a repo')
def create_repo(browser):
    repository_name_input = browser.find_element(By.ID, 'repository_name')
    repository_description_input = browser.find_element(By.ID, 'repository_description')
    create_button = browser.find_element(By.XPATH, '//button[@class="btn-primary btn"]')

    repository_name_input.send_keys(REPOSITORY_NAME)
    repository_description_input.send_keys(REPOSITORY_DESCRIPTION)
    time.sleep(2)
    create_button.click()


@then('I am in the new repo page')
def go_repo_page(browser):
    get_url = browser.current_url
    assert get_url == NEW_REPO_PAGE

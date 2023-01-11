# About The Project
The project has the testing suites to solve the GoSpace QA  assessment.

## Getting Started
This file contains a summary of the project and guidelines for setup and executions of implemented tests.

### Prerequisites
The Python (version 3.10) libraries needed to run the project can be found in the file **requirements.txt**.

To install them it is necessary to execute the following command
* python
  ```sh
  pip install -r requirements.txt
  ```
  
### Parameters File
In order to avoid parameter coding and use environment variables, it is necessary to use a **.env** file in the main path of the project.

An example of this file is shown below.
* .env
  ```plain 
  GITHUB_REPOS_LIST = 'https://api.github.com/orgs/Insityou/repos'
  GITHUB_REPO_CREATED = 'https://api.github.com/repos/Insityou/'
  GITHUB_LOGIN_PAGE = 'https://github.com/login'
  REPOS_PAGE_URL = 'https://github.com/eespinoza-ja?tab=repositories'
  NEW_REPO_URL = 'https://github.com/new'
  HOME_PAGE_URL = 'https://github.com/'
  NEW_REPO_PAGE = 'https://github.com/eespinoza-ja/test-repo-gospace'
  API_TOKEN = '***************************************************************'
  USERNAME = 'test_user'
  PASSWORD = ***************
  REPOSITORY_NAME = 'test-repo-gospace'
  REPOSITORY_DESCRIPTION = 'A testing repo'
  ```
  
## Usage
There are two types of testing approaches. API testing and GitHub UI testing. Therefore, you can execute the one you need.

### Run API Tests
Use the following command
* sh
```sh
python -m pytest --verbose -k "api" --html=report-api-testing.html
```

### Run UI Tests
Use the following command
* sh
```sh
python -m pytest --verbose -k "ui" --html=report-ui-testing.html
```

## Artifacts
The above commands generate an HTML file each. These files have a summary of the executed test cases.

### HTML API Tests
The file name is **report-api-testing.html**, it contains a small report with information of the last API testing execution.

### HTML UI Tests
The file name is **report-ui-testing.html** , it contains a small report with information of the last UI testing execution.

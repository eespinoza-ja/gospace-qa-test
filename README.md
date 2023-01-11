## Getting Started
This file contains a summary of the project and guidelines for setup and executions of implemented tests.

### Prerequisites
The Python (version 3.10) libraries needed to run the project can be found in the file **requirements.txt**.

To install them it is necessary to execute the following command
* python
  ```sh
  pip install -r requirements.txt
  ```
## Usage
There are two types of testing approaches. API testing and GitHub UI testing. Therefore, you can execute the one you need.

### Run API Tests
Use the following command
* python
```sh
python -m pytest --verbose -k "api" --html=report-api-testing.html
```

### Run UI Tests
Use the following command
* python
```sh
python -m pytest --verbose -k "ui" --html=report-ui-testing.html
```

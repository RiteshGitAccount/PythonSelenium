# Python-Test-Automation-Framework

# Description

This is a sample project for automating day to day manual test cases which are performed on web browsers.
This project will help testers perform there task efficiently and provide the detailed results to respective
stakeholders.

### Features

- Has generic in built functions for keyboard actions, mouse actions and file actions.
- Ready to use utilities for reading/writing into Excel and reading Prop/JSON files.
- Option to send email with attachments after every run.
- Reporting capability using Allure Reports to generate detailed test reports.
- Custom logging feature that can be implemented for each step of the test case.
- Support Chrome/Firefox/Edge Driver auto installation/upgrade

# Prerequisite

* Python >= 3x
* Allure commandline tool
* Pycharm or any other IDE for code edition and access

# Tech details

* Automation Tool - Selenium
* Programming Language - Python
* Framework - Pytest

# Setup / Installation

- Clone Repository in local system
- Create virtual environment "python -m venv venv"
- Activate virtual environment "venv/Scripts/activate"
- Need to install the dependencies mentioned in "requirements.txt" using command 'pip install -r requirements.txt'

# How to create new Test Cases

- Under folder 'page_objects' create page-wise classes for all pages for the application under test.
- Each page function class should inherit the BaseClass.
- Each page function class should contain all methods to performs actions on that particular web page eg: Login(self) /
  Logout(self)
  etc.
- Log statements can be added as and when needed.
- Generic functions mentioned in Base class should be used while creating the methods.
    - e.g.-
        - To enter text user --> send_text
        - To click on the button -->
          click_element
- To write a code for click_element the syntax would be
    - click_element(self, locator, locator_type="xpath")
        - if locator = "Inputs" and locator_type = "link" then the statement would be as follows:
          - self.click_element("Inputs", locator_type="link")

# How to run the Test Cases

- The test cases can be executed from IDE by right click on 'tests' folder and selecting the Run button.
- To execute the test from Terminal or Command Prompt use the following command:
    - py.test -v -s --alluredir="report_path"
- To view allure reports use the command:
    - allure serve \<reports directory path>
- To re-run only the failed test cases, add flag :
    - --lf
- To re-run test cases with specific severities, add flag :
    - --allure-severities <severity_name>
- To re-run test cases with specific feature, add flag :
    - --allure-features <feature_name>
- To re-run test cases with specific story, add flag :
    - --allure-stories <story_name>
- To re-run only the priory test cases, add flag :
    - -m "p1"
- Framework can also be integrated with CI tools like Jenkins to run the test cases in cloud.

# References
- For allure reporting and framework details-> https://docs.qameta.io/allure/
- For pytest framework - online content available e.g
  - https://www.guru99.com/pytest-tutorial.html
  - https://docs.pytest.org/en/7.1.x/getting-started.html
  - https://www.tutorialspoint.com/pytest/index.htm
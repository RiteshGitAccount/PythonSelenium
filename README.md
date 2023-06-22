# Python-Test-Automation-Framework

Automation Suite - Selenium
Programming Language - Python

# Description

The selenium python automation framework has the following features:

- Framework follows Page Object Model
- Has generic in built functions for keyboard actions, mouse actions and file actions.
- Ready to use utilities for reading/writing into excel and reading JSON files.
- Option to send email with attachments after every run.
- Reporting capability using Allure Reports to generate detailed test reports.
- Custom logging feature that can be implemented for each step of the test case.
- Chrome Driver auto upgrade

# Installation

- Need to install the dependencies mentioned in "requirements.txt" using command 'pip install -r requirements.txt'

# Create new Test Cases

- Under folder 'page_objects' create page-wise classes for all pages for the application under test.
- Each class should inherit the BaseClass.
- Each class should contain all methods to performs actions on that particular web page eg: Login(self) / Logout(self) etc.
- Log statements can be added as and when needed.
- Generic functions mentioned in Base class(eg: to enter text user --> send_text/to click on the button --> click_elements) 
  should be used while creating the methods.
- To write a code for click_element the syntax would be "click_element(self, locator, locator_type="xpath")"
  if locator = "Inputs" and locator_type = "link" then the statement would be as follows:
  self.click_element("Inputs", locator_type="link")

# Run the Test Cases

- The test cases can be executed from IDE by right click on 'tests' folder and selecting the Run button.
- To execute the test from Terminal or Command Prompt use the following command: py.test -v -s --alluredir="report_path"
- To view allure reports use the command : allure serve <reports directory path>
- To re-run only the failed test cases use the command : pytest -v -s --lf .\tests\ --alluredir="report_path"
- Framework can also be integrated with CI tools like Jenkins to run the test cases in cloud.
  ## run by caegories add code



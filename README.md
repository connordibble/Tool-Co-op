
# Tool Stack: #
Everyone will be running Python 3.7

Django 3.0.2
# Version-Control Procedure: #
The procedure that we are going to be following is to have one master branch that any code that is going to be added has been reviewed by at least one team member and then we will have our own branches that we will do our own work on.
# Naming Scheme/Organization: # 
The naming scheme that we are going to be following is the lowerCamelCase for variables and class names as UpperCamelCase. 

We are going to follow the standard Django organization scheme.

# Build Instructions: #
Install Python 3

Install Django:
`pip install Django`

Pull latest code from specified branch.

Then run: `python manage.py runserver`

# Unit Testing Instructions: #
While using the unittest.TestCase library we must have `__init__.py` file in our `test/` directory

The test directory must be named `test/` with the test files matching pattern `test_*.py` 

Subdirectories can have any name.

Run all tests with `python -m unittest`

# System Testing Instructions: #

We will go through our use case diagrams or requirements doc and make sure that it is working as expected.


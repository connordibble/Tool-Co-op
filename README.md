
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

Run: `python manage.py migrate`

Then run: `python manage.py runserver`

# Unit Testing Instructions: #
While using the unittest.TestCase library Django automatically generates a test.py file that will contain our unit test.
in order to run all of the unit tests use the command `python manage.py test`

# System Testing Instructions: #
We will go through our use case diagrams or requirements doc and make sure that it is working as expected.


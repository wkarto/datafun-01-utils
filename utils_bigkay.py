''' ITERATION 3

Module: Venirr Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Process:

In this third iteration, I declare additional variables to show skills with different data types.
'''

#####################################
# Declare global variables - keep byline at the end 
# We will use this information in a smarter byline 
#####################################
# Boolean variable to indicate if the company has internation clients
has_international_clients: bool = False

# Integer variable for the number of years in operation
years_in_operation: int = 4

# List of strings representing the skills offered by the company
skills_offered: list = ["Data Engineering", "Artificial Intelliegnce", "Machine Learning"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.7, 5.0, 4.5]

# List of clients
clients = ['ABC', 'XYZ', 'IJK']

#####################################
# Declare a global variable named byline.
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
---------------------------------------------------
Venirr Analytics: Delivering Professional Insights
---------------------------------------------------
Has International Clients:      {has_international_clients}
Years in Operation:             {years_in_operation}
Clients:     {clients}
Skills Offered:                 {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}

"""

#####################################
# Define the get_byline() Function.
#####################################

def get_byline() -> str:
   ''' Return a byline for my analytics projects.'''
   return byline

#####################################
# Define a main() function for this module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()

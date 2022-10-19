"""
Contains example of monkey patching in python.

Monkey patching when we dynamically alter the behavior of a
piece of code at run time

Classes:

    Employee

Functions:

    None

Misc variables:

    None
"""


class Employee:
    """
    Example Employee class with a predefined raise amount
    """

    def __init__(self, first_name: str, last_name: str) -> None:
        """Initialize the class with provided variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = 10_000

    def get_email(self) -> str:
        """Returns the email from the defined names"""
        return f"{self.first_name.lower()}.{self.last_name.lower()}@company.com"


def say_hello(self):
    """Method that returns hello"""
    return "Hello"


# The first employee instance created will print the
# correct employee email
emp1 = Employee(first_name="John", last_name="Doe")
print(emp1.get_email())
# Will print instead of 'john.doe@company.com'

# *** MONKEY PATCH 1 ***
#
# We completely replace the method to get user email
# with a method that always returns a string 'Hello'
# Any instance created after the line will be altered
# as python is executes sequentially (line by line)
#
Employee.get_email = say_hello

# After we have applied a monkey patch
emp2 = Employee(first_name="Jane", last_name="Doe")
print(emp2.get_email())
# Will print "Hello" instead of 'jane.doe@company.com'

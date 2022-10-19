"""
Contains a method to check whether a number is an Armstrong numer.

A number is considered to be an Armstrong number if the power of it's
individual items added together results in the same number.

E.g An Armstrong check of order 3 would be

123 = (1*1*1) + (2*2*2) + (3*3*3)

Classes:

    None

Functions:

    is_armstrong_number(number: int):
        recieves an integer and returns True if it is an
        Armstrong number and False if not

Misc variables:

    None
"""


def is_armstrong_number(number: int) -> bool:
    """
    Returns True if 'number' is an Armstrong number and False otherwise.

    Parameters:
        number (int):
            The number to be checked

    Returns:
        bool:
            True if the number is Armstrong or Fasle if not

    Raises:
        None
    """

    pass


if __name__ == "__main__":
    print(is_armstrong_number(number=123))

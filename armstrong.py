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
    The 'length' of the number will be consider as the order.

    Parameters:
        number (int):
            The number to be checked

    Returns:
        bool:
            True if the number is Armstrong or Fasle if not

    Raises:
        None
    """

    if number < 0:
        return False

    order = len(str(number))

    numbers = [int(i) ** order for i in str(number)]

    return sum(numbers) == number


if __name__ == "__main__":
    print(is_armstrong_number(number=123))
    print(is_armstrong_number(number=407))
    print(is_armstrong_number(number=153))
    print(is_armstrong_number(number=100))

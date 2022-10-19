"""
Contains methods that can shuffle items in a list 

Classes:

    None

Functions:

    shuffle(input_list: list[str | int]):
        recieves the input list and returns list of the items shuffled

Misc variables:

    None
"""
import random

from typing import List, Union


def shuffle(input_list: List[Union[int, str]]):
    """
    Recieves an input list and returns a shuffled version of it.
    The output will return a randomly shuffled version every execution time

    Parameters:
        input_list (list[int | str]):
            The input list to be shufled

    Returns:
        output_list (list[int | str]):
            The shuffled version of the input list

    Raises:
        None
    """

    random.shuffle(input_list)

    return input_list


if __name__ == "__main__":
    example_list = ["A", "D", 1, 100]

    print(shuffle(input_list=example_list))

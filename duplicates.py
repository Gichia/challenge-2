"""
Contains a class Duplicate with a method that recieves a list
of numbers and returns an output list with diplicates from the original.

See method duplicates description

Classes:

    Duplicate

Functions:

    main(input_list):
        recieves the input list and returns list with any duplicates

Misc variables:

    None
"""

class Duplicate:
    """
    The duplicate class to implement method to return duplicates in a list

    ...

    Attributes
    ----------
    None

    Methods
    -------
    get_duplicates(input_list: list[int]):
        Returns a list of duplicate items from the input list
    """

    @classmethod
    def get_duplicates(cls, input_list: list[int]) -> list[int]:
        """
        Returns a list of any duplicate items from the input list

        Parameters:
            input_list (list[int]):
                The input list

        Returns:
            output_list (list[int]):
                The output list containing any duplicates

        Raises:
            None
        """

        output_list = [el for el in input_list if input_list.count(el) > 1]

        return list(set(output_list))


if __name__ == "__main__":
    test_li = [10, 2, 11, 2, -1, -1, -1, 10, 30]

    print(Duplicate.get_duplicates(input_list=test_li))

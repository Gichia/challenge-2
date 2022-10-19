"""
Contains method to draw a star pattern.

Classes:

    None

Functions:

    draw_star():
        Prints a star pattern of height provided

Misc variables:

    None
"""


def draw_star(n: int = 4) -> None:
    """Method to draw a start pattern of height 4"""

    for i in range(1, n + 1):
        print(" " * (n - i), "*" * i)
    
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), "*"*i)
    

if __name__ == "__main__":
    draw_star()

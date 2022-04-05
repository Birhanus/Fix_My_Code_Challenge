#!/usr/bin/python3
"""Define square class that return area of the square and
   permiter of the square
"""


class square():

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Square class initialized """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Permiter of the square """
        return self.width + self.width + self.height + self.height

    def __str__(self):
        """ String representation of the square instance """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create Square instance """
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())

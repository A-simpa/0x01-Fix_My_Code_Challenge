#!/usr/bin/python3

class Square():

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 2 and \
         (list(kwargs.values())[0] == list(kwargs.values())[1]):
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif len(args) == 2 and (args[0] == args[1]):
            self.width = a[0]
            self.height = a[1]

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())

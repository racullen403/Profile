import random


class Dice:

    """Basic Class for created a n-sided dice and rolling it

        Instance Variables:
            - val: current value of the die
            - n_sides: number of sides of the die
    """

    def __init__(self, n):
        self.n_sides = n
        self.val = self.roll()

    def roll(self):
        self.val = random.randint(1, self.n_sides)
        return self.val

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return "Dice({}) : {}".format(self.n_sides, self.val)


# __str__ let's us change how print function works
print(Dice(20))


# __repr__ gives a print out of the object in a list
roll_list = [Dice(6), Dice(20)]
print(roll_list)
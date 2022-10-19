"""
Let us now consider the Tower of Hanoi problem:

    There are 3 poles, we must move all the disks from one pole to the last pole, with only
    2 constraints, we can only move one disk at a time and a larger disk cannot be placed
    on top of a smaller disk.

    E.G.

        1
        2
        3
        4
        _      _       _
        A       B       C

        We have a tower of 4 disks, logically we would move the tower of 3 disks to B,
        move disk 4 to C, and then move the tower of 3 disks to C.

        However, we can only move one disk at a time, so to move the tower of 3 disks to B,
        we move a tower of 2 disks to C, move disk 3 to B, then move the tower of 2 from C
        to B.

        But to move the tower of 2 disks to C we have to move disk 1 to B, move disk 2 to C,
        then move disk 1 from B to C. This is our base case, when we are moving a tower of
        height 1 (a single disk).

        Consider for poles A, B and C, where A is the starting pole, B is the empty
        middle pole and C is the empty last pole we want to move the disks to:

            1. Move tower height-1 from start A to middle pole B, using the final
            pole C as temp intermediate.
            2. Move remaining disk from start pole A to final pole C.
            3. Move tower height-1 from middle pole B to final pole C, using the
            start pole A as the temp intermediate.
"""


class HanoiTowers:

    def __init__(self, size=5):
        self.poles = [list(range(size, 0, -1)), [], []]
        self.height = size

    def move_tower(self):
        self.move_tower_height(self.height, self.poles[0], self.poles[1], self.poles[2])

    def move_tower_height(self, height, start, intermediate, end):
        if height > 0:
            self.move_tower_height(height-1, start, end, intermediate)
            self.move_disk(start, end)
            print("\n----- Swap -----")
            self.show_towers()
            self.move_tower_height(height-1, intermediate, start, end)

    def move_disk(self, start, end):
        end.append(start.pop())

    def show_towers(self):
        a = ["A", "B", "C"]
        for i in range(3):
            print(a[i] + ":" + str(self.poles[i]), end="  ")
        print()


def example():
    towers = HanoiTowers()
    towers.move_tower()


example()

"""
Let us now consider the Tower of Hanoi problem:

    There are 3 poles, we must move all the disks from one pole to the last pole, with only
    2 constraints, we can only move one disk at a time and a larger disk cannot be placed
    on top of a smaller disk.

    E.G.

        1
        2
        3
        4       _       _
        A       B       C

        We have a tower of 4 disks, logically we would move the tower of 3 disks to B,
        move disk 4 to C, and then move the tower of 3 disks to C.

        However we can only move one disk at a time, so to move the tower of 3 disks to B,
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


def move_tower(height, start, final, intermediate):
    if height >= 1:
        move_tower(height-1, start, intermediate, final)
        move_disk(start, final, intermediate)
        move_tower(height-1, intermediate, final, start)


def move_disk(start, final, inter):
    print("\nMoving disk from {}: {} to {}: {}".format(start[0], start[1], final[0], final[1]))
    final[1].append(start[1].pop())
    print("  --->   {}:{}     {}:{}    {}:{}".format(start[0], start[1], final[0], final[1], inter[0], inter[1]))

move_tower(4, ("A", [4, 3, 2, 1]), ("C", []), ("B", []))
"""
Given a list of objects, we will create a new list containing all possible subsets of the original list.
"""


# Assuming all objects in list are unique, this will produce a list of all subsets
def create_subsets(input_list):
    n = len(input_list)
    objs = [([input_list[i]], i) for i in range(n)]
    subsets = [[]]
    while objs:
        obj = objs.pop()
        subsets.append(obj[0])
        for i in range(obj[1]+1, n):
            objs.append((obj[0] + [input_list[i]], i))
    return subsets


def example1():
    input_list = ["1", "2", "3", "4"]
    print("Starting Set:", input_list)
    subs = create_subsets(input_list)
    print("Subset List:", subs)


# In the case of non-unique objs, we sort first to extract only unique objs
def create_subsets_v2(input_list):
    objs = []
    lookup = {}
    for obj in input_list:
        if lookup.get(obj) is None:
            objs.append(obj)
            lookup[obj] = True
    return create_subsets(objs)


def example2():
    input_list = ["1", "2", "1", "3", "2", "1", "3"]
    print("Starting Set:", input_list)
    subs = create_subsets_v2(input_list)
    print("Subset List:", subs)




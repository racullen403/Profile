import random
from matplotlib import pyplot as plt, animation


# generator to yield the state of the list each time a swap occurs or we reach the end
def bubble_sort(alist):
    swap = False
    for last_item in range(len(alist) - 1, 0, -1):
        for i in range(last_item):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                swap = True
            yield alist, i, last_item
        if swap is False:
            return


def visualize(list_length=20):
    # create the list 1-20 and randomise it, then create generator for the sorting
    # algorithm
    alist = list(range(1, list_length+1))
    random.shuffle(alist)
    generator = bubble_sort(alist)

    # fig is the top level container, holding all plot elements
    # ax is single Axes Object, or an array of objects
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort")
    ax.set_xlim(-1, list_length)

    # bar plot (x-coords, height)
    bar_sub = ax.bar(range(len(alist)), alist)

    # helper to update frames in the plot (bar_sub)
    def update(new_values, old_values):
        i = 0
        for old, new in zip(old_values, new_values[0]):
            old.set_color("b")
            if i == new_values[1]+1:
                old.set_color("r")
            if i > new_values[2] or new_values[2] <= 2:
                old.set_color("g")
            old.set_height(new)
            i += 1

    # create animation object that repeatedly calls the update function
    # the first argument of func is called in "frames=..." ie our generator
    # additional position args can be passed into "fargs=..."
    vis = animation.FuncAnimation(fig,
                                  func=update,
                                  frames=generator,
                                  fargs=[bar_sub],
                                  repeat=False,
                                  interval=200)
    
    plt.show()
    plt.close()
    

visualize(list_length=20)
import random
from matplotlib import pyplot as plt, animation


# selection sort generator
def gen_selection_sort(a):
    for i in range(len(a)):
        largest = 0
        for j in range(len(a)-i):
            if a[j] > a[largest]:
                largest = j
            yield a, j, largest, len(a)-1-i
        a[largest], a[len(a)-1-i] = a[len(a)-1-i], a[largest]
        yield a, len(a)-1-i, largest, len(a)-1-i
    return


def visualise(n=30):
    a = list(range(1, n+1, 1))
    random.shuffle(a)
    generator = gen_selection_sort(a)
    fig, ax = plt.subplots()
    ax.set_xlim(-1, n)
    bar_sub = ax.bar(range(len(a)), a)

    def updater(new_values, old_values):
        i = 0
        for new, old in zip(new_values[0], old_values):
            old.set_color("b")
            if i == new_values[1]:
                old.set_color("r")
            if i == new_values[2]:
                old.set_color("yellow")
            if i > new_values[3] or new_values[3] == 0:
                old.set_color("g")
            old.set_height(new)
            i += 1

    vis = animation.FuncAnimation(fig,
                                  func=updater,
                                  frames=generator,
                                  fargs=[bar_sub],
                                  interval=50,
                                  repeat=False)

    plt.show()
    plt.close()

visualise(n=20)
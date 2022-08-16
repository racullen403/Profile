import random
from matplotlib import pyplot as plt, animation


def gen_insertion_sort(a):
    for i in range(len(a)):
        store = a[i]
        j = i-1
        yield a, i, j, False
        while j >= 0 and a[j] > store:
            a[j+1] = a[j]
            yield a, i, j, False
            j -= 1
        a[j+1] = store
        yield a, i, j, True
    yield a, i, j, None


def visualize(n=20):
    a = list(range(1, n+1))
    random.shuffle(a)
    generator = gen_insertion_sort(a)

    fig, ax = plt.subplots()
    ax.set_title("Insertion Sort")
    ax.set_xlim(-1, n+1)

    bar_sub = ax.bar(range(len(a)), a)

    def updater(new_values, old_values):
        i = 0
        for new, old in zip(new_values[0], old_values):
            old.set_color("b")
            if i == new_values[1]:
                old.set_color("y")
            if i < new_values[1]:
                old.set_color("g")
            if i == new_values[2]:
                old.set_color("r")
            if new_values[3] is True and i == new_values[2]:
                old.set_color("purple")
            if new_values[3] is None:
                old.set_color("g")
            old.set_height(new)
            i += 1

    vis = animation.FuncAnimation(fig,
                                  func=updater,
                                  frames=generator,
                                  fargs=[bar_sub],
                                  repeat=False,
                                  interval=100)
    plt.show()
    plt.close()


visualize(n=20)


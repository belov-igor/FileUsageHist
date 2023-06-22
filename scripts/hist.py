# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib


def hist_drawer(title, x_axis, y_axis, x_label, y_label):
    """

    """
    matplotlib.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots()

    # Нарисовать горизонтальную гистограмму методом barh
    ax.barh(range(len(y_axis)), x_axis, height=0.7, color='steelblue', alpha=0.8)  # Рисуем снизу вверх
    ax.set_yticks(range(len(y_axis)))
    ax.set_yticklabels(y_axis)

    ax.set_xlabel(x_label)
    ax.set_title(title)

    for x, y in enumerate(x_axis):
        ax.text(y + 0.2, x - 0.1, '%s' % y)

    plt.savefig("test1.png")
    plt.show()

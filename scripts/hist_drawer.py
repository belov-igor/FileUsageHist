# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib


def hist_drawer(title, x_axis, y_axis, x_label, name):
    """
    Рисует горизонтальную гистограмму на основе переданных данных и сохраняет ее в файл.
    :param title: Заголовок гистограммы.
    :param x_axis: Список значений для оси X.
    :param y_axis: Список значений для оси Y.
    :param x_label: Название оси X.
    :param name: Имя файла для сохранения гистограммы.
    :return: None.
    """

    matplotlib.rcParams['axes.unicode_minus'] = False  # использовать обычный символ минус (-) вместо символа Unicode

    # Создание фигуры и осей графика
    fig, ax = plt.subplots()

    # Нарисовать горизонтальную гистограмму методом barh
    ax.barh(range(len(y_axis)), x_axis, height=0.7, color='steelblue', alpha=0.8)  # Рисуем снизу вверх
    ax.set_yticks(range(len(y_axis)))
    ax.set_yticklabels(y_axis, fontsize=8)
    ax.set_xlabel(x_label)
    ax.set_title(title)

    # Добавление значений на гистограмму
    for x, y in enumerate(x_axis):
        ax.text(y + 0.2, x - 0.1, '%s' % y)

    # Регулировка отступов и сохранение гистограммы в файл
    plt.subplots_adjust(left=0.21)
    plt.savefig(name)
    plt.show()

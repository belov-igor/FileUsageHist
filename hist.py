import matplotlib.pyplot as plt
import matplotlib

# matplotlib.rcParams['axes.unicode_minus'] = False

price = [39.5, 39.9, 45.4, 38.9, 33.34]
categories = ['host1', "host2", "host3", 'host4', 'host5']

fig, ax = plt.subplots()

# Нарисовать горизонтальную гистограмму методом barh
ax.barh(range(len(categories)), price, height=0.7, color='steelblue', alpha=0.8)  # Рисуем снизу вверх
ax.set_yticks(range(len(categories)))
ax.set_yticklabels(categories)

ax.set_xlabel("%")
ax.set_title("Цены на книги на разных площадках")

for x, y in enumerate(price):
    ax.text(y + 0.2, x - 0.1, '%s' % y)

plt.savefig("test2.webp")
plt.show()

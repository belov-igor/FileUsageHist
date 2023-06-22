import plotly.graph_objects as go
import plotly.io as pio

# Входные данные для гистограммы
data = [1, 2, 3, 4, 5, 4, 3, 2, 1]

# Построение гистограммы
fig = go.Figure(data=[go.Histogram(x=data)])

# Преобразование графика в HTML-страницу
html = pio.to_html(fig, full_html=False)

# Вывод HTML-кода
print(html)

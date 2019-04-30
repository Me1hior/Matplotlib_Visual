import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# plot() строит осмысленное графическое представление для данных
# plt.plot(squares)
plt.plot(input_values, squares, linewidth=2)

# Назначение заголовка диаграммы
plt.title("Square Numbers", fontsize=24)

# Назначение заголовка меток осей.
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', labelsize=14)


# +++ Назначение диапазона для каждой оси.
#plt.axis([0, 300, 0, 90000])


# Нанесение и оформление отдельных точек функцией scatter()

#1) Нанесение точки на графике
# plt.scatter(2, 4)
# plt.scatter(2, 4, s=200)            # аргумент s задает размер точек

#2) вывести на диаграмме серию точек
#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]
#plt.scatter(x_values, y_values, s=100)

#3) Автоматическое вычисление данных
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
#plt.scatter(x_values, y_values, edgecolor='none',  s=20)   # арг. edgecolor='none' удаляет контуры вокруг точек
#plt.scatter(x_values, y_values,  c='red', edgecolor='none',  s=20)    # арг. с='' - color цвет
#plt.scatter(x_values, y_values,  c=(1, 0.5, 0.8), edgecolor='none',  s=20)

#4) Цветовая карта
#  передаем в c список y-values, а затем указываем pyplot, какая цветовая
# карта должна использоваться, при помощи аргумента cmap.
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
# Все цветовые карты, доступные в pyplot, можно просмотреть на сайте http://matplotlib.org/; откройте раздел Examples,
# прокрутите содержимое до пункта Color Examples и щелкните на ссылке colormaps_reference

# Можно либо вывести инфу на экран, либо сохранить инфу в файл


# Вызов plt.show() открывает окно просмотра matplotlib и выводит график
plt.show()

# Автоматическое сохранение диаграмм
#plt.savefig('squares_plot.png', bbox_inches='tight')    # Первый аргумент содержит имя файла для сохранения диаграммы;
                                                        # Второй аргумент отсекает от диаграммы лишние пропуски.




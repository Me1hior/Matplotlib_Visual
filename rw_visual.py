import matplotlib.pyplot as plt
from randomwalk import RandomWalk


#1) Вывод случайного блуждания

# Построение случайного блуждания и нанесение точек на диаграмму.
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=5)
plt.show()


'''
#2) Генерирование нескольких случайных блужданий
# Новые блуждания строятся до тех пор, пока программа остается активной.
while True:
	# Построение случайного блуждания и нанесение точек на диаграмму.
	rw = RandomWalk()
	rw.fill_walk()
	plt.scatter(rw.x_values, rw.y_values, s=5)
	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
'''

'''
#3) Оформление случайного блуждания
# Назначение цветов
# Мы используем цветовую карту для отображения точек блуждания
while True:
	# Построение случайного блуждания и нанесение точек на диаграмму.
	rw = RandomWalk()
	rw.fill_walk()
	point_numbers = list(range(rw.num_points))
	# функция range() используется для генерирования списка чисел, размер
	# которого равен количеству точек в блуждании. Полученный результат сохраняется
	# в списке point_numbers, который используется для назначения цвета каждой точки
	# в блуждании. 
	
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens, edgecolor='none', s=15)
	# передаем point_numbers в аргументе c, используем цветовую карту
	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
'''

'''
#4) Начальные и конечные точки + Удаление осей
while True:
	# Построение случайного блуждания и нанесение точек на диаграмму.
	rw = RandomWalk(50000)
	rw.fill_walk()
	
	# Назначение размера области просмотра.
	plt.figure(figsize=(20, 12))
	# Функция figure() управляет шириной, высотой, разрешением и цветом фона
	# диаграммы. Параметр figsize получает кортеж с размерами окна диаграммы
	# в дюймах.

	point_numbers = list(range(rw.num_points))
	# функция range() используется для генерирования списка чисел, размер
	# которого равен количеству точек в блуждании. Полученный результат сохраняется
	# в списке point_numbers, который используется для назначения цвета каждой точки
	# в блуждании. 
	
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=5)
	# передаем point_numbers в аргументе c, используем цветовую карту
	
	# Выделение первой и последней точек.
	plt.scatter(0, 0, c='green', edgecolor='black', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='black', s=100)
	
	# Удаление осей.
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
'''

'''
#4) Молекулярное движение: 
while True:
	# Построение случайного блуждания и нанесение точек на диаграмму.
	rw = RandomWalk(5000)
	rw.fill_walk()
	
	# Назначение размера области просмотра.
	plt.figure(figsize=(20, 12))
	# Функция figure() управляет шириной, высотой, разрешением и цветом фона
	# диаграммы. Параметр figsize получает кортеж с размерами окна диаграммы
	# в дюймах.

	point_numbers = list(range(rw.num_points))
	# функция range() используется для генерирования списка чисел, размер
	# которого равен количеству точек в блуждании. Полученный результат сохраняется
	# в списке point_numbers, который используется для назначения цвета каждой точки
	# в блуждании. 
	
	plt.plot(rw.x_values, rw.y_values, linewidth=2)
	# передаем point_numbers в аргументе c, используем цветовую карту
	
	# Выделение первой и последней точек.
	plt.scatter(0, 0, c='green', edgecolor='black', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='black', s=100)
	
	# Удаление осей.
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
'''

from random import choice
import matplotlib.pyplot as plt

"""Случайным блужданием (random walk) называется путь,
который не имеет четкого направления, но определяется
серией полностью случайных решений."""

class RandomWalk():
	"""Класс для генерирования случайных блужданий."""
	def __init__(self, num_points=5000):
		"""Инициализирует атрибуты блуждания."""
		self.num_points = num_points
		
		# Все блуждания начинаются с точки (0, 0).
		self.x_values = [0]
		self.y_values = [0]
			

	def fill_walk(self):
		"""Вычисляет все точки блуждания."""

		# Шаги генерируются до достижения нужной длины.
		while len(self.x_values) < self.num_points:
			x_step = get_step()
			y_step = get_step()
			
			if x_step == 0 and y_step == 0:
				continue

			# Вычисление следующих значений x и y.
			# следующее значение по x, мы прибавляем значение
			# x_step к последнему значению, хранящемуся в x_values
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			# Новые значения присоединяются к x_values
			# и y_values.
			self.x_values.append(next_x)
			self.y_values.append(next_y)
			
def get_step():
		direction = choice([1, -1])
		distance = choice([0, 1, 2, 3, 4])
		return  direction * distance
		


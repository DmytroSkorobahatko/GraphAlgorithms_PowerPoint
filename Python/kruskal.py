"""
Алгоритм Краскала, пошук мінімального дерева графа
"""


class KruskalAlgorithm:
	def __init__(self, graph, file_out_path):
		self.graph = graph  # (weight, v1, v2)
		self.graph_sorted = sorted(self.graph, key=lambda x: x[0])
		self.connected = set()  # оброблені
		self.vertex_groups = {}  # группи
		self.tree = []  # відповідь
		self.path = file_out_path
		self.file = open(self.path, "a")  # зв'язок із файлом

	def Kruskal(self):
		for r in self.graph_sorted:  # ребра від меншого до більшого
			if r[1] not in self.connected or r[2] not in self.connected:  # хочаб одна вільна вершина
				if r[1] not in self.connected and r[2] not in self.connected:  # якщо вершини не з'єднані, то
					self.vertex_groups[r[1]] = [r[1], r[2]]
					self.vertex_groups[r[2]] = self.vertex_groups[r[1]]
					# формируем в словаре ключ с номерами вершин и связываем их с одним списком вершин
				else:
					if not self.vertex_groups.get(r[1]):  # если в словаре нет первой вершины, то
						self.vertex_groups[r[2]].append(r[1])  # добавляем в список первую вершину
						self.vertex_groups[r[1]] = self.vertex_groups[r[2]]  # и добавляем ключ с номером первой вершины
					else:
						self.vertex_groups[r[1]].append(r[2])  # иначе, все то же самое делаем со второй вершиной
						self.vertex_groups[r[2]] = self.vertex_groups[r[1]]

				self.tree.append(r)  # добавляем ребро до дерева
				self.connected.add(r[1])  # добавляем вершины в множество self.connected
				self.connected.add(r[2])

		for r in self.graph_sorted:  # проходим по ребрам второй раз и объединяем разрозненные группы вершин
			if r[2] not in self.vertex_groups[r[1]]:  # если вершины принадлежат разным группам, то объединяем
				self.tree.append(r)  # добавляем ребро в остов
				gr1 = self.vertex_groups[r[1]]
				self.vertex_groups[r[1]] += self.vertex_groups[r[2]]  # объединем списки двух групп вершин
				self.vertex_groups[r[2]] += gr1

	def WriteToFile(self):
		self.file.write(str(self.tree) + "\n")

	def PrintMinimalTree(self):
		print(self.tree)


import random
from mancalog.scripts.components.graph_component import GraphComponent


class Node(GraphComponent):
	
	def __init__(self, id):
		self._id = id
		# self._color = "blue"

	def get_labels(self):
		return Node._labels

	def __str__(self):
		return f'node({self._id})'

	def __hash__(self):
		return hash(str(self))

	def to_json_string(self):
		return '{"id":"' + str(self._id) + '", "label": "' + str(self._id) + '}'

	# def set_color(self, color):
	# 	self._color = color

	# def get_color(self):
	# 	return self._color

	def getId(self):
		return self._id

	def __eq__(self, node):
		result = False
		if isinstance(self, type(node)):
			result = self is node

			result = result or (self._id == node.getId())

		return result
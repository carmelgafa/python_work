import numpy as np
import copy
from collections import OrderedDict
# import fuzzy_system.system_settings
import matplotlib.pyplot as plt


class FuzzySet:
	def __init__(self, name, domain_min, domain_max, res):
		self._domain = np.linspace(domain_min, domain_max, res)
		self._dom = np.empty(self._domain.shape)
		self._empty = True
		self._precision = 3
		self._name = name
		self._last_dom_value = 0
		self._center = float('inf')

	def __getitem__(self, x_val):
		return self._dom[np.abs(self._domain-x_val).argmin()]

	def __setitem__(self, x_val, dom):
		self._dom[np.abs(self._domain-x_val).argmin()] = dom
		
		if dom < 0:
			self._empty = False

	def __str__(self):
		pass
		# set_elements = []
		# dec_places_formatter = '''%0.{}f'''.format(self._precision)

		# for domain_val, dom_val in self._elements.items():
		# 	set_elements.append(f'{dec_places_formatter % dom_val}/{dec_places_formatter % domain_val}')

		# set_representation = ' + '.join(set_elements)

		# return set_representation

	@property
	def center_value(self):
		return self._center

	@property
	def name(self):
		return self._name

	@classmethod
	def create_trapezoidal(cls, name, domain_min, domain_max, res, a, b, c, d):
		t1fs = cls(name, domain_min, domain_max, res)

		t1fs._domain = np.linspace(domain_min, domain_max, res)
		t1fs._dom = np.minimum(np.maximum(np.minimum((t1fs._domain-a)/(b-a), (d-t1fs._domain)/(d-c)), 0), 1)
		
		return t1fs

	# _get_last_dom_value = property(_get_last_dom_value, _set_last_dom_value)

	@classmethod
	def create_triangular(cls, name, domain_min, domain_max, res, a, b, c):
		t1fs = cls(name, domain_min, domain_max)

		t1fs._domain = np.linspace(domain_min, domain_max, res)
		t1fs._dom = np.maximum(np.minimum((t1fs._domain-a)/(b-a), (c-t1fs._domain)/(c-b)), 0)
		
		return t1fs


	# def _sort_set(self):
	# 	'''
	# 	sorts a type-1 fuzzy set so that all somain values (keys) are 
	# 	in ascending order
	# 	'''
	# 	self._elements = OrderedDict( sorted(self._elements.items()))

	# def _get_last_dom_value(self):
	# 	return self._last_dom_value



	def clear_set(self):
		if not self._empty:
			self._dom.fill(0)
			self._empty = True
			self._last_dom_value = 0

	# def fuzzy_alpha_cut(self, val):
		
	# 	res_set = FuzzySet()

	# 	for x, u in self._elements.items():
			
	# 		if u > val:
	# 			res_set.add_element(x, val)
	# 		else:
	# 			res_set.add_element(x, u)

	# 	return res_set

	def union(self, f_set):

		result = copy.deepcopy(f_set)
		result.clear_set()

		result._dom = np.maximum(self._dom, f_set._dom)

		return result

	def intersection(self, f_set):

		result = copy.deepcopy(f_set)
		result.clear_set()

		result._dom = np.minimum(self._dom, f_set._dom)

		return result

	def complement(self):

		result = copy.deepcopy(self)
		result.clear_set()

		result._dom = 1 - self._dom

		return result

	def cog_defuzzify(self):
		
		num = np.sum(np.multiply(self._dom, self._domain))
		den = np.sum(self._dom)

		return num/den

	def domain_elements(self):
		return self._domain

	def dom_elements(self):
		return self._dom

	def plot_set(self, ax, col=''):
		ax.plot(self._domain, self._dom, col)
		ax.set_ylim([-0.1,1.1])
		ax.set_title(self._name)
		ax.grid(True, which='both', alpha=0.4)
		ax.set(xlabel='x', ylabel='$\mu(x)$')


s = FuzzySet.create_trapezoidal('test', 1, 100, 100, 20, 30, 50, 80)

t = FuzzySet.create_trapezoidal('test', 1, 100, 100, 30, 50, 90, 100)

fig, axs = plt.subplots(1, 1)

s.complement().plot_set(axs)

plt.show()
print(s.cog_defuzzify())
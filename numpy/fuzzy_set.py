import numpy as np
import copy
from collections import OrderedDict
# import fuzzy_system.system_settings


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
		s = np.minimum(np.maximum(np.minimum((t1fs._domain-a)/(b-a), (d-t1fs._domain)/(d-c)), 0), 1)
		
		return s

	# _get_last_dom_value = property(_get_last_dom_value, _set_last_dom_value)

	@classmethod
	def create_triangular(cls, name, domain_min, domain_max, res, a, b, c):
		t1fs = cls(name, domain_min, domain_max)

		t1fs._domain = np.linspace(domain_min, domain_max, res)
		s = s = np.maximum(np.minimum((t1fs._domain-a)/(b-a), (c-t1fs._domain)/(c-b)), 0)
		
		return s


	# def _sort_set(self):
	# 	'''
	# 	sorts a type-1 fuzzy set so that all somain values (keys) are 
	# 	in ascending order
	# 	'''
	# 	self._elements = OrderedDict( sorted(self._elements.items()))

	# def _get_last_dom_value(self):
	# 	return self._last_dom_value

	# def _set_last_dom_value(self, d):
	# 	if d < 0:
	# 		self._last_dom_value = 0
	# 	elif d > 1:
	# 		self._last_dom_value = 1
	# 	else:
	# 		self._last_dom_value = d

	# def add_element(self, domain_val, dom_val):
	# 	'''
	# 	Adds a new element to the t1fs. If there is already an element at the stated
	# 	domain value the maximum degree of membership value is kept

	# 	Arguments:
	# 	----------
	# 	domain_val -- float, the value of x
	# 	degree_of_membership, float value between 0 and 1. The degree of membership
	# 	'''
	# 	if dom_val > 1:
	# 		raise ValueError('degree of membership must not be greater than 1, {} : {}'.format(domain_val, dom_val))

	# 	if domain_val in self._elements:
	# 		self._elements[domain_val] = max(self._elements[domain_val], dom_val)
	# 	else:
	# 		self._elements[domain_val] = dom_val
	# 		self._empty = False

	# 	if dom_val == 1:
	# 		self._center = min(self._center, domain_val)

	# def clear_set(self):
	# 	if not self._empty:
	# 		self._elements = {}
	# 		self._empty = True
	# 		self._precision = 3
	# 		self._name = name
	# 		self._last_dom_value = 0

	# def fuzzy_alpha_cut(self, val):
		
	# 	res_set = FuzzySet()

	# 	for x, u in self._elements.items():
			
	# 		if u > val:
	# 			res_set.add_element(x, val)
	# 		else:
	# 			res_set.add_element(x, u)

	# 	return res_set

	# def union(self, f_set):

	# 	result = copy.deepcopy(f_set)

	# 	for x, u in self._elements.items():
	# 		if x in result._elements:
	# 			result[x] = max( result[x], u)
	# 		else:
	# 			result.add_element(x, u)

	# 	result._sort_set()
	# 	return result

	# def intersection(self, f_set):

	# 	result = copy.deepcopy(f_set)

	# 	for x, u in self._elements.items():
	# 		if x in result._elements:
	# 			result[x] = min( result[x], u)
	# 		else:
	# 			result.add_element(x, u)

	# 	result._sort_set()
	# 	return result

	# def complement(self):

	# 	result = copy.deepcopy(self)

	# 	for x, u in self._elements.items():
	# 		result[x] = 1 - u

	# 	result._sort_set()
	# 	return result

	# def cog_defuzzify(self):
		
	# 	num = 0
	# 	den = 0

	# 	for x, u in self._elements.items():
	# 		num = round(num + x * u, fuzzy_system.system_settings.PRECISION)
	# 		den = round(den + u , fuzzy_system.system_settings.PRECISION)

		# return(num/den)

	def domain_elements(self):
		return self._domain

	def dom_elements(self):
		return self._dom

	# def plot_set(self, ax, col=''):
	# 	ax.plot(self.domain_elements(), self.dom_elements(), col)
	# 	ax.set_ylim([-0.1,1.1])
	# 	ax.set_title(self._name)
	# 	ax.grid(True, which='both', alpha=0.4)
	# 	ax.set(xlabel='x', ylabel='$\mu(x)$')


s = FuzzySet.create_trapezoidal('test', 1, 100, 100, 20, 30, 50, 80)
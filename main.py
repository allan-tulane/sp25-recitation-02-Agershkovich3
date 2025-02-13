"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###


def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
	if n == 1:
		return 1
	return a * simple_work_calc(n // b, a, b) + n


def work_calc(n, a, b, f):
	"""
	Compute the value of the recurrence W(n) = aW(n/b) + f(n).

	Params:
	n: Integer, size of input
	a: Integer, number of subproblems
	b: Integer, division factor
	f: Function that computes the work at each level

	Returns:
	Integer representing W(n)
	"""
	if n <= 1:
			return 1  # Base case: W(1) = 1
	return a * work_calc(n // b, a, b, f) + f(n)


def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence W(n) = aW(n/b) + f(n)."""
	if n == 1:
			return 1
	elif n == 0:
			return 0
	return span_calc(n // b, a, b, f) + f(n)



def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000]):
	"""
	Compare two work functions over a range of input sizes.

	Params:
	work_fn1, work_fn2: Functions that compute work W(n)
	sizes: List of input sizes

	Returns:
	A list of tuples (n, work_fn1(n), work_fn2(n))
	"""
	result = []
	for n in sizes:
			result.append((n, work_fn1(n), work_fn2(n)))  # Compute work for both functions
	return result


def print_results(results):
	""" done """
	print(
	    tabulate.tabulate(results,
	                      headers=['n', 'W_1', 'W_2'],
	                      floatfmt=".3f",
	                      tablefmt="github"))


def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000]):
	"""
	Compare two span functions over a range of input sizes.

	Params:
	span_fn1, span_fn2: Functions that compute span S(n)
	sizes: List of input sizes

	Returns:
	A list of tuples (n, span_fn1(n), span_fn2(n))
	"""
	result = []
	for n in sizes:
			result.append((n, span_fn1(n), span_fn2(n)))  # Compute span for both functions
	return result


if __name__ == "__main__":
	print("n=1:", work_calc(1, 1, 2, lambda n: n))
	print("n=10:", work_calc(10, 1, 2, lambda n: n))
	print("n=100:", work_calc(100, 1, 2, lambda n: n))
	print("n=1000:", work_calc(1000, 1, 2, lambda n: n))
	print("n=10000:", work_calc(10000, 1, 2, lambda n: n))


from main import *


def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(8, 2, 2) == 32
	assert simple_work_calc(6, 2, 2) == 16
	assert simple_work_calc(4, 2, 2) == 12


def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n * n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(20, 2, 2, lambda n: 1) == 31
	assert work_calc(10, 1, 2, lambda n: n * n) == 130
	assert work_calc(10, 1, 2, lambda n: n) == 18



def test_compare_work():
		sizes = [10, 20, 50, 100, 1000, 5000]

		# Case 1: Root-Dominated (Recursion dominates: a/(b^c) > 1)
		work_fn1 = lambda n: work_calc(n, 16, 2, lambda n: n**2)  # b = 2

		# Case 2: Balanced Case (a/(b^c) = 1)
		work_fn2 = lambda n: work_calc(n, 16, 4, lambda n: n**2)  # b = 4

		# Case 3: Work-Dominated (Work dominates: a/(b^c) < 1)
		work_fn3 = lambda n: work_calc(n, 16, 8, lambda n: n**2)  # b = 8

		print("\nComparing Work Cases for Different Values of b:")

		results = []
		for n in sizes:
				w1 = work_fn1(n)  # Root-Dominated (b = 1)
				w2 = work_fn2(n)  # Balanced (b = 2)
				w3 = work_fn3(n)  # Work-Dominated (b = 8)
				results.append((n, w1, w2, w3))

		print("\nTable: Work Comparison for Different Values of b")
		print("|   n   |  W_1 (Root-Dominated, b=2)  |  W_2 (Balanced, b=4)  |  W_3 (Work-Dominated, b=8)  |")
		print("|-------|----------------------------|----------------------|----------------------|")
		for row in results:
				print(f"|  {row[0]:5} | {row[1]:28} | {row[2]:22} | {row[3]:22} |")

from main import *

def test_compare_span():
	sizes = [10, 20, 50, 100, 1000, 5000]

	# Case 1: f(n) = O(1) -> Constant work at each level
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: 1)  # O(1)

	# Case 2: f(n) = O(log n) -> Logarithmic work at each level
	span_fn2 = lambda n: span_calc(n, 2, 2, lambda n: math.log(n) if n > 0 else 0)  # O(log n)

	# Case 3: f(n) = O(n) -> Linear work at each level
	span_fn3 = lambda n: span_calc(n, 2, 2, lambda n: n)  # O(n)

	print("\nComparing Span Cases for Different Growth Rates:")

	results = []
	for n in sizes:
			s1 = span_fn1(n)  # O(1)
			s2 = span_fn2(n)  # O(log n)
			s3 = span_fn3(n)  # O(n)
			results.append((n, s1, s2, s3))

	print("\nTable: Span Comparison for Different Growth Rates")
	print("|   n   |  S_1 (O(1))  |  S_2 (O(log n))  |  S_3 (O(n))  |")
	print("|-------|--------------|-----------------|--------------|")
	for row in results:
			print(f"|  {row[0]:5} | {row[1]:12} | {row[2]:15.6f} | {row[3]:12} |")
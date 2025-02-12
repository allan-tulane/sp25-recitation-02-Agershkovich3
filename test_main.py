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

	# Case 1: c < log_b a → Recursion dominates (O(n^log_b(a)))
	work_fn1 = lambda n: work_calc(n, 2, 2, lambda n: n**0.5)  # f(n) = n^0.5

	# Case 2: c > log_b a → Work dominates (O(n^c))
	work_fn2 = lambda n: work_calc(n, 2, 2, lambda n: n**2)  # f(n) = n^2

	# Case 3: c = log_b a → Balanced (O(n log n))
	work_fn3 = lambda n: work_calc(n, 2, 2, lambda n: n)  # f(n) = n

	print("\nComparing Work Cases (Three Different Recurrence Scenarios):")

	results = []
	for n in sizes:
		w1 = work_fn1(n)  # c < log_b a
		w2 = work_fn2(n)  # c > log_b a
		w3 = work_fn3(n)  # c = log_b a
		results.append((n, w1, w2, w3))

	print("\nTable: Work Comparison for Different f(n) Cases")
	print("|   n   |  W_1 (O(n))  |  W_2 (O(n^2))  |  W_3 (O(n log n))  |")
	print("|-------|--------------|---------------|------------------|")
	for row in results:
		print(f"|  {row[0]:5} | {row[1]:12} | {row[2]:13} | {row[3]:16} |")


def test_compare_span():
	sizes = [10, 20, 50, 100, 1000, 5000]

	# Case 1: O(log n) → f(n) = 1
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: 1)

	# Case 2: O(n) → f(n) = n
	span_fn2 = lambda n: span_calc(n, 2, 2, lambda n: n)

	# Case 3: O(n^2) → f(n) = n^2
	span_fn3 = lambda n: span_calc(n, 2, 2, lambda n: n**2)

	print("\nComparing Span Cases (Parallel Execution Time):")

	results = []
	for n in sizes:
		s1 = span_fn1(n)  # Expected O(log n)
		s2 = span_fn2(n)  # Expected O(n)
		s3 = span_fn3(n)  # Expected O(n^2)
		results.append((n, s1, s2, s3))

	print("\nTable: Span Comparison for Different f(n) Cases")
	print("|   n   |  S_1 (O(log n))  |  S_2 (O(n))  |  S_3 (O(n^2))  |")
	print("|-------|-----------------|-------------|--------------|")
	for row in results:
		print(f"|  {row[0]:5} | {row[1]:15} | {row[2]:11} | {row[3]:13} |")

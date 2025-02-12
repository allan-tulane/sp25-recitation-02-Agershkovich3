# CMPS 2200  Recitation 02

**Name (Team Member 1):**_____________Joshua Sasson____________  
**Name (Team Member 2):** Aaron Gershkovich

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.
f(n) = 1 and b>a example: b =2 a =1 will be balanced so the work will be O(lg(n)). 
n=1: 1
n=10: 4
n=100: 7
n=1000: 10
n=10000: 14
these work values scale at a log(n) rate 

f(n) = log(n) b=2 a =1 this will be root dominated so the work will be O(lg(n)). 
n=1: 1
n=10: 5.605170185988092
n=100: 18.111347423968603
n=1000: 37.78583226092475
n=10000: 66.15446482034221
these work values scale at a log(n) rate as the n values scale at an exponential rate 

f(n) = n b=2 a =1 this will be root dominated so the work will be O(n).
n=1: 1
n=10: 18
n=100: 197
n=1000: 1994
n=10000: 19995
these work values scale by an exponential rate as the n values scale at an exponential rate showing it is O(n) 
since the work value scales like n scales


- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

Table: Work Comparison for Different f(n) Cases
|   n   |  W_1 (O(n))  |  W_2 (O(n^2))  |  W_3 (O(n log n))  |
|-------|--------------|---------------|------------------|
|     10 | 21.291267864660337 |           174 |               36 |
|     20 | 47.054671684320255 |           748 |               92 |
|     50 | 110.23620513578395 |          4790 |              276 |
|    100 | 230.4724102715679 |         19580 |              652 |
|   1000 | 2075.117102760963 |       1990744 |             9120 |
|   5000 | 14251.20819850244 |      49957880 |            61728 |

When c is less than log_b(a), we expect that the estimated complexity will be O(n^(log_b a)), which is close to the O(n) time complexity, because it is leaf dominated, which is indicated by the almost linear growth of the function shown by the data. When c > log_b(a), we will expect an O(n^c), ( O(n^2) in this case) time complexity, meaning it is root dominated, which is supported by the exponential growth of the data shown. When c = log_b(a), the estimated time complexity will be n^c * logn, as it is balanced, or just nlogn time complexity, which increases faster than O(n), but slower than O(n^2).

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

test_main.py 
Comparing Span Cases (Parallel Execution Time):

Table: Span Comparison for Different f(n) Cases
|   n   |  S_1 (O(log n))  |  S_2 (O(n))  |  S_3 (O(n^2))  |
|-------|-----------------|-------------|--------------|
|     10 |               4 |          18 |           130 |
|     20 |               5 |          38 |           530 |
|     50 |               6 |          97 |          3315 |
|    100 |               7 |         197 |         13315 |
|   1000 |              10 |        1994 |       1333214 |
|   5000 |              13 |        9995 |      33332873 |

This also matches our knowledge because the span of O(logn) is the lowest power of 2 that is larger than n, which makes sense because thats how many splits there would need to be in the branches to cover all the. It follows that the depth of O(n) would increase linearly because as more elements are added, there is a linear relation to the amount of dependencies that are added, which is why that increase is correlated. For O(n^2), the same idea takes place as adding a linear amount of data would cause a growth exponentialy larger than the n being added.
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

Table: Work Comparison for Different Values of b
|   n   |  W_1 (Root-Dominated, b=2)  |  W_2 (Balanced, b=4)  |  W_3 (Leaf-Dominated, b=8)  |
|-------|----------------------------|----------------------|----------------------|
|     10 |                         1068 |                    196 |                    108 |
|     20 |                         8944 |                    664 |                    496 |
|     50 |                       104780 |                   4740 |                   2852 |
|    100 |                       848240 |                  17816 |                  11216 |
|   1000 |                    509190592 |                1930848 |                1139912 |
|   5000 |                 143543110592 |               49110112 |               28559944 |

These results align with our initial thinking because when c < log_b (a) in the root dominated system, recursion dominates, which leads to more work, and in the leaf dominated system, where c > log_b(a), the growth is a lot slower. The balanced system has an intermediate growth, which is also consistent as c = log_b(a).

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 


Table: Span Comparison for Different Growth Rates
|   n   |  S_1 (O(1))  |  S_2 (O(log n))  |  S_3 (O(n))  |
|-------|--------------|-----------------|--------------|
|     10 |            4 |        5.605170 |           18 |
|     20 |            5 |        8.600902 |           38 |
|     50 |            6 |       13.506177 |           97 |
|    100 |            7 |       18.111347 |          197 |
|   1000 |           10 |       37.785832 |         1994 |
|   5000 |           13 |       56.944124 |         9995 |


The results for this are consistent as well because for O(n) the span maintains mostly constant, for O(logn) corresponds to a balanced recursive tree, which follows a similar shape to logn, and finally, O(n) follows a very linear shape. The span is mostly proportional to the function itself.
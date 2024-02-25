
- [Induction and Recursion](#induction-and-recursion)
    - [5.1 Mathematical Induction](#51-mathematical-induction)
    - [5.2 Strong Induction and Well-Ordering](#52-strong-induction-and-well-ordering)
    - [5.3 Recursive Definitions and Structural Induction](#53-recursive-definitions-and-structural-induction)
    - [5.4 Recursive Algorithms](#54-recursive-algorithms)









## Induction and Recursion
### 5.1 Mathematical Induction
- **PRINCIPLE OF MATHEMATICAL INDUCTION** : To prove that $P(n)$ is true for all positive integers $n$, we complete two steps:
    - **BASIS STEP** : We verify that $P(1)$ is true
    - **INDUCTIVE STEP**: We show that the conditional statement $P(k) → P(k + 1)$ is true for all positive integers $k$




<br>

### 5.2 Strong Induction and Well-Ordering
- **STRONG INDUCTION** : To prove that $P(n)$ is true for all positive integers $n$, we complete two steps:
    - **BASIS STEP** : We verify that the proposition $P(1)$ is true
    - **INDUCTIVE STEP** : We show that the conditional statement $[P(1) ∧ P(2) ∧ ⋯ ∧ P(k)] → P(k + 1)$ is true for all positive integers $k$
- Strong induction is sometimes called the **second principle of mathematical induction** or **complete induction**
- A polygon is called **simple** if no two nonconsecutive sides intersect
- The validity of both the principle of mathematical induction and strong induction follows from a fundamental axiom of the set of integers, the **well-ordering property**. The well-ordering property states that every nonempty set of nonnegative integers has a least element




<br>

### 5.3 Recursive Definitions and Structural Induction
- We use two steps to define a function with the set of nonnegative integers as its domain, and such a definition is called a **recursive** or **inductive definition**:
    - **BASIS STEP** : Specify the value of the function at zero
    - **RECURSIVE STEP** : Give a rule for finding its value at an integer from its values at smaller integers
- A proof by **structural induction** consists of two parts:
    - **BASIS STEP** : Show that the result holds for all elements specified in the basic step of the recursive definition to be in the set
    - **RECURSIVE STEP** : Show that if the statement is true for each of the elements used to construct new elements in the recursive step of the definition, the result holds for these new elements
- We can extend mathematical induction to prove results about other sets that have the well-ordering property besides the set of integers




<br>

### 5.4 Recursive Algorithms
- An algorithm is called **recursive** if it solves a problem by reducing it to an instance of the same problem with smaller input
- Mathematical induction, and its variant strong induction, can be used to prove that a recursive algorithm is correct, that is, that it produces the desired output for all possible input values
-  Instead of successively reducing the computation to the evaluation of the function at smaller integers, we can start with the value of the function at one or more integers, the base cases, and successively apply the recursive definition to find the values of the function at successive larger integers. Such a procedure is called **iterative**





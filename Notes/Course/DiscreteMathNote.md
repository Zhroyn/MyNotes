<!-- TOC -->

- [Logic and Proofs](#logic-and-proofs)
  - [1.1 Propositional Logic](#11-propositional-logic)
  - [1.2 Applications of Propositional Logic](#12-applications-of-propositional-logic)
  - [1.3 Propositional Equivalences](#13-propositional-equivalences)
  - [1.4 Predicates and Quantifiers](#14-predicates-and-quantifiers)
  - [1.6 Rules of Inference](#16-rules-of-inference)
  - [1.7 Introduction to Proofs](#17-introduction-to-proofs)
  - [1.8 Proof Methods and Strategy](#18-proof-methods-and-strategy)
- [Basic Structures](#basic-structures)
  - [2.1 Sets](#21-sets)
  - [2.2 Set Operations](#22-set-operations)
  - [2.3 Functions](#23-functions)
  - [2.5 Cardinality of Sets](#25-cardinality-of-sets)
- [Algorithms](#algorithms)
  - [3.1 Algorithms](#31-algorithms)
  - [3.2 The Growth of Functions](#32-the-growth-of-functions)
  - [3.3 Complexity of Algorithms](#33-complexity-of-algorithms)
- [Number Theory and Cryptography](#number-theory-and-cryptography)
  - [4.1 Divisibility and Modular Arithmetic](#41-divisibility-and-modular-arithmetic)
- [Induction and Recursion](#induction-and-recursion)
  - [5.1 Mathematical Induction](#51-mathematical-induction)
  - [5.2 Strong Induction and Well-Ordering](#52-strong-induction-and-well-ordering)
  - [5.3 Recursive Definitions and Structural Induction](#53-recursive-definitions-and-structural-induction)
  - [5.4 Recursive Algorithms](#54-recursive-algorithms)
- [Counting](#counting)
  - [6.1 The Basics of Counting](#61-the-basics-of-counting)
  - [6.2 The Pigeonhole Principle](#62-the-pigeonhole-principle)
  - [6.3 Permutations and Combinations](#63-permutations-and-combinations)
  - [6.4 Binomial Coefficients and Identities](#64-binomial-coefficients-and-identities)
  - [6.5 Generalized Permutations and Combinations](#65-generalized-permutations-and-combinations)
  - [6.6 Generating Permutations and Combinations](#66-generating-permutations-and-combinations)
- [Advanced Counting Techniques](#advanced-counting-techniques)
  - [8.1 Applications of Recurrence Relations](#81-applications-of-recurrence-relations)

<!-- /TOC -->





## Logic and Proofs

### 1.1 Propositional Logic
- A proposition is a declarative sentence that is either true or false, but not both

- `negation` : $\neg p$
  - The truth value of the negation of a proposition in fuzzy
logic is 1 minus the truth value of the proposition
- `conjunction` : $p \land q$
  - The truth value of the conjunction of two propositions in
fuzzy logic is the minimum of the truth values of the two
propositions
- `disjunction` : $p \vee q$
  - The truth value of the disjunction of two propositions in
fuzzy logic is the maximum of the truth values of the two
propositions
- `exclusive or` : $p \oplus q$
- `nor` : $p \downarrow q$
  - True when both p and q are false
- `conditional statement` : $p \rightarrow q$
  - True when both p and q are true and when p is false
  - `if p, then q` is equivalent to `p only if q`, `q whenever p`, `q follows from p` and `q unless ¬p`
  - `converse` : $q \rightarrow p$
  - `contrapositive` : $\neg q \rightarrow \neg p$
  - `inverse` : $\neg p \rightarrow \neg q$
- `biconditional statement` : $p \leftrightarrow q$
  - True when p and q have the same truth values
  - Equivalent to `p iff q` and `p exactly then q`

|Operator| Precedence|
| :-: | :-: |
|$\neg$| 1 |
|$\land$| 2 |
|$\vee$| 3 |
|$\rightarrow$| 4 |
|$\leftrightarrow$| 5 |

### 1.2 Applications of Propositional Logic
- System specifications should be **consistent**, that is, they should not contain conflicting requirements that could be used to derive a contradiction

### 1.3 Propositional Equivalences
- A compound proposition that is always true, no matter what the truth values of the propositional variables that occur in it, is called a **tautology**
- A compound proposition that is always false is called a **contradiction**
- A compound proposition that is neither a tautology nor a contradiction is called a **contingency**
<br>

- The compound propositions p and q are called **logically equivalent** if $p \leftrightarrow q$ is a tautology
- The notation $p \equiv q$ or $p \Leftrightarrow q$ denotes that p and q are logically equivalent
<br>

- Identity laws : $p \land T ≡ p$, $p \vee F ≡ p$
- Domination laws : $p \vee T ≡ T$, $p \land F ≡ F$
- Idempotent laws : $p \vee p ≡ p$, $p \land p ≡ p$
- Double negation law : $\neg (\neg p) ≡ p$ 
- Commutative laws : $p \vee q ≡ q \vee p$, $p \land q ≡ q \land p$
- Associative laws : $(p \vee q) \vee r ≡ p \vee (q \vee r)$, $(p \land q) \land r ≡ p \land (q \land r)$
- Distributive laws : $p \vee (q \land r) ≡ (p \vee q) \land (p \vee r)$, $p \land (q \vee r) ≡ (p \land q) \vee (p \land r)$
- De Morgan’s laws : $\neg (p \land q) ≡ \neg p \vee \neg q$, $\neg(p \vee q) ≡ \neg p \land \neg q$
  - $\neg(\vee_{j=1}^n p_j) \equiv \land_{j=1}^n \neg p_j$, $\neg(\land_{j=1}^n p_j) \equiv \vee_{j=1}^n \neg p_j$
- Absorption laws : $p \vee (p \land q) ≡ p$, $p \land (p \vee q) ≡ p$
- Negation laws : $p \vee \neg p ≡ T$, $p \land \neg p ≡ F$
<br>

- $p → q ≡ ¬p ∨ q$
- $p → q ≡ ¬q → ¬p$
- $p ∨ q ≡ ¬p → q$
- $p ∧ q ≡ ¬(p → ¬q)$
- $¬(p → q) ≡ p ∧ ¬q$
- $(p → q) ∧ (p → r) ≡ p → (q ∧ r)$
- $(p → r) ∧ (q → r) ≡ (p ∨ q) → r$
- $(p → q) ∨ (p → r) ≡ p → (q ∨ r)$
- $(p → r) ∨ (q → r) ≡ (p ∧ q) → r$
<br>

- $p ↔ q ≡ (p → q) ∧ (q → p)$
- $p ↔ q ≡ ¬p ↔ ¬q$
- $p ↔ q ≡ (p ∧ q) ∨ (¬p ∧ ¬q)$
- $¬(p ↔ q) ≡ p ↔ ¬q$
<br>

- $p \oplus q \equiv (p \land \neg q)\vee(\neg p \land q)$
- $p \downarrow p \equiv \neg p$
- $(p \downarrow q)\downarrow(p \downarrow q) \equiv p \vee q$

### 1.4 Predicates and Quantifiers
- Many mathematical statements assert that a property is true for all values of a variable in a particular domain, called the **domain of discourse**, often just referred to as the **domain**
- The area of logic that deals with predicates and quantifiers is called the **predicate calculus**
<br>

- The statement $P(x)$ is said to be the value of the **propositional function** $P$ at $x$. Once a value has been assigned to the variable $x$, the statement $P(x)$ becomes a proposition and has a truth value
- A statement of the form $P(x_1, x_2, \dots , x_n)$ is the value of the propositional function $P$ at the n-tuple $(x_1, x_2, \dots , x_n)$, and $P$ is also called an **n-place predicate** or an **n-ary predicate**
<br>

- The statements that describe valid input are known as **preconditions** 
- The conditions that the output should satisfy when the program has run are known as **postconditions**
<br>

- The notation $∀xP(x)$ denotes the universal quantification of $P(x)$. Here $\forall$ is called the **universal quantifier**. An element for which $P(x)$ is false is called a **counterexample** to $∀xP(x)$
- The notation $∃xP(x)$ denotes the existential quantification of $P(x)$. Here $\exist$ is called the **existential quantifier**
- The notation $∃!xP(x)$ or $∃_1xP(x)$ states “There exists a unique $x$ such that $P(x)$ is true.” Here $∃!$ is called the **uniqueness quantifier**
- The quantifiers $∀$ and $∃$ have higher precedence than all logical operators from propositional calculus
<br>

- Statements involving predicates and quantifiers are **logically equivalent** if and only if they have the same truth value no matter which predicates are substituted into these statements and which domain of discourse is used for the variables in these propositional functions
- Suppose p and q are statements involving predicates and quantifiers, we can show p and q are logically equivalent by showing that if one of them is true, then the other is true
<br>

- $∀x(P(x) ∧ Q(x)) \equiv ∀xP(x) ∧ ∀xQ(x)$
- $\exist x(P(x) \vee Q(x)) \equiv \exist xP(x) \vee \exist xQ(x)$
- De Morgan’s laws for quantifiers : $¬∀xP(x) ≡ ∃x ¬P(x)$, $¬∃xQ(x) ≡ ∀x ¬Q(x)$


### 1.6 Rules of Inference
- An **argument** in propositional logic is a sequence of propositions. All but the final proposition in the argument are called **premises** and the final proposition is called the **conclusion**. An argument is **valid** if the truth of all its premises implies that the conclusion is true.
- An **argument form** in propositional logic is a sequence of compound propositions involving propositional variables. An argument form is valid if no matter which particular propositions are substituted for the propositional variables in its premises, the conclusion is true if the premises are all true.

|Rule of Inference|Tautology|Name|
|---|---|---|
| $p$<br>$p → q$<br>$∴ q$ | $(p ∧ (p → q)) → q$ | Modus ponens |
| $¬q$<br>$p → q$<br>$∴ ¬p$ | $(¬q ∧ (p → q)) → ¬p$ | Modus tollens |
| $p → q$<br>$q → r$<br>$∴ p → r$ | $((p → q) ∧ (q → r)) → (p → r)$ | Hypothetical syllogism |
| $p ∨ q$<br>$¬p$<br>$∴ q$ | $((p ∨ q) ∧ ¬p) → q$ | Disjunctive syllogism |
| $p$<br>$∴ p ∨ q$ | $p → (p ∨ q)$ | Addition |
| $p ∧ q$<br>$∴ p$ | $(p ∧ q) → p$ | Simplification |
| $p$<br>$q$<br>$∴ p ∧ q$ | $((p) ∧ (q)) → (p ∧ q)$ | Conjunction |
| $p ∨ q$<br>$¬p ∨ r$<br>$∴ q ∨ r$ | $((p ∨ q) ∧ (¬p ∨ r)) → (q ∨ r)$ | Resolution |

- The proposition $((p → q) ∧ q) → p$ is not a tautology. This type of incorrect reasoning is called the **fallacy of affirming the conclusion**
- The proposition $((p → q) ∧ ¬p) → ¬q$ is not a tautology. This type of
incorrect reasoning is called the **fallacy of denying the hypothesis**

|Rule of Inference|Name|
|--|--|
| $∀xP(x)$<br>$∴ P(c)$ | Universal instantiation |
| $P(c)$ for an arbitrary c<br>$∴ ∀xP(x)$ | Universal generalization |
| $∃xP(x)$<br>$∴ P(c)$ for some element c | Existential instantiation |
| $P(c)$ for some element c<br>$∴ ∃xP(x)$ | Existential generalization |
| $∀x(P(x) → Q(x))$<br>$P(a)$<br>$∴ Q(a)$ | Universal modus ponens|
| $∀x(P(x) → Q(x))$<br>$¬Q(a)$<br>$∴ ¬P(a)$ | Universal modus tollens|



### 1.7 Introduction to Proofs
- A **direct proof** of a conditional statement $p → q$ is constructed when the first step is the assumption that $p$ is true, and then we show that $q$ must also be true
<br>

- Proofs of theorems that do not start with the premises and end with the conclusion, are called **indirect proofs**
- An extremely useful type of indirect proof is known as **proof by contraposition**. In a proof by contraposition of $p → q$, we take $¬q$ as a premise, and using axioms, definitions, and then we show that $¬p$ must follow
- Because the statement $r ∧ ¬r$ is a contradiction whenever $r$ is a proposition, we can prove that $p$ is true if we can show that $¬p → (r ∧ ¬r)$ is true for some proposition $r$. Proofs of this type are called **proofs by contradiction**
<br>

- If we can show that $p$ is false, then we have a proof, called a **vacuous proof**, of the conditional statement $p → q$
- A proof of $p → q$ that uses the fact that $q$ is true is called a **trivial proof**


### 1.8 Proof Methods and Strategy
- The original conditional statement with a hypothesis made up of a disjunction of the propositions $p_1, p_2, … , p_n$ can be proved by proving each of the n conditional statements $p_i → q, i = 1, 2, … , n$,  individually. Such an argument is called a **proof by cases**
- Some theorems can be proved by examining a relatively small number of examples. Such proofs are called **exhaustive proofs**, or **proofs by exhaustion** because these proofs proceed by exhausting all possibilities
<br>

- A proof of a proposition of the form $∃xP(x)$ is called an **existence proof**. There are several ways to prove a theorem of this type
- One type of existence proof is called **constructive**
- Another type of existence proof is **nonconstructive**; that is, we directly prove that $∃xP(x)$ is true in some other way. One common method is to use proof by contradiction; that is, we show that the negation of the existential quantification implies a contradiction
<br>

- The two parts of a **uniqueness proof** are:
  - Existence: We show that an element $x$ with the desired property exists.
  - Uniqueness: We show that if $x$ and $y$ both have the desired property, then $x = y$
<br>

- Using the premises, together with axioms and known theorems, you can construct a proof using a sequence of steps that leads to the conclusion. This type of reasoning is called **forward reasoning**
- In such cases it may be helpful to use **backward reasoning**. To reason backward to prove a statement $q$, we find a statement $p$ that we can prove with the property that $p → q$








## Basic Structures
### 2.1 Sets
- **elements** or **members** : $a ∈ A$ or $a ∉ A$
- describe a set : use **roster method** or **set builder** notation
- **equal** if and only if have the same elements
- **subject** : $A ⊆ B$ or $A ⊈ B$
- **superset** : $B ⊇ A$
- **proper subset** : $A ⊂ B$
<br>

- If there are exactly $n$ distinct elements in $S$ where $n$ is a nonnegative integer, we say that $S$ is a **finite set** and that $n$ is the **cardinality** of $S$. The cardinality of $S$ is denoted by $|S|$
- A set is said to be **infinite** if it is not finite
- The **power set** of $S$ is the set of all subsets of the set $S$, which is denoted by $P(S)$
<br>

- **ordered n-tuple** : $(a_1, a_2, … , a_n)$
- **ordered pairs** : $(a_1, a_2)$
- **Cartesian product** : $A1 × A2 × ⋯ × An = \{(a_1, a_2, … , a_n) ∣ a_i ∈ A_i \; for \; i = 1, 2, … , n\}$
- A subset $R$ of the Cartesian product $A × B$ is called a **relation** from the set $A$ to the set $B$
<br>

- $∀x ∈ S(P(x))$ is shorthand for $∀x(x ∈ S → P(x))$
- $∃x ∈ S(P(x))$ is shorthand for $∃x(x ∈ S ∧ P(x))$
- We define the **truth set** of $P$ to be the set of elements $x$ in $D$ for which $P(x)$ is true, which is denoted by $\{x ∈ D ∣ P(x)\}$


### 2.2 Set Operations
- **union** : $A ∪ B$
- **intersection** : $A ∩ B$
  - Two sets are called **disjoint** if their intersection is the empty set
- **difference of A and B** or **complement of B with respect to A** : $A − B$
- **complement** : $\bar{A}$

|Identity|Name|
|--|--|
|$A ∩ U = A$ <br> $A ∪∅= A$ | Identity laws |
|$A ∪ U = U$ <br> $A ∩∅=∅$ | Domination laws  |
|$A ∪ A = A$ <br> $A ∩ A = A$ | Idempotent laws  |
|$(A) = A$ | Complementation law |
|$A ∪ B = B ∪ A$ <br> $A ∩ B = B ∩ A$ | Commutative laws |
|$A ∪ (B ∪ C) = (A ∪ B) ∪ C$ <br> $A ∩ (B ∩ C) = (A ∩ B) ∩ C$ | Associative laws |
|$A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)$ <br> $A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)$ | Distributive laws |
|$A ∩ B = A ∪ B$ <br> $A ∪ B = A ∩ B$ | De Morgan's laws |
|$A ∪ (A ∩ B) = A$ <br> $A ∩ (A ∪ B) = A$ | Absorption laws |
|$A ∪ A = U$ <br> $A ∩ A = ∅$ | Complement laws |

- A **multiset** (short for multiple-membership set) $\{m_1 ⋅ a_1, m_2 ⋅ a_2, … , m_r ⋅ a_r\}$ is an unordered collection of elements where an element can occur as a member more than once. The numbers $m_i , i = 1, 2, … , r$, are called the **multiplicities** of the elements $a_i , i = 1, 2, … , r$
- In the **union** of the multisets P and Q, the multiplicity is the maximum
- In the **intersection** of the multisets P and Q, the multiplicity is the minimum
- In the **difference** of P and Q, the multiplicity is the difference of P less Q unless this difference is negative
- In the **sum** of P and Q, the multiplicity is the sum of multiplicities in P and Q

### 2.3 Functions
- A **function** $f$ from $A$ to $B$ is an assignment of exactly one element of $B$ to each element of $A$.
- We write $f(a) = b$ if $b$ is the unique element of $B$ assigned by the function $f$ to the element $a$ of $A$, and we say that $b$ is the **image** of $a$ and $a$ is a **preimage** of $b$. The **range**, or **image** of $f$, is the set of all images of elements of $A$
- If $f$ is a function from $A$ to $B$, we write $f : A → B$ and we say that $A$ is the **domain** of $f$ and $B$ is the **codomain** of $f$.
- Let $f_1$ and $f_2$ be functions from $A$ to $R$. Then $f_1 + f_2$ and $f_1 f_2$ are also functions from $A$ to $R$ defined for all $x ∈ A$ by
  - $(f_1 + f_2)(x) = f_1(x) + f_2(x)$
  - $(f_1f_2)(x) = f_1(x)f_2(x)$
- The **image** of $S$ : $f(S) = \{t ∣ ∃s∈S (t = f(s))\}$ or $\{f(s) ∣ s ∈ S\}$
<br>

- A function $f$ is said to be **one-to-one**, or an **injection**, if and only if $f(a) = f(b)$ implies that $a = b$ for all $a$ and $b$ in the domain of $f$. A function is said to be **injective** if it is one-to-one
- A function f from A to B is called **onto**, or a **surjection**, if and only if for every element $b ∈ B$ there is an element $a ∈ A$ with $f(a) = b$. A function is called **surjective** if it is onto
- The function f is a **one-to-one correspondence**, or a **bijection**, if it is both one-to-one and onto. We also say that such a function is **bijective**
<br>

- The **inverse function** of $f$ is denoted by $f^{−1}$
- Let $g$ be a function from the set $A$ to the set $B$ and let $f$ be a function from the set $B$ to the set $C$, then the **composition** of the functions $f$ and $g$ is denoted by $f \circ g$
- The value of the **floor function** at $x$ is denoted by $⌊x⌋$
- The value of the **ceiling function** at $x$ is denoted by $⌈x⌉$
- A **partial function** $f$ from $A$ to $B$ is an assignment to each element $a$ in a subject of $A$, called the domain of definition of $f$ , of a unique element $b$ in $B$. We say that $f$ is undefined for elements in $A$ that are not in the domain of definition of $f$. When the domain of definition of $f$ equals $A$, we say that $f$ is a **total function**




### 2.5 Cardinality of Sets
- The sets $A$ and $B$ have the same cardinality if and only if there is a one-to-one correspondence from $A$ to $B$, and this is denoted by $|A| = |B|$
- If there is a one-to-one function from $A$ to $B$, we write $|A| ≤ |B|$
- A set that is either finite or has the same cardinality as the set of positive integers is called **countable**, and we denote the cardinality of this set by $ℵ_0$. We write $|S| = ℵ_0$ and say that $S$ has cardinality "aleph null"

- If $A$ and $B$ are countable sets, then $A ∪ B$ is also countable
-  **Schröder-Bernstein theorem** :  If $A$ and $B$ are sets with $|A| ≤ |B|$ and $|B| ≤ |A|$, then $|A| = |B|$. In other words, if there are one-to-one functions $f$ from $A$ to $B$ and $g$ from $B$ to $A$, then there is a one-to-one correspondence between $A$ and $B$









## Algorithms
### 3.1 Algorithms
- Algorithms that make what seems to be the best choice at each step are called **greedy algorithms**
<br>

- $Input$. An algorithm has input values from a specified set.
- $Output$. From each set of input values an algorithm produces output values from a specified set. The output values are the solution to the problem.
- $Definiteness$. The steps of an algorithm must be defined precisely.
- $Correctness$. An algorithm should produce the correct output values for each set of input values.
- $Finiteness$. An algorithm should produce the desired output after a finite (but perhaps large) number of steps for any input in the set.
- $Effectiveness$. It must be possible to perform each step of an algorithm exactly and in a finite amount of time.
- $Generality$. The procedure should be applicable for all problems of the desired form, not just for a particular set of input values.

### 3.2 The Growth of Functions
- We say that $f(x)$ is $O(g(x))$ if there are constants $C$ and $k$ such that $|f(x)| ≤ C|g(x)|$ whenever $x > k$. This is read as "$f(x)$ is big-oh of $g(x)$." The constants $C$ and $k$ in the definition of big-O notation are called **witnesses** to the relationship $f(x)$ is $O(g(x))$.
- We say that $f(x)$ is $Ω(g(x))$ if there are constants $C$ and $k$ such that $|f(x)| ≥ C|g(x)|$ whenever $x > k$. This is read as "$f(x)$ is big-Omega of $g(x)$."
- We say that $f(x)$ is $Θ(g(x))$ if $f(x)$ is $O(g(x))$ and $f(x)$ is $Ω(g(x))$. When $f(x)$ is $Θ(g(x))$, we say that $f(x)$ is big-Theta of $g(x)$, that $f(x)$ is of order $g(x)$, and that $f(x)$ and $g(x)$ are of the same order.
<br>

- Suppose that $f_1(x)$ is $O(g_1(x))$ and that $f_2(x)$ is $O(g_2(x))$. Then $(f_1 + f_2)(x)$ is $O(g(x))$, where $g(x) = (max(|g_1(x)|, |g_2(x)|)$ for all $x$
- Suppose that $f_1(x)$ is $O(g_1(x))$ and that $f_2(x)$ is $O(g_2(x))$. Then $(f_1f_2)(x)$ is $O(g_1(x)g_2(x))$
- Let $f(x) = a_nx_n + a_{n−1}x_{n−1} + ⋯ + a_1x + a_0$, where $a_0, a_1, … , a_n$ are real numbers with $a_n ≠ 0$. Then $f(x)$ is of order $x_n$

### 3.3 Complexity of Algorithms
- An **algorithmic paradigm** is a general approach based on a particular concept that can be used to construct algorithms for solving a variety of problems
- In a **brute-force algorithm**, a problem is solved in the most straightforward manner based on the statement of the problem and the definitions of terms
<br>

- A problem that is solvable using an algorithm with polynomial (or better) worst-case complexity is called **tractable**
-  Problems for which a solution can be checked in polynomial time are said to belong to the **class NP** (tractable problems are said to belong to **class P**) The abbreviation NP stands for *nondeterministic polynomial* time
-  There is also an important class of problems, called **NP-complete problems**, with the property that if any of these problems can be solved by a polynomial worst-case time algorithm, then all problems in the class NP can be solved by polynomial worst-case time algorithms
-  The **P versus NP problem** asks whether NP, the class of problems for which it is possible to check solutions in polynomial time, equals P, the class of tractable problems










## Number Theory and Cryptography
### 4.1 Divisibility and Modular Arithmetic
- The notation $a \mid b$ denotes that $a$ divides $b$. We write $a \nmid b$ when $a$ does not divide $b$
- Let $a$ be an integer and $d$ a positive integer. Then there are unique integers $q$ and $r$, with $0 ≤ r < d$, such that $a = dq + r$. $d$ is called the **divisor**, $a$ is called the **dividend**, $q$ is called the **quotient**, and $r$ is called the **remainder**. This notation is used to express the quotient and remainder: $q = a \; div \; d$, $r = a \; mod \; d$
<br>

- If $m$ divides $a − b$, we say that $a$ is congruent to $b$ modulo $m$ with the notation $a ≡ b (mod \; m)$, and we say that $a ≡ b (mod m)$ is a **congruence** and that $m$ is its **modulus**
- $a ≡ b (mod \; m)$ if and only if there is an integer $k$ such that $a = b + km$
- If $a ≡ b (mod \; m)$ and $c ≡ d (mod \; m)$, then $a + c ≡ b + d (mod \; m)$ and $ac ≡ bd (mod \; m)$
- The operations $+_m$ and $⋅_m$ are called addition and multiplication modulo $m$ and when we use these operations, we are said to be doing **arithmetic modulo** $m$








## Induction and Recursion
### 5.1 Mathematical Induction
- **PRINCIPLE OF MATHEMATICAL INDUCTION** : To prove that $P(n)$ is true for all positive integers $n$, we complete two steps:
  - **BASIS STEP** : We verify that $P(1)$ is true
  - **INDUCTIVE STEP**: We show that the conditional statement $P(k) → P(k + 1)$ is true for all positive integers $k$

### 5.2 Strong Induction and Well-Ordering
- **STRONG INDUCTION** : To prove that $P(n)$ is true for all positive integers $n$, we complete two steps:
  - **BASIS STEP** : We verify that the proposition $P(1)$ is true
  - **INDUCTIVE STEP** : We show that the conditional statement $[P(1) ∧ P(2) ∧ ⋯ ∧ P(k)] → P(k + 1)$ is true for all positive integers $k$
- Strong induction is sometimes called the **second principle of mathematical induction** or **complete induction**
- A polygon is called **simple** if no two nonconsecutive sides intersect
- The validity of both the principle of mathematical induction and strong induction follows from a fundamental axiom of the set of integers, the **well-ordering property**. The well-ordering property states that every nonempty set of nonnegative integers has a least element

### 5.3 Recursive Definitions and Structural Induction
- We use two steps to define a function with the set of nonnegative integers as its domain, and such a definition is called a **recursive** or **inductive definition**:
  - **BASIS STEP** : Specify the value of the function at zero
  - **RECURSIVE STEP** : Give a rule for finding its value at an integer from its values at smaller integers
- A proof by **structural induction** consists of two parts:
  - **BASIS STEP** : Show that the result holds for all elements specified in the basic step of the recursive definition to be in the set
  - **RECURSIVE STEP** : Show that if the statement is true for each of the elements used to construct new elements in the recursive step of the definition, the result holds for these new elements
- We can extend mathematical induction to prove results about other sets that have the well-ordering property besides the set of integers


### 5.4 Recursive Algorithms
- An algorithm is called **recursive** if it solves a problem by reducing it to an instance of the same problem with smaller input
- Mathematical induction, and its variant strong induction, can be used to prove that a recursive algorithm is correct, that is, that it produces the desired output for all possible input values
-  Instead of successively reducing the computation to the evaluation of the function at smaller integers, we can start with the value of the function at one or more integers, the base cases, and successively apply the recursive definition to find the values of the function at successive larger integers. Such a procedure is called **iterative**








## Counting
### 6.1 The Basics of Counting
- **THE PRODUCT RULE** : Suppose that a procedure can be broken down into a sequence of two tasks. If there are $n_1$ ways to do the first task, and for each of these ways of doing the first task, there are $n_2$ ways to do the second task, then there are $n_1n_2$ ways to do the procedure
- **THE SUM RULE** : If a task can be done either in one of $n_1$ ways or in one of $n_2$ ways, where none of the set of $n_1$ ways is the same as any of the set of $n_2$ ways, then there are $n_1 + n_2$ ways to do the task
- **THE SUBTRACTION RULE** : If a task can be done in either $n_1$ ways or $n_2$ ways, then the number of ways to do the task is $n_1 + n_2$ minus the number of ways to do the task that are common to the two different ways. The subtraction rule is also known as the **principle of inclusion–exclusion**
- **THE DIVISION RULE** : There are $n∕d$ ways to do a task if it can be done using a procedure that can be carried out in $n$ ways, and for every way $w$, exactly $d$ of the $n$ ways correspond to way $w$


### 6.2 The Pigeonhole Principle
- **THE PIGEONHOLE PRINCIPLE** : If $k$ is a positive integer and $k + 1$ or more objects are placed into $k$ boxes, then there is at least one box containing two or more of the objects
- The pigeonhole principle is also called the **Dirichlet drawer principle**
- **THE GENERALIZED PIGEONHOLE PRINCIPLE** If $N$ objects are placed into $k$ boxes, then there is at least one box containing at least $⌈N∕k⌉$ objects. Proof:
  - Suppose that none of the boxes contains more than $⌈N∕k⌉ − 1$ objects. Then, the total number of objects is at most $k(⌈N/k⌉ − 1) < k ((N/k + 1) − 1) = N$
  - Thus, the total number of objects is less than $N$. This completes the proof by contraposition


### 6.3 Permutations and Combinations
- An ordered arrangement of $r$ elements of a set is called an **r-permutation**. If $n$ is a positive integer and $r$ is an integer with $1 ≤ r ≤ n$, then there are $\displaystyle P(n, r) = n(n − 1)(n − 2) ⋯ (n − r + 1) = \frac{n!}{(n-r)!}$
- An **r-combination** of elements of a set is an unordered selection of r elements from the set. Thus, $\displaystyle C(n, r) = \frac{n!}{r!(n-r)!}$. $C(n, r)$ is also denoted by $\begin{pmatrix} n \\ r \end{pmatrix}$ and is called a **binomial coefficient**
<br>

- A **combinatorial proof** of an identity is a proof that uses counting arguments to prove that both sides of the identity count the same objects but in different ways or a proof that is based on showing that there is a bijection between the sets of objects counted by the two sides of the identity. These two types of proofs are called **double counting proofs** and **bijective proofs**, respectively


### 6.4 Binomial Coefficients and Identities
- $\displaystyle (x+y)^n = \sum_{j=0}^n \begin{pmatrix} n \\ j \end{pmatrix}x^{n-j}y^j $
- $\displaystyle \sum_{k=0}^n \begin{pmatrix} n \\ k \end{pmatrix} = 2^n $
- $\displaystyle \sum_{k=0}^n (-1)^k\begin{pmatrix} n \\ k \end{pmatrix} = 0 $
- $\displaystyle \sum_{k=0}^n 2^k\begin{pmatrix} n \\ k \end{pmatrix} = 3^n $
- Pascal’s Identity : $\displaystyle \begin{pmatrix} n+1 \\ k \end{pmatrix} = \begin{pmatrix} n \\ k-1 \end{pmatrix} + \begin{pmatrix} n \\ k \end{pmatrix}$
- Vandermonde’s Identity : $\displaystyle \begin{pmatrix} m+n \\ r \end{pmatrix} = \sum_{k=0}^r \begin{pmatrix} m \\ r-k \end{pmatrix} \begin{pmatrix} n \\ k \end{pmatrix}$
  - $\displaystyle \begin{pmatrix} 2n \\ n \end{pmatrix} = \sum_{k=0}^n \begin{pmatrix} n \\ k \end{pmatrix}^2$
- $\displaystyle \begin{pmatrix} n+1 \\ r+1 \end{pmatrix} = \sum_{j=r}^n \begin{pmatrix} j \\ r \end{pmatrix}$


### 6.5 Generalized Permutations and Combinations
- **Permutations with Repetition** : The number of r-permutations of a set of $n$ objects with repetition allowed is $n^r$
- **Combinations with Repetition** : There are $C(n + r − 1, r) = C(n + r − 1, n − 1)$ r-combinations from a set with $n$ elements when repetition of elements is allowed.
- **Permutations with Indistinguishable Objects** : The number of different permutations of $n$ objects, where there are $n_1$ indistinguishable objects of type 1, $n_2$ indistinguishable objects of type 2, … , and $n_k$ indistinguishable objects of
type k, is $\displaystyle \frac{n!}{n_1! n_2! ⋯ n_k!}$
- **Distributing Objects into Boxes**
  - **Distinguishable Objects and Distinguishable Boxes** : The number of ways to distribute $n$ distinguishable objects into $k$ distinguishable boxes so that $n_i$ objects are placed into box $i$, $i = 1, 2, … , k$, equals $\displaystyle \frac{n!}{n_1! n_2! ⋯ n_k!}$
  - **Indistinguishable Objects and Distinguishable Boxes** : There are $C(n + r − 1, n − 1)$ ways to place $r$ indistinguishable objects into $n$ distinguishable boxes
  - **Distinguishable Objects and Indistinguishable Boxes**
    - Let $S(n, j)$ denote the number of ways to distribute $n$ distinguishable objects into $j$ indistinguishable boxes so that no box is empty. The numbers $S(n, j)$ are called **Stirling numbers of the second kind**.
    - It can be shown that $\displaystyle S(n, j) = \frac{1}{j!}\sum_{i=0}^{j-1} (-1)^i\begin{pmatrix} j \\ i \end{pmatrix} (j-i)^n $
    - So the number of ways to distribute $n$ distinguishable objects into $k$ indistinguishable boxes equals $\displaystyle \sum_{j=1}^k S(n, j) = \sum_{j=1}^k\frac{1}{j!}\sum_{i=0}^{j-1} (-1)^i\begin{pmatrix} j \\ i \end{pmatrix} (j-i)^n $
  - **Indistinguishable Objects and Indistinguishable Boxes** : No simple closed formula exists for this number.



### 6.6 Generating Permutations and Combinations
- A general method can be described for producing the next larger permutation in increasing order following a given permutation $a_1a_2 ⋯ a_n$:
  - First, find the integers $a_j$ and $a_{j+1}$ with $a_{j} < a_{j+1}$ and $a_{j+1} > a_{j+2} > ⋯ > a_{n}$, that is, the last pair of adjacent integers in the permutation where the first integer in the pair is smaller than the second.
  - Then, the next larger permutation in lexicographic order is obtained by putting in the $j$th position the least integer among $a_{j+1}, a_{j+2}, ⋯, a_{n}$ that is greater than $a_j$, and then listing in increasing order the rest of the integers $a_j, a_{j+1}, ⋯, a_{n}$ in positions $j + 1$ to $n$.
-  The next r-combination after $a_1a_2 ⋯ a_r$ can be obtained in the following way:
   - First, locate the last element $a_i$ in the sequence such that $a_i ≠ n − r + i$.
   - Then, replace $a_i$ with $a_i + 1$ and $a_j$ with $a_i + j − i + 1$, for $j = i + 1, i + 2, … , r$.








## Advanced Counting Techniques
### 8.1 Applications of Recurrence Relations
- A rule for determining subsequent terms from those that precede them, is called a **recurrence relation**







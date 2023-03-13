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
- A $function f$ from $A$ to $B$ is an assignment of exactly one element of $B$ to each element of $A$.
- We write $f(a) = b$ if $b$ is the unique element of $B$ assigned by the function $f$ to the element $a$ of $A$, and we say that $b$ is the **image** of $a$ and $a$ is a **preimage** of $b$. The **range**, or **image** of $f$, is the set of all images of elements of $A$
- If $f$ is a function from $A$ to $B$, we write $f : A → B$ and we say that $A$ is the **domain** of $f$ and $B$ is the **codomain** of $f$.
- Let $f_1$ and $f_2$ be functions from $A$ to $R$. Then $f_1 + f_2$ and $f_1 f_2$ are also functions from $A$ to $R$ defined for all $x ∈ A$ by
  - $(f_1 + f_2)(x) = f_1(x) + f_2(x)$
  - $(f_1f_2)(x) = f_1(x)f_2(x)$
- The **image** of $S$ : $f(S) = \{t ∣ ∃s∈S (t = f(s))\}$ or $\{f(s) ∣ s ∈ S\}$
<br>

- A function $f$ is said to be **one-to-one**, or an **injection**, if and only if $f(a) = f(b)$ implies that $a = b$ for all $a$ and $b$ in the domain of $f$. A function is said to be injective if it is one-to-one
- A function f from A to B is called **onto**, or a **surjection**, if and only if for every element $b ∈ B$ there is an element $a ∈ A$ with $f(a) = b$. A function is called **surjective** if it is onto
- The function f is a **one-to-one correspondence**, or a **bijection**, if it is both one-to-one and onto. We also say that such a function is **bijective**
<br>

- The **inverse function** of $f$ is denoted by $f^{−1}$
- Let $g$ be a function from the set $A$ to the set $B$ and let $f$ be a function from the set $B$ to the set $C$, then the **composition** of the functions $f$ and $g$ is denoted by $f \circ g$
- The value of the **floor function** at $x$ is denoted by $⌊x⌋$
- The value of the **ceiling function** at $x$ is denoted by $⌈x⌉$
- A **partial function** $f$ from $A$ to $B$ is an assignment to each element $a$ in a subject of $A$, called the domain of definition of $f$ , of a unique element $b$ in $B$. We say that $f$ is undefined for elements in $A$ that are not in the domain of definition of $f$. When the domain of definition of $f$ equals $A$, we say that $f$ is a **total function**









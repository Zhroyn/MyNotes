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

### 1.5 Nested Quantifiers


### 1.6 Rules of Inference


### 1.7 Introduction to Proofs


### 1.8 Proof Methods and Strategy
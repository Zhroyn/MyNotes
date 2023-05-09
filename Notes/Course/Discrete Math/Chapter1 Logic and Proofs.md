<!-- TOC -->

- [Logic and Proofs](#logic-and-proofs)
  - [1.1 Propositional Logic](#11-propositional-logic)
  - [1.2 Applications of Propositional Logic](#12-applications-of-propositional-logic)
  - [1.3 Propositional Equivalences](#13-propositional-equivalences)
  - [1.4 Predicates and Quantifiers](#14-predicates-and-quantifiers)
  - [1.5 Nested Quantifiers and Normal Form](#15-nested-quantifiers-and-normal-form)
  - [1.6 Rules of Inference](#16-rules-of-inference)
  - [1.7 Introduction to Proofs](#17-introduction-to-proofs)
  - [1.8 Proof Methods and Strategy](#18-proof-methods-and-strategy)

<!-- /TOC -->





## Logic and Proofs

### 1.1 Propositional Logic
- A proposition is a declarative sentence that is either true or false, but not both
<br>

- `negation` : $\neg p$
  - The truth value of the negation of a proposition in fuzzy logic is 1 minus the truth value of the proposition
- `conjunction` : $p \land q$
  - The truth value of the conjunction of two propositions in fuzzy logic is the minimum of the truth values of the two propositions
- `disjunction` : $p \vee q$
  - The truth value of the disjunction of two propositions in fuzzy logic is the maximum of the truth values of the two propositions
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

- $p \leftrightarrow q ≡ (p → q) ∧ (q → p)$
- $p \leftrightarrow q ≡ ¬p \leftrightarrow ¬q$
- $p \leftrightarrow q ≡ (p ∧ q) ∨ (¬p ∧ ¬q)$
- $¬(p \leftrightarrow q) ≡ p \leftrightarrow ¬q$
<br>

- $p \oplus q \equiv (p \land \neg q)\vee(\neg p \land q)$
- $p \downarrow p \equiv \neg p$
- $(p \downarrow q)\downarrow(p \downarrow q) \equiv p \vee q$
- $(p \downarrow p)\downarrow(q \downarrow q) \equiv p \land q$




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
- The notation $∃xP(x)$ denotes the existential quantification of $P(x)$. Here $\exists$ is called the **existential quantifier**
- The notation $∃!xP(x)$ or $∃_1xP(x)$ states “There exists a unique $x$ such that $P(x)$ is true.” Here $∃!$ is called the **uniqueness quantifier** 
- The quantifiers $∀$ and $∃$ have higher precedence than all logical operators from propositional calculus
<br>

- Statements involving predicates and quantifiers are **logically equivalent** if and only if they have the same truth value no matter which predicates are substituted into these statements and which domain of discourse is used for the variables in these propositional functions
- Suppose $p$ and $q$ are statements involving predicates and quantifiers, we can show $p$ and $q$ are logically equivalent by showing that if one of them is true, then the other is true
<br>

- $∀x(P(x) ∧ Q(x)) \equiv ∀xP(x) ∧ ∀xQ(x)$
- $\exists x(P(x) \vee Q(x)) \equiv \exists xP(x) \vee \exists xQ(x)$
- $∀xP(x) \vee ∀xQ(x) \Rightarrow ∀x(P(x) \vee Q(x))$
- $\exists x(P(x) \land Q(x)) \Rightarrow \exists xP(x) \land \exists xQ(x)$
- De Morgan’s laws for quantifiers : $¬∀xP(x) ≡ ∃x ¬P(x)$, $¬∃xQ(x) ≡ ∀x ¬Q(x)$





### 1.5 Nested Quantifiers and Normal Form
- A conjunction with disjunctive clauses as its conjuncts is said to be in **conjunctive normal form (CNF)** : $(A_{11} \vee … \vee A_{1n_1}) \land … \land (A_{k1} \vee … \vee A_{kn_k}).$
- A disjunction with conjunctive clauses as its disjuncts is said to be in **disjunctive normal form (DNF)** : $(A_{11} \land … \land A_{1n_1}) \vee … \vee (A_{k1} \land … \land A_{kn_k}).$
<br>

- A minterm is a conjunction of literals in which each variable is represented exactly once.
-  If a formula is expressed as a disjunction of minterms, it is said to be in **full disjunctive normal form**.
<br>

- A statement is in **prenex normal form** if it is of the form $Q_1x_1\cdots Q_nx_nB$, where $Q_i$ is $\forall$ or $\exists$ and the predicate $B$ is quantifier free. 
- A formula with no quantifiers is regarded as a trivial case of a prenex normal form.
<br>

- $(\forall x P)\land Q = \forall xP\land Q $
- $(\forall x P)\vee Q = \forall xP\vee Q $
- $(\exists x P)\land Q = \forall xP\land Q $
- $(\exists x P)\vee Q = \forall xP\vee Q $
<br>

- $(\forall x P)\rightarrow Q = \forall x(P\rightarrow Q) $
- $(\exists x P)\rightarrow Q = \exists x(P\rightarrow Q) $
- $P \rightarrow(\forall x Q) = \forall x(P\rightarrow Q) $
- $P \rightarrow(\exists x Q) = \exists x(P\rightarrow Q) $
<br>

- $\forall xP(x) \land \forall xQ(x) \equiv \forall x(P(x) \land Q(x))$
- $\forall xP(x) \land \exists xQ(x) \equiv \forall x\exists y(P(x) \land Q(y))$
- $\exists xP(x) \land \forall xQ(x) \equiv \exists x\forall y(P(x) \land Q(y))$
- $\exists xP(x) \land \exists xQ(x) \equiv \exists x\exists y(P(x) \land Q(y))$
<br>

- $\forall xP(x) \vee \forall xQ(x) \equiv \forall x\forall y(P(x) \vee Q(y))$
- $\forall xP(x) \vee \exists xQ(x) \equiv \forall x\exists y(P(x) \vee Q(y))$
- $\exists xP(x) \vee \forall xQ(x) \equiv \exists x\forall y(P(x) \vee Q(y))$
- $\exists xP(x) \vee \exists xQ(x) \equiv \exists x(P(x) \vee Q(x))$






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








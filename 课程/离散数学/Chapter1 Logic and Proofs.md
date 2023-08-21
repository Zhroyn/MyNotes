
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Logic and Proofs](#logic-and-proofs)
  - [1.1 Propositional Logic](#11-propositional-logic)
  - [1.2 Applications of Propositional Logic](#12-applications-of-propositional-logic)
  - [1.3 Propositional Equivalences](#13-propositional-equivalences)
  - [1.4 Predicates and Quantifiers](#14-predicates-and-quantifiers)
  - [1.5 Nested Quantifiers and Normal Form](#15-nested-quantifiers-and-normal-form)
  - [1.6 Rules of Inference](#16-rules-of-inference)
  - [1.7 Introduction to Proofs](#17-introduction-to-proofs)
  - [1.8 Proof Methods and Strategy](#18-proof-methods-and-strategy)
- [Shorthand](#shorthand)

<!-- /code_chunk_output -->







## Logic and Proofs

### 1.1 Propositional Logic
- A proposition is a declarative sentence that is either true or false, but not both
<br>

- `negation` : $\neg p$
  - The truth value of the negation of a proposition in fuzzy logic is 1 minus the truth value of the proposition
- `conjunction` : $p \wedge q$
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
|$\wedge$| 2 |
|$\vee$| 3 |
|$\rightarrow$| 4 |
|$\leftrightarrow$| 5 |








<br>

### 1.2 Applications of Propositional Logic
- System specifications should be **consistent**, that is, they should not contain conflicting requirements that could be used to derive a contradiction






<br>

### 1.3 Propositional Equivalences
- A compound proposition that is always true, no matter what the truth values of the propositional variables that occur in it, is called a **tautology**
- A compound proposition that is always false is called a **contradiction**
- A compound proposition that is neither a tautology nor a contradiction is called a **contingency**
<br>

- The compound propositions p and q are called **logically equivalent** if $p \leftrightarrow q$ is a tautology
- The notation $p \equiv q$ or $p \Leftrightarrow q$ denotes that p and q are logically equivalent
<br>

- Identity laws : $p \wedge T ≡ p$, $p \vee F ≡ p$
- Domination laws : $p \vee T ≡ T$, $p \wedge F ≡ F$
- Idempotent laws : $p \vee p ≡ p$, $p \wedge p ≡ p$
- Double negation law : $\neg (\neg p) ≡ p$ 
- Commutative laws : $p \vee q ≡ q \vee p$, $p \wedge q ≡ q \wedge p$
- Associative laws : $(p \vee q) \vee r ≡ p \vee (q \vee r)$, $(p \wedge q) \wedge r ≡ p \wedge (q \wedge r)$
- Distributive laws : $p \vee (q \wedge r) ≡ (p \vee q) \wedge (p \vee r)$, $p \wedge (q \vee r) ≡ (p \wedge q) \vee (p \wedge r)$
- De Morgan’s laws : $\neg (p \wedge q) ≡ \neg p \vee \neg q$, $\neg(p \vee q) ≡ \neg p \wedge \neg q$
  - $\neg(\vee_{j=1}^n p_j) \equiv \wedge_{j=1}^n \neg p_j$, $\neg(\wedge_{j=1}^n p_j) \equiv \vee_{j=1}^n \neg p_j$
- Absorption laws : $p \vee (p \wedge q) ≡ p$, $p \wedge (p \vee q) ≡ p$
- Negation laws : $p \vee \neg p ≡ T$, $p \wedge \neg p ≡ F$
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

- $p \oplus q \equiv (p \wedge \neg q)\vee(\neg p \wedge q)$
- $p \downarrow p \equiv \neg p$
- $(p \downarrow q)\downarrow(p \downarrow q) \equiv p \vee q$
- $(p \downarrow p)\downarrow(q \downarrow q) \equiv p \wedge q$







<br>

### 1.4 Predicates and Quantifiers
- Many mathematical statements assert that a property is true for all values of a variable in a particular domain, called the **domain of discourse**, often just referred to as the **domain**
- The area of logic that deals with predicates and quantifiers is called the **predicate calculus**

**Predicates**
- The statement $P(x)$ is said to be the value of the **propositional function** $P$ at $x$. Once a value has been assigned to the variable $x$, the statement $P(x)$ becomes a proposition and has a truth value
- A **predicate** (propositional function) is a statement that contains variables. Once the values of the variables are specified, the function has a truth value.
- A statement of the form $P(x_1, x_2, \dots , x_n)$ is the value of the propositional function $P$ at the n-tuple $(x_1, x_2, \dots , x_n)$, and $P$ is also called an **n-place predicate** or an **n-ary predicate**
<br>

**Quantifiers**
- The notation $∀xP(x)$ denotes the universal quantification of $P(x)$. Here $\forall$ is called the **universal quantifier**. An element for which $P(x)$ is false is called a **counterexample** to $∀xP(x)$
- The notation $∃xP(x)$ denotes the existential quantification of $P(x)$. Here $\exists$ is called the **existential quantifier**
- The notation $∃!xP(x)$ or $∃_1xP(x)$ states “There exists a unique $x$ such that $P(x)$ is true.” Here $∃!$ is called the **uniqueness quantifier** 

**Quantifiers with Restricted Domains**
- An abbreviated notation is often used to restrict the domain of a quantifier.
- In this notation, a condition a variable must satisfy is included after the quantifier, e.g. $\forall x < 0 (x^2 > 0) \equiv \forall x(x < 0 \rightarrow x^2 > 0)$, $\exists z > 0 (z^2 = 2) \equiv \exists z(z > 0 \wedge z^2 = 2) $

**Precedence of Quantifiers**
- The quantifiers $∀$ and $∃$ have higher precedence than all logical operators from propositional calculus

**Binding Variables**
- When a quantifier is used on the variable x, we say that this occurrence of the variable is **bound**.
- An occurrence of a variable that is not bound by a quantifier or set equal to a particular value is said to be **free**.
- The part of a logical expression to which a quantifier is applied is called the **scope** of this quantifier. Consequently, a variable is free if it is outside the scope of all quantifiers in the formula that specify this variable.

**Logical Equivalences Involving Quantifiers**
- Statements involving predicates and quantifiers are **logically equivalent** if and only if they have the same truth 
  - for every predicate substituted into these statements
  - for every domain of discourse used for the variables in the expressions
- Suppose $p$ and $q$ are statements involving predicates and quantifiers, we can show $p$ and $q$ are logically equivalent by showing that if one of them is true, then the other is true
<br>

- $∀x(P(x) ∧ Q(x)) \equiv ∀xP(x) ∧ ∀xQ(x)$
- $\exists x(P(x) \vee Q(x)) \equiv \exists xP(x) \vee \exists xQ(x)$
- $∀xP(x) \vee ∀xQ(x) \Rightarrow ∀x(P(x) \vee Q(x))$
- $\exists x(P(x) \wedge Q(x)) \Rightarrow \exists xP(x) \wedge \exists xQ(x)$
<br>

- $(\forall x P)\wedge Q \equiv \forall x(P\wedge Q) $
- $(\forall x P)\vee Q \equiv \forall x(P\vee Q) $
- $(\exists x P)\wedge Q \equiv \exists x(P\wedge Q) $
- $(\exists x P)\vee Q \equiv \exists x(P\vee Q) $
<br>

- $(\forall x P)\rightarrow Q \equiv \forall x(P\rightarrow Q) $
- $(\exists x P)\rightarrow Q \equiv \exists x(P\rightarrow Q) $
- $P \rightarrow(\forall x Q) \equiv \forall x(P\rightarrow Q) $
- $P \rightarrow(\exists x Q) \equiv \exists x(P\rightarrow Q) $

**Negating Quantified Expressions**
De Morgan’s laws for quantifiers : 
$$¬∀xP(x) ≡ ∃x ¬P(x)\\
¬∃xQ(x) ≡ ∀x ¬Q(x)$$








<br>

### 1.5 Nested Quantifiers and Normal Form
**Nested Quantifier**
- Two quantifiers are **nested** if one is within the scope of the other.
- Everyone has exactly one best friend : $\forall x \exists y \forall z(B(x, y)\wedge ((z \neq y)\rightarrow \neg B(x, z)))$
- The order of nested quantifiers matters if quantifiers are of different types.
<br>

- $\forall xP(x) \wedge \forall xQ(x) \equiv \forall x(P(x) \wedge Q(x))$
- $\forall xP(x) \wedge \exists xQ(x) \equiv \forall x\exists y(P(x) \wedge Q(y))$
- $\exists xP(x) \wedge \forall xQ(x) \equiv \exists x\forall y(P(x) \wedge Q(y))$
- $\exists xP(x) \wedge \exists xQ(x) \equiv \exists x\exists y(P(x) \wedge Q(y))$
<br>

- $\forall xP(x) \vee \forall xQ(x) \equiv \forall x\forall y(P(x) \vee Q(y))$
- $\forall xP(x) \vee \exists xQ(x) \equiv \forall x\exists y(P(x) \vee Q(y))$
- $\exists xP(x) \vee \forall xQ(x) \equiv \exists x\forall y(P(x) \vee Q(y))$
- $\exists xP(x) \vee \exists xQ(x) \equiv \exists x(P(x) \vee Q(x))$

**Normal Form**
- Disjunctions with literals as disjuncts are called **disjunctive clauses**.
- Conjunctions with literals as conjuncts are called **conjunctive clauses**.
- Disjunctive and conjunctive clauses are simply called clauses.
<br>

- A disjunction with conjunctive clauses as its disjuncts is said to be in **disjunctive normal form (DNF)** : $(A_{11} \wedge … \wedge A_{1n_1}) \vee … \vee (A_{k1} \wedge … \wedge A_{kn_k}).$
- A conjunction with disjunctive clauses as its conjuncts is said to be in **conjunctive normal form (CNF)** : $(A_{11} \vee … \vee A_{1n_1}) \wedge … \wedge (A_{k1} \vee … \vee A_{kn_k}).$
<br>

- A minterm is a conjunction of literals in which each variable is represented exactly once.
- If a formula is expressed as a disjunction of minterms, it is said to be in **full disjunctive normal form**.
- A disjunction of minterms is true if and only if one of its constituents minterms is true, so the number of cases when the statement is true is exactly the number of minterms.
$$
\begin{aligned}
  & (p \wedge q)\vee(\neg p \wedge r)\vee(q \wedge r) \\
  \equiv & (p \wedge q \wedge (r \vee \neg r))\vee(\neg p \wedge (q \vee \neg q) \wedge r)\vee((p \vee \neg p) \wedge q \wedge r) \\
  \equiv & (p \wedge q \wedge r)\vee(p \wedge q \wedge \neg r)\vee(\neg p \wedge q \wedge r)\vee(\neg p \wedge \neg q \wedge r) \\
  & \vee(p \wedge q \wedge r)\vee(\neg p \wedge q \wedge r) \\
  \equiv & (p \wedge q \wedge r)\vee(p \wedge q \wedge \neg r)\vee(\neg p \wedge q \wedge r)\vee(\neg p \wedge \neg q \wedge r)
\end{aligned}
$$

- A statement is in **prenex normal form** if it is of the form $Q_1x_1\cdots Q_nx_nB$, where $Q_i$ is $\forall$ or $\exists$ and the predicate $B$ is quantifier free. 
- A formula with no quantifiers is regarded as a trivial case of a prenex normal form.









<br>

### 1.6 Rules of Inference
- An **argument** in propositional logic is a sequence of statements that end with a conclusion.
- All but the final proposition in the argument are called **premises**.
- The final proposition is called the **conclusion**.
- Proofs in mathematics are **valid arguments**. An argument is valid if the truth of all its premises implies that the conclusion is true.
<br>

- An **argument form** in propositional logic is a sequence of compound propositions involving propositional variables.
- An argument form is valid if no matter which particular propositions are substituted for the propositional variables in its premises, the conclusion is true if the premises are all true.
<br>

- **Rules of inference** are simple argument forms whose correctness we can establish with truth tables.
- To use resolution as the only rule of inference, we can firstly write the premises and the conclusion as CNF.

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







<br>

### 1.7 Introduction to Proofs
- A **direct proof** of a conditional statement $p → q$ is constructed when the first step is the assumption that $p$ is true, and then we show that $q$ must also be true
<br>

- Proofs of theorems that do not start with the premises and end with the conclusion, are called **indirect proofs**
- An extremely useful type of indirect proof is known as **proof by contraposition**. In a proof by contraposition of $p → q$, we take $¬q$ as a premise, and using axioms, definitions, and then we show that $¬p$ must follow
- Because the statement $r ∧ ¬r$ is a contradiction whenever $r$ is a proposition, we can prove that $p$ is true if we can show that $¬p → (r ∧ ¬r)$ is true for some proposition $r$. Proofs of this type are called **proofs by contradiction**
<br>

- If we can show that $p$ is false, then we have a proof, called a **vacuous proof**, of the conditional statement $p → q$
- A proof of $p → q$ that uses the fact that $q$ is true is called a **trivial proof**







<br>

### 1.8 Proof Methods and Strategy
- The original conditional statement with a hypothesis made up of a disjunction of the propositions $p_1, p_2, … , p_n$ can be proved by proving each of the n conditional statements $p_i → q, i = 1, 2, … , n$,  individually. Such an argument is called a **proof by cases**
- Some theorems can be proved by examining a relatively small number of examples. Such proofs are called **exhaustive proofs**, or **proofs by exhaustion** because these proofs proceed by exhausting all possibilities
<br>

- A proof of a proposition of the form $∃xP(x)$ is called an **existence proof**. There are several ways to prove a theorem of this type
- One type of existence proof is called **constructive**
- Another type of existence proof is **nonconstructive**; that is, we directly prove that $∃xP(x)$ is true in some other way. One common method is to use proof by contradiction; that is, we show that the negation of the existential quantification implies a contradiction
<br>

- The two parts of a **uniqueness proof** are:
  - Existence: show that an element $x$ with the desired property exists.
  - Uniqueness: show that if $x$ and $y$ both have the desired property, then $x = y$
<br>

- Using the premises, together with axioms and known theorems, you can construct a proof using a sequence of steps that leads to the conclusion. This type of reasoning is called **forward reasoning**
- In such cases it may be helpful to use **backward reasoning**. To reason backward to prove a statement $q$, we find a statement $p$ that we can prove with the property that $p → q$







<br>

## Shorthand
**Propositional Logic**
- converse
- inverse
- contrapositive

**Propositional Equivalences**
- tautology
- contradiction
- **contigency**
<br>

- Absorption laws : $p \vee (p \wedge q) ≡ p$, $p \wedge (p \vee q) ≡ p$
- $p → q ≡ ¬p ∨ q$
- $p \leftrightarrow q ≡ (¬p ∨ q) ∧ (p ∨ ¬q) ≡ (p ∧ q) ∨ (¬p ∧ ¬q)$
- $(p → q) ∧ (p → r) ≡ p → (q ∧ r)$
- $(p → r) ∧ (q → r) ≡ (p ∨ q) → r$
- $(p → q) ∨ (p → r) ≡ p → (q ∨ r)$
- $(p → r) ∨ (q → r) ≡ (p ∧ q) → r$
<br>

- $p \downarrow p \equiv \neg p$
- $(p \downarrow q)\downarrow(p \downarrow q) \equiv p \vee q$
- $(p \downarrow p)\downarrow(q \downarrow q) \equiv p \wedge q$


**Predicates and Quantifiers**
- $∀x(P(x) ∧ Q(x)) \equiv ∀xP(x) ∧ ∀xQ(x)$
- $\exists x(P(x) \vee Q(x)) \equiv \exists xP(x) \vee \exists xQ(x)$
- $∀xP(x) \vee ∀xQ(x) \Rightarrow ∀x(P(x) \vee Q(x))$
- $\exists x(P(x) \wedge Q(x)) \Rightarrow \exists xP(x) \wedge \exists xQ(x)$

**Nested Quantifiers and Normal Form**
- CNF
- DNF

**Rules of Inference**
- $(p ∧ (p → q)) → q$
- $(¬q ∧ (p → q)) → ¬p$
- $((p → q) ∧ (q → r)) → (p → r)$
- $((p ∨ q) ∧ ¬p) → q$
- $p → (p ∨ q)$
- $(p ∧ q) → p$
- $((p) ∧ (q)) → (p ∧ q)$
- Resolution
<br>

- Universal instantiation
- Universal generalization
- Existential instantiation
- Existential generalization
- Universal modus ponens
- Universal modus tollens

**Introduction to Proofs**
- proof by contraposition
- proofs by contradiction
- vacuous proof: a proof show that $p$ is false
- trivial proof: a proof show that $q$ is true

**Proof Methods and Strategy**
- Existence proof
  - constructive
  - nonconstructive : the negation of the existential quantification implies a contradiction
- Uniqueness proof
  - Existence
  - Uniqueness : if $x$ and $y$ both have the desired property, then $x = y$






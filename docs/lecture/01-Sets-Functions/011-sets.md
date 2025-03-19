# Sets

This lecture will not cover the foundations of logic and the axiomatic approach to set theory.
We stick to the *naive* set theory in the sense that we will not encounter "too large objects" for which paradox may arise if the objects are defined too naively&mdash;see Russell's paradox.
We refer to Jech[@jech2003] for a comprehensive overview of set theory.

The language of set theory consists of the binary predicate $\in$ that describes the membership relation between objects, that is, $x\in A$ means that $x$ is an *element* or a member of $A$.
A set is a collection of objects that belong to it.
We usually denote sets with capital letters $A,B,\ldots$ and elements of these sets with lowercase letters $x,y,\ldots$.
Note that sets can also be elements of other sets.
We can define sets either by an explicit listing such as $A=\{\text{pig},\text{horse},\text{table}\}$, or by a "property rule" $P$, i.e. $A=\{x\colon x\text{ has property }P\}$.
To avoid logical problems, we assume that this rule applies only to some elements of a given larger set.
For instance,

\[2\mathbb{Z}:=\{x\in\mathbb{Z}\colon x\text{ is even}\}\]

Typical sets we will use are:

- Natural numbers: $\mathbb{N}=\{1,2,3,\ldots\}$ and $\mathbb{N}_0=\{0,1,2,\ldots\}$;
- Integers: $\mathbb{Z}=\{\ldots,-2,-1,0,1,2,\ldots\}$;
- Rational numbers: $\mathbb{Q}$;
- Real numbers: $\mathbb{R}$;
- $\mathbb{R}^d$, the $d$-dimensional Euclidean space.

Let us introduce the following operations or relations between sets:

- **Inclusion** $\subseteq$: Given two sets $A$ and $B$, we denote by $A\subseteq B$ that every element $x$ in $A$ also belongs to $B$.
    The inclusion defines a partial order (it is reflexive, transitive, and antisymmetric).
- **Empty set** $\emptyset$: The set containing no elements is called the empty set and is denoted by $\emptyset$.
    It is the smallest set with respect to inclusion and is universal in this axiomatic system.
- **Intersection** $\cap$: The intersection of two sets $A$ and $B$, denoted by $A\cap B$, is defined as the largest set that is contained in both $A$ and $B$.
    In other words, $A\cap B=\{x\colon x\in A\text{ and }x\in B\}$.
    Two sets $A$ and $B$ are said to be **disjoint** if their intersection is empty, i.e. $A\cap B=\emptyset$.
- **Union** $\cup$: The union of two sets $A$ and $B$, denoted by $A\cup B$, is defined as the smallest set that contains all elements of either $A$ or $B$.
    In other words, $A\cup B=\{x\colon x\in A\text{ or }x\in B\}$.
- **Complement** ${}^c$: Given a set $X$, the complement of a subset $A$ (relative to $X$) is given by $A^c=\{x\in X\colon x\not\in A\}$.
- **Difference** $\setminus$: Given two subsets $A$ and $B$ of a set $X$, the difference $A\setminus B$ is defined as $\{x\colon x\in A\text{ and }x\not\in B\}$, which is equivalent to $A\cap B^c$.
- **Symmetric difference** $\Delta$ Given two subsets $A$ and $B$ of a set $X$, the symmetric difference is defined as $A\Delta B:=(A\setminus B)\cup(B\setminus A)$.

Given a set $X$, we can define its **power set** as $2^X:=\{A\subseteq X\}$.
Note that the power set always contains both $X$ and the empty set $\emptyset$.
In particular, $2^\emptyset=\{\emptyset\}$ is the set containing only the empty set.

!!! proposition "Proposition"
    The power set $2^X$ of a set $X$, together with the operations $\cup$, $\cap$, ${}^c$, and the two distinguished elements $\emptyset$ and $X$, satisfies the properties of a Boolean algebra.
    
    1. $\emptyset^c=X$ and $X^c=\emptyset$.
    2. Identity laws: $A\cap\emptyset=\emptyset$, $A\cap X=A$, $A\cup\emptyset=A$, and $A\cup X=X$.
    3. Complement laws: $A\cap A^c=\emptyset$ and $A\cup A^c=X$.
    4. Double complement law: $(A^c)^c=A$.
    5. Idempotent laws: $A\cap A=A$ and $A\cup A=A$.
    6. De Morgan laws: $(A\cap B)^c=A^c\cup B^c$ and $(A\cup B)^c=A^c\cap B^c$.
    7. Commutative laws: $A\cap B=B\cap A$ and $A\cup B=B\cup A$.
    8. Associative laws: $A\cap(B\cap C)=(A\cap B)\cap C$ and $A\cup(B\cup C)=(A\cup B)\cup C$.
    9. Distributive laws: $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$ and $A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$.

??? proof "Proof"
    Left as an exercise.



??? remark "Remark: Boolean Ring"
    The power set $2^X$ of a set $X$, together with the operations $\Delta$, $\cap$, and the two distinguished elements $\emptyset$ and $X$, satisfies the properties of a Boolean ring, that is:

    1. $\Delta$ and $\cap$ are associative and commutative.
    2. Identity law: $A\Delta\emptyset=A$ and $A\cap X=A$.
    3. Inverse law: $A\Delta A^c=X$.
    4. Distributive law: $A\cap(B\Delta C)=(A\cap B)\Delta(A\cap C)$.


The *Cartesian product* $A\times B$ of two sets $A$ and $B$ is the collection of ordered pairs $(x,y)$ such that $x\in A$ and $y\in B$.

Given the Cartesian product, we can define functions:

!!! definition "Definition: Functions"
    A function $f:X\to Y$ is an ordered triple $(X, Y, G)$, where $G\subseteq X\times Y$ is called the *graph* of $f$ and satisfies the property that for every $x\in X$, there exists a unique $y\in Y$ such that $(x,y)\in G$.(1)
    {.annotate}

    1. This definition requires $Y$ to be non-empty if $X$ is non-empty. If $X$ is empty, then $G=\emptyset$, and this function is called the empty function.

    For $x\in X$, this unique element $y\in Y$ such that $(x,y)\in G$ is denoted by $f(x)$.

A function is called

* **injective** if $x\neq y$ implies $f(x)\neq f(y)$;
* **surjective** if for every $y\in Y$, there exists $x\in X$ such that $f(x)=y$;
* **bijective** if it is both injective and surjective.

Given a set $I$ and a non-empty set $X$, a *family* of elements in $X$ is a function $f:I\to X$, $i\mapsto f(i)$.
We usually denote this function as $(x_i)_{i\in I}$, where $x_i\in X$ for every $i$.(1)
If $I=\mathbb{N}$, we also call it a *sequence* or a *countable family*.
If there is no risk of confusion, we use the notation $(x_i)$ for an arbitrary family of elements in $X$ and $(x_n)$ for a countable family&mdash;or sequence&mdash;in $X$.
{.annotate}

1. A family $(x_i)_{i\in I}$ is different from the collection $\{x_i: i\in I\}$.
  For instance, consider the family $(x_n)_{n\in\mathbb{N}}$ where $x_n=1$ if $n$ is odd and $x_n=0$ if $n$ is even.
  Then $\{x_n:n\in\mathbb{N}\}=\{0,1\}$, while $(x_n)_{n\in\mathbb{N}}=(1,0,1,0,1,\ldots)$.}


Given a family of sets $(X_i)=(X_i)_{i\in I}$, we define the Cartesian product of these sets as the collection of families $(x_i)=(x_i)_{i\in I}$ such that $x_i$ is in $X_i$ for every $i$, denoted by

\[
\prod X_i=\prod_{i\in I}X_i=\{(x_i)\colon x_i\in X_i \text{ for every } i\}.
\]

!!! proposition "Proposition"
    The Boolean algebra $2^X$ is *complete*, meaning that for every family of sets $(A_i)$, there exists a minimum and a maximum with respect to inclusion in $2^X$.(1)
    {.annotate}

    1. That is, there exist subsets $A$ and $B$ such that $A\subseteq A_i\subseteq B$ for every $i$, and if $\tilde{A}$ and $\tilde{B}$ also satisfy this property, then $\tilde{A}\subseteq A$ and $B\subseteq \tilde{B}$.

    We denote this minimum and maximum by

    \[
    \begin{align*}
      \bigcap A_i&=\{x\in X\colon x\in A_i \text{ for all } i\}
      &
      \bigcup A_i& =\{x\in X\colon x\in A_i \text{ for some } i\}
    \end{align*}
    \]

    Furthermore, it holds that

    \[
    \begin{equation}
    \left(\bigcap A_i\right)^c=\bigcup A_i^c, \quad
    \left(\bigcup A_i\right)^c=\bigcap A_i^c
    \end{equation}
    \]

    as well as

    \[
    \begin{equation}
    C\cap\left(\bigcup A_i\right)=\bigcup (C\cap A_i), \quad
    C\cup\left(\bigcap A_i\right)=\bigcap (A_i\cup C)
    \end{equation}
    \]

??? proof "Proof"
    Left to the reader.


Given a function $f:X\to Y$ and subsets $A\subseteq X$ and $B\subseteq Y$, we define the

* **image:** 

    \[
    \begin{equation}
    f(A) := \left\{ y\in Y\colon y=f(x) \text{ for some } x\in A \right\}\subseteq Y
    \end{equation}
    \]

* **pre-image:**

    \[
    \begin{equation}
    f^{-1}(B) := \left\{ x\in X\colon f(x)\in B \right\}\subseteq X
    \end{equation}
    \]

<span id="prop-preimage"></span>
!!! proposition 
    The image and pre-image define functions from $2^X$ to $2^Y$ and $2^Y$ to $2^X$, respectively, with the following properties:

    \[
    \begin{align}
      f(A_1) &\subseteq f(A_2), & f^{-1}(B_1) &\subseteq f^{-1}(B_2)\\
      f\left(\cup A_i\right) &= \cup f(A_i), & f^{-1}\left(\cup B_j\right) &= \cup f^{-1}(B_j)\\
      f\left(\cap A_i\right) &\subseteq \cap f(A_i), & f^{-1}\left(\cap B_j\right) &= \cap f^{-1}(B_j)\\
      f(A^c) &\subseteq f(A)^c, & f^{-1}(B^c) &= \left(f^{-1}(B)\right)^c\\
      A &\subseteq f^{-1}\left(f(A)\right), & B &\subseteq f\left(f^{-1}(B)\right)
    \end{align}
    \]

??? proof "Proof"
    Left to the reader.

!!! remark "Remark"
    The pre-image function&mdash;unlike the image function&mdash;respects the Boolean operations of the power set.
    In other words, it is a morphism.
    Any structure defined on a subset of $2^Y$ with intersection, union, and complementation will carry over to a substructure of $2^X$ with the same properties via the pre-image function.


As for the **cardinality** of sets, we say that a set $X$ has cardinality smaller than $Y$ if there exists an injective function $f:X\to Y$.
Two sets have same cardinality if such a function is bijective.
A set $X$ is called 

* **finite** if there exists $n$ in $\mathbb{N}$ such $X$ has the same cardinality as $\{1, \ldots, n\}$.
  In this case $n$ is the cardinality of this set.
* **enumerable** if $X$ has the same cardinality as $\mathbb{N}$.
  In this case we denote by $\aleph_0$ the cardinality of this set.
* **countable** if $X$ is either finite or enumerable.

The emptyset has cardinality $0$ and is the only such set.
If $X$ is finite of cardinality $n$ in $\mathbb{N}$, then the cardinality of $2^X$ is $2^n$.
In general, the cardinality of $2^X$ is always strictly greater than the cardinality of $X$, that is, while there obviously exists an injective function $X \ni x \mapsto \{x\} \in 2^X$, the reverse is not true.
The set of real numbers of any interval of real numbers has a cardinality that is striclty larger than $\mathbb{N}$.
However, $\mathbb{Z}$ is obviously enumerable by the injective function $f\colon \mathbb{Z}\to \mathbb{N}$ such that $n \mapsto f(n)=2n$ if $n$ is positive and $n \mapsto f(n) = -2n -1$ if $n$ is strictly negative.
Classsical but less obvious is that $\mathbb{Q}$ has the same cardinality as $\mathbb{N}$.

!!! proposition 

    Let $(X_n)$ be a countable family of countable sets, then $\cup X_n$ is countable.

    In particular $\mathbb{Q}$ is countable.

??? proof

    Define $X = \cup X_n$.
    Without loss of generality, we can assume that the family is enumerable, that is $(X_n) = (X_n)_{n=1, \ldots}$.
    Furthermore, up to redefining sequentially $Y_1 = X_1$ and $Y_{n+1} = X_{n+1} \setminus Y{n}$ for which holds $\cup Y_n = X$, we can also assume that the $(X_n)$ are pairewize disjoint.
    Up to slight modification, we can also assume that each $X_n$ is itself enumerable.
    Since each set is enumerable, we can write uniquely $X_n =\{ x_{n,m}: m \in \mathbb{N}\}$ such that $X = \{x_{n, m}\colon n \in \mathbb{N} \text{ and } m \in \mathbb{N}\}$ which has the same cardinality as $\mathbb{N}\times \mathbb{N}$.
    However $\mathbb{N}\times \mathbb{N}$ has the same cardinality as $\mathbb{N}$.
    Indeed, it is equal to the countable union of the disjoint finite sets $Y_k =\{(m, n)\colon m+n = k\}$ each being of cardinality $k$ from which an injection can be built into $\mathbb{N}$.

    As for $\mathbb{Q}$, it is the countable union of the countable sets $X_n = \{m / n\colon m \in \mathbb{Z} \}$.
    

Given a sequence $(X_n)$ of sets we define the $\limsup$ and $\liminf$ of this sequence as the sets:

\[
\begin{align*}
  \limsup X_n &:= \cap_n \cup_{k\geq n} X_k & \liminf X_n &:= \cup_n \cap_{k \geq n} X_k
\end{align*}
\]

In other term, the $\limsup$ represent the set of those elements $x$ which are contained in infinitely many $X_n$ while the $\liminf$ represent the set of those elements $x$ that are contained in all but finitely many $X_n$.
For $x$ in $\liminf X_n$, it follows that there exists $n_0$ such that $x$ belongs to any $X_n$ for $n\geq n_0$. 
Hence $x$ is in $\cup_{k\geq n} X_k$ for any $n$ showing that $x$ is in $\limsup X_n$.
Therefore $\liminf X_n \subseteq \limsup X_n$.
The sequence of sets converges if $\liminf X_n = \limsup X_n$.

!!! definition 

    Given a subset $A$ of $X$, we define the **indicator** function of $A$ as the function

    \[
    \begin{equation*}
      \begin{split}
        1_A \colon X & \longrightarrow \mathbb{R}\\
                   x & \longmapsto 1_A(x) = 
                        \begin{cases}
                          1 & \text{if }x \in A\\
                          0 & \text{otherwize }
                        \end{cases}
      \end{split}
    \end{equation*}
    \]


![Indicator Function](./../../images/indicator_dark.svg#only-dark){align = right}
![Indicator Function](./../../images/indicator_white.svg#only-light){ align = right}


!!! exercise

    * Show that $(0,1)$ has the same cardinality as $(0, 1]$.
    * Let $f\colon \mathbb{R} \to \mathbb{R}$ be an increasing function.
      Show that the set $X = \{x \in \mathbb{R}\colon \lim_{y\nearrow x} f(y) < \lim_{y\searrow x} f(y)\}$ of discountinuity of $f$ is countable.
    * Show that $(\limsup X_n^c)^c = \liminf X_n$, $\liminf X_n = \{x \in X\colon \liminf 1_{A_n}(x) = 1\}$ and $\limsup X_n = \{x \in X \colon \limsup 1_{A_n}(x) = 1\}$.
    * Show that $1_{\cup A_n} = \sum 1_{A_n}$ whenever $(A_n)$ are disjoints.
      Show that $1_{\cap A_n} = \prod 1_{A_n}$.


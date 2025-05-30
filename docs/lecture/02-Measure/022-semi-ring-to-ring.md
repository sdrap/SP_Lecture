# From Semi-Ring to Ring

The definition of measure is well and fine, but beyond the obvious countable sets, we want to be able to construct measure on more complex sets such as the Lebesgue measure on the Borel $\sigma$-algebra.
In other terms if such objects do really make sense.

In view of the Lebesgue's measure, let us consider the slightly more general concept of **Stieljes** integral.
Consider the real line $X = \mathbb{R}$ with the semi-ring $\mathcal{S}$ of half open intervals $(a, b]$ for $a\leq b$.
Given any increasing function $F\colon \mathbb{R} \to \mathbb{R}$, increasing and right continuous, that is, $F(x) = \lim_{y \searrow x} F(y)$.
We define the set function $\mu \colon \mathcal{S}\to [0, \infty]$ given by

\[
\begin{equation*}
 \mu[(a, b] ] = F(b)-F(a) \quad \text{for any }a\leq b
\end{equation*}
\]

It is direct to check that this indeed defines a pre-measure on $\mathcal{S}$.
The case of the Lebesgue's measure is by taking $F(x) = x$.

This represents the basic requirement we want to have given $F$ for a measure.
The first step to carry is whether this set function can be extended uniquely to a set function on the ring generated by $\mathcal{S}$.


<span id="prop-pre-mes-semi-ring-to-ring"></span>
!!! proposition "Proposition"
    Let $\mu$ be a pre-measure on a semi-ring $\mathcal{S}$.
    There exists a unique pre-measure extension of $\mu$ on the ring $\mathcal{R}=r(\mathcal{S})$ generated by $\mathcal{S}$.

!!! proof "Proof"
    We know from the [proposition](./../01-Sets-Functions/012-measurability-topology.md#prop-semi-ring-to-ring) on the relationship between semi-ring and rings that every element of $\mathcal{R}$ can be written as a finite union of disjoint elements of $\mathcal{S}$.
    Let $A=\cup_{1\leq k\leq n}A_k$ for a finite disjoint family $(A_k)_{1\leq k\leq n}$ and define

    \[
    \begin{equation}
        \nu\left[ A \right]=\sum_{1\leq k\leq n} \mu\left[ A_k \right].
    \end{equation}
    \]

    This definition does not depend on the choice of the disjoint family.
    Indeed, suppose $A=\cup_{1\leq l\leq m}B_j$ for another finite disjoint family $(B_l)_{1\leq l\leq m}$ of elements of $\mathcal{S}$.
    Since $A_k=\cup_{1\leq l\leq m}A_k\cap B_l$ as well as $B_l=\cup_{1\leq k\leq n}A_k\cap B_l$ are both disjoint unions of elements in $\mathcal{S}$ for every $k$ and $l$, it holds

    \[
    \begin{align}
        \nu\left[ A \right] &= \sum_{1\leq k\leq n}\mu\left[A_k\right]\\
        &=\sum_{1\leq k\leq n}\sum_{1\leq l\leq m}\mu\left[ A_k\cap B_l \right]\\
        &=\sum_{1\leq l\leq m}\sum_{1\leq k\leq n} \mu\left[ A_k\cap B_l \right]\\
        &=\sum_{1\leq l\leq m}\mu\left[ B_l \right].
    \end{align}
    \]

    This shows that $\nu$ is well defined on $\mathcal{R}$.
    By definition, it clearly holds that $\nu$ is an extension of $\mu$.
    Let us show that it is a content.
    Clearly, $\nu[\emptyset]=\mu[\emptyset]=0$.
    For $A=\cup_{1\leq k\leq n}A_k$, a finite disjoint union of elements in $\mathcal{R}$, we can write each $A_k=\cup_{1\leq l\leq m_k}B_{lk}$ as a finite union of elements in $\mathcal{S}$.
    It follows that $A=\cup_{1\leq k}\cup_{1\leq l\leq m_l}B_{kl}$ is a finite disjoint union of elements in $\mathcal{S}$.
    Hence

    \[
    \begin{equation}
        \nu\left[ A \right]=\sum_{1\leq k\leq n}\sum_{1\leq l\leq m_l}\mu\left[ B_{kl} \right]=\sum_{q\leq k\leq n}\nu\left[\cup_{1\leq l\leq m_k}B_{kl}  \right]=\sum_{1\leq k\leq n}\nu\left[ A_k \right].
    \end{equation}
    \]

    This proves finite additivity.

    As for the uniqueness of the extension as a content, it is immediate from the finite additivity and the fact that every element in $\mathcal{R}$ can be written as a disjoint union of finitely many elements in $\mathcal{S}$.  


Before handling the extension under the additional assumption that $\mu$ is $\sigma$-additive, let us treat some properties of contents.


<span id="lem-propcontentsemiring"></span>
!!! lemma
    Let $\mu$ be a pre-measure on a semi-ring $\mathcal{S}$.
    Then it holds:

    * *(i)* $\mu$ is monotone, that is $\mu[A]\leq \mu[B]$ for every $A\subseteq B$ with $A,B$ in $\mathcal{S}$.
    * *(ii)* $\mu$ is sub-additive.
    * *(iii)* $\mu$ is $\sigma$-additive if and only if $\mu$ is $\sigma$-sub-additive.

    ------------

    Let $\mu$ be a pre-measure on a ring $\mathcal{R}$.
    Then it holds:

    * *(a)* $\mu[B\setminus A]=\mu[B]-\mu[A]$ for every $A\subseteq B$ with $A,B$ in $\mathcal{R}$.
    * *(b)* $\mu[A\cup B]+\mu[A\cap B]=\mu[A]+\mu[B]$ for every $A,B$ in $\mathcal{R}$.
    * *(c)* $\sum \mu[A_n]\leq \mu[A]$ for every sequence $(A_n)$ of mutually disjoint sets in $\mathcal{R}$ and $A\in \mathcal{R}$ such that $\cup A_n \subseteq A$.

??? proof "Proof"
    
    *(i)* Let $A\subseteq B$ with $A$ and $B$ in $\mathcal{S}$.
    It follows that $B\setminus A=\cup_{1\leq k\leq n}C_k$ for a disjoint family $(C_k)_{1\leq k\leq n}$ in $\mathcal{S}$.  
    Due to the additivity and positivity of $\mu$, it follows  

    \[
    \begin{align}
        \mu[B] & =\mu[A\cup B\setminus A]=\mu[A\cup (\cup_{1\leq k\leq n}C_k)]\\
        & =\mu[A]+\sum_{1\leq k\leq n}\mu[C_k]\geq \mu[A].
    \end{align}
    \]

    *(ii)* Let $(A_k)_{1\leq k\leq n}$ be a countable family of elements in $\mathcal{S}$ and $A\in \mathcal{S}$ be such that $A\subseteq \cup_{k\leq n}A_k$.
    Define $B_1=A_1$ and $B_k=A_k\setminus (\cup_{1\leq l<k}A_l)=\cap_{1\leq l<k}(A_k\setminus (A_k\cap A_l))$.
    By definition of a semi-ring, there exists $(C_{kl})_{1\leq l\leq r_k}$, a disjoint family in $\mathcal{S}$, such that $B_k=\cup_{1\leq l\leq r_k} C_{kl}$.  
    Note also that $B_k\subseteq A_k$.
    Since $A_k\setminus B_k=\cap_{1\leq l\leq c_k}(A_k\setminus (A_k\cap C_{kl}))$, a similar argument yields the existence of $(D_{kj})_{1\leq j\leq p_k}$, a disjoint family in $\mathcal{R}$, such that $A_k\setminus B_k =\cup_{1\leq j\leq p_k} D_{kj}$.
    By additivity, we deduce that

    \[
    \begin{align}
        \mu[A_k] &= \mu[A_k\setminus B_k \cup B_k]\\
        & =\mu[(\cup_{1\leq j\leq p_k}D_{kj})\cup (\cup_{1\leq l\leq r_k}C_{kl})]\\
        &=\sum_{1\leq j\leq p_k}\mu[D_{kj}]+\sum_{1\leq l\leq r_k}\mu[C_{kl}]\\
        & \geq \sum_{1\leq l\leq r_k}\mu[C_{kl}].
    \end{align}
    \]

    Using this inequality, the monotonicity and additivity of $\mu$, as well as the fact that  

    \[
    A=A\cap (\cup_{1\leq k\leq n}A_k)=A\cap(\cup_{1\leq k\leq n}B_k)=A\cap (\cup_{k\leq n}\cup_{1\leq l\leq r_k}C_{kl})=\cup_{1\leq k\leq n}\cup_{1\leq l\leq r_k}(A\cap C_{kl}),
    \]

    it follows that

    \[
    \begin{align}
        \mu[A] &= \mu\left[\cup_{1\leq k\leq n}\cup_{1\leq l\leq r_k}(A\cap C_{kl})  \right]\\
        & = \sum_{1\leq k\leq n}\sum_{1\leq l\leq r_k}\mu[A\cap C_{kl}]\\
        & \leq \sum_{1\leq k\leq n}\sum_{1\leq l \leq r_k}\mu[C_{kl}]\\
        & \leq \sum_{1\leq k\leq n}\mu[A_k],
    \end{align}
    \]

    showing the sub-additivity.

    *(iii)* Suppose that $\mu$ is $\sigma$-additive.  
    The fact that $\mu$ is $\sigma$-sub-additive follows from the same argumentation with a family $(A_n)$ instead of $(A_k)_{1\leq k\leq n}$.
    Suppose therefore that $\mu$ is a $\sigma$-sub-additive content, and let us show that $\mu$ is $\sigma$-additive.
    Let $(A_n)$ be a disjoint family in $\mathcal{S}$ such that $\cup A_n \in \mathcal{S}$.
    Denote by $\nu$ the unique extension to the ring $\mathcal{R}$ generated by $\mathcal{S}$.
    Since $\nu=\mu$ on $\mathcal{S}$ and $\nu$ is additive as well as monotone, it follows that

    \[
    \begin{align}
        \sum \mu[A_n] & =\sup_n \sum_{1\leq k\leq n}\mu[A_k]\\
        &=\sup_n \sum_{1\leq k\leq n}\nu[A_k]\\
        &=\sup_n \nu[\cup_{1\leq k\leq n}A_k]\\
        &\leq\sup_n \nu[\cup A_n]\\
        &=\nu[A]=\mu[A].
    \end{align}
    \]

    The $\sigma$-sub-additivity yields the reverse equality, showing $\sigma$-additivity.

    *(a)* Let $A\subseteq B$ for $A,B$ in $\mathcal{R}$.
    It follows that $B\setminus A \in \mathcal{R}$.
    Hence, additivity yields $\mu[B]=\mu[A\setminus B\cup B]=\mu[B\setminus A]+\mu[A]$.

    *(b)* For $A,B$ in $\mathcal{R}$, it holds $A\cup B=A\cup (B\setminus A)$ and $B=A\cap B\cup (B\setminus A)$.
    Since all elements of the decomposition are in $\mathcal{R}$, we get $\mu[A\cup B]=\mu[A]+\mu[B\setminus A]$ and $\mu[B]=\mu[A\cap B]+\mu[B\setminus A]$, from which follows the assertion.

    *(c)* Let $(A_n)$ be a pairwise disjoint sequence of elements in $\mathcal{R}$ and $A\in \mathcal{R}$ such that $\cup A_n \subseteq A$.
    By monotonicity, additivity, and stability of $\mathcal{R}$ under finite union, it holds $\sum_{1\leq k\leq n}\mu[A_k]=\mu[\cup_{1\leq k\leq n} A_k]\leq \mu[A]$ for every $n$.
    Hence the assertion.



Extending a content from a semi-ring to a ring is fairly straightforward.  
However, for the sake of the next extension to a $\sigma$-algebra, it may be interesting to see if the same result holds for a pre-measure.  

!!! proposition 

    Let $\mu$ be a pre-measure on a semi-ring $\mathcal{S}$.
    Suppose that $\mu$ is either $\sigma$-additive or $\sigma$-sub-additive.
    Then the unique extension of $\mu$ as a pre-measure $\nu$ on $\mathcal{R}$ -- the ring generated by $\mathcal{S}$ -- is also $\sigma$-additive.

!!! proof
    The fact that we can assume that $\mu$ is either $\sigma$-additive or $\sigma$-sub-additive follows from the equivalence between both properties due to the previous Lemma.
    Assume therefore that $\mu$ is $\sigma$-additive and let us show that $\nu$ is so too.
    Let $(A_n)$ be a family of pairwise disjoint elements in $\mathcal{R}$ such that $A=\cup A_n$ is in $\mathcal{R}$.
    Denote by $A=\cup_{1\leq l\leq m}B_l$ and $A_n=\cup_{1\leq k\leq r_n} B_{nk}$ with $(B_l)_{1\leq l\leq n}$ and $(B_{nk})_{1\leq k\leq r_n}$ pairwise disjoint families in $\mathcal{S}$.
    Defining $C_{lnk}=B_l\cap B_{nk}$, it follows that

    \[
    B_l=\cup_{n}\cup_{1\leq k\leq r_n}C_{lnk}, \quad \text{and} \quad B_{nk}=\cup_{1\leq l\leq m} C_{lnk}
    \]

    are disjoint decompositions into sets in $\mathcal{S}$.
    By additivity of $\mu$, it follows that $\mu[B_{nk}]=\sum_{1\leq l\leq m}\mu[C_{lnk}]$ and by $\sigma$-additivity of $\mu$, also $\mu[B_l]=\sum_{n}\sum_{1\leq k\leq r_n}\mu[C_{lnk}]$.
    Since we can switch infinite sums of positive numbers, it follows that

    \[
    \begin{align}
        \nu\left[ A \right] & =\sum_{1\leq l\leq m}\mu[B_l]=\sum_{1\leq l\leq m}\sum_{n}\sum_{1\leq k\leq r_n}\mu[C_{lnk}]\\
        & =\sum_{n}\sum_{1\leq k\leq r_n}\sum_{1\leq l\leq m}\mu[C_{lnk}]\\
        &=\sum_{n}\sum_{1\leq k\leq r_n}\mu[B_{nk}]=\sum_n \nu[A_n]
    \end{align}
    \]

    showing the $\sigma$-additivity.

!!! example "Example: Lebesgue/Stieljes Measure"

    Let us study the example of the Lebesgue/Stieljes measure presented in the introduction of this section.
    Given a right continuous increasing function $F:\mathbb{R}\to \mathbb{R}$, on the semi-ring $\mathcal{S}=\{(a,b]\colon a\leq b, a,b \in \mathbb{R}\}$, the Lebesgue/Stieljes pre-measure is defined as the set function $\mu[(a,b] ]=F(b)-F(a)$.
    Let us show that $\mu$ is indeed a pre-measure.

    - $\mu[\emptyset]=\mu[(a,a]]=F(a)-F(a)=0$.
    - Let $(a_k,b_k]$ be disjoint intervals for $1\leq k\leq n$ such that $\cup_{1\leq k\leq n} (a_k,b_k]=(a,b] \in \mathcal{S}$.
        Up to reordering, without loss of generality, we can assume that $a_1\leq b_1\leq a_{2}\leq b_2\leq \ldots \leq a_n\leq b_n$ since the intervals are disjoint.
        Furthermore, since $\cup_{1\leq k\leq n} (a_k,b_k]=(a,b]$ is an interval itself, it follows that $a_k=b_{k+1}$ for every $k=1,\ldots, n-1$ and $a=a_1$ and $b=b_n$.
        Hence  

        \[
          \sum_{1\leq k\leq n}\mu[(a_k,b_k]]=\sum_{1\leq k\leq n}F(b_k)-F(a_k)=F(b_n)-F(a_1)=F(b)-F(a)=\mu[(a,b]]
        \]

        showing the additivity.  

    We can extend $\mu$ to the ring generated by $\mathcal{S}$ as shown in a previous [proposition](022-semi-ring-to-ring.md#prop-pre-mes-semi-ring-to-ring).

    Interestingly though, $\mu$ is $\sigma$-additive on this ring.
    The reason for which is strongly related to compactness arguments.
    According to the previous proposition and lemma, it is enough to show that $\mu$ is $\sigma$-sub-additive on the semi-ring $\mathcal{S}$.
    Let $(a,b]\in \mathcal{S}$ and $((a_n,b_n])$ be a countable family in $\mathcal{S}$ such that $(a,b]\subseteq \cup (a_n,b_n]$.

    Let $\varepsilon>0$, and by right continuity of $F$ choose some $a^\varepsilon$ in $(a,b)$ such that $F(a^\varepsilon)-F(a)<\varepsilon/2$.
    Also, using right continuity of $F$, choose $b^\varepsilon_n>b_n$ for every $n$ such that $F(b_n^\varepsilon)-F(b_n)\leq \varepsilon 2^{-n-1}$.
    It follows that

    \[
      [a^\varepsilon,b]\subseteq (a^\varepsilon,b]\subseteq (a,b]\subseteq \cup (a_n,b_n]\subseteq (a_n,b_n^\varepsilon).
    \]

    However, $[a^\varepsilon,b]$ is a bounded closed interval, and therefore compact.
    Hence, the open covering $\cup (a_n,b_n^\varepsilon)$ of $[a^\varepsilon,b]$ can be chosen finite, that is, there exists $n_0$ such that

    \[
      (a^\varepsilon,b]\subseteq [a^\varepsilon,b]\subseteq \cup_{1\leq k\leq n_0}(a_k,b_k^\varepsilon)\subseteq \cup_{k\leq n_0}(a_k,b_k^\varepsilon].
    \]

    Hence, since $\mu$ is sub-additive by means of of the previous lemms, it follows that  

    \[
    \begin{align}
      \mu[(a,b]]  & = F(b)-F(a)\\
                  & \leq \varepsilon/2 + F(b)-F(a^\varepsilon)\\
                  & \leq \varepsilon/2 + \sum_{k=1}^{n_0}\left(F(b_k^\varepsilon)-F(a_k)\right)\\
                  & \leq \varepsilon/2 + \varepsilon \sum_{k=1}^{n_0}2^{-k-1} +\sum_{k=1}^{n_0} \left(F(b_n)-F(a_n)\right)\\
                  & \leq \varepsilon +\sum \left(F(b_n)-F(a_n)\right)\\
                  & =\varepsilon+\sum \mu[(a_n,b_n]]
    \end{align}
    \]

    Since $\varepsilon$ is arbitrarily small, it follows that $\mu$ is $\sigma$-sub-additive, hence $\sigma$-additive on the semi-ring $\mathcal{S}$.

    From the previous proposition, $\mu$ extends uniquely to a $\sigma$-additive content on the ring generated by $\mathcal{S}$.

The main question now is whether it is possible to extend the Lebesgue or Lebesgue-Stieltjes content to a measure on the $\sigma$-algebra $\mathcal{B}(\mathbb{R})$ which is generated by $\mathcal{S}$.  


# Introduction/Notations

After treating the notion of measurable spaces and measures, we will now address integration.
However this lecture is about stochastics and therefore, even if many notions extends to more general theory we will stick to probability spaces.
To do so, let us first fix the probabilistic historical jargon and notations.


* $(\Omega, \mathcal{F}, P)$ is called a **probability space** if $\mathcal{F}$ is a $\sigma$-algebra on $\mathcal{F}$ and $P$ is a finite measure with $P[\Omega] = 1$;

* Elements of $\Omega$ are called **states** and usually denoted by $\omega$;
* Elements of $\mathcal{F}$ are called **events**;
* The measure $P[A]$ of an event $A$ is called the **probability of ** $A$.
* A **random variable** is a measurable function from $\Omega$ to $\mathbb{R}$ where $\mathbb{R}$ is endowed with the Borel $\sigma$-algebra.
     Usually, random variables are denoted with capital letters $X, Y, Z, \cdots$

As mentioned, the following does not change if you assume that $P$ is a $\sigma$-finite measure.  


Throughout, we denote by $\mathcal{L}^0:=\mathcal{L}^0(\Omega,\mathcal{F})$ the set of all random variables.
Given a random variable $X$, we also use the following shorthand notations for events:

\[
\begin{align*}
  \{X \in B\}   & := \{\omega \in \Omega\colon X(\omega)\in B\}\\
  \{X \leq t\} & := \{\omega \in \Omega\colon X(\omega)\leq t\}
  \ldots
\end{align*}
\]

for $B \in \mathcal{F}$ and $t\in \mathbb{R}$.  

As for the measure of these events, we adopt the notations:

\[
P[X \in B] := P[\{X \in B\}], \quad P[X\leq t]:= P[\{X \leq t\}], \dots
\]

Given an event $A$ we define the **indicator function** $1_A$ as the function:

\[
\begin{equation}
  \begin{split}
     1_A\colon \Omega &\longrightarrow \mathbb{R}\\
    \omega &\longmapsto 1_A(\omega)=
    \begin{cases}
        1 &\text{if } \omega \in A\\
        0 &\text{otherwise}
    \end{cases}
  \end{split}
\end{equation}
\]

![Indicator Function](./../../images/indicator_dark.svg#only-dark){align = right}
![Indicator Function](./../../images/indicator_white.svg#only-light){ align = right}



Throughout, we will also deal with *extended real-valued* random variables, that is, functions $X:\Omega \to [-\infty,\infty]$ which are measurable.  
We denote this set by $\bar{\mathcal{L}}^0$.  

Note that for $X \in \bar{\mathcal{L}}^0$, we can write:

\[
X=-\infty 1_A +Y1_B+\infty1_C
\]

where $A$, $B$, and $C$ are pairwise disjoint and $Y\in \mathcal{L}^0$.

Further, we denote by $\mathcal{L}^0_+$ or $\bar{\mathcal{L}}^0_+$ the set of those random variables or extended real-valued random variables that are positive.  

-------

This chapter is divided as follows

* [Expectation, Lebesgue's Convergence](031-expectation.md)
* [$L^p$-Spaces and Classical Inequalities](032-lp-spaces-inequalities.md)
* [Radon-Nykodym and Conditional Expectation](033-radon-nikodym-cond-exp.md)
* [Independence](034-independence.md)
* [Funini-Tonelli](035-fubini-tonelli.md)
* [Uniform Integrability](036-uniform-integrability.md)


# Measure

In the previous chapter, we described the class of sets that can be measures.
This present chapter deals with how to measure these sets in a consistent way.
Let us first discuss the most natural example, which is the Lebesgue measure on the real line.

This function, historically denoted by $\lambda$, should provide the "measure" of subsets of the real line.
It should have the following properties: the measure of an interval should be equal to its length.
In other terms,

\[
\begin{equation}
    \lambda\left[ (a,b] \right]=b-a
\end{equation}
\]

for $a<b$ reals.

It should also have an additive property, meaning that the length of disjoint intervals should equal their sum,

\[
\begin{equation}
    \lambda\left[ (a_1,b_1]\cup(a_2,b_2] \right]=(b_1-a_1)+(b_2-a_2)=\lambda\left[ (a_1,b_1] \right]+\lambda\left[ (a_2,b_2] \right].
\end{equation}
\]

Finally, if a subset $A=\cup (a_n,b_n]$ is a countable union of disjoint intervals $(a_n,b_n]$, then its measure should be equal to the limit of the total length of all intervals, that is,

\[
\begin{equation}
    \lambda\left[ A \right]=\lambda\left[ \cup (a_n,b_n] \right]=\sum (b_n-a_n)=\sum \lambda\left[ (a_n,b_n] \right].
\end{equation}
\]

This raises the following questions:

* First, on which subclass of sets of the real line should $\lambda$ be defined?
* Second, which continuity property should this set function satisfy?

We saw that the collection of intervals of the form $(a,b]$ forms a semi-ring on which the Lebesgue measure can be defined easily.
As for the additivity property of the measure, we then have to extend it to the ring it generates.
Finally, as for the continuity property, we have to extend it to the $\sigma$-algebra it generates since it is stable under finite union.``


Throughout, given a class of sets $\mathcal{C}$ containing the emptyset and a set function $\mu \colon \mathcal{C} \to \mathbb{R}\cup\{\pm \infty\}$ we say that $\mu$ is

* **positive**: if $\mu[A]\geq 0$ for every $A$;
* **additive**: if for any two disjoint sets $A$ and $B$ in $\mathcal{C}$ with $A\cup B$ in $\mathcal{C}$ it holds $\mu[A\cup B] = \mu[A] + \mu[B]$;
* **sub-additive**: if for any two sets $A$ and $B$ in $\mathcal{C}$ it holds $\mu[A\cup B] \leq \mu[A] + \mu[B]$;

* **$\sigma$-additive**: if for any countable family of pairwize disjoint sets $(A_n)$ in $\mathcal{C}$ such that $\cup A_n$ is in $\mathcal{C}$, it holds $\mu [\cup A_n] = \sum \mu[A_n]$;
* **$\sigma$-sub-additive**: if for any countable family of sets $(A_n)$ in $\mathcal{C}$ such that $\cup A_n$ is in $\mathcal{C}$, it holds $\mu [\cup A_n] \leq  \sum \mu[A_n]$;

We say that a set function $\tilde{\mu}$ defined on a $\tilde{\mathcal{C}}\supseteq \mathcal{C}$ **extends** $\mu$ is they coincide on $\mathcal{C}$.


!!! definition "Measure"

    Let $\mathcal{F}$ be a $\sigma$-algebra.
    A set function $\mu \colon \mathcal{F} \to [0, \infty]$ is called a **measure** if

    * $\mu[\emptyset] = 0$;
    * **$\sigma$-Additivity**: for any countable family $(A_n)$ of pairwize disjoint sets in $\mathcal{F}$, it holds

        \[
            \mu\left[ \cup A_n \right] = \sum \mu[A_n]
        \]

    A triple $(X, \mathcal{F}, \mu)$ where $\mathcal{F}$ is a $\sigma$-algebra on $X$ and $\mu$ is a measure on $\mathcal{F}$ is called a **measured space**.

    -----

    Let $\mathcal{S}$ be a semi-ring.
    A set function $\mu \colon \mathcal{S}\to [0, \infty]$ is called a **pre-measure** if

    * $\mu[\emptyset] = 0$;
    * **Additivity**: for any two dijoints sets $A$ and $B$ in $\mathcal{S}$  such that $A \cup B$ is in $\mathcal{S}$ it holds

        \[
            \mu\left[ A \cup B \right] = \mu[A] + \mu[B]
        \]

In other terms, a measure on a $\sigma$-algebra is a positive set function equal to $0$ on the emptyset and $\sigma$-additive, while a pre-measure on a ring is just with additivity.

We say that a measure $\mu$ is 

* **finite** if $\mu[X]<\infty$
* **$\sigma$-finite**: if $\mu[A_n]<\infty$ for some increasing sequence $(A_n)$ with $\cup A_n = X$.

!!! remark

    This lecture is essentially about stochastics and we will therefore mainly consider finite measures $\mu$ normalized to $\mu[X] = 1$.
    Such a measure is called a **probability measure**.


!!! example "Example: Probability on a Countable set"

    Suppose that $X=\{x_1, \ldots, x_N\}$ is a finite set with $\sigma$-algebra $\mathcal{F} = 2^X$.
    Since any subset $A$ of $X$ can be written as a finite union of disjoint singletons
    
    \[
        A = \cup_{i \in I}x_i
    \]

    for some $I\subseteq \{1, \ldots, N\}$, from $\sigma$-additivity, it holds

    \[
        \mu[A] = \sum_{i \in I}\mu[\{x_i\}]
    \]

    the measure is equivalently given by a positive function $m\colon X\to [0, \infty]$ with $m(x_i) = \mu[\{x_i\}]$.

    Due to $\sigma$-additivity, the same argumentation holds for $X = (x_n)$ being a countable set where measures on $\mathcal{F} = 2^X$ are entirely described by functions $m\colon X \to [0, \infty]$ through $m(x_n) = \mu[\{x_n\}]$.

!!! example "Example: Dirac Measure"

    Let $(X, \mathcal{F})$ be a measurable space and $x_0$ be an element of $X$.
    The dirac measure $\delta_{x_0}\colon \mathcal{F} \to [0, 1]$ is defined as

    \[
       \begin{equation}
           \delta_{x_0}[A]=
           \begin{cases}
               1 & \text{if }x_0\text{ is in } A\\
               0 & \text{otherwise}
           \end{cases}
       \end{equation}
    \]

    for any $A$ in $\mathcal{F}$.
    Straightforward inspection shows that it is a probability measure.


!!! example "Example: Counting Pre-Measure"

    Let $\mathcal{S}$ be a semi-ring on $X$.
    Define $\mu\colon \mathcal{F}\to [0, \infty]$ as

    \[
       \begin{equation}
           \mu[A]=
           \begin{cases}
               \# A &\text{if }A\text{ is finite}\\
               \infty & \text{otherwise}
           \end{cases}, \quad A \in \mathcal{F}.
       \end{equation}
    \]

    It is easy to check that $\mu$ is a pre-content, which is $\sigma$-additive if and only if $A$ is finite.

!!! example "Example: Normal Distribution"

    For $X=\mathbb{R}$ and $\mathcal{F} = \mathcal{B}(\mathbb{R})$ the Borel $\sigma$-algebra we define  

    \[
       \begin{equation}
           \mu[A]=\frac{1}{\sigma\sqrt{2\pi}}\int_A e^{-\frac{(x-\mu)^2}{2\sigma^2}} \lambda(dx), \quad A \in \mathcal{F},
       \end{equation}
    \]

    where $\lambda$ is the Lebesgue measure on $\mathbb{R}$ (we do not yet know if such an object exists).

    This is the famous *normal distribution*, which is a probability measure on the real line.


Another way to generate measures is to use measurable functions and by the pre-image properties can also transport forward (pushforward) measures through measurable functions

!!! definition "Definition: Pullback Measure"

    Let f\colon X \to Y$ be a measurable function for the $\sigma$-algebra $\mathcal{F}$ and $\mathcal{G}$ on $X$ and $Y$, respectively.

    Given a measure $\mu$ on $\mathcal{F}$, we can define the pushforward measure $\mu_{\#f} \colon \mathcal{G} \to [0, \infty]$ as

    \[
        \mu_{\# f}[B] = \mu \left[ f \in B \right] = \mu\left[ \left\{ x \in X \colon f(x) \in B \right\} \right] 
    \]
    
    for any $B$ in $\mathcal{G}$.



Easy inspection shows that $\mu_{\# f}$ is indeed a measure on $\mathcal{G}$.

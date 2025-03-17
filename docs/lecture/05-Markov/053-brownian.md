# Brownian Motion

??? note "Note: Browninan Motion and Wiener Measure"

    The Brownian motion, named after the botanist Robert Brown, was first observed in 1827 when Brown noticed the erratic motion of pollen particles suspended in water.
    While Brown initially attributed this movement to some "life force," it was later understood as a physical phenomenon resulting from molecular collisions.
    
    At the end of the 19th and the beginning of the 20th century, physicists such as Albert Einstein and Marian Smoluchowski provided theoretical models that linked Brownian motion to the kinetic theory of gases, demonstrating the random behavior of particles in a fluid.
    This work provided critical evidence for the atomic theory of matter.
    
    In spite of its success and applications, it tooks a century until a rigorous mathematical formulation and proof of the existence of Brownian motion as a stochastic process was achieved by Norbert Wiener in the 1930 ies.
    This layed the foundation for modern probability theory and the study of continuous-time stochastic processes.
    The resulting process, is now often called the Wiener process.

The Brownian motion is one of the central objects of continuous time stochastic analysis.
Though being classical and intuitive, it is not an easy object with fascinating mathematical properties.

!!! definition "Definition: Brownian Motion"
    Let $(\Omega,\mathcal{F},P)$ be a probability space.
    A stochastic process $B$ is called a **Brownian Motion** if

    - **Independence of Increments:** The increments $B_{t_n}-B_{t_{n-1}}$, $B_{t_{n-1}}-B_{t_{n-2}}$, $\ldots$, $B_{t_1}-B_{t_0}$ are independent for every finite family $0\leq t_0<t_1<\ldots<t_n$.
    - **Normal Behavior of Increments:** Increments are normally distributed $B_{t}-B_s\sim \mathcal{N}(0,t-s)$.
    - **Continuity of paths:** (almost surely)

        \[
        P\left[ \left\{ \omega \colon t\mapsto B_t(\omega) \text{ is continuous} \right\} \right]=1
        \]

Note that we do not require any filtration in the definition of the Brownian motion.
As we will see later, we will often consider the filtration $\mathcal{F}_t=\sigma(B_s\colon s\leq t)$ up to completion, and this filtration has particular properties.

It is intuitive to see the Brownian motion as a scaling limit of a symmetric random wall&mdash;and it actually is.
However, one of the first questions to ask is whether such an object exists.
Precisely, one asks if, for an adequate measurable space $(\Omega,\mathcal{F})$ and stochastic process $B$, there exists a probability measure $P\colon\mathcal{F}\to [0,1]$ such that under $P$, the stochastic process $B$ is a Brownian motion.
This measure is called the **Wiener measure**.

There are several ways to construct such a measure, including a wavelet construction, a Hilbert space approach, or an appropriate scaling of the symmetric random walk together with some weak convergence.
Hereafter, we will present a pure stochastic construction based on the **Kolmogorov-Carathéodory extension theorem**.
It may be a little technical, but it has the advantage of presenting several important aspects of measure theory without relying on any advanced functional analysis assumptions.

The construction will follow two important steps:

* **Construction of a measure $P$ on the path space** such hat the canonical process $X$ satisfies the two first properties. $\leadsto$ Kolmogorov extension Theorem.
* **Modification of the Canonical process** $X$ to $B$ such that $B$ additionally satisfies the continuity property. $\leadsto$ Kolmogorov-Centov Theorem.

## Kolmogorov-Carathéodory extension Theorem.

For a given index set $\mathbf{T}$, we consider $(S,\mathcal{S})$ where $S$ is a Polish space[^1] with Borel $\sigma$-algebra $\mathcal{S}$.
For ease, you may assume that $S \subseteq \mathbb{R}^d$ is a closed or open subset.
The product of countable Polish spaces is Polish, and recall the following theorem from Ulam.

!!! theorem "Ulam"
    Let $P$ be a probability measure on $(S,\mathcal{S})$, then $P$ is regular, that is

    \[
      P\left[ A \right]=\sup\left\{ P[K]\colon K\subseteq A, K\text{ compact} \right\}
    \]

    for every Borel set $A\subseteq S$.


??? proof

    Let $A \subseteq S$ be a Borel set.
    By inner regularity of the probability measure $P$, we have

    \[
    P(A) = \sup\{P(K) \colon K \subseteq A, K \text{ compact} \}.
    \]

    To prove this, define

    \[
    \mu(A) = \sup\{P(K) \colon K \subseteq A, K \text{ compact} \}.
    \]

    Clearly, $\mu$ is an outer measure with $\mu(S) = 1$ and $\mu \leq P$.

    Now, consider an open set $G \supseteq A$.
    Since $S$ is Polish, there exists an increasing sequence of compact sets $(K_n)$ such that $G = \bigcup_{n=1}^\infty K_n$.
    By the continuity of $P$,

    \[
    \mu(G) = \lim_{n \to \infty} P(K_n) \leq P(G).
    \]

    Taking the infimum over all such open sets $G$ containing $A$ gives

    \[
    \mu(A) \geq P(A).
    \]

    Combining both inequalities, we conclude $\mu(A) = P(A)$, proving the result.


Recall standard notations for the path space:

- **Sample space** given by $\Omega :=\{\omega=(\omega_t) :\omega_t \in  S \text{ for all } t\}=S^{\mathbf{T}}$.
- **Coordinate process** $X$ given by $X_t(\omega)=\omega_t$ for every $t$ and $\omega$.
- **Projection** For $F$ and $G$ subsets of $\mathbf{T}$ define the projections:
  
    \[
    \begin{equation*}
      \begin{split}
        \pi_F \colon \Omega & \longrightarrow S^{F}\\
                      \omega & \longmasto  \pi_F(\omega) = (\omega_t)_{t\in F}
      \end{split}
    \end{equation*}
    \]
    
    and
    
    \[
    \begin{equation*}
      \begin{split}
        \pi_{GF} \colon S^{G} & \longrightarrow S^{F}\\
                      (\omega_t)_{t \in G} & \longmasto  \pi_{GF}(\omega) = (\omega_t)_{t\in F}
      \end{split}
    \end{equation*}
    \]



$\pi_F(\omega) = (\omega_t)_{t\in F}$ for $F\subseteq \mathbf{T}$ and $\pi_{GF}((\omega)_{t \in G})=(\omega)_{t\in F}$ for every two sets $F\subseteq G \subseteq \mathbf{T}$.
- **Algebra** $\mathcal{C}$ of those sets $C=\pi^{-1}_F(A)=\{ \omega \in \Omega\colon (\omega_{t_1},\ldots,\omega_{t_n})\in A \}=\{(X_{t_1},\ldots X_{t_n})\in A\}$ where $A$ is in the Borel $\sigma$-algebra $\mathcal{F}^F:=\mathcal{B}(S^F)$ and $F\subseteq\mathbf{T}$ is finite.[^2]
- **Product $\sigma$-Algebra** $\mathcal{F}=\sigma(\mathcal{C})$

!!! definition "Consistent family"
    A family $(P_{F})$ of probability measures $P_F:\mathcal{F}^F\to [0,1]$ for every finite subset $F$ of $\mathbf{T}$ is called *consistent* if $P_{F}(A)=P_{G}\left( B \right)$ for every $F\subseteq G$ and $A\in \mathcal{F}^F$ and $B=\pi_{GF}^{-1}(A)$.

We can now formulate the Kolmogorov extension theorem, a consequence of Carathéodory's Theorem.

!!! theorem "Kolmogorov Extension Theorem"
    Let $(P_F)$ be a consistent family of Borel probability measures.
    Then, there exists a unique probability measure $P$ on $\mathcal{F}$ such that $P(C)=P_F(A)$ for every $A \in \mathcal{F}^F$ and $C=\pi^{-1}_F(A)$.

In other words, it is possible to construct a unique probability measure whose finite-dimensional restriction coincides exactly with each given finite-dimensional distribution $P_F$, provided they are consistent with each other.

[^1]: A complete metric space which is separable.
[^2]: Check that it is indeed an Algebra.




We first ignore the last requirement of almost sure continuity of paths and concentrate on the existence by means of Kolmogorov's Theorem.


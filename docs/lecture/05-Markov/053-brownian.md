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

## Pre-Brownian Motion: Kolmogorov-Carathéodory extension Theorem

For a given index set $\mathbf{T}$, we consider $(S,\mathcal{S})$ where $S$ is a Polish space[^1] with Borel $\sigma$-algebra $\mathcal{S}$.
For ease, you may assume that $S \subseteq \mathbb{R}^d$ is a closed or open subset.
The product of countable Polish spaces is Polish, on which according to Ulam, probability measures are regular.

!!! theorem "Ulam"
    Let $P$ be a probability measure on $(S,\mathcal{S})$, then $P$ is **regular**, that is

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
- **Projection** For $F$ and $G$ subsets of $\mathbf{T}$ with $F\subseteq G$, define the projections:
  
    \[
    \begin{equation*}
      \begin{split}
        \pi_F \colon \Omega & \longrightarrow S^{F}\\
                      \omega & \longmapsto  \pi_F(\omega) = (\omega_t)_{t\in F}
      \end{split}
    \end{equation*}
    \]
    
    and
    
    \[
    \begin{equation*}
      \begin{split}
        \pi_{GF} \colon S^{G} & \longrightarrow S^{F}\\
                      (\omega_t)_{t \in G} & \longmapsto  \pi_{GF}\left((\omega_t)_{t \in G}\right) = (\omega_t)_{t\in F}
      \end{split}
    \end{equation*}
    \]

    Note that for $F\subseteq G$, it holds that $\pi_{GF}(\pi_G) = \pi_F$ from which follows that the preimage satisfies $\pi^{-1}_G(\pi^{-1}_{GF}) = \pi^{-1}_F$.

- **Algebra** $\mathcal{C}$ of those sets $C=\pi^{-1}_F(A)=\{ \omega \in \Omega\colon (\omega_{t_1},\ldots,\omega_{t_n})\in A \}=\{(X_{t_1},\ldots X_{t_n})\in A\}$ where $A$ is in the Borel $\sigma$-algebra $\mathcal{F}^F:=\mathcal{B}(S^F)$ and $F\subseteq\mathbf{T}$ is finite.
- **Product $\sigma$-Algebra** $\mathcal{F}=\sigma(\mathcal{C}) =\otimes_{t \in \mathbf{T}}\mathcal{S}$

!!! definition "Consistent family"
    A family $(P_{F})$ of probability measures $P_F:\mathcal{F}^F\to [0,1]$ for every finite subset $F$ of $\mathbf{T}$ is called **consistent** if
      
    \[
      P_{F}(A)=P_{G}\left( B \right)
    \]

    for every $F\subseteq G$ and $A\in \mathcal{F}^F$ where $B=\pi_{GF}^{-1}(A)$.

We can now formulate the Kolmogorov extension theorem, a consequence of Carathéodory's Theorem.

!!! theorem "Kolmogorov Extension Theorem"
    Let $(P_F)$ be a consistent family of Borel probability measures.
    Then, there exists a unique probability measure $P$ on $\mathcal{F}$ such that

    \[
    \begin{equation*}
        P(C)=P_F(A)    
    \end{equation*}
    \]

    for every $A \in \mathcal{F}^F$ where $C=\pi^{-1}_F(A)$.

In other words, it is possible to construct a unique probability measure whose finite-dimensional restriction coincides exactly with each given finite-dimensional distribution $P_F$, provided they are consistent with each other.

[^1]: A complete metric space which is separable.


!!! proof
    Note that for every finite family $(C_k)_{k\leq n}=(\pi^{-1}_{F_k}(A_k))_{1\leq k\leq n}$, if we define $F=\cup_{k\leq n}F_k$ and $B_k=\pi^{-1}_{FF_k}(A_k) \in \mathcal{F}^F$, it follows that $C_k=\pi^{-1}_{F}(B_k)$.
    In particular, up to enlargement, we can always assume that we take a common finite family to represent the $(C_k)$.
    Furthermore, if the $(C_k)$ are disjoint, then so are the $(B_k)$.

    **Step 1:** Definition of $P$ as a set function  
    Define $P:\mathcal{C}\to [0,1]$ by setting $P[C]=P_F(A)$ where $C=\pi^{-1}_F(A)$ for $A\in \mathcal{F}^F$.
    This function is well-defined due to consistency.
    Suppose $C=\pi^{-1}_F(A)=\pi^{-1}_{G}(B)$ for $A$ in $\mathcal{F}^F$ and $B$ in $\mathcal{F}^G$.
    Then $D := \pi^{-1}_{F\cup G F}(A) = \pi^{-1}_{F\cup G G}(B)$ and $\pi^{-1}_{F\cup G}(D)=C$.
    By the consistency of the family, it follows that $P_F(A)=P_{F\cup G}(D)=P_{G}(B)$, confirming that $P$ is well-defined.

    **Step 2:** $P$ as an additive measure  
    Clearly, $P[\emptyset]=0$ and $P[\Omega]=1$.
    As mentioned above, let $(C_k)_{k\leq n}=(\pi^{-1}_{F}(A_k))_{k\leq n}$ be a finite disjoint family of elements in the algebra $\mathcal{C}$ with common finite set $F$.
    Since $P_F$ is a probability measure, it follows that

    \[
    P\left[\cup_{k\leq n} C_k\right] = P_F\left[\cup_{k\leq n} A_k\right] = \sum_{k\leq n} P_F[A_k] = \sum_{k\leq n} P[C_k].
    \]

    Therefore, $P$ is an additive probability measure on the algebra $\mathcal{C}$.

    **Step 3:** $P$ is $\sigma$-additive  
    Using continuity at $\emptyset$, let $(C_n) = (\pi^{-1}_{F_n}(A_n))$ be a decreasing sequence of elements in $\mathcal{C}$ such that $\cap C_n = \emptyset$ and suppose that $P[C_n] \geq \varepsilon > 0$ for some $\varepsilon > 0$.
    Up to redefining $\tilde{F}_n = \cup_{k\leq n}F_k$ and $\tilde{A}_n = \pi^{-1}_{\cup_{k\leq n}F_k F_n}(A_n)$, where $C_n = \pi_{\tilde{F}_n}(\tilde{A}_n)$ with $\tilde{A}_n$ in $\mathcal{F}^{\tilde{F}_n}$, we may assume that $(F_n)$ is an increasing sequence of finite subsets of $\mathbf{T}$.
    Since $(F_n)$ is increasing and $(C_n)$ decreasing, it follows that $A_{n+1}\subseteq \pi_{F_{n+1}F_n}^{-1}(A_n)$.
    By inner regularity of Borel probability measures on $\mathbb{R}$, we can find a sequence of compacts $(\tilde{K}_n)$ such that $\tilde{K}_n\subseteq A_n$ and $P_{F_n}[A_n\setminus \tilde{K}_n]\leq \varepsilon/2^{n+1}$.
    However, we do not know whether this sequence of compacts fulfills the same monotonicity condition as $(A_n)$.
    We therefore shrink the compacts to 

    \[
    K_n=\cap_{k\leq n}\pi^{-1}_{F_nF_k}(\tilde{K}_k)\subseteq \tilde{K}_n
    \]

    ensuring $K_{n+1} \subseteq \pi^{-1}_{F_{n+1}F_n}(K_n)$ for every $n$.
    By construction,

    \[
      \begin{align*}
         P_{F_n}\left[ K_n \right] 
          & = P_{F_n}[A_n]-P_{F_n}[A_n\setminus K_n]\\
          & \geq \varepsilon -P_{F_n}[A_n\setminus \cap_{k\leq n}\pi^{-1}_{F_nF_k}(\tilde{K}_k)]\\
          & =\varepsilon -P_{F_n}[\cup_{k\leq n} A_n\setminus \pi^{-1}_{F_nF_k}(\tilde{K}_k)]\\
          & \geq \varepsilon -P_{F_n}[\cup_{k\leq n} \pi^{-1}_{F_nF_k}(A_k\setminus \tilde{K}_k)]\\
          & \geq \varepsilon -\sum_{k\leq n}P_{F_n}[\pi^{-1}_{F_nF_k}(A_k\setminus \tilde{K}_k)]\\
          & =\varepsilon -\sum_{k\leq n}P_{F_k}[A_k\setminus \tilde{K}_k]\\
          & \geq \varepsilon -\sum_{k=1}^{n}\frac{\varepsilon}{2^{k+1}}\\
          & \geq \frac{\varepsilon}{2}
      \end{align*}
    \]

    In particular, each compact is non empty, so let $\omega_n$ be in $\pi^{-1}_{F_n}(K_n)$, that is $\pi_{F_n}(\omega_n)$ is in $K_n$.
    It holds from $K_n \subseteq \pi_{F_1}^{-1}(K_1)$ that $\pi_{F_1}(\omega_n)\in K_1$ for every $n$.
    By compactness of $K_1$, we have for a subsequence, again denoted by $(\omega_n)$, that $\pi_{F_1}(\omega_{n})\to \pi_{F_1}(\bar{\omega}_1)$ some $\bar{\omega}_1$ in $\Omega$.
    Further, from $K_n\subseteq \pi_{F_2}^{-1}(K_2)$ we have for the same reason as before for a sub-subsequence also denoted by $(\omega_n)$, that $\pi_{F_2}(\omega_n)\to \pi_{F_2}(\bar{\omega}_2)$.
    Since $\pi_{F_1}(\bar{\omega}_1)=\pi_{F_1}(\bar{\omega}_2)$, we deduce that the coordinates of $\bar{\omega}_2$ and $\bar{\omega}_1$ coincide on $F_1$.
    Doing so forth, we can construct a point $\bar{\omega}$ by setting arbitrarily points on $(\cup F_n)^c$ such that $\pi_{F_n}(\bar{\omega})=\pi_{F_n}(\bar{\omega}_n)$ for every $n$.
    It follows in particular that $\bar{\omega}\in \pi^{-1}_{F_n}(K_n)\subseteq C_n$ for every $n$ showing that $\cap C_n\neq \emptyset$, contradicting our initial assumption that $\cap C_n = \emptyset$.

    **Step 4:** Carathéodory's Extension Theorem  
    Since $P$ is a $\sigma$-additive probability measure on the algebra $\mathcal{C}$, by Carathéodory's Theorem, it can be uniquely extended to $\mathcal{F}=\sigma(\mathcal{C})$, hence the theorem.

!!! example "Example: Existence of iid Sequences and Henceforth a Random Walk"
    We can apply Kolmogorov's extension theorem to show the existence of iid desquences and henceforth a Random Walk.
    Let $S = \{-1, 1\}$, which is a closed subset of $\mathbb{R}$ with the Borel $\sigma$-algebra $\mathcal{S}$, which reduces to $2^S$.
    Let $\mathbb{T} = \mathbb{N}_0$ and $0<p<1$.
    For every finite subset $F = \{t_0 < t_1 \ldots < t_n\} \subset \mathbb{N}_0$, define

    \[
      P_F\left[ (\omega_{t_1},\ldots, \omega_{t_n})=(e_1,\ldots, e_n) \right] = p^l(1-p)^{n-l},
    \]

    where $e_i \in \{-1, 1\}$ for every $i$, and $l = \#\{ i \colon e_i = 1, i = 1, \ldots, n \}$, which defines a probability measure on $\mathcal{F}^F = \otimes_F \mathcal{S}$.

    It is straightforward to check that the family $(P_F)$ is a consistent family of probability measures.
    By Kolmogorov's extension theorem, there exists a unique probability measure on $S^{\mathbf{T}} = \{-1, 1\}^{\mathbb{N}_0}$ with the product $\sigma$-algebra such that

    \[
      P[B] = P_F[A] 
    \]

    where $B = \pi^{-1}_F(A)$ for any $F \subseteq \mathbb{N}_0$ finite and $A$ in $\mathcal{F}^F$.
    In particular,

    \[
      P[X_t = 1] = P_{\{t\}}[\omega_t = 1] = p \quad \text{and} \quad P\left[ X_t = -1 \right] = 1 - p.
    \]

    A straightforward computation shows that the canonical process $X$ is a sequence of i.i.d. random variables.
    As seen before, it is also a Markov process.

    Doing so, the random walk $S_0 =0$ and $S_t = \sum_{s=1}^t X_s$ is well defined.


With this extension theorem at hand, we can therefore construct a *pre*-Brownian motion.


!!! proposition "Proposition: Existence of a Pre-Brownian Motion"

    Taking $S = \mathbb{R}$ and $\mathbf{T} = [0, \infty)$, with the notations of the sample space here above, there exists a probability measure on $\mathcal{F}$ such that $X$ is, up to continuity of paths, a Brownian motion.

!!! proof
    For the sample space $\Omega =\mathbb{R}^{[0,\infty)}$ with the $\sigma$-algebra $\mathcal{F}=\sigma(\mathcal{C})$ where $\mathcal{C}$ is the collection of those $C=\pi_{F}^{-1}(A)$ for $A$ in $\mathcal{B}(\mathbb{R}^F)$, $F=\{t_0, t_1,\ldots,t_n\}$ for $0< t_0<t_1< \ldots<t_n$, we define the conditional probability distribution

    \[
      p(t,x,y)=\frac{1}{\sqrt{t2\pi}}\exp\left( -\frac{(x-y)^2}{2t} \right)
    \]

    for $t>0$ and $x$, $y$ in $\mathbb{R}$.
    For $x=(x_1,\ldots,x_n)$ we set the cumulative distribution 

    \[
    P_F\left[ X_{t_0}\leq x_0, \ldots, X_{t_n}\leq x_n \right]
    =\int_{-\infty}^{x_0}\int_{-\infty}^{x_1}\ldots \int_{-\infty}^{x_n}p(t_0,0,y_0)p(t_1-t_0,y_0,y_1)\ldots p(t_n-t_{n-1},y_{n-1},y_n)dy_0\ldots dy_{n}   
    \]

    For $F\subseteq G\subseteq \mathbf{T}$ both finite set and $A \in \mathcal{B}(\mathbb{R}^F)$, it holds $D=\pi_{GF}^{-1}(A)\approx \mathbb{R}^{G\setminus F}\times A$ where $\approx$ stands for reordering of the coordinates of $G$ along those who belong to $F$.
    It follows that

    \[
    P_{F}\left[ A \right]=\int_{A}^{}dP_{F}=\int_{A}^{}\int_{\mathbb{R}^{G\setminus F}}^{}dP_{F}dP_{G\setminus F}=\int_{D}^{}dP_{G}=P_{G}[D] 
    \]

    showing that $(P_{F})$ is a consistent family of probability measures.
    Hence, by Kolmogorov extension's theorem, it follows that it can uniquely be extended to $\Omega$ and it holds

    \[
    P\left[ X \in \pi_{F}^{-1}(A) \right]=P_{F}\left[ A \right]
    \]

    for any $A$ in $\mathcal{F}^{F}$ where $F=\{t_0,t_1,\ldots, t_n\} with $0< t_0< t_1<\ldots<t_n$.


    Let us show that $X$ under $P$ fulfills the first two properties of a Brownian motion.
    As for the first property, it holds that

    \[
      \begin{align*}
         P\left[ X_t-X_s \leq x \right]   & =P_{\{s,t\}}\left[ \{(x_1,x_2)\in \mathbb{R}^2 \colon x_2\leq x+x_1\} \right]\\
                                          & =\int_{\mathbb{R}}^{}\int_{-\infty}^{x+y_1}p(s,0,y_1)p(t-s,y_1,y_2)dy_1dy_2\\ 
                                          & =\int_{\mathbb{R}}^{}\int_{-\infty}^{x}p(s,0,y_1)p(t-s,y_1,y_2-y_1)dy_1dy_2\\
                                          & =\int_{-\infty}^{x}p(t-s,0,y_2)dy_2
      \end{align*}
    \]

    showing that $X_t-X_s\sim \mathcal{N}(0,t-s)$.

    As for the independence, $(X_{t_n}-X_{t_{n-1}}, \ldots, X_{t_1}-X_{t_0})$ is a Gaussian vector for every finite $0\leq t_0<\ldots< t_n$.
    Indeed, by the definition of $P$, every linear combination of them yields a normal distribution -- check it as an exercise.
    Hence, being a Gaussian vector, it is enough to check that their covariance is equal to $0$.

    We check it for $n=2$, and the general case being left to you.
    By obvious variable change we have

    \[
      \begin{align*}
         E\left[ (X_{t_{2}}-X_{t_1})(X_{t_1}-X_{t_0}) \right]
            & = \int_{\mathbb{R}^4} \left( x_3-x_2 \right)\left( x_1-x_0 \right)p(t_0,0,x_0)p(t_0-t_1,x_0,x_1)p(t_1-t_2,x_1,x_2)p(t_3-t_2,x_2,x_3)dx_0dx_1dx_2dx_3\\
            & =\int_{\mathbb{R}^2} y_1 y_2 p(t_1-t_0,0,y_1)p(t_3-t_2,0,y_2)dy_1dy_2\\
            & =0
      \end{align*}
    \]

    finishing the proof.


## Continuity of Paths: Kolmogorov-&#268;entov Theorem

As for the continuity, we should prove that

\[
  P[\{\omega \colon t\mapsto X_t(\omega)\text{ is continuous}\}]=1
\]

to ensure that we have a Brownian motion.
Since $X$ is the canonical process, it follows that $\{\omega \colon t\mapsto X_t(\omega)\text{ is continuous}\}$ is exactly the set $C[0,t)\subseteq \mathbb{R}^{[0,\infty)}$ of continuous functions.
A naive way to show this would be to show that $P$ assigns probability one to the subset $C[0,t)\subseteq \mathbb{R}^{[0,\infty)}$ of continuous functions.
In that case, it would follow that almost all the paths of $X$ are concentrated under $P$ in the space of continuous functions.
This strategy is hopeless as the following proposition shows.

!!! proposition
    The set of continuous functions is not a measurable set for the product $\sigma$-algebra of $\mathbb{R}^{[0,\infty)}$.

??? proof
    Intuitively, it follows from the fact that measurable sets of $\mathbb{R}^{[0,\infty)}$ for the product $\sigma$-algebra are generated by finite-dimensional ones of the form

    \[
      C=\{\omega \colon \omega_{t_0}\in A_0, \ldots, \omega_{t_n}\in A_n\}, \quad A_k \in \mathcal{B}(\mathbb{R})
    \]

    As an exercise, try to show why this proposition holds.

To overcome this difficulty, we will *modify* the canonical process $X$ to another process $B$ which has continuous paths with probability $1$, that is construct a version of the Brownian motion that has continuous paths.

!!! definition "Definition: Modification vs Indistinguishable"

    Let $(\Omega, \mathcal{F}, P)$ be a probability space and $X$ and $Y$ be two stochastic processes.
    We say that

    * $X$ is a **modification** of $Y$ if

        \[
          P\left[ X_t = Y_t \right] = 1 \text{ for any }t \text{ in }\mathbf{T}
        \]

    * $X$ is **indistinguishable** from $Y$ if

        \[
          P\left[ \{ \omega\colon X_t(\omega) = Y_t(\omega) \text{ for all }t \text{ in }\mathbf{T}\}\right] = 1
        \]

!!! remark

    Clearly, indistinguishable implies modification.
    If $\mathbf{T}$ is countable, then the reciprocal is true as

    \[
        P[\{ \omega\colon X_t(\omega) \neq Y_t(\omega) \text{ for some }t \text{ in }\mathbf{T}\}] = P\left[ \cup_{t \in \mathbf{T}} \{X_t \neq Y_t\} \right] \leq \sum_{t \in \mathbf{T}} P[X_t \neq Y_t] = 0
    \]
    
    If $\mathbf{T}$ is not countable, then $\cup_{t \in \mathbf{T}}\{X_t\}$ is not a countable union of measurable sets and we can not apply subadditivity.
    The following counter example illustrate this fact.

    Let $\Omega = [0,1]^{\mathbf{T}}$ and $\mathcal{F} = \otimes_{t \in \mathbf{T}} \mathcal{B}([0,1])$ for $\mathbf{T} = [0,1]$.
    As for the measure we consider the product measure such that each marginal is equal to lebesgue.
    Define the two processes

    \[
        X_t \equiv 0 \quad \text{and}\quad Y_t (\omega) = 
          \begin{cases}
          0 & \text{if }\omega \neq t\\
          \omega & \text{if }\omega = t
          \end{cases}
    \]

    This defines two stochastic processes.
    Clearly, for every $t$, the two processes differes only on one point which is of lebesgue measure $0$.
    Hence they are modifications of each others.
    However $\{\omega\colon X_t(\omega) = Y_t(\omega)\text{ for all }0\leq t\leq 1\} = \emptyset$. 

If $P$ is a probability measure on the path space such that $X$ is a pre-Brownian motion and $B$ is a modification of $X$, then $B$ is a pre Brownian motion as well as it only involves finitely many marginals.
The goal is therefore to find a modification $B$ of $X$ such that $P[\{\omega\colon t \mapsto B_t(\omega) \text{ is continuous }\}] = 1$ which is a consequence of the following theorem

!!! theorem "Kolmogorov-&#268;entov"
    Let $(\Omega,\mathcal{F},P)$ be a probability space and $\tilde{X}=(\tilde{X}_{t})_{0\leq t\leq T}$ be a stochastic process.
    Suppose that
    
    \[
      E\left[ |\tilde{X}_t-\tilde{X}_s|^{\alpha} \right]\leq C|t-s|^{1+\beta}
    \]

    for every $s<t\leq T$ and some strictly positive constants $\alpha,\beta$, and $C$.
    Then $\tilde{X}$ admits a continuous modification $X$ which is locally H&#246;lder continuous for every exponent $0<\gamma<\beta/\alpha$, that is

    \[
      P\left[ \left\{ \omega \colon \sup_{0<t-s<h(\omega), t,s\leq T}\frac{|X_t(\omega)-X_s(\omega)|}{|t-s|^\gamma}\leq \delta \right\} \right]=1
    \]

    where $h$ is an almost surely strictly positive random variable and $\delta>0$.

!!! proof
    We show it for $T=1$ and define $\Pi^n=\{k/2^n\colon k=0,\ldots,2^n\}$ as well as $\Pi=\cup \Pi^n$, the sequence of dyadic numbers in $[0,1]$.

    - **Step 1: H&#246;lder continuity restricted to $\Pi^n$**
        Denote by
      
        \[
          A_n = \max_{\substack{s,t \in \Pi^n\\ |t-s|\leq 2^{-n}}}|\tilde{X}_t-\tilde{X}_s|\geq 2^{-n\gamma}
        \]

        By Markov's inequality,
      
        \[
          P[|\tilde{X}_t-\tilde{X}_s|\geq \varepsilon] \leq \frac{1}{\varepsilon^\alpha} E[|\tilde{X}_t-\tilde{X}_s|^\alpha] \leq C \varepsilon^{-\alpha}|t-s|^{1+\beta}.
        \]

        Hence for $0<\gamma < \beta/\alpha$ and $\varepsilon=2^{-\gamma n}$, it holds

        \[
        \begin{align*}
           P\left[ A_n \right] 
            & = P\left[ \bigcup_{k=1}^{2^n}\left\{ |\tilde{X}_{k/2^n}-\tilde{X}_{(k-1)/2^n}|\geq 2^{-n\gamma} \right\} \right]\\
            & \leq \sum_{k=1}^{2^n}P\left[ |\tilde{X}_{k/2^n}-\tilde{X}_{(k-1)/2^n}|\geq 2^{-n\gamma} \right]\\
            & \leq C\sum_{k=1}^{2^n} 2^{-n(1+\beta-\alpha\gamma)}\\
            & =C2^{-n(\beta-\alpha \gamma)}
        \end{align*}
        \]

        Since $\beta-\alpha \gamma >0$ by the very choice of $\gamma$, it follows from Borel-Cantelli that

        \[
        P\left[\limsup A_n \right] = P\left[ \bigcap_n \bigcup_{k\geq n} A_k \right]=0
        \]

        In other terms, for each $\omega$ out of a set $\mathcal{N}$ of zero measure, it holds that $1_{\cap_{k \geq n} }A_k^c (\omega) \rightarrow 1$.
        Denote by  

        \[
        n_0\left( \omega \right) = \inf\left\{ n \in \mathbb{N}\colon 1_{ \cap_{k\geq n}A_k^c}(\omega)\geq \frac{1}{2}\right\}
        \]

        it follows that $n_0$ is a random variable finite on $\Omega \setminus \mathcal{N}$.
        Hence  

        \[
        \max_{\substack{s,t \in \Pi^n\\ |t-s|\leq 2^{-n}}}|\tilde{X}_t(\omega)-\tilde{X}_s(\omega)|< 2^{-n\gamma}
        \]

        for all $n$ greater than $n_0(\omega)$.

    2. **Step 2: Hölder continuity restricted to** $\Pi$.  
        
        Fixing $\omega$ outside of $\mathcal{N}$, some integer $n$, we first show per induction that for every $m$ greater than $n+1$ it holds  

        \[
        |\tilde{X}_t(\omega)-\tilde{X}_s(\omega)|\leq 2 \sum_{k=n+1}^{m} 2^{-\gamma k}
        \]
        
        for every two $s$ and $t$ in $\Pi^m$ with $|t-s| <2^{-n}$.

        - For $m=n+1$, from $|t-s|<2^n$, we can only have $s=(k-1)/2^{n+1}$ and $t=k/2^{n+1}$ for some $k\in \{1,\ldots, 2^{n+1}\}$.
          Applying the relations from the previous steps the recursion hypothesis follows immediately for $m=n+1$.

        - Suppose that the recursion assumption holds up to $m-1$ for $m\geq n+1$, and let us show that it follows for $m$.
          For $s<t$ with $s,t$ in $\Pi^m$ and $|t-s|<2^n$, we define $s_1=\min\{\tilde{s}\in \Pi^{m-1}\colon \tilde{s}\geq s\}$ and $t_1=\max\{\tilde{t}\in \Pi^{m-1}\colon \tilde{t}\leq t\}$.
          It follows that $s\leq s_1\leq t_1\leq t$, $s_1,t_1$ are in $\Pi^{m-1}$ with $|t_1-s_1|\leq 2^n$ and $|t-t_1|\leq 2^{m}$ and $|s_1-s|\leq 2^{m}$.
          From the previous step, it follows that $|\tilde{X}_t(\omega)-\tilde{X}_{t_1}(\omega)| \leq 2^{-\gamma m}$ and $|\tilde{X}_{s_1}(\omega)-\tilde{X}_s(\omega)|\leq 2^m$.
          From the recursion hypothesis it also holds $|\tilde{X}_{t_1}(\omega)-\tilde{X}_{s_1}(\omega)|\leq 2\sum_{k=n+1}^{m-1} 2^{-\gamma k}$.
          These three inequalities together with the triangular inequality yields 

            \[
            \begin{align*}
            |\tilde{X}_t(\omega)-\tilde{X}_s(\omega)| 
              & \leq |\tilde{X}_t(\omega)-\tilde{X}_{t_1}(\omega)|+|\tilde{X}_{t_1}(\omega)-\tilde{X}_{s_1}(\omega)|+|\tilde{X}_{s_1}(\omega)-\tilde{X}_s(\omega)|\\
              & \leq 2^{-\gamma m}+2\sum_{k=n+1}^{m-1} 2^{-\gamma k}+2^{-\gamma m}\\
              & =2\sum_{k=n+1}^{m} 2^{-\gamma k}
            \end{align*}
            \]

            ending the proof of the recursion.

        Now for every $t$ and $s$ in $\Pi$ with $0<|t-s|< h(\omega)$ where $h(\omega)=2^{-n_0(\omega)}$, we pick $n\geq n_0(\omega)$ such that $2^{-(n+1)}\leq |t-s|< 2^{n}$.
        From the result of the recursion, and $\gamma>0$, we get
        
        \[
          \begin{align*}
             |\tilde{X}_t(\omega)-\tilde{X}_s(\omega)|
                & \leq 2\sum_{k=n+1}^{\infty} 2^{-\gamma k}\\
                & =\frac{2}{1-2^{-\gamma}}2^{-\gamma (n+1)}\\
                & \leq \delta |t-s|^{\gamma}
          \end{align*}
        \]

        for every $t$ and $s$ in $\Pi with $0<|t-s|<h(\omega)$ where $\delta = 2/(1-2^{-\gamma})$, showing that $t \mapsto \tilde{X}_t(\omega)$ is uniformly Hölder continuous of order $\gamma$ on $\Pi$.



    3. **Step3: Definition of the continuous version** $X$.  
        
        For $\omega$ in $\mathcal{N}$ we set $X(\omega)=0$.
        For $\omega$ outside of $\mathcal{N}$, and $t$ we pick a sequence $(s_n)$ of elements in $\Pi$ converging to $t$ which by the uniform continuity of $\tilde{X}(\omega)$ on $\Pi$ yields a limit $X_t(\omega)=\lim \tilde{X}_{s_n}(\omega)$ independent of the choice of the sequence $(s_n)$ in $\Pi$ converging to $t$.
        It follows that $X$ has continuous paths.
        Defined as a limit of sequence of random variables, it follows also that $X$ is a process.
        Finally, $\{X_t=\tilde{X}_t\}$ is contained in the set of those $\omega$ such that $\tilde{X}_{s_n}(\omega)$ has a limit for some sequence $(s_n)$ in $\Pi$ converging to $t$, it follows that $\{X_t = \tilde{X}_t\}\supseteq \mathcal{N}^c$.
        Hence $P[X_t=\tilde{X}_t]\geq P[\mathcal{N}^c]=1$ showing that $X$ is a version of $\tilde{X}$ which ends the proof of the Theorem.

!!! proposition
    There exists a probability space $(\Omega,\mathcal{F},P)$ and a stochastic process $B$ such that $B$ is a Brownian motion.

!!! proof
    As seen is a proposition above consequence of Kolomogorov extension theorem, we can construct a probability measure $P$ on the canonical space $(\Omega,\mathcal{F})$ such that the canonical process $X$ is a pre-brownian motion.
    To verify the conditions of Kolmogorov- &#268;entov's Theorem, recall that if a random variable $Y \sim \mathcal{N}(0,\sigma^2)$, then it holds that $E[Y^{2n}] = \sigma^n(2n-1)(2n-3)\ldots$.
    Since $X_t-X_s \sim \mathcal{N}(0,t-s)$, it follows that

    \[
    E\left[ \left| X_t-X_s \right|^{2n} \right]=C_n|t-s|^{n}
    \]

    where $C_n = (2n-1)(2n-3)\ldots$.
    Hence, for $\beta_n = n-1$ and $\alpha_n = 2n$, it follows that we can find a continuous version $B$ of $X$ locally Hölder continuous of order $0<\gamma < \beta_n/\alpha_n=1/2-1/(2n)$ for every $n$.
    The continuous version $B$ having the same finite dimensional distribution properties as $X$ we deduce that $B$ is a Brownian motion.

!!! proposition
    Almost all paths of the Brownian motion are nowhere locally Hölder continuous of order $\gamma>1/2$.
    In particular, they are nowhere differentiable.

!!! proof
    Homework sheet.

Some properties of the Brownian motion.

!!! proposition
    Let $B$ be a Brownian motion.  
    Then the following processes:

    1. $B_{s+\cdot}-B_s$ is a Brownian motion independent of $\sigma(B_u\colon u\leq s)$;  
    2. $-B$ is a Brownian motion;  
    3. $\sigma B_{\cdot / \sigma^2}$ is a Brownian motion for every $\sigma > 0$;  
    4. $X_0 = 0$ and $X_t = t B_{1/t}$ for $t > 0$ is a Brownian motion.  

!!! proof
    Is left as an exercise of the homework sheet.


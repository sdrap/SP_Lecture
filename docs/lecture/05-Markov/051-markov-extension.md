# Markov Chain and Extension

In this section we will study a special class of stochastic processes namely those which immediate next evolution only depends on the current state.
In other terms they are memory less.
We will first introduce them in general framework and dive down into the more intuitive markov chain framework.

In this section we consider a time index $\mathbf{T}$ which can be either $\mathbb{N}_0$ or $[0,\infty)$.
The Markov process will take value in a measurable state space $(S, \mathcal{S})$ where $S$ is a closed or open subset of $\mathbb{R}^d$ and $\mathcal{S}$ is the Borel $\sigma$-Algebra&mdash;in particular $S$ is a Polish space.
Though we can always consider processes from any abstract probability space, it is always possible to map it on the canonical space of paths with the product $\sigma$-algebra.

!!! definition "Definition: Path Space (or Canonical Space)"
  
    The canonical space with values in $(S, \mathcal{S})$ is given by the triplet

    \[
      (\Omega, \mathcal{F}, \mathbb{F})
    \]

    together with the canonical process $X = (X_t)_{t \in \mathbf{T}}$ where

    * **State Space**: 

        \[
          \Omega = \left\{ \omega = (\omega_t)_{t \in \mathbf{T}}\colon \omega_t \in S \right\} = S^{\mathbf{T}}
        \]

    * **$\sigma$-Algebra**: is the resulting product $\sigma$-algebra

        \[
          \mathcal{F} = \otimes_{t \in \mathbf{T}} \mathcal{S}
        \]

    * **Canonical Process**: $X = (X_t)_{t \in \mathbf{T}}$ where

        \[
          \begin{equation*}
            \begin{split}
              X_t \colon \Omega &\longrightarrow S \\
                        \omega = (\omega_s)_{s \in \mathbf{T}} & \longmapsto X_t(\omega) = \omega_t
            \end{split}
          \end{equation*}
        \]
        
        which is basically the projection process.
        By definition of the product $\sigma$-algebra $X$ is a stochastic process.

    * **Filtration**: $\mathbb{F}=(\mathcal{F}_t)_{t \in \mathbf{T}}$ where

        \[
          \mathcal{F}_t = \sigma\left( X_s \colon s\leq t \right)
        \]

        turning $X$ into an adapted process, its own filtration.


!!! definition "Definition: Markov Process on Canonical Space"

    The canonical process $X$ under a given probability measure $P$ is called a **Markov process** if it satisfies the **Markov property**:

    \[
    \begin{equation}
        P\left[ X_{t} \in B |\mathcal{F}_s \right]=P\left[ X_{t} \in B |X_s \right]
    \end{equation}
    \]

    for every $s\leq t$ and Borel set $B \in \mathcal{S}$.

    The probability distribution $B\mapsto \mu[B]:=P[X_0 \in B]$ is called the **start distribution** of the Markov process.

Note that the Markov property is equivalent to $E[ f(X_t)|\mathcal{F}_s ]=E[ f(X_t)| X_s ]$ for every bounded measurable function $f:S \to \mathbb{R}$.

!!! remark
    In this definition, a Markov process is in fact the specification of a probability measure on the path space such that the canonical process satisfies the **Markov property**.

    Note that we can alternatively give ourselves any abstract filtrated probability space $(\tilde{\Omega}, \tilde{\mathcal{F}}, \tilde{\mathbb{F}},\tilde{P})$ and define Markov processes as adapted processes $\tilde{X}$ satisfying the markov property.

    However the mapping $\omega \mapsto (t\mapsto \tilde{X}_t(\omega))$ from $\tilde{\Omega}$ to $\Omega$ with the pullback measure $P:=\tilde{P}\circ\tilde{X}^{-1}$ specifies the probability measure $P$ under which the canonical process $X$ is a Markov process with the same start distribution and same law.

From this remark, we see that defining a Markov process corresponds precisely to specifying the probability on the canonical space $\Omega = S^{\mathbf{T}}$.
In other terms, providing the structure of the mappings

\[
\begin{equation*}
    P_{s,t}(B):=P\left[ X_t \in B |X_s \right] \quad \text{and}\quad \mu(B)=P[X_0 \in B]
\end{equation*}
\]






for every $B \in \mathcal{S}$ and $s\leq t$.  

!!! example
    A typical way to see a discrete time finite state Markov process is as follows.  
    We set $S=\{1,2,3\}$ and $\mu:=\delta_1$.
    We further assume that the Markov process $X$ is time homogeneous, that is $P[X_{t+1}\in B|X_s]=P[X_1 \in B|X_0]$ providing the following evolution starting from $1$.

    \[
    \begin{equation*}
        p=\begin{pmatrix}
            0 & 1/2 & 1/2 \\ 1/2 &
            1/4 & 1/4\\ 2/3 & 1/3 & 0
        \end{pmatrix}.     
    \end{equation*}
    \]



    ```mermaid
    flowchart LR
      s2((State 2)) -->|1/4| s2
      s2 -->|1/2| s1((State 1))
      s1 -->|1/2| s2
      s1 -->|1/2| s3
      s3 -->|2/3| s1
      s3 -->|1/3| s2
      s2 -->|1/4| s3((State 3))
    ```



!!! example "Random walk"
    Let $Y$ be a discrete stochastic process of independent random variables with values in $S=\mathbb{Z}^d$.
    Define $X_t:=\sum_{s=0}^{t} Y_s$ and $\mathcal{F}_t:=\sigma(X_s\colon s\leq t)$.
    For $y\in\mathbb{Z}^d$, it holds

    \[
    \begin{align*}
        P[X_{t+1}=y | \mathcal{F}_t]
        & =P[Y_{t+1} =y-X_t | \mathcal{F}_t]
        \\
        &=\sum_{x\in\mathbb{Z}^d} P[Y_{t+1}=y-x | \mathcal{F}_t] 1_{\{X_t=x\}} 
        \\
        & = \sum_{x\in\mathbb{Z}^d} P[Y_{t+1}=y-x ] 1_{\{X_t=x\}} 
        \\
        & = \sum_{x\in\mathbb{Z}^d} P[Y_{t+1}=y-x | X_t] 1_{\{X_t=x\}}
        \\
        & = P[Y_{t+1}=y-X_t | X_t]
        \\
        & = P[X_{t+1}=y | X_t].
    \end{align*}
    \]

In both examples, we are either providing the transition probabilities or assuming a probability measure on the full space without checking whether such a probability measure can be constructed.

Hence

* A Markov process defines a start measure $\mu_0$ and family of transition probabilities $P_{st}(\cdot, \cdot)$. What are these transition probabilities? What are their properties?
* Is it possible to construct a markov process (or in other terms a probability measure $P$ on the path space) from families of transition probabilities? If so, under which conditions?

This is the content of the following section

## From Markov Process to Transition probability

Every $\sigma(X_s)$-measurable random variable $Y$ can be written as $Y = f(X_s)$ for some measurable function $f:S\to \mathbb{R}$.
Hence, there exist measurable functions $x\mapsto P_{st}(x,B)$ such that

\[
\begin{equation*}
    P_{st}(X_s,B)=P\left[ X_t\in B|X_s \right]
\end{equation*}
\]

for every $s<t$ and $B\in \mathcal{S}$.
Furthermore, it seems very natural that $B\mapsto P_{st}(x,B)$ should be a probability measure.
This leads us to the notion of stochastic kernel and transition probability which is an alternative way to see Markov processes.

!!! definition "Definition: Stochastic Kernel (see Fubini-Tonelli in Chapter 3)"
    A *stochastic kernel* on $(S, \mathcal{S})$ is a function $K:S\times \mathcal{S}\to [0,\infty)$ such that

    - $x \mapsto K(x,B)$ is measurable for every event $B$ in $\mathcal{S}$.
    - $B \mapsto K(x,B)$ is a measure for every $x$ in $S$.

    If $K(x,\cdot)$ is a probability measure, then we call it sometimes refered to as a **transition probability**.

For a measurable function $f:S\to \mathbb{R}$ and two kernels $K$ and $L$, we define

\[
\begin{equation*}
    Kf(x)=\int_{}^{} f(y)K(x,dy) \quad \text{and}\quad KL(x,A)=\int_{}^{}L(y,A) K(x,dy)
\end{equation*}
\]

An easy exercise shows that $Kf$ is a measurable function and that $KL$ is once again a stochastic kernel.
The question of whether the mapping $B\mapsto P_{st}(x,B)$ is a probability measure for every $x$ is in general not true.
However, it holds on Borel spaces as the following proposition shows.


!!! proposition "Regular conditional distribution"
    
    Let $X$ and $Y$ be two $S$ valued random variables.
    Then, there exists a stochastic kernel $K:S\times \mathcal{S}\to [0,1]$ such that

    \[
    K\left( X,B \right)= P\left[ Y \in B | X \right]
    \]

    almost surely for every Borel set $B$ and this stochastic kernel is unique almost surely.

!!! proof
    
    Without loss of generality, we may assume that $S=\mathbb{R}$.
    For every rational $r$, there exists a measurable function $f(\cdot,r): S\to [0,1]$ such that $f(X,r)=P[ Y\leq r |X ]$ almost surely.
    Since $f(X,r)\leq f(X,q)$ almost surely for every $r\leq q$ and $\lim_{r \to  \infty} f(X,r) =1$ and $\lim_{r\to -\infty}f(X,r)=0$ almost surely, and these conditions are countable and only depending on $X$, there exists a set $A\in \sigma(X)$ of measure one such that $f(x,r)$ is increasing with limit at $\pm \infty$ being $0$ or $1$.
    
    Hence, defining

    \[
    F(x,t)=1_A(x)\inf_{r>t, r\in \mathbb{Q}}f(x,r)+1_{A^c}(x)1_{[0,\infty)}(t)
    \]

    we get that $F(x,\cdot)$ is a cumulative distribution function for every $x\in \mathbb{R}$.
    In particular, there exists probability measures $K(x, \cdot)$ such that

    \[
    K(x,B)=\int_{B}^{} F(x,dt)
    \]

    and by construction $x\mapsto K(x,B)$ is measurable for every $x$.
    A monotone class argument together with monotone convergence for conditional expectation shows that

    \[
    K(X,B)=P\left[ Y \in B|X \right]
    \]

    and uniqueness almost surely follows from the uniqueness almost surely of the conditional expectation.

!!! remark
    
    In particular for any bounded measurable function $f:\mathbb{R}^2\to \mathbb{R}$, it holds

    \[
    E\left[ f(X,Y)| X \right]=\int_{}^{} f(X,y)K(X,dy) = g(X)
    \]

    where

    \[
    g(x) = \int_{}^{} f(x,y)K(x,dy)
    \]

This statement leads to the following proposition.

!!! proposition "Markov process transition probabilities"
    
    If $X$ is a Markov process under $P$ with start distribution $\mu$, there exists a family $(P_{st})_{s<t}$ of transition probabilities such that

    \[
    P\left[ X_t \in B |\mathcal{F}_s \right]=P_{st}(X_s,B)
    \]

    for every $s<t$.
    Furthermore, $(P_{st})_{s<t}$ satisfies the semi-group property

    \[
    P_{st}P_{tu}=P_{su}
    \]

    for every $s<t<u$.

!!! proof
    
    Suppose that $X$ is a Markov process.
    According to Proposition "Regular conditional distribution", it follows that there exists a family of stochastic kernels $P_{st}$ such that $P[ X_t \in B|X_s ]=P_{st}(X_s, B)$, hence Property.

    As for the semi-group property, it follows from the tower property of conditional expectation.
    Indeed, it holds $P_{st}(x,B)=P[X_t\in B|X_s=x]$ almost surely for every $x$, $B\in \mathcal{S}$ and $s<t$ as well as $E[f(X_t)|\mathcal{F}_s]=E[f(X_t)|X_s]=\int_{}^{} f(y)P_{st}(X_s,dy)$.
    Hence, using the Markov property,

    \[
    P_{st}P_{tu}(X_s,B)=\int_{S}^{} P_{tu}(y,B)P_{st}(X_s,dy)=E\left[ P_{tu}(X_t,B)|\mathcal{F}_s \right] = E\left[ E\left[ 1_{\{X_u \in B\}}|X_t \right]|\mathcal{F}_s \right]
    \]

    \[
    E\left[ E\left[ 1_{\{X_u \in B\}} |\mathcal{F}_t\right] |\mathcal{F}_s\right]=E\left[ 1_{\{X_u \in B\}} |\mathcal{F}_s\right]=E\left[ 1_{\{X_u \in B\}} | X_s\right]=P_{su}(X_s,B)
    \]

    By the uniqueness of the stochastic kernel, we deduce that $P_{st}P_{tu}=P_{su}$.

## From Transition Probabilities to Markov

The most interesting, and involving question though is the reciprocal.
In other terms, given a start distribution $\mu$ and a family of transition probabilities, does there exists a probability measure $P$ on the path space such that the canonical process is a Markov process with the given transition probabilities?
Is this process unique?
It is indeed true and based on the fondamental Kolmogorov extension Theorem that we will treat in a separate subsection during the construction of the Brownian motion.

!!! proposition "Existence of Markov process"
    
    Given a probability distribution $\mu$ and a family of transition probabilities $(P_{st})_{s<t}$ satisfying the semi-group property, then there exists a probability measure $P^\mu$ such that $X$ is a Markov process with start distribution $\mu$ and such that the transition probability holds.

!!! proof
    
    We define the family of probability measures $(P^\mu_I)$ for every finite family $I=\{0<t_1<\ldots<t_n\}\subseteq \mathbf{T}$ by setting for every $n+1$-dimensional Borel set $A_0\times A_1\times \cdots A_n$

    \[
    P^\mu_I(A_0\times \ldots \times A_n )=\int_{A_0}^{}\mu(dx_0)\int_{A_1}^{}P_{0t_1}(x_0,dx_1)\int_{A_2}^{}P_{t_1t_2}(x_1,dx_2)\cdots \int_{A_n}^{} P_{t_{n-1}t_n}(x_{n-1},dx_n)
    \]

    Due to the semi-group property, it defines a consistent family of probability measures.
    Hence, by means of the Kolmogorov extension theorem, we can extend this projective family to a unique probability measure $P^\mu$ such that $X$ by definition fulfills the transition probability property.
    Hence, $X$ is a Markov process under $P^\mu$ with start distribution $\mu$ and transition probability $(P_{st})_{s<t}$.

!!! remark
    
    Note that given a family of transition probabilities $(P_{st})$ we can define a probability measure $P^\mu$ on the path space such that $X$ is a Markov process with start distribution $\mu$.
    We denote in that case $E^\mu$ the expectation under this probability measure.
    This is in particular the case for all the Dirac measures $\delta_{x}$ for $x$ in $S$, that is, for Markov processes starting at $x$.
    We denote $P^x$ instead of $P^{\delta_x}$ and $E^x$ instead of $E^{\delta_x}$.
    Given $P^x$ for every $x$ and a distribution $\mu$, we can recover any $P^\mu$ as follows.

    \[
    P^{\mu}[A]=\int_{}^{} P^{x}[A] \mu(dx)
    \]

    In fact, $(x,A)\mapsto P^{x}[A]$ is a stochastic kernel on $S\times \mathcal{F}$ and therefore the relation

    \[
    P^{\mu}[A]=\int_{}^{} P^{x}[A] \mu(dx)
    \]

## Markov Property

**From now on, we will only consider time homogeneous Markov processes:**

!!! definition "Time homogeneous Markov process"
    
    A Markov process is called **time homogeneous** if and only if $P_{st}=P_{0t-s}$, or in other terms, $P[X_t\in B|X_s]=P[X_{t-s}\in B|X_0]$.


In that case, we only have to specify the start distribution $\mu$ and a family of transition probabilities $P_t$.

Let $Z$ be a random variable on $\Omega$, that is, $\mathcal{F}=\mathcal{F}_{\infty}=\sigma(X_t\colon t \in \mathbf{T})$-measurable.
It is, in particular, a function $\omega=(\omega_t)\mapsto Z(X(\omega))=Z((\omega)_{t \in \mathbf{T}})$.

However:

- If $Z$ is $\mathcal{F}_{t}=\sigma(X_s\colon s\leq t)$-measurable, then $Z$ can actually be seen as a measurable function that only depends on the paths up to time $t$, that is, $\omega \mapsto Z((X_s(\omega))_{s\leq t})=Z((\omega)_{s\leq t})$.
- If $Z$ is $\sigma(X_t)$-measurable, then it can be seen as a measurable function that only depends on the value of the path at time $t$, that is, $\omega \mapsto Z(X_t(\omega))=Z(\omega_t)$.

In particular, for the shift operator of a path by $t$:

\[
\begin{aligned}
    \theta_t :\Omega & \longrightarrow \Omega\\
    \omega =(\omega_s)_{s \in \mathbf{T}} & \longmapsto \theta_t(\omega)=(\omega_{s+t})_{s\in \mathbf{T}}
\end{aligned}
\]

we have that $Z\circ \theta_t(\omega)=Z\left( (\omega_{s+t})_{s\in \mathbf{T}} \right)$ is the evaluation of the random variable $Z$ on the shifted path space by $t$.
In particular, if $Z$ is $\sigma(X_s)$-measurable, then it holds that $Z\circ \theta_t(\omega)=Z(\omega_{t+s})$ is $\sigma(X_{t+s})$-measurable.

!!! proposition "**Markov Property**"
    
    Let $(P_{t})$ be a family of transition probabilities and $\mu$ be a probability distribution.
    For every bounded or positive measurable random variable $Z$, it holds that $x \mapsto E^x[Z]$ is measurable.
    In particular, for every $t$, the function $E^{X_t}[Z]$ defined as

    \[
    \omega \mapsto E^{X_t(\omega)}[Z]
    \]

    is $\sigma(X_t)$-measurable, and the Markov property holds

    \[
    E^\mu\left[ Z\circ \theta_t |\mathcal{F}_t  \right]=E^{X_t}\left[ Z \right]
    \]

!!! proof
    
    By monotony and approximation arguments, it is enough to show the proposition for the function $Z = 1_{A_0\times A_1\times \ldots \times A_n}(X_0,X_{t_{1}},\ldots, X_{t_n})$ where $A_k$ are Borel sets.
    By definition of $P^x$ and the previous remarks, it follows that

    \[
      \begin{align*}
         E^x[Z] & = \int_{A_0}^{}\delta_x(dx_0)\int_{A_1}^{}P_{t_1}(x_0,dx_1)\ldots \int_{A_n}^{}P_{t_n-t_{n-1}}(x_{n-1},dx_n)\\
                & = 1_{A_0}(x)\int_{A_1}^{}P_{t_1}(x,dx_1)\ldots \int_{A_n}^{}P_{t_n - t_{n-1}}(x_{n-1},dx_n)
      \end{align*}
    \]

    Since $x \mapsto 1_{A_0}(x)$ is measurable, and the $(P_{st})$ are stochastic kernels, the first assertion follows.
    In particular, for this specific form of $Z$, it holds  

    \[
    E^{X_t}[Z]=1_{A_0}(X_t)\int_{A_1}^{}P_{t_1}(X_t,dx_1)\ldots \int_{A_n}^{}P_{t_n-t_{n-1}}(x_{n-1},dx_n)
    \]

    As for the second assertion, once again with a monotone class argument, it is enough to show that

    \[
      E^\mu[ Z\circ \theta_t Y ]=E^\mu[ E^{X_t}[ Z ]Y]
    \]

    for $Y = 1_{B_0\times B_1\times \ldots \times B_m}(X_0,X_{s_{1}},\ldots, X_{s_m})$ where $A_k$ are Borel sets and $s_m= t$.
    By definition of $P^\mu$, the shift operator, and the expression of $E^{X_t}[Z]$ above we get

    \[
      \begin{align*}
         E^\mu[ Z\circ \theta_t Y ] & = E^\mu\left[ 1_{A}(X_{t}, X_{t+t_1}, \ldots, X_{t+t_n}) 1_B(X_{0}, \ldots, X_{s_m}) \right]\\
                                    & = \int_{B_0}^{}\mu(dx_0)\int_{B_1}^{}P_{s_1}(x_0,dx_1)\ldots\\
                                    & \qquad \qquad \qquad\ldots \int_{B_m\cap A_0}^{}P_{t-s_{m-1}}(x_{m-1},dx_m)\int_{A_1}^{} P_{t+t_1-t}(x_{m},dy_1)\cdots \int_{A_n}^{} P_{t+t_{n} -t-t_{n-1}}(y_{n-1},dy_n)\\
                                    & = \int_{B_0}^{}\mu(dx_0)\int_{B_1}^{}P_{s_1}(x_0,dx_1)\ldots \int_{B_m\cap A_0}^{}P_{t-s_{m-1}}(x_{m-1},dx_m)\int_{A_1}^{} P_{t_1}(x_{m},dy_1)\cdots\\
                                    & \qquad \qquad \qquad \cdots \int_{A_n}^{} P_{t_{n}-t_{n-1}}(y_{n-1},dy_n)\\
                                    & = E^\mu[ E^{X_t}[ Z ]Y]
      \end{align*}
    \]




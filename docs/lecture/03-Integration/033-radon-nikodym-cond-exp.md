# Radon-Nykodym and Conditional Expectation

## Radon-Nykodym Change of Measure

In this section, we will make use of a central theorem of Functional Analysis applied in the special case of Hilbert spaces.

!!! note

    A (real) Hilbert space is a vector space with a bilinear form $⟨\cdot,\cdot⟩:H\times H \to \mathbb{R}$, that is linear in the first as well as in the second argument, such that $⟨x,y⟩ =⟨y,x⟩$ and $⟨x,x⟩ \geq 0$ with equality if and only if $x=0$.
    
    Hence, $\left\Vert x\right\Vert=\left\vert\langle x,y\rangle\right\vert^{1/2}$ defines a norm on $H$ due to the Cauchy-Schwarz inequality that states that $\left\vert\langle x,y\rangle\right\vert\leq \left\Vert x\right\Vert\left\Vert y\right\Vert$.
    
    The finite-dimensional vector space $\mathbb{R}^d$ is a Hilbert space for the dot product $\langle x,y\rangle=\sum_{k\leq d} x_ky_k$ and defines the Euclidean norm $\left\Vert x\right\Vert=\sqrt{\sum_{k\leq d}x_k^2}$.
    
    More importantly in our case, given a finite measure $P$, the space $L^2$ with the bilinear form $⟨X,Y⟩=\int XY dP$ is, due to Hölder's inequality
    
    \[
    \int \left\vert XY\right\vert dP\leq \left( \int \left\vert X\right\vert^2dP \right)^{1/2} \left( \int \left\vert Y\right\vert^2dP \right)^{1/2},
    \]

    a Hilbert space with resulting norm $\left\Vert X\right\Vert_{L^2(P)}=\left(\int X^2 dP\right)^{1/2}$, which is the $L^2$ norm as defined before.

Recall that a linear functional $T:H\to \mathbb{R}$ where $(H,\langle \cdot,\cdot\rangle)$ is a Hilbert space is continuous if and only if

\[
\sup_{\left\Vert x\right\Vert=\langle x,x\rangle \leq 1}\left\vert T(x)\right\vert<\infty
\]

!!! theorem "Riesz Representation Theorem"

    Let $H$ be a Hilbert space, and $T:H\to \mathbb{R}$ be a continuous linear functional.
    Then there exists $y$ in $H$ such that $T(x)=\langle y,x\rangle$ for every $x$ in $H$.

This theorem allows us to treat the following central theorem of measure theory in a rather simple way.

!!! theorem "Radon-Nikodym Theorem"

    Let $(\Omega, \mathcal{F})$ be a measurable space and $P, Q$ two finite measures on $\mathcal{F}$ such that $Q \ll P$.
    Then there exists a $P$-almost surely unique and positive random variable $Z$ in $L^1(P)$ such that

    \[
    Q\left( A \right)=\int_{A}Z dP, \quad \text{for every }A \in \mathcal{F}
    \]

The random variable $Z$ is called the *Radon-Nikodym derivative* of $Q$ with respect to $P$ and denoted by $dQ/dP$.

In particular, it holds

\[
\int X dQ = \int X \frac{dQ}{dP} dP, \quad \text{for every }X \text{ in }L^1(Q).
\]

!!! proof

    The proof is based on the argumentation of John von Neumann.
    The measure
    
    \[
    \tilde{Q}[A]=P[A]+Q[A] \quad \text{for } A \in \mathcal{F}
    \]
    
    is such that $\tilde{Q}$ is equivalent to $P$.
    Indeed, for any event $A$, on the one hand, $P[A]=0$ implies that $Q[A]=0$ and therefore $\tilde{Q}[A]=P[A]+Q[A]=0$.
    On the other hand, the positivity of $Q$ and $P$ implies $P[A]=0$ whenever $\tilde{Q}[A]=0$, showing $P\sim \tilde{Q}$.
    The equivalence between $P$ and $\tilde{Q}$ implies in particular that two random variables $X$ and $Y$ agree $P$-almost surely if and only if they agree $Q$-almost surely.
    Hence, $L^0(P)=L^0(\tilde{Q})$.
    For any random variable $X$ in $L^0(P)=L^0(\tilde{Q})$, it holds

    \[
    \left\Vert X\right\Vert_{L^2(P)}^2= \int X^2 dP\leq \int X^2 d(P+Q)=\left\Vert X\right\Vert_{L^2(\tilde{Q})}^2
    \]

    showing that $L^2(\tilde{Q})\subseteq L^2(P)$.
    
    Define now the linear functional

    \[
    T\colon L^2(\tilde{Q})\to \mathbb{R}, \quad X \mapsto T(X)=\int X dP
    \]

    which is well-defined since $L^2(\tilde{Q})\subseteq L^2(P)$.
    Using Jensen's inequality and the fact that $\tilde{Q}/\tilde{Q}(\Omega)$ is a probability measure, it holds

    \[
    \left| T(X) \right|\leq \sqrt{\tilde{Q}(\Omega)}\left\Vert X\right\Vert_{L^2(\tilde{Q})}.
    \]

    As a consequence,

    \[
    \sup_{X \in L^2(\tilde{Q}), \left\Vert X\right\Vert_{L^2(\tilde{Q})}\leq 1} \left\vert T(X)\right\vert\leq \sqrt{\tilde{Q}(\Omega)}<\infty,
    \]

    showing that $T$ is a continuous linear functional on the Hilbert space $L^2(\tilde{Q})$.
    Applying the Riesz Representation Theorem, there exists $Y$ in $L^2(\tilde{Q})$ such that

    \[
    T(X)=\langle X, Y\rangle = \int XY d\tilde{Q},\quad \text{for every }X\in L^2(\tilde{Q}).
    \]

    Taking $X=1_A$ for $A=\{Y\leq 0\}$, it follows that $P[A]=0$, showing that $Y>0$ $P$-almost surely.
    Similarly, we obtain $0<Y\leq 1$ $\tilde{Q}$- and $P$-almost surely.
    Defining $Z=1/Y-1$, which is a positive measurable function in $L^1(P)$, it follows that

    \[
    Q\left( A \right)=\tilde{Q}(A)-Q(A)=\int_A Z dP, \quad \text{for every } A \in \mathcal{F}
    \]

    which ends the proof of existence.
    
    Uniqueness is left as an exercise.


## Conditional Expectation

The Radon-Nikodym Theorem allows us to prove easily the existence of conditional expectations.

!!! theorem "Theorem: Conditional Expectation"

    Let $(\Omega,\mathcal{F},P)$ be a probability space and $\mathcal{G}\subseteq \mathcal{F}$ be a sub-$\sigma$-algebra.
    For every integrable random variable $X$, there exists a $P$-almost surely unique $\mathcal{G}$-measurable and integrable random variable $Y$ such that

    \[
    E\left[ 1_A X \right]=E\left[ 1_A Y \right],\quad \text{for every }A \in \mathcal{G}
    \]

    Denoting $E[X|\mathcal{G}]:=Y$, provided all the following random variables are all in $L^1$, it holds:

    1. $X\mapsto E[X | \mathcal{G}]$ is linear, monotone, and $E[c|\mathcal{G}]=c$ for every constant.
    2. $E[X|\mathcal{G}]=E[X]$ if $\mathcal{G}=\{\emptyset, \Omega\}$.
    3. $E[X_n|\mathcal{G}]\nearrow E[X|\mathcal{G}]$ whenever $0\leq X_n\nearrow X$.
    4. $E[YX|\mathcal{G}]=YE[X|\mathcal{G}]$ and $E[Y|\mathcal{G}]=Y$ whenever $Y$ is $\mathcal{G}$-measurable.
    5. $E[E[X|\mathcal{G}_2]|\mathcal{G}_1]=E[X|\mathcal{G}_1]$ for every two $\sigma$-algebras $\mathcal{G}_1\subseteq \mathcal{G}_2\subseteq \mathcal{F}$.
    6. $\varphi(E[X|\mathcal{G}])\leq E[\varphi(X)|\mathcal{G}]$ if $\varphi$ is convex with $\varphi(X)\in L^1$.
    7. $E[\left\vert E[X|\mathcal{G}]\right\vert]\leq E[\left\vert X\right\vert]$.
    8. $E[\liminf X_n|\mathcal{G}]\leq \liminf E[X_n|\mathcal{G}]$ if $X_n\geq Y \in L^1$ and $\liminf X_n \in L^1$.
    9. $E[X|\mathcal{G}]=\lim E[X_n |\mathcal{G}]$ if $X_n \to X$ almost surely and $|X_n|\leq Y\in L^1$.
    10. $E[XE[Y|\mathcal{G}]]=E[E[X|\mathcal{G}]Y]=E[E[X|\mathcal{G}]E[Y|\mathcal{G}]]$.

This unique random variable is called the $\mathcal{G}$-*conditional expectation* of $X$, and is denoted by $E[X|\mathcal{G}]$.




!!! proof

    For $X$ in $L^1$, it defines two finite measures on $\mathcal{G}$ given by

    \[
    Q^{\pm}(A)=E\left[ 1_A X^{\pm}\right], \quad A \in \mathcal{G}
    \]

    which are by definition both absolutely continuous with respect to $P$.
    It follows from the Radon-Nikodym Theorem {#thm:radonnikodym} that there exist two $P$-almost surely unique positive $\mathcal{G}$-measurable random variables $Z^{\pm}\in L^1(\mathcal{G})$ such that

    \[
    Q^{\pm}(A)=E[1_A Z^{\pm}].
    \]

    Defining $E\left[ X|\mathcal{G} \right]=Z^+-Z^-\in L^1(\mathcal G)$ as the conditional expectation ends the proof of existence and uniqueness.

    In the following, we assume that the integrability conditions are sufficient for the assertions.

    - **Point 1**: Follows immediately from the linearity and monotonicity of the expectation.
    - **Point 2**: Let $Y=E[X|\mathcal{G}]$. Since $\mathcal{G}$ is the trivial $\sigma$-algebra, it follows that $Y$ is constant. Furthermore, $E[Y1_\Omega]=E[X1_{\Omega}]=E[X]$, hence $Y=E[X]$ per definition of the conditional expectation.
    - **Point 3**: For $X_n \nearrow X$ almost surely, by monotonicity of the conditional expectation, it follows that $E[X_n|\mathcal{G}]\leq E[X|\mathcal{G}]$ and is an increasing sequence whose limit is denoted by $Y$.  
        For $A=\{Y < E[X|\mathcal{G}]\}$, which is in $\mathcal{G}$, we have by monotone convergence

        \[
        E[ 1_A (E[ X|\mathcal{G} ]-Y) ]=\lim E[ 1_A E[X-X_n|\mathcal{G}] ]=\lim E[ X-X_n]=0
        \]

        showing that $P[A]=0$ since $E[X|\mathcal{G}]\geq Y$.
    - **Point 4**: For $Y=1_A$ with $A \in \mathcal{G}$, it holds

        \[
        E[ 1_BE[ YX|\mathcal{G} ]]=E[ 1_B YX ]=E[ 1_{B\cap A}X ]=E[ 1_{B\cap A}E[ X|\mathcal{G} ]]=E[1_B YE[ X|\mathcal{G} ]].
        \]

        Since $YE[X|\mathcal{G}]$ is $\mathcal{G}$-measurable, by uniqueness of the conditional expectation, we get $YE[X|\mathcal{G}]=E[YX|\mathcal{G}]$ for every $Y$ of the form $Y=1_A$ with $A$ in $\mathcal{G}$.
        By linearity of the conditional expectation, it holds for every simple step $\mathcal{G}$-measurable $Y$.
        By approximating from below by simple step functions and using Point 3, it holds for any positive $\mathcal{G}$-measurable random variable $Y$.

        The general case follows from the linearity of the conditional expectation and the decomposition $Y=Y^+-Y^-$.
    - **Point 5**: Let $A$ in $\mathcal{G}_1\subseteq \mathcal{G}_2$.
        By the definition of the conditional expectation applied twice, it follows that

        \[
        E[1_A E[E[X|\mathcal{G}_2]|\mathcal{G}_1]]=E[1_A E[ X|\mathcal{G}_2]]=E[1_AX]
        \]

        showing that $E[E[X|\mathcal{G}_2]|\mathcal{G}_1]=E[X|\mathcal{G}_1]$.
    - **Point 6**: This follows from Jensen's inequality using the fact that the conditional expectation is linear and monotone, plus monotone convergence from Point 3.
    - **Point 7**: Applying Point 6 for $\varphi(x)=|x|$.
    - **Point 8**: For the Fatou assertion, it follows from Point 3 by considering the increasing sequence $Z_n=\sup_{k\geq n}X_k$.
    - **Point 9**: Follows from the dominated convergence theorem.

For your interest, here is the proof of the existence of conditional expectation using Hilbert projections.

!!! proof

    Suppose first that $X \in L^2(\mathcal{F})$.
    Note that $L^2(\mathcal{F})$ is a Hilbert space for the norm $\left\Vert\cdot\right\Vert_2$ and $L^2(\mathcal{G})$ is a closed linear subspace of $L^2(\mathcal{F})$.
    Hence, by Hilbert's projection theorem, there exists a unique $Y \in L^2(\mathcal{G})$ such that $X-Y$ is orthogonal to $L^2(\mathcal{G})$.
    Since $1_A \in L^2(\mathcal{G})$ for every $A \in \mathcal{G}$, it follows that

    \[
    E\left[ (X-Y)1_A \right]=\langle X-Y,1_A\rangle=0, \quad A \in \mathcal{G}
    \]

    showing the main assertion.



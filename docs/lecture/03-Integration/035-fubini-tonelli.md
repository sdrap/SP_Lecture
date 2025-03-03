# Fubini-Tonelli, Stochastic Kernel

The theorem of Fubini-Tonelli is concerned with the definition of sound product measures on finite product spaces and their properties.
To do so, we will make use of Carathéodory's extension Theorem.
In the following, we consider the two-dimensional case.

Let $(\Omega_1,\mathcal{F}_1)$ and $(\Omega_2, \mathcal{F}_2)$ be two measurable spaces and define $\Omega =\Omega_1 \times \Omega_2$ endowed with the product $\sigma$-algebra $\mathcal{F}=\mathcal{F}_1\otimes \mathcal{F}_2$.

!!! proposition

    Let $A$ be an event in the product $\sigma$-algebra $\mathcal{F}=\mathcal{F}_1\otimes \mathcal{F}_2$ and $X\colon \Omega \to \mathbb{R}$ be a measurable function.
    Define

    \[
    \begin{align}
        A_{\omega_1} & :=\{\omega_2\in \Omega_2\colon (\omega_1,\omega_2)\in A\}\subseteq \Omega_2,  &\quad A_{\omega_2} & :=\{\omega_1\in \Omega_1\colon (\omega_1,\omega_2)\in A\}\subseteq \Omega_1,\\
        X_{\omega_1} & :=X(\omega_1,\cdot):\Omega_2\to \mathbb{R},  &\quad X_{\omega_2} & :=X(\cdot,\omega_2):\Omega_1\to \mathbb{R}.
    \end{align}
    \]

    Then it holds that $A_{\omega_1}$ and $A_{\omega_2}$ are events in $\mathcal{F}_2$ and $\mathcal{F}_1$ respectively.
    Furthermore, $X_{\omega_1}$ is $\mathcal{F}_2$-measurable, and $X_{\omega_2}$ is $\mathcal{F}_1$-measurable.

!!! proof

    Let $\mathcal{C}$ be the collection of those $A\in\mathcal{F}$ such that $A_{\omega_2}\times A_{\omega_1}$ is in $\mathcal{F}_1\times \mathcal{F}_2$.
    It clearly holds that $\mathcal{F}_1\times \mathcal{F}_2\subseteq \mathcal{C}$.
    Direct inspection shows that $\mathcal{C}$ is a $\sigma$-algebra, and therefore 

    \[
      \mathcal{F}=\sigma(\mathcal{F}_1\times \mathcal{F}_2)\subseteq \mathcal{C}\subseteq \mathcal{F},
    \]

    showing the first assertion.

    As for the second point, let $B$ be a Borel set in $\mathbb{R}$.
    It follows that $\{X_{\omega_1}\in B\}=\{X\in B\}_{\omega_1}$, which is an element of $\mathcal{F}_2$ by what has just been shown.
    Hence, $X_{\omega_1}$ is $\mathcal{F}_2$-measurable.
    The same argumentation holds for $X_{\omega_2}$.

!!! definition "Definition: Stochastic Kernel"

    A *stochastic kernel* on $\Omega_1\times \mathcal{F}_2$ is a function $K\colon \Omega_1\times \mathcal{F}_2\to [0,1]$ such that

    1. $\omega_1\mapsto K(\omega_1,A_2)$ is $\mathcal{F}_1$-measurable for every event $A_2$ in $\mathcal{F}_2$.
    2. $A_2\mapsto K(\omega_1,A_2)$ is a probability measure on $\mathcal{F}_2$ for every $\omega_1 \in \Omega_1$.

A stochastic kernel is, in some sense, a measurable family of probability measures on $\mathcal{F}_1$, one for each state $\omega_1$ in $\Omega_1$.
A special case of a stochastic kernel is the constant one $K(\omega_1,\cdot)=P_2$ for all states $\omega_1$ in $\Omega_1$, where $P_2$ is a probability measure on $\mathcal{F}_2$.

Given a probability measure $P_1$ on $\mathcal{F}_1$, we want to define a probability measure $P$ on the product $\sigma$-algebra $\mathcal{F}$ such that

\[
P[A]=\int_{\Omega_1}\left( \int_{\Omega_2}1_A(\omega_1,\omega_2)K(\omega_1,d\omega_2) \right)P_1(d\omega_1).
\]

This is the subject of the following theorem.

!!! theorem "Stochastic variant of Tonelli's Theorem"

    Let $P_1$ be a measure on $\mathcal{F}_1$ and $K$ a stochastic kernel on $\Omega_1\times \mathcal{F}_2$.
    Then there exists a unique probability measure $P$ on $\mathcal{F}$ such that for every positive random variable $X\colon \Omega \to \mathbb{R}$, it holds

    \[
      E_P\left[ X \right]=\int_{\Omega_1}\left( \int_{\Omega_2} X(\omega_1,\omega_2)K(\omega_1,d\omega_2) \right)P_1(d\omega_1)
    \]

    In particular,

    \[
      P[A]=\int_{\Omega_1}K(\omega_1, A_{\omega_1})P_1(d\omega_1)
    \]

    for any event $A$ in $\mathcal{F}$.

!!! proof

    Define $\mathcal{R}=\mathcal{F}_1\times \mathcal{F}_2$ and the set function $P\colon \mathcal{R}\to [0,1]$ given by

    \[
      P[A]=\int_{A_1}K(\omega_1,A_2)P_1(d\omega_1)
    \]

    For any element $A_1 \times A_2$ in $\mathcal{R}.
    Inspection shows that $\mathcal{R}$ is a semi-ring that contains $\Omega$.
    To apply Carathéodory’s extension Theorem, we must show that $P$ is a $\sigma$-additive pre-measure.

    It clearly holds that $P[\emptyset]=0$ and 

    \[
      P[\Omega]=\int_{\Omega_1}K(\omega_1,\Omega_2)P_1[d\omega_1]=\int_{\Omega_1}P_1[d\omega_1]=1.
    \]

    Let $(A_1^n\times A_2^n)$ be a sequence of pairwise disjoint elements of $\mathcal{R}$ such that $\cup A_1^n\times A_2^n=A_1\times A_2$ in $\mathcal{R}$ for some $A_1\in \mathcal{F}_1$ and $A_2 \in \mathcal{F}_2$ and define the functions

    \[
    \begin{aligned}
        X_n(\omega_1)&:=1_{A_1^n}(\omega_1)K(\omega_1,A_2^n)=\int_{\Omega_2}1_{A_1^n\times A_2^n}(\omega_1,\omega_2)K(\omega_1,d\omega_2),\\
        X(\omega_1)&:=1_{A_1}(\omega_1)K(\omega_1,A_2)=\int_{\Omega_2}1_{A_1\times A_{2}}(\omega_1,\omega_2)K(\omega_1,d\omega_2).
    \end{aligned}
    \]

    Furthermore, due to the pairwise disjointness of $(A_1^n\times A_2^n)$, as well as monotone convergence, it follows that
    
    \[
    \sum X_n(\omega_1)=\int_{\Omega_1}\sum 1_{A_1^n\times A_2^n}(\omega_1,\omega_2)K(\omega_1,d\omega_2)=\int_{\Omega_2}1_{\cup A_1^n\times A_2^n}K(\omega_1,d\omega_2)=X(\omega_1)
    \]
    
    for any state $\omega_1$ in $\Omega_1$.    
    Hence, once again, monotone convergence yields
    
    \[
      P[A_1\times A_2]=\int_{\Omega_1}X(\omega_1)P_1(d\omega_1)=\sum\int_{\Omega_1}X_n(\omega_1)P_1(d\omega_1)=\sum P[A_1^n\times A_2^n].
    \]
    
    showing the $\sigma$-additivity.
    
    It follows that we can apply Carathéodory's extension Theorem, ensuring the existence of a unique measure $P$ on $\mathcal{F}$ satisfying
    
    \[
      P[A_1\times A_2]=\int_{A_1}K(\omega_1,A_2)P_{1}(d\omega_1), \quad A_1 \times A_2 \in \mathcal{F}_1\times \mathcal{F}_2.
    \]
    
    Let us now show that

    \[
      P[A]=\int_{\Omega_1}K(\omega_1, A_{\omega_1})P_1(d\omega_1)
    \]

    holds.
    Define the collection $\mathcal{C}$ of those events $A$ in $\mathcal{F}$ such that this relation holds.    
    For $A=A_1\times A_2$, it follows that $A_{\omega_1}=A_2$ if $\omega_1 \in A_1$ and $\emptyset$ otherwise.
    It follows that 
    
    \[
      K(\omega_1,A_{\omega_1})=1_{A_1}(\omega_1)K(\omega_1,A_2),
    \]
    
    showing that $\mathcal{F}_1\times \mathcal{F}_2\subseteq \mathcal{C}$.    
    In particular, $\Omega \in \mathcal{C}$.
    Furthermore, for every pairwise disjoint sequence $(A^n)$ of elements in $\mathcal{C}$, denoting $A=\cup A^n$, it follows from monotone convergence that 
    
    \[
    \begin{align}
        P\left[ A\right]&=\sum P[A^n]
        =\int_{\Omega_1}\sum K(\omega_1,A_{\omega_1}^n)P_1(d\omega_1)\\
        &=\int_{\Omega_1}K(\omega_1,\cup A_{\omega_1}^n)P(d\omega_1)
        =\int_{\Omega_1}K(\omega_1,A_{\omega_1})P(d\omega_1)
    \end{align}
    \]
    
    showing that $A \in \mathcal{C}$.
    Finally, for $A \in \mathcal{C}$, it follows that
    
    \[
      P[A^c]=1-P[A] =\int_{\Omega_1} \left( 1-K(\omega_1,A_{\omega_1}) \right)P(d\omega_1) =\int_{\Omega_1} K(\omega_1,A_{\omega_1}^c)P(d\omega_1)
    \]
    
    showing that $A^c \in \mathcal{C}$.
    Hence, $\mathcal{C}$ is a $\lambda$-system that contains the $\pi$-system $\mathcal{F}_1\times \mathcal{F}_2$.
    Hence, by Dynkin's $\pi$-$\lambda$ lemma, it follows that
    
    \[
    \sigma(\mathcal{F}_1\times \mathcal{F}_2)\subseteq \mathcal{C}\subseteq \mathcal{F}=\sigma(\mathcal{F}_1\times \mathcal{F}_2)
    \]
    
    showing that $\mathcal{C}=\mathcal{F}$, that is, showing that the second equation of the Theorem holds for any event $A$ in $\mathcal{F}$.
    
    As for expectation equality from the theorem, it follows from the fact that every positive random variable $X\colon\Omega \to \mathbb{R}$ can be approximated by step functions, ending the proof.
   

!!! definition "Definition: Product Measure"

    With the notations of Theorem the previous theorem, we denote this unique measure by $P=P_1\otimes K$.

    In the case where $K(\omega_1,\cdot)=P_2$ for all $\omega_1 \in \Omega_1$ for some measure $P_2$ on $\mathcal{F}_2$, then $P$ is called the **product measure** of $P_1$ and $P_2$ on the product space and is denoted by $P=P_1\otimes P_2$.


In the case of a product measure, due to symmetry, it holds in particular

\[
\int_{\Omega}X(\omega)P(d\omega)=\int_{\Omega_1}\left( \int_{\Omega_2}X(\omega_1,\omega_2) P_2(d\omega_2)\right)P_1(d\omega_1)=\int_{\Omega_2}\left( \int_{\Omega_1}X(\omega_1,\omega_2) P_1(d\omega_1)\right)P_2(d\omega_2).
\]

!!! corollary

    Let $X$ be a positive random variable on some probability space $(\Omega,\mathcal{F},P)$. Then it holds

    \[
    E[X]=\int_{0}^\infty P\left[ X>x \right]\lambda(dx),
    \]

    where $\lambda$ is the Lebesgue measure on $\mathbb{R}$.

!!! proof

    For almost all state $\omega$ in $\Omega$, we have $X(\omega)\geq 0$, and therefore

    \[
      X(\omega)=\int_{0}^{X(\omega)}\lambda(dx)=\int_{0}^{\infty}1_{\{X(\omega)>x\}}\lambda(dx),
    \]

    where $\lambda$ is the Lebesgue measure on $\mathbb{R}$.
    Since $(\omega,x)\mapsto 1_{\{X(\omega)>x\}}$ is a $\mathcal{F}\otimes \mathcal{B}(\mathbb{R}_+)$-measurable function, by Fubini-Tonelli for the product measure $P\otimes \lambda$, it holds

    \[
    \begin{align}
        E\left[ X \right] &=\int_{\Omega} \left(\int_{0}^{\infty} 1_{\{X(\omega)>x\}}\lambda(dx)\right)P(d\omega) \\
        &=\int_{\Omega\times \mathbb{R}_+} 1_{\{X(\omega)>x\}}P\otimes \lambda(d\omega dx) \\
        &=\int_{0}^{\infty} \left(\int_{\Omega} 1_{\{X(\omega)>x\}}P(d\omega)\right)\lambda(dx) \\
        &=\int_{0}^{\infty} E\left[ 1_{\{X>x\}} \right]\lambda(dx) \\
        &=\int_{0}^{\infty} P\left[ X>x \right]\lambda(dx).
    \end{align}
    \]

We now address the stochastic variant of Fubini's theorem since we considered a stochastic kernel instead of a simple probability measure.
Let $X$ and $Y$ be two random variables on some probability space $(\Omega,\mathcal{F},P)$.
We consider the probability measure $P_{(X,Y)}$ on the product Borel $\sigma$-algebra of $\mathbb{R}^2$ given by

\[
  P_{(X,Y)}[B]=P\left[ (X,Y)\in B \right]
\]

for any Borel set $B$ on $\mathbb{R}^2$.
We suppose that this joint distribution $P_{(X,Y)}$ can be decomposed into $P_1\otimes K$ for some probability measure $P_1$ on $\mathcal{B}(\mathbb{R})$ and a stochastic kernel $K$ on $\mathbb{R}\times \mathcal{B}(\mathbb{R})$.
We will see later that this is always the case.
Note that by Tonelli's Theorem, it holds

\[
\begin{align}
    P_X[B_1]&=P[X\in B_1]=P\left[ (X,Y)\in B_1\times \mathbb{R} \right]=P_{(X,Y)}[B_1\times \mathbb{R}]\\
    &=\int_{\mathbb{R}}1_{B_1}(x)K(x,\mathbb{R})P_1(dx)=\int_{\mathbb{R}}1_{B_1}(x)P_1(dx)=P_1[B_1]
\end{align}
\]

showing that $P_X=P_1$, justifying therefore the notation $P_{(X,Y)}=P_X\otimes K_{Y|X}$.

!!! theorem

    Let $X$ and $Y$ be two random variables whose joint distribution is given by $P_X\otimes K_{Y|X}$, where $P_X$ is the distribution of $X$ and $K_{Y|X}$ is a stochastic kernel on $\mathbb{R}\times \mathcal{B}(\mathbb{R})$.

    For every positive random variable $g\colon \mathbb{R}^2\to \mathbb{R}_+$ such that $g(X,Y)$ is integrable, it holds

    \[
      E\left[ g(X,Y)|\sigma(X) \right]=\int_{\mathbb{R}}g(X,y)K_{Y|X}(X,dy)
    \]

    $P$-almost surely.


This relation means that for $P$-almost all $\omega \in \Omega$, it holds

\[
E\left[ g(X,Y)|\sigma(X) \right](\omega)=\int_{\mathbb{R}}g(X(\omega),y)K_{Y|X}(X(\omega),dy).
\]

!!! proof

    From Tonelli's Theorem's proof, the function $x\mapsto h(x):=\int_{\mathbb{R}}g(x,y)K_{Y|X}(x,dy)$ for $x$ in $\mathbb{R}$, is measurable, and therefore 

    \[
      h(X)=\int_{\mathbb{R}}g(X,y)K_{Y|X}(X,dy)
    \]

    is a positive random variable.
    Let $A$ be an event in $\sigma(X)$. 
    It follows that $A=X^{-1}(B)$ for some Borel set $B \in \mathbb{R}$.
    Therefore,

    \[
    \begin{align}
        E\left[ 1_{A}g(X,Y) \right] &= E\left[ 1_{B}(X)g(X,Y) \right] \\
        &=\int_{\mathbb{R}^2} 1_{B}(x)g(x,y)P_X\otimes K_{Y|X}(dx,dy) \\
        &=\int_{\mathbb{R}}\left( \int_{\mathbb{R}}1_B(x)g(x,y) K_{Y|X}(x,dy)\right)P_X(dx) \\
        &=\int_{\mathbb{R}}1_{B}(x)\left( \int_{\mathbb{R}}g(x,y) K_{Y|X}(x,dy)\right)P_X(dx) \\
        &=\int_{\mathbb{R}}1_B(x)h(x)P_{X}(dx) \\
        &=E\left[ 1_A h(X) \right].
    \end{align}
    \]

    This concludes the proof.

!!! remark

    As in the previous theorem, let $X$ and $Y$ be two random variables whose joint distribution is given by $P_{(X,Y)}$.
    Suppose that $P_{(X,Y)}$ is absolutely continuous with respect to the Lebesgue measure on $\mathbb{R}^2$.
    It follows that there exists a Lebesgue-almost surely unique positive function $f_{(X,Y)}\colon \mathbb{R}^2\to \mathbb{R}$ with expectation $1$ such that

    \[
    E\left[ g(X,Y) \right]=\int_{\mathbb{R}^2} g(x,y)f_{(X,Y)}(x,y)dxdy.
    \]

    It follows that the density of $X$ and $Y$ are respectively given by

    \[
    f_X(x)=\int_{\mathbb{R}} f_{(X,Y)}(x,y)dy\quad \text{and}\quad f_{Y}(y)=\int_{\mathbb{R}} f_{(X,Y)}(x,y)dx.
    \]

    By defining

    \[
    f_{Y|X}(x,y)=\frac{f_{(X,Y)}(x,y)}{f_{X}(x)}1_{\{f_X(x)>0\}}+f_{Y}(y)1_{\{f_X(x)=0\}},
    \]

    inspection shows that

    \[
    K_{Y|X}(x,A):=\int_{A} f_{Y|X}(x,y)dy
    \]

    defines a kernel.
    It holds

    \[
    \begin{align}
        P_X\otimes K_{Y|X}[A\times B]&=\int_{\mathbb{A}} \left(\int_{B} \frac{f_{(X,Y)}(x,y)}{f_{X}(x)}1_{\{f_X(x)>0\}}+f_{Y}(y)1_{\{f_X(x)=0\}} dy\right)f_{X}(x)dx\\
        &=\int_{\mathbb{A}} \int_{B} f_{(X,Y)}(x,y) dydx=P_{(X,Y)}[A\times B]
    \end{align}
    \]

    for every $A$ and $B$ in $\mathcal{B}(\mathbb{R})$.
    From the uniqueness assumption of Fubini-Tonelli's theorem, it follows that 

    \[
    P_{(X,Y)}=P_X\otimes K_{Y|X}.
    \]

    And following the theorem, it follows that

    \[
      E\left[ g(X,Y) \right]=\int_{\mathbb{R}^2} g(x,y)f_{(X,Y)}(x,y)dxdy=\int_{\mathbb{R}} \left(\int_{\mathbb{R}} g(x,y)f_{Y|X}(x,y)dy\right)f_{X}(x)dx.
    \]


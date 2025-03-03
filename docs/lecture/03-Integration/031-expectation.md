# Expectation

# Integration, Lebesgue Convergence Theorem


<div class = "grid" markdown>


!!! definition "Definition: Simple Random Variables"
	  A random variable $X$ is said to be **simple** if there exists a finite family $(A_k)_{1\leq k\leq n}$ of pairwise disjoint events and real nonzero numbers $(\alpha_k)_{1\leq k\leq n}$ such that:

    \[
      X=\sum_{k=1}^n \alpha_k 1_{A_k}
    \]

	  We denote by $\mathcal{L}^{0,step}$ the set of all simple random variables.


![Simple RV](./../../images/simple_rv_dark.svg#only-dark){align = right}
![Simple RV](./../../images/simple_rv_white.svg#only-light){ align = right}

</div>





!!! warning

    Clearly, $\mathcal{L}^{0,step}$ is a subset of $\mathcal{L}^0$.
    However, the decomposition of a simple random variable $X$ into $(A_k)_{1\leq k\leq n}$ and $(\alpha_k)_{1\leq k\leq n}$ is not unique.
    Indeed, let $A$ and $B$ be two elements of $\mathcal{F}$ such that $A\subseteq B$.
    It follows that $X=1_B=1_{B\setminus A}+1_A$.

!!! lemma
	  The spaces $\mathcal{L}^0$ as well as $\mathcal{L}^{0,step}$ are vector spaces.

!!! proof
    The proof is left as an exercise.

Let $X=\sum_{1\leq k\leq n}\alpha_k 1_{A_k}$ and $Y=\sum_{1\leq l\leq m}\beta_l 1_{B_l}$ be two simple random variables.
It is possible to find a finite family $(C_r)_{1\leq j\leq r}$ of pairwise disjoint elements in $\mathcal{F}$ and two finite families $(\tilde{\alpha_j})_{1\leq j\leq r}$ and $(\tilde{\beta}_j)_{1\leq j\leq r}$ of nonzero numbers such that:

\[
 \begin{equation}
   X=\sum_{1\leq j\leq r} \tilde{\alpha}_j 1_{C_j},\quad Y=\sum_{1\leq j\leq r} \tilde{\beta}_j 1_{C_j}
 \end{equation}
\]

Indeed, let $C_{kl}=A_k\cap B_l$, which constitutes a finite family of pairwise disjoint elements in $\mathcal{F}$.
It follows that:

\[
 X=\sum_{1\leq k\leq n}\sum_{1\leq l\leq m} \alpha_k 1_{C_{kl}},\quad Y=\sum_{1\leq k\leq n}\sum_{1\leq l\leq m} \beta_{l} 1_{C_{kl}}
\]

In other words, any two simple random variables can be decomposed on the same common family of pairwise disjoint elements.


<div class = "grid" markdown>

!!! definition "Definition: Expectation 1.0"
	  We define the **expectation** of a simple random variable $X=\sum_{1\leq k\leq n}\alpha_k 1_{A_k}$ with respect to $P$ as:

    \[
	  \hat{E}[X]:=\sum_{k\leq n} \alpha_k P[A_k]
    \]


![Expectation Simple RV](./../../images/expectation_dark.svg#only-dark){align = right}
![Expecation Simple RV](./../../images/expectation_white.svg#only-light){ align = right}

</div>



!!! exercise
	  Show that the definition of expectation is a well-defined operator on $\mathcal{L}^{0,step}$.
	  Indeed, the decomposition of $X$ is not unique.

!!! proposition
	  On $\mathcal{L}^{0,step}$, the following properties hold:

	  - *Monotonicity:* $\hat{E}[X]\leq \hat{E}[Y]$ whenever $X\leq Y$.
	  - *Linearity:* $\hat{E}$ is a linear operator on $\mathcal{L}^{0,step}$.

!!! proof
	  Let $X$ and $Y$ be two simple random variables.
	  Since those two simple random variables can be decomposed on a common set of events we can write:

    \[
  	  X=\sum_{k\leq n} \alpha_k 1_{A_k}, \quad Y=\sum_{k\leq m}\beta_k 1_{A_k}
    \]

	  If $X\leq Y$, it follows that $\alpha_k=X(\omega)\leq Y(\omega)=\beta_k$ for every state $\omega$ in $A_{k}$.
	  Hence:

    \[
  	  \hat{E}[X]=\sum_{k\leq n}\alpha_k P[A_{k}]\leq \sum_{k\leq n} \beta_k P[A_{k}]=\hat{E}[Y]
    \]

	  For real numbers $a$ and $b$, it holds:

    \[
	  \hat E[a X+bY]=\sum_{k\leq n} (a\alpha_k+b\beta_k)P[A_k]=a\sum_{k\leq n} \alpha_k P[A_k]+b\sum_{k\leq n} \beta_k P[A_k]=a\hat E[X]+b\hat E[Y]
    \]


This proposition is important in so far that ir shows that the expectation is a linear operator which is monotone.
This monotonicity property allows to extends naturally from below the expectation to the class of positive random variables.

<div class = "grid cards" markdown>

- __First Approximation__

    ----
    
    ![Expectation 1](./../../images/expectation1_dark.svg#only-dark){align = right}
    ![Expectation 1](./../../images/expectation1_white.svg#only-light){ align = right}

- __Second Approximation__

    ---
    
    ![Expectation 2](./../../images/expectation2_dark.svg#only-dark){align = right}
    ![Expectation 2](./../../images/expectation2_white.svg#only-light){ align = right}

</div>

!!! definition "Definition: Expectation 2.0"
  
	  For any positive extended random variable $X$ in $\bar{\mathcal{L}}^0_+$, we define the **expectation** of which as

    \[
	    E[X]:=\sup \left\{ \hat E[Y]\colon Y\leq X,Y \in \mathcal{L}^{0,step}_+ \right\}
    \]

    ----

    A random variable $X$ is called **integrable** if $E[X^+]<\infty$ and $E[X^-]<\infty$.
    The set of integrable random variables is denoted by $\mathcal{L}^1$ and the expectation of which is defined as

    \[
      E[X]:= E[X^+] - E[X^-]
    \]



!!! remark

    * Show as an exercise that for a positive extended random variable $X$ where $P[X=\infty]>0$, then it follows that $E[X]=\infty$;
    * Clearly $\mathcal{L}^{0,step}\subseteq \mathcal{L}^1$;
    * Also, by definition and monotonicity of $\hat{E}$, for every $X \in \mathcal{L}^{0,step}$, it holds that $E[X]=\hat{E}[X]$.
      In other terms, $E$ is an extension of $\hat{E}$ to the space $\bar{\mathcal{L}}^0_+$.
      We therefore remove the hat on the top of the expectation symbol everywhere.


!!! lemma
	For every $X$ and $Y$ in $\bar{\mathcal{L}}^0_+$ and $a,b$ positive numbers, it holds:

	- $E[X]\leq E[Y]$ whenever $X\leq Y$.
	- $E\left[ aX+b Y \right]=a E\left[ X \right]+b E\left[ Y \right]$.

!!! proof
	The proof is left as an exercise.

!!! theorem "Theorem: Lebegue's Monotone Convergence Theorem"

    Let $(X_n)$ be an increasing sequence of positive random variables.
    Denote by $X = \lim X_n = \sup X_n$ the resulting extended positive random variable limit of the sequence.
    Then it holds

    \[
	    E[X] = E[\lim X_n] = \lim E[X_n]
    \]

!!! proof
    By monotonicity, we clearly have $E[X_n]\leq E[X]$ for every $n$, therefore $\sup E[X_n]\leq E[X]$.
    Reciprocally, suppose that $E[X]<\infty$ and pick $\varepsilon>0$ and some simple positive random variable $Y$ such that $Y\leq X$ and $E[X]-\varepsilon\leq E[Y]$.
    For $0<c<1$ define the sets $A_n=\{X_n\geq cY\}$.
    Since $X^n$ is increasing to $X$, it follows that $A_n$ is an increasing sequence of events.
    Furthermore, since $cY\leq Y\leq X$ and $cY<X$ on $\{X>0\}$, it follows that $\cup A_n=\Omega$. 
    By non-negativity of $X_n$ and monotonicity, it follows that
    
    \[
    cE[1_{A_n}Y]\leq E[1_{A_n}X_n]\leq E[X_n]
    \]
    
    and so
    
    \[
    c\sup E[1_{A_n}Y]\leq \sup E[X_n]
    \]
    
    Since $Y=\sum_{l\leq k} \alpha_l 1_{B_l}$ for $\alpha_1,\ldots,\alpha_k \in \mathbb{R}_+$ and $B_1,\ldots, B_k\in \mathcal{F}$, it follows that
    
    \[
    E\left[ 1_{A_n}Y \right]=\sum_{l\leq k}\alpha_l P[A_n\cap B_l].
    \]
    
    However, since $P$ is a probability measure, and $A_n$ is increasing to $\Omega$, it follows from the lower semi-continuity of probability measures that $P[A_n\cap B_l]\nearrow P[\Omega\cap B_l]=P[B_l]$, and so
    
    \[
    \sup E[1_{A_n}Y]=\sum_{l\leq k}\alpha_l \sup P[A_n\cap B_l]=\sum \alpha_l P[B_l]=E[Y].
    \]
    
    Consequently
    
    \[
    E[X]\geq \lim E[X_n]=\sup E[X_n]\geq cE[Y] \geq cE[X]-c\varepsilon
    \]
    
    which by letting $c$ converging to $1$ and $\varepsilon$ to $0$ yields the result.
    The case where $E[X]=\infty$ is similar and left to the reader.


As the previous figure suggests, it is actually possible to construct by hand a sequential approximation of positive random variables by simple ones.

!!! proposition "Proposition: Approximation by Simple Random Variables"
	For any positive random variabel $X$, there exists an increasing sequence of simple positive random variables $(X_n)$ such that $X_n(\omega)\nearrow X(\omega)$ and uniformly on each set $\{X\leq M\}$ where $M\in \mathbb{R}$.

!!! proof
	Let $A_k^n=\{(k-1)/2^n\leq X<k/2^n\}$ for $k=1,\ldots, n2^n$ and define

	\[
	X_n:=\sum_{k=1}^{n2^n} \frac{k-1}{2^n}1_{A_k^n}+n1_{\{X>n\}}
	\]

	From the definition, it follows that $X_n\leq X$ for every $n$ and $X(\omega)-2^{-n}\leq X_n(\omega)$ for every $\omega \in \{X\leq n\}$.
	This, along with the monotonicity, concludes the proof.

!!! proposition
    	
    For $X$ and $Y$ in $\mathcal{L}^1$, a real number $a$ and two disjoint events $A,B$ in $\mathcal{F}$.
    The following assertions hold:
    
    1. $1_A X$, $X+Y$, $aX$ and $|X+Y|$ are integrable.
    2. $E[(1_A+1_B)X]=E[1_AX]+E[1_B Y]$.
    3. $E[X+Y]=E[X]+E[Y]$ and $E[aX]=aE[X]$.
    4. $E[X]\leq E[Y]$ whenever $X\leq Y$.
    5. If $X\geq 0$ and $E[X]=0$, then $P[X=0]=1$.
    6. If $P[X\neq Y]=0$, then $E[X]=E[Y]$.
    7. If $Z$ is a random variable such that $|Z|\leq X$, then $Z$ is integrable.

!!! remark

    In particular, $\mathcal{L}^1$ is a vector space and the expectation operator $E:\mathcal{L}^1\to \mathbb{R}$ is a monotone, positive, and linear functional.

!!! proof

    1. It holds $|X+Y|\leq |X|+|Y|$.
        According to Lemma \ref{lem:linearityL0+}, it follows that $E[|X+Y|]\leq E[|X|+|Y|]=E[|X|]+E[|Y|]<\infty$, showing that $X+Y$ and $|X+Y|$ are integrable.
        The argumentation for $1_AX$ and $aX$ follows the same line.

    2. It holds $\left( 1_A+1_B \right)X=(1_A+1_B)X^+-(1_A+1_B)X^-$.
        From the linearity on $\mathcal{L}^0_+$, it follows that $E[(1_A+1_B)X^\pm]=E[1_AX^\pm]+E[1_BX^\pm]$, showing that $E[(1_A+1_B)X]=E[1_AX]+E[1_BX]$.

    3. Without loss of generality, assume that $a\geq 0$.
        Here again, it follows from $aX=aX^+-aX^-$ and from the linearity on $\mathcal{L}_+^0$ that $E[aX^\pm]=aE[X^{\pm}]$.
        Also, since $X+Y=(X^++Y^+)-(X^-+Y^-)=(X+Y)^+-(X+Y)^-$, it follows that $(X^++Y^+)+(X+Y)^-=(X^-+Y^-)+(X+Y)^+$.
        However, again from the linearity on $\mathcal{L}_0^+$, it holds $E[(X^++Y^+)+(X+Y)^-]=E[X^+]+E[Y^+]+E[(X+Y)^-]$ and $E[(X^-+Y^-)+(X+Y)^+]=E[X^-]+E[Y^-]+E[(X+Y)^+]$, showing that $E[X+Y]=E[(X+Y)^+]-E[(X+Y)^-]=E[X^+]-E[X^-]+E[Y^+]-E[Y^-]=E[X]+E[Y]$.

    4. If $X\leq Y$, it follows that $0\leq Y-X$.
        According to the proposition stating the approximation from below, let $(Z_n)$ be an increasing sequence of positive simple random variables such that $Z_n\nearrow Y-X$.
        It follows from the monotone convergence Theorem that $0\leq E[Z^n]\leq \sup E[Z_n]=E[Y-X]$.
        Applying the previous point, we get $E[Y-X]=E[Y]-E[X]$, yielding the assertion.

    5. Let $A_n=\{X\geq 1/n\}$ which is an increasing sequence of events such that $\cup A_n=\{X>0\}$.
        It follows that $1_{A_n}1/n\leq 1_{A_n}X\leq X$ since $X$ is positive.
        Monotonicity from the previous point yields $P[A_n]/n\leq E[1_{A_n}X]\leq E[X]=0$, showing that $P[A_n]=0$ for every $n$.
        By the lower semi-continuity property of measures, it follows that $P[A]=\sup P[A_n]=0$, showing that $P[X>0]=0$.

    6. Suppose that $P[X\neq 0]=0$ and define $X_n=|X|1_{\{X=0\}}+(|X|\wedge n)1_{A_n}$ where $A_n=\{|X|\geq 1/n\}$.
        On the one hand, by definition, $A_n$ is an increasing sequence such that $\cup A_n=\{|X|\neq 0\}$.
        Hence, $0\leq X_n\nearrow |X|$, which by the monotone convergence Theorem implies that $E[X_n]\nearrow E[|X|]$.
        On the other hand, $A_n\subseteq \{X\neq 0\}$, which by monotonicity of the measure implies that $P[A_n]=0$ for every $n$.
        Hence, $E[X_n]\leq nP[A_n]=0$ for every $n$.
        We conclude that $E[|X|]=0$, which implies that $E[X]=0$.

    7. Follows directly from the linearity on $\mathcal{L}_+^0$.

!!! remark

    Note that for $X \in \bar{\mathcal{L}}^{0}$ with $X^- \in \mathcal{L}^1$, and $Y \in \mathcal{L}^1$, the same argumentation as above yields that:
    
    \[
      \begin{equation}
		    -\infty<E[X-Y]=E[X^+-X^--Y]=E[X^+]-E[X^-]-E[Y]=E[X]-E[Y]
		  \end{equation}
    \]


We finish this section with two of the most important assertions of integration theory.

!!! theorem "Theorem: Fatou's Lemma and Lebegue's Dominated Convergence"
    Let $(X_n)$ be a sequence in $\mathcal{L}^0$.

    - **Fatou's Lemma:** Suppose that $X_n\geq Y$ for some $Y \in \mathcal{L}^1$.
        Then it holds

        \[
          \begin{equation}
          E\left[ \liminf X_n \right]\leq \liminf E\left[ X_n \right].
        \end{equation}
        \]

    - **Dominated Convergence Theorem:** Suppose that $|X_n|\leq Y$ for some $Y \in \mathcal{L}^1$ and $X_n(\omega)\to X(\omega)$ for any state $\omega$.
        Then it holds

        \[
        \begin{equation}
          E\left[ X \right]=\lim E\left[ X_n \right].
        \end{equation}
        \]

!!! proof
    By linearity, up to the variable change $X_n-Y$, we can assume that $X_n$ is positive since $E[\liminf X_n-Y]=E[\liminf X_n]-Y$ and $E[X_n-Y]=E[X_n]-Y$ for every $n$.
    Let $Y_n=\inf_{k\geq n}X_n$, which is an increasing sequence of positive random variables that converges to $\liminf X_n=\sup_n \inf_{k\geq n}X_k$.
    Notice also that $Y_n\leq X_k$ for every $k\geq n$, and therefore by monotonicity of the expectation $E[Y_n]\leq \inf_{k\geq n}E[X_k]$.
    We conclude Fatou's lemma with the monotone convergence theorem as follows:

    \[
    \begin{equation}
        E\left[ \liminf X_n \right]=\lim E\left[ Y_n \right]=\sup E\left[ Y_n \right]\leq \sup_n\inf_{k\geq n}E[X_k]=\liminf E[X_n].
    \end{equation}
    \]

    A simple sign change shows that Fatou's lemma holds in the other direction.
    That is, if $X_n\leq Y$ for some $Y \in \mathcal{L}^1$, then it holds

    \[
    \begin{equation}
        \limsup E\left[ X_n \right]\leq E\left[ \limsup X_n \right].
    \end{equation}
    \]

    Now the dominated convergence theorem assumptions yield that $-Y\leq X_n\leq Y$ for some $Y \in \mathcal{L}^1$.
    Hence, since $X=\lim X_n=\liminf X_n=\limsup X_n$, it follows that

    \[
    \begin{equation}
        \limsup E\left[ X_n \right]\leq E\left[ \limsup X_n \right]=E\left[ X \right]=E\left[ \liminf X_n \right]\leq \liminf E\left[ X_n \right].
    \end{equation}
    \]

    However, $\liminf E\left[ X_n \right]\leq \limsup E[X_n]$, showing that $E[X_n]$ converges, and

    \[
    \begin{equation}
        E[X]=\liminf E[X_n]=\limsup E[X_n]=\lim E[X_n].
    \end{equation}
    \]

    which ends the proof.



!!! example "Example: Defining a Probability Measure from a Density"

    The concept of density is quite often used in statistics as it defines new measures.
    Let us formalize it using dominated convergence.

    On a probability space $(\Omega, \mathcal{F}, P)$, consider a positive integrable random variable $Z$ such that $E[Z]=1$.
    We define the set function 

    \[
        \begin{split}
            Q\colon \mathcal{F} & \longmapsto [0,1]\\
                    A & \longmapsto Q[A] = E[Z1_A]
        \end{split}
    \]

    which is clearly well defined and mapping to $[0,1]$ since $Z$ is positive and $E[Z 1_A]\leq E[Z]=1$.

    It follows that $Q$ defined as such is a new probability measure.
    Indeed

    * $Q[\emptyset] = E[Z1_{\emptyset}]=E[0] =0$, $Q[\Omega] = E[Z1_{\Omega}] = E[Z] = 1$;
    * **$\sigma$-additivity**: Let $(A_n)$ be a sequence of disjoint events.
        It follows that

        \[
            1_{\cup_{k\leq n}A_k} = \sum_{k\leq n} 1_{A_k} \nearrow \sum 1_{A_n} = 1_{\cup A_n}
        \]

        By monotone convergence

        \[
            \begin{align*}
                \sum Q[A_n] & = \lim \sum_{k\leq n} Q[A_k]\\
                            & = \lim \sum_{k\leq n}E[Z 1_{A_k}]\\
                            & = \lim E\left[ Z \sum_{k\leq n} 1_{A_k} \right]\\
                            & = E\left[ Z \sum 1_{A_n} \right]\\
                            & = E[Z 1_{\cup A_n}] = Q[\cup A_n]
            \end{align*}
        \]

    It can be shown using step functions that integration under $P$ and $Q$ are related through the formula

    \[
        E^Q[X] = E^P\left[ Z X \right]
    \]

    for any bounded random variable $X$ or any $X$ with sufficient integrability under $Q$.

    Another particular property of the probability measure $Q$ so defined is that it is **absolutely continuous** with respect to $P$ in the sense that

    \[
        P[A] = 0 \quad \text{implies} \quad Q[A] = 0
    \]

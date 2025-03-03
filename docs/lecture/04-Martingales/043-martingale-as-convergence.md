# Martingale: Almost Sure Convergence

Given a martingale $X$, this section treats the questions whether there exists $X_\infty$ such that $X_t\to X_\infty$ in the almost sure sense.
In other terms we want to study the asymptotic behavior of a stochastic process $X$.

Given a stochastic process $X$, we can classify the different behaviors of the paths $t \mapsto X_t(\omega)$ as follows

* **Convergence to $\pm \infty$**: the path converges to either $\infty$ or $-\infty$.
    The corresponding event of those states where it happens is given by

    \[C = \{\limsup X_t = -\infty \text{ or }\liminf X_t = \infty\}\]

* **Convergence in $\mathbb{R}$**: the path converges to a real limit, that is, $\lim X_t(\omega)$ exists in $\mathbb{R}$.
    The corresponding event of those states where it happens is given by

    \[B = \{-\infty < \liminf X_t = \limsup X_t<\infty\}\]

* **Oscillatory behavior**: In the case of non convergence, the path will oscillate infinitely.
    The corresponding event of those states where it happens is given by

    \[A = \{\liminf X_t < \limsup X_t\}\]


Clearly each of these sets are events and build a partition of $\Omega$.
The seminal idea of Doob was to recognize that sub-martingales have properties helping to estimate the probability of the latter set.
The building bloc for which is the Doob's upcrossing lemma.


## Doob's Upcrossing Lemma and Martingale Convergence

Let $X$ be a process, $x<y$ be real numbers and $F$ be a finite subset of $\mathbb{N}_0$.
Usually we take $F = [\![0, T ]\!] :=\{0, 1, \cdots, T\}$.
We wish to count the number of upcrossings of the path $t \mapsto X_t(\omega)$ on the set $F$.
We proceed as follows by defining the stopping times

\[
\begin{equation*}
    \tau_0=0
\end{equation*}
\]

and recursively

\[
\begin{align*}
    \tau_1 & = \inf\left\{t \in F: t\geq \tau_0 \text{ and } X_t \leq x\right\}\\
    \tau_2 & = \inf\left\{t \in F: t\geq \tau_1 \text{ and } X_t \geq y\right\}\\
           & \vdots\\
    \tau_{2k-1} & = \inf\left\{t \in F: t\geq \tau_{2k-2}, X_t \leq x\right\}\\
    \tau_{2k} & = \inf\left\{t \in F: t\geq \tau_{2k-1}, X_t \geq y\right\}
\end{align*}
\]

with the convention that the infimum over the empty set is infinite.

![Upcrossings](./../../images/upcrossing_dark.svg#only-dark){align = right}
![Upcrossings](./../../images/upcrossing_white.svg#only-light){ align = right}

We define the random quantity

\[
\begin{equation*}
    U_F\left( x,y,X(\omega) \right)=\sup\left\{k:\tau_{2k}(\omega)<\infty\right\}.
\end{equation*}
\]

This corresponds to the strict positive number of up-crossing of $[x,y]$ by $t\mapsto X_t(\omega)$ on $F$.

Finally, we adopt the notation $[\![s, t ]\!]:=\{s,s+1,\ldots,t\}$ for every integers $s\leq t$.

!!! lemma "Doob's Upcrossing Lemma"
    
    Let $X$ be a sub-martingale.
    Then for every two reals $x<y$, the number $U_{[\![0, T ]\!]}(x,y,X)$ of up-crossing of $[x,y]$ by $t\mapsto X_t$ up to time $T$, is a positive random variable and it holds

    \[
    \begin{equation}
        (y-x)E\left[ U_{[\![0, T ]\!] }\left( x,y,X \right) \right]\leq E\left[ \left(X_T-x\right)^+ \right]-E\left[ \left( X_0-x \right)^+ \right].
    \end{equation}
    \]

!!! proof

    First of all, the random times $\tau_k$, $k=0,1,\ldots$ defining the up-crossing function are all stopping times.
    Since $[\![0, T ]\!]$ is a discrete interval here, it follows that $U:=U_{[\![0, T ]\!]}(x,y,X)$ is a positive random variable.
    Define now the predictable gamble strategy, that is, the predictable process

    \[
    \begin{equation*}
        H_t=\sum_{k\geq 1} 1_{]\tau_{2k-1},\tau_{2k}]}(t) = 
        \begin{cases}
          1 & \text{if } \tau_{2k-1}< t\leq \tau_{2k} \text{ for some }k\\
          0 & \text{otherwize}
        \end{cases}
    \end{equation*}
    \]

    for which holds $H_0=0$.
    It is predictable since it takes only values $0$ and $1$ and it holds

    \[
    \begin{equation*}
        \{H_t=1\}=\cup \left\{ \tau_{2k-1}<t \right\}\cap\left\{ \tau_{2k}<t \right\}^c \in \mathcal{F}_{t-1}
    \end{equation*}
    \]

    This gamble strategy $H$ is a bet on upcrossings.
    Note that by the definition of $\tau_{2k}$ it follows that for every $\omega \in \Omega$, either $\tau_{2k}(\omega)\leq t$ or $\tau_{2k}(\omega)=\infty$.
    Further, by the definition of $U$ it holds that $U(\omega)\leq t$, and therefore $\tau_{2U(\omega)}\leq t$ as well as $\tau_{2U(\omega)+2}=\infty$ for every $\omega$.
    Finally, since $U$ is a random variable, it follows that $\tau_{2U}$ is a random time.

    We translate our problem at $0$ by defining the process $Y=(X-x)^+$.
    Since $\varphi(z)= (z-x)^+$ is increasing and convex function, it follows that $Y$ is a sub-martingale too.
    It clearly holds that $U$ also counts the number of up-crossings of $[0,y-x]$ up to time $T$ by $t\mapsto Y_t$ and therefore since $\tau_{2U}\leq T$ and $\tau_{2U+2} = \infty$, it holds

    \[
    \begin{align*}
        H\bullet Y_T &=\sum_{t=1}^T H_t\left( Y_{t}-Y_{t-1} \right)\\
        &=\sum_{t=1}^T\sum_{k\geq 1} 1_{]\tau_{2k-1},\tau_{2k}]}(t)\left( Y_{t}-Y_{t-1} \right)\\
        &=\sum_{k\geq 1}\sum_{t=(\tau_{2k-1}+1)\wedge T}^{\tau_{2k}\wedge T}\left( Y_t-Y_{t-1} \right)\\
        & = \sum_{k=1}^{U}\left( Y_{\tau_2k} - Y_{\tau_{2k-1}}\right) + (Y_T - Y_{\tau_{2U+1}\wedge T})\\
        & = \sum_{k=1}^{U}\left( Y_{\tau_2k} - Y_{\tau_{2k-1}}\right) + (Y_T - Y_{\tau_{2U+1}})1_{\{\tau_{2U+1}<T\}}\\
    \end{align*}
    \]

    On the one hand, we know that if $k\leq U$, then $Y_{\tau_{2k}}-Y_{\tau_{2k-1}}\geq y-x$.
    On the other hand, since $Y_{\tau_{2U+1}}$ is equal to $0$ on $\{\tau_{2U+1}<T\}$, it follows that  $(Y_T - Y_{\tau_{2U+1}})1_{\{\tau_{2U+1}<T\}}\geq 0$.
    Hence it holds

    \[
    \begin{align*}
        E[H\bullet Y_T] & =E\left[\sum_{k=1}^U (Y_{\tau_{2k}}-Y_{\tau_{2k-1}})\right]+E\left[(Y_{T}-Y_{\tau_{2U+1}})1_{\{T> \tau_{2U+1}\}}\right]\\
         & \geq E\left[\sum_{k=1}^U (y-x)\right]=(y-x)E[U]
    \end{align*}
    \]
    
    Defining $K_t=1-H_t$ for every $t\geq 1$ and $K_0=0$ which is a positive predictable process, hence by means of Doob's optional sampling theorem, it follows that $K\bullet Y$ is a sub-martingale and therefore $E[K\bullet Y_T]\geq E[K\bullet Y_0]= 0$.
    Since $K+H=1_{\{1\leq \cdot\} }$, it follows that
    
    \[
    \begin{align*}
        (y-x)E\left[ U \right]  & \leq E\left[ H\bullet Y_T \right]\\
                                & \leq E\left[ H\bullet Y_T \right]+E[K\bullet Y_T] \\
                                & = E\left[ \sum_{t=1}^T Y_{t}-Y_{t-1} \right]\\
                                & = E\left[ Y_T-Y_0 \right]\\
                                & =E\left[ \left( X_T-x \right)^+ \right]-E\left[ \left( X_0-x \right)^+ \right]
    \end{align*}
    \]
    
    which ends the proof.
  


!!! theorem "Theorem: Martingale Convergence $P$-Almost Sure"

    Let $X$ be a sub-martingale such that $\sup E[X_t^+]<\infty$.
    Then $X_t \to X_\infty$ almost surely for some integrable random variable $X_\infty$.

!!! proof

    Note that if $X$ is a sub-martingale, then $\sup E[\left\vert X\right\vert_t]<\infty$ is equivalent to $\sup E[X^+_t]<\infty$.
    Indeed, it follows from $\left\vert X\right\vert_t= 2X_t^+-X_t$ and the sub-martingale property, that $E[X_t]\geq E[X_0]>-\infty$.

    Let

    - $A$ be the event of those states $\omega$ such that $t\mapsto X_t(\omega)$ is oscillatory discontinuous.
        In other terms, the path will cross infinitely many times some interval $[q, r]$ for $q<r$ rationals.
        According to the definition in Doob's Upcrossing lemma, it follows that $U_{\mathbb{N}_0}(q, r, X)(\omega) = \lim_{T\to \infty} U_{[\![0, T ]\!]} (q, r, X)(\omega) = \infty$.
        Hence we can write

        \[
        \begin{equation*}
            A= \bigcup_{q<r \text{ and }q,r \in \mathbb{Q}}\left\{ U_{\mathbb{N}_0}\left( q,r,X\right)=\infty\right\}=\bigcup_{q<r\text{ and } q,r \in \mathbb{Q}}\left\{ \sup_{T \in \mathbb{N}_0}U_{[\![0, T ]\!]}(q,r,X)=\infty\right\}
        \end{equation*}
        \]

    - $B$ be the event of those states $\omega$ such that $t \mapsto X_t(\omega)$ has a real valued limit, that is

        \[
        \begin{equation*}
          B=\left\{ \infty <\liminf X_t=\limsup X_t <\infty \right\}
        \end{equation*}
        \]

    - $C$ be the event of those states $\omega$ such that $t \mapsto X_t(\omega)$ diverges to either $\infty$ or $-\infty$, that is

        \[
          C = \left\{ \limsup X_t = -\infty \text{ or }\liminf X_t = \infty \right\}
        \]

    In other terms $t\mapsto X_t$ converges to some extended random variable $X_\infty$ on $B\cup C$.
    As for $A$, it is a measurable set as a countable union of measurable sets.
    Furthermore, by means of Doob's up-crossing's Lemma, as well as monotone convergence, the assumptions of the theorem yield

    \[
    \begin{equation*}
       E\left[ \sup_{t \in \mathbb{N}_0}U_{[\![0, T ]\!]}(q,r,X) \right]=\sup_{t \in \mathbb{N}_0}E\left[ U_{[\![0, T ]\!] }(q,r,X) \right]\leq \frac{1}{q-r}\sup_{t}\left\{ E\left[ \left( X_t-q \right)^+ \right] -E\left[ \left( X_0-q \right)^+ \right]\right\}<\infty
    \end{equation*}
    \]

    It follows that $P[\sup_{t \in \mathbb{N}_0}U_{[\![0, T ]\!] }(q,r,X)=\infty]=0$ from which follows

    \[
    \begin{equation*}
        P[A]\leq \sum_{q<r\text{ and }q,r \in \mathbb{Q}}P\left[ \sup_{t \in \mathbb{N}_0}U_{[\![0, T ]\!]}(q,r,X)=\infty \right]=0.
    \end{equation*}
    \]

    Hence, $P[B\cup C]=1$, showing that $t\mapsto X_t$ converges almost surely to the extended real valued random variable $X_\infty$.
    Finally, by Fatou's Lemma,

    \[
    \begin{equation*}
        E[|X_\infty|]\leq \liminf E[|X_t|]\leq \sup E[|X|_t]<\infty
    \end{equation*}
    \]

    showing integrability of $X_\infty$ and also that $P[X_\infty=\infty\text{ or }X_\infty=-\infty]=P[C]=0$.

!!! corollary 
    Let $X$ be a super-martingale such that $\sup_t E[X_t^-]<\infty$.
    Then $X_t\to X_\infty$ almost surely for some integrable random variable $X_\infty$.

## Applications of $P$-almost Sure Convergence

This almost sure convergence results has numerous applications.
We present in the following several of them that as a consequence recovers the Borel-Cantelli lemma.

!!! theorem 

    Let $X$ be a martingale with $X_0=0$.
    Suppose that $|X_{t+1}-X_t|\leq c$ for every $t$ and some constant $c>0$.
    Then it holds

    \[
    \begin{equation*}
        P\left[ B\cup D \right]=1,
    \end{equation*}
    \]

    where

    \[
    \begin{equation*}
        B =\left\{ -\infty<\liminf X_t=\limsup X_t<\infty\right\} \text{ and } D =\left\{ \liminf X_t=-\infty \text{ and } \limsup X_t=\infty \right\}.
    \end{equation*}
    \]

This theorem states that martingales with uniformly bounded increments either converge to a real value or oscilate infinitely between $-\infty$ and $\infty$.


!!! proof

    Define the stopping time $\tau_k=\inf\{t\colon X_t > k\}$.
    According to Doob's sampling theorem, it follows that $X^{\tau_k}$ is a martingale such that $\sup_tE[(X^{\tau_k}_t)^+]\leq k+c<\infty$.
    Indeed, on $\{t < \tau_k\}$, it holds $X_t^{\tau_k}\leq k$ and on $\{\tau_k\leq t\}$, it holds $X_t^{\tau_{k}}=X_{\tau_k}\leq X_{\tau_k-1}+(X_{\tau_k}-X_{\tau_k-1})\leq k+c$.
    By the martingale convergence theorem, $\lim_{t\to \infty} X_t^{\tau_k}$ exists almost surely.
    On $\{\tau_k=\infty\}$ the processes $X$ and $X^{\tau_k}$ coincide, so that $\lim  X_t$ exists almost surely on $\{\tau_k=\infty\}$.
    In particular $\lim X_t$ exists almost surely on

    \[
    \begin{equation*}
        \bigcup\{\tau_k=\infty\}=\left\{\limsup X_t<\infty\right\}.
    \end{equation*}
    \]

    A similar argumentation for $-X$ shows that $\lim X_t$ exists almost surely on $\{\liminf X_t>-\infty\}$.
    That is $\lim X_t$ exists almost surely on $\{\liminf X_t>-\infty \}\cup\{\limsup X_t<\infty\}=D^c$.
    It means that $P[D^c\setminus B]=P[D^c\cap B^c]=0$.
    Hence, taking complementation, it follows that $P[B\cup D]=P[(D^c\cap B^c)]=1$ which ends the proof.

!!! corollary "Corollary: Pre Borel-Cantelli"

    We suppose that $\mathcal{F}_0=\{\emptyset,\Omega\}$.
    Let $(A_t)$ be a sequence of events in $\mathcal{F}$ such that $A_t$ is in $\mathcal{F}_t$ for every $t$.
    Then

    \[
    \begin{align*}
        \limsup A_t&=\bigcap_{t}\bigcup_{s\geq t}A_s=\left\{\omega:\omega\in A_t\text{ for infinitely many }t\right\}=\left\{\sum P(A_t|\mathcal{F}_{t-1})
            =\infty\right\}
    \end{align*}
    \]

    holds almost surely, whereby $P[A_t|\mathcal{F}_{t-1}]=E[1_{A_t}|\mathcal{F}_{t-1}]$.

!!! proof "Proof"

    We define the process $X$ as follows

    \[
    \begin{equation*}
        X_0=0\quad \text{ and }\quad X_t=\sum_{s=1}^t1_{A_s}-P\left[ A_s|\mathcal{F}_{s-1} \right], \quad \text{ for }t\geq 1
    \end{equation*}
    \]

    Since $\mathcal{F}_0=\{\emptyset,\Omega\}$, it follows that $X$ is a martingale.
    Indeed, $X$ is clearly adapted by definition, and $|X_t|\leq 2t$ so that $X$ is integrable.
    Furthermore, $E[X_1-X_{0}|\mathcal{F}_{0}]=E[X_1-X_0]=P[A_1]-P[A_1]=0$ and

    \[
    \begin{equation*}
        E[X_t-X_{t-1}|\mathcal{F}_{t-1}]=E[1_{A_t}-E[1_{A_t}|\mathcal{F}_{t-1}]|\mathcal{F}_{t-1}]=E[E[1_{A_t}-1_{A_t}|\mathcal{F}_{t-1}|\mathcal{F}_{t-1}]=0
    \end{equation*}
    \]

    for every $t\geq 2$.
    Since $|X_{t+1}-X_t|\leq 2$ holds for every $t$, we may apply the previous theorem of convergence for martingales with bounded bounded increments.
    On $B=\{\liminf X_t=\limsup X_t \in\mathbb{R}\}$, it holds

    \[
    \begin{equation*}
       \sum 1_{A_t}=\infty\quad \text{if, and only if,}\quad\sum P\left[A_n | \mathcal{F}_{t-1}\right]=\infty. 
    \end{equation*}
    \]

    On $D=\{\liminf X_t=-\infty\text{ and }\limsup X_t=\infty\}$ it holds

    \[
    \begin{equation*}
       \sum 1_{A_t}=\infty\quad \text{and}\quad \sum P\left[A_t| \mathcal{F}_{t-1}\right]=\infty. 
    \end{equation*}
    \]

    Since $P[B\cup D]=1$ we deduce

    \[
    \begin{equation*}
        \sum 1_{A_t}=\infty\quad \text{if, and only if,}\quad \sum P[A_t|\mathcal{F}_{t-1}]=\infty
    \end{equation*}
    \]

    almost surely.
    Moreover, $\limsup A_t=\{\sum 1_{A_t}=\infty\}$, hence the claim follows.


We close these application with Borel-Cantelli's lemma.

!!! lemma "Borel-Cantelli's Lemma"


    * If $(A_t)$ is a sequence of events in $\mathcal{F}$ and $\sum P[A_t]<\infty$, then it holds $P[\limsup A_t]=0$.
    * If $(A_t)$ is an independent sequence of events in $\mathcal{F}$ and $\sum P(A_t)=\infty$, then it holds $P[\limsup A_t]=1$.

!!! proof

    We consider the filtration $\mathbb{F}=(\mathcal{F}_t)_{t \in \mathbb{N}_0}$ given by $\mathcal{F}_0=\{\emptyset, \Omega\}$ and $\mathcal{F}_t:=\sigma(A_s\colon s\leq t)$ for $t\geq 1$.
    Define $\xi:=\sum P[A_t|\mathcal{F}_{t-1}]$.
    The monotone convergence theorem as well as the tower property shows that

    \[
    \begin{equation*}
        E[\xi]=E\left[\sum E[1_{A_t}|\mathcal{F}_{t-1}]\right]=\sum E[E[1_{A_t}|\mathcal{F}_{t-1}]]=\sum P[A_t].
    \end{equation*}
    \]

    1. If $\sum P[A_t]<\infty$, then it holds $P[\xi=\infty]=0$.
        The previous corollary yields $P[\limsup A_t]=0$.

    2. Suppose that $(A_t)$ is an independent sequence of events, therefore $A_t$ is independent of $\mathcal{F}_{t-1}$ which implies $P[A_t| \mathcal{F}_{t-1}]=P[A_t]$ for all $t$.
       Hence $\sum P[A_t|\mathcal{F}_{t-1}]=\sum P[A_t]=\infty$ almost surely and by the previous corollary it follows that $P[\limsup A_t]=1$.





# Martingales $L^p$-Convergence

As astonishing and useful the martingales convergence in the $P$-almost sure case can be due to Doob's optional sampling and upcrossing lemma it is often limiting from a topological viewpoint.
The $P$-almost sure convergence does not provides a satisfactory topology on spaces of random variable (in particular it is not a locally convex topology).
We would prefer in most case to get stronger convergence in terms of norms.

It turns out that convergence in $L^p$ for $p>1$ can be derived as shown in the subsequent section due to **Doob's maximal inequalities**.
The case of $L^1$ due to its topological particularity (is not a reflexive space) is not available without additional uniform integrability conditions.


## Doob's Maximal Inequalities and $L^p$ Convergence

The building block for $L^p$ convergence are the so-called Doob's maximal inequalities.
In the following, given a process $X$ we define the

- **Running supremum process** $\overline{X}$ by $\overline{X}_t=\sup_{s\leq t}X_s$.
- **Running infimum process** $\underline{X}$ by $\underline{X}_t=\inf_{s\leq t}X_s$.
- **Running absolute supremum process** $X^\ast$ by $X^\ast_t=\sup_{s\leq t} |X_s|$.

!!! proposition "Proposition: Doob's Maximal Inequalities"

    The following assertions hold true.

    1. Let $X$ be a sub-martingale and $\lambda>0$.
        Then it holds

        \[
        \begin{align*}
           \lambda P\left[ \overline{X}_t\geq \lambda \right]&\leq E\left[ 1_{\{\overline{X}_t \geq \lambda\}}X_t \right]\leq E\left[ X_t^+ \right];\\
           \lambda P\left[ \underline{X}_t\leq -\lambda \right]&\leq E\left[ 1_{\{\underline{X}_t >- \lambda\}} X_t \right]-E[X_0]\leq E\left[ X_t^+ \right]-E\left[ X_0 \right].
        \end{align*}
        \]

    2. For $X$ a positive sub-martingale and $p>1$, it holds

        \[
        \begin{equation*}
           \left\Vert\sup_{s \leq t}X_s\right\Vert_p\leq \frac{p}{p-1}\left\Vert X_t\right\Vert_p.
        \end{equation*}
        \]

!!! remark

    Note that Doob's maximal inequalities are similar to Markov inequality.
    The fundamental difference though and powerfull fact is that the probability of the behavior of the whole path between $0$ and $t$ is controled by the expectation of the sub martingale at the begining and end.

    Note also that the second statement shows that the norm of the running maximum of the path between $0$ and $t$, which can be arbitrarily large, is controled by the norm at time $t$.
    This however only holds for $p>1$.
    
    Those statements about the path being controled by the values at its boundary is certainly not trivial.



!!! proof "Proof"

    1. For the stopping time $\tau=\inf\{s:X_s\geq \lambda \}$, observe that $\{\tau\leq t\}=\{\overline{X}_t\geq \lambda\}$.
        Also, on $\{\tau\leq t\}$, it holds $X^\tau_{t}=X_{\tau\wedge t}\geq \lambda$.
        Hence,

        \[
        \begin{equation*}
           X_{\tau\wedge t}=X_{\tau}1_{\{\overline{X}_t\geq \lambda\}}+X_t1_{\{\tau>t\}}\geq \lambda 1_{\{\overline{X}_t\geq \lambda\}}+X_t1_{\{\tau>t\}}.
        \end{equation*}
        \]

        It also holds, $X_t1_{\{\tau>t\}}\geq -X_t^-$.
        Altogether, with Doob's optional sampling theorem and $X$ being a sub-martingale, we get

        \[
        \begin{align*}
           E\left[ X_t \right]  & = E\left[ E\left[X_t |\mathcal{F}_{t\wedge \tau} \right] \right]\\
                                & \geq E\left[ X_{\tau\wedge t} \right]\\
                                & \geq \lambda P\left[ \overline{X}_t\geq \lambda \right]+E\left[ 1_{\{\tau>t\}} X_t\right]\\
                                & \geq \lambda P\left[ \overline{X}_t\geq \lambda \right]-E\left[ X_t^- \right],
        \end{align*}
        \]

        and conclude the first inequality by observing that, on the one hand, $E[X_t^+]=E[X_t]+E[X_t^-]$, and on the other hand,

        \[
        \begin{equation*}
           E[X_t]-E\left[ 1_{\{\tau>t\}} X_t\right]=E[(1- 1_{\{\overline{X}_t<\lambda\}}) X_t]=E[1_{\{\overline{X}_t\geq \lambda \}}X_t].
        \end{equation*}
        \]

        As for the second inequality, for the stopping time $\sigma=\inf\{s: X_s\leq -\lambda\}$, observe that $\{\sigma\leq t\}=\{\underline{X}_t\leq -\lambda\}$.
        Also, on $\{\sigma\leq t\}$, it holds $X^\sigma_{t}=X_{\sigma\wedge t}\leq -\lambda$.
        Hence,

        \[
        \begin{equation*}
           X_{\sigma\wedge t}=X_{\sigma}1_{\{\underline{X}_t\leq -\lambda\}}+X_t1_{\{\sigma>t\}}\leq -\lambda 1_{\{\underline{X}_t\leq -\lambda\}}+X_t1_{\{\sigma>t\}}.
        \end{equation*}
        \]

        Altogether, with Doob's optional sampling theorem and $X$ being a sub-martingale, we get

        \[
        \begin{equation*}
           E\left[ X_0 \right]\leq E\left[ X_{\sigma\wedge t} \right]\leq -\lambda P\left[ \underline{X}_t \leq -\lambda\right]+E\left[ 1_{\{\sigma>t\}} X_t \right]\leq -\lambda P\left[ \underline{X}_t \leq -\lambda\right]+E\left[ X_t^+ \right]
        \end{equation*}
        \]

        showing the second inequality by observing that $E[1_{\{\sigma>t\}}X_t]=E[1_{\{\underline{X}_t>-\lambda\}}X_t]$.

    2. Define the random variables $Y=\sup_{s\leq t}X_s$ and $Z=X_t=X_t^+$ since $X$ is positive.
        For $\varphi$ an increasing, right-continuous function with $\varphi(0)=0$, by Fubini's theorem and the previous inequalities, it holds

        \[
        \begin{align*}
           E\left[ \varphi(Y) \right] & = E\left[ \int_{0}^\infty 1_{\{\lambda \leq Y\}}d\varphi(\lambda) \right]\\
                                      & = \int_{0}^\infty P\left[ Y\geq \lambda \right]d\varphi(\lambda)\\
                                      & \leq \int_0^\infty E\left[1_{\{Y\geq \lambda\}}Z\right]\frac{d\varphi(\lambda)}{\lambda}\\
                                      & = E\left[ Z \int_0^\infty 1_{\{Y\geq \lambda\}}\frac{d\varphi(\lambda)}{\lambda} \right].
        \end{align*}
        \]

        If we consider $\varphi(\lambda)=\lambda^p$, $p>1$, and define $q=p/(p-1)$ for which holds $1/p+1/q=1$, it follows from Hölder's inequality that

        \[
        \begin{equation*}
           \left\Vert Y\right\Vert_p^p\leq pE\left[ Z \int_0^\infty 1_{\{Y\geq \lambda\}}\lambda^{p-2}d\lambda \right]=\frac{p}{p-1}E\left[ Z Y^{p-1} \right]\leq q \left\Vert Z\right\Vert_p \left\Vert Y^{p-1}\right\Vert_q=q \left\Vert Z\right\Vert_p \left\Vert Y\right\Vert_p^{p/q}.
        \end{equation*}
        \]

        If $0<\left\Vert Y\right\Vert^{p/q}_p<\infty$, dividing the inequality by $\left\Vert Y\right\Vert^{p/q}_p$, noting that $p-p/q =1$, yields

        \[
        \begin{equation*}
           \left\Vert\sup_{s\leq t}X_s\right\Vert_p=\left\Vert Y\right\Vert_p\leq q \left\Vert Z\right\Vert_p=q \left\Vert X_t\right\Vert_p,
        \end{equation*}
        \]

        as desired.


!!! corollary

    If $X$ is a martingale, and $p>1$, it holds

    \[
    \begin{equation}    
        \left\Vert X^\ast_t\right\Vert_p=E\left[ \left( \sup_{s\leq t}\left\vert X_s\right\vert \right)^p \right]^{1/p}\leq \left(\frac{p}{p-1}\right) \left\Vert X_t\right\Vert
    \end{equation}
    \]

!!! proof

    Follows immediately that $|X|$ is a sub-martingale and the doob's maximal inequalities.


!!! theorem "Martingale Convergence Theorem"

    Let $X$ be a martingale such that $\sup_{t}E[|X_t|^p]<\infty$ for some $p>1$.
    Then, there exists a random variable $X_{\infty}$ in $L^p$ such that $X_t \to X_{\infty}$ almost surely and in $L^p$.

!!! proof

    Since Jensen's inequality yields $E[X_t^+]\leq E[|X_t|]\leq E[|X_t|^p]^{\frac{1}{p}}$, it follows that $\sup E[X_t^+]<\infty$.
    By the $P$-almost sure martingale convergence Theorem, there exists an integrable random variable $X_{\infty}$ for which $X_t\to X_{\infty}$ almost surely.

    We are left to show that the sequence $|X_t-X_\infty|^p$ satisfies the assumptions of Lebesgue's dominated convergence.
    It holds

    \[
    \begin{equation*}
        |X_t -X_\infty|^p\leq c\left(| X_t|^p + |X_\infty|^p \right)\leq c\left(\sup |X_t|^p+|X_\infty|^p\right).
    \end{equation*}
    \]

    On the one hand, by Fatou's lemma we have $E[|X_\infty|^p]\leq\liminf E [|X_t|^p]<\infty$.
    On the other hand, by means of the previous corollary, it holds

    \[
    \begin{equation*}
        E[\sup_{s\leq t}|X_s|^p]\leq (p/(p-1))^p E[|X_t|^p]
    \end{equation*}
    \]

    showing that

    \[
    \begin{equation*}
        E[\sup|X_t|^p]=\sup_tE[\sup_{s\leq t}|X_s|^p]\leq (p/(p-1))^p\sup E[|X_t|^p]<\infty. 
    \end{equation*}
    \]

    Thus, the dominated convergence theorem yields $X_t\to X_\infty$ in $L^p$.

## Applications of $L^p$ Convergence, Law of Large Numbers

We apply the $L^p$-convergence of martingales to show the law of large numbers that states that the sample average of independently distributed random variables with finite mean converges almost surely to its mean.

!!! theorem

    Let $X$ be a square integrable martingale for which holds

    \[
    \begin{equation*}
        \sum E\left[ \left( X_t-X_{t-1} \right)^2 \right]<\infty.
    \end{equation*}
    \]

    Then, the sequence $(X_t)$ converges almost surely and in $L^2$.


!!! proof

    Beforehand, let us show the following lemma.

    !!! lemma
    
        Let $X$ be a martingale such that $X_t$ is square integrable for every $t$.
        It follows that
    
        \[
        \begin{align*}
            E\left[ \left( X_u-X_t \right)X_s \right] & =0,\\
            E\left[ \left( X_t-X_s \right)^2|\mathcal{F}_s \right]&=E\left[ X_t^2|\mathcal{F}_s \right]-X_s^2,
        \end{align*}
        \]
    
        for every $s\leq t\leq u$.
    
    !!! proof
    
        Since $s\leq t\leq u$ and $X$ is a square integrable martingale, it follows from the properties of the conditional expectation
    
        \[
        \begin{equation*}
            E\left[ \left( X_u-X_t \right)X_s \right]=E\left[ E\left[\left( X_u-X_t \right)X_s |\mathcal{F}_t\right]\right]=E\left[ E\left[\left( X_u-X_t \right) |\mathcal{F}_t\right]X_s\right]=0
        \end{equation*}
        \]
    
        showing the first equality.
        The same reasoning yields
    
        \[
        \begin{align*}
            E\left[ \left( X_t-X_s \right)^2 |\mathcal{F}_s\right] & = E\left[ X_t^2 |\mathcal{F}_s\right]-E\left[ X_tX_s|\mathcal{F}_s \right]-E\left[ (X_t-X_s)X_s|\mathcal{F}_s \right]\\
            & = E\left[ X_t^2 |\mathcal{F}_s\right]- X_sE\left[ X_t|\mathcal{F}_s \right]-X_sE\left[ X_t-X_s|\mathcal{F}_s \right]\\
            & = E\left[ X_t^2 |\mathcal{F}_s\right]- X_s^2,
        \end{align*}
        \]
    
        showing the second equality.

    For every $t$, by means of this lemma, it follows that

    \[
    \begin{align*}
        E\left[ X_t^2 \right] & = E\left[X_0^2\right]+\sum_{s=1}^tE\left[X_{s}^2-X_{s-1}^2\right]\\
                              & = E\left[X_0^2\right]+\sum_{s=1}^tE\left[E\left[X_{s}^2-X_{s-1}^2|\mathcal{F}_{s-1}\right]\right]\\
                              & = E\left[X_0^2\right]+\sum_{s=1}^tE\left[E\left[\left(X_{s}-X_{s-1}\right)^2|\mathcal{F}_{s-1}\right]\right]\\
                              & = E\left[X_0^2\right]+\sum_{s=1}^tE\left[\left(X_{s}-X_{s-1}\right)^2\right]\\
                              & \leq E\left[ X_0^2 \right]+\sum E\left[ \left( X_s-X_{s-1} \right)^2 \right].
    \end{align*}
    \]

    It follows that $\sup_{t}E\left[ X_t^2 \right]<\infty$ and therefore, by means of martingale convergence theorem, it follows that $X_t\to X_\infty$ almost surely and in $L^2$.

!!! theorem

    Let $X$ be a martingale and $a=(a_t)$ be an increasing sequence such that $a_t\to \infty$.
    If

    \[
    \begin{equation*}
        \sum E[(X_t-X_{t-1})^2/a_t^2]<\infty,
    \end{equation*}
    \]

    then it follows that

    \[
    \begin{equation*}
        \frac{X_t}{a_t}\longrightarrow 0 \quad \text{almost surely}
    \end{equation*}
    \]

    
    In particular, if $\sup E[(X_t-X_{t-1})^2]<\infty$, then it holds

    \[
    \begin{equation*}
        \frac{X_t}{t}\longrightarrow 0 \quad \text{almost surely}
    \end{equation*}
    \]


!!! proof

    Define the process $Y$ by $Y_0=0$ and $Y_t=\sum_{s=1}^t (X_s-X_{s-1})/a_s$ for $t\geq 1$.
    It follows that $Y$ is a martingale.
    Indeed, adaptiveness and integrability are immediate since $X$ is a martingale.
    As for the martingale property, it holds

    \[
    \begin{equation*}
        E\left[ Y_{t}-Y_{t-1} |\mathcal{F}_t\right]=\frac{1}{a_t}E\left[ X_t-X_{t-1}|\mathcal{F}_t \right]=0.
    \end{equation*}
    \]

    Furthermore, it holds

    \[
    \begin{equation*}
        \sum E\left[ \left( Y_t-Y_{t-1} \right)^2 \right]=\sum \frac{1}{a_t^2}E\left[ \left( X_t-X_{t-1} \right)^2 \right]<\infty
    \end{equation*}
    \]

    which by means of the previous Theorem implies that 

    \[
    \begin{equation*}
        Y_t=\sum_{s=1}^t\frac{X_s-X_{s-1}}{a_s}\longrightarrow Y_T=\sum \frac{X_t-X_{t-1}}{a_t}
    \end{equation*}
    \]

    almost surely and in $L^2$.
    The Kronecker's lemma states that if $\sum b_t/a_t<\infty$ for two sequences $(a_t)$ and $(b_t)$ whereby $(a_t)$ is an increasing sequence of strictly positive numbers, it follows that $(\sum b_t)/a_t=0$.
    Hence, applying Kronecker's lemma, it follows that

    \[
    \begin{equation*}
        \frac{X_t}{a_t}=\frac{1}{a_t}\sum_{s=1}^t X_s-X_{s-1}\to 0
    \end{equation*}
    \]

    almost surely.
    In particular, if $\sup E[(X_t-X_{t-1})^2]<\infty$ it follows that 


    \[
      \sum E[(X_t-X_{t-1})^2/t^2]\leq \sup E[(X_t-X_{t-1})^2]\sum \frac{1}{t^2}<\infty
    \]
    
    and the second assertion of the theorem follows.

!!! corollary

    Let $(X_t)$ be a sequence of integrable independent random variables such that $E[X_t]=0$ for every $t$ and such that $\sum E[X_t^2]/a_t^2<\infty$ for some increasing sequence $(a_t)$ of strictly positive real numbers such that $a_t\to \infty$.
    Then it holds

    \[
    \begin{equation*}
        \frac{1}{a_t}\sum_{s=1}^t X_s\longrightarrow 0 \quad \text{almost surely}
    \end{equation*}
    \]

!!! proof

    Define $\mathcal{F}_0=\{\emptyset,\Omega\}$ and $\mathcal{F}_t=\sigma(X_s\colon s\leq t)$ and the process $S$ by $S_0=0$ and $S_t=\sum_{s=1}^t X_s$.
    It follows that $S$ is a martingale.
    Indeed, it is integrable by assumption.
    It is furthermore adapted since $\mathbb{F}$ is the filtration generated by $X$.
    Finally due to the independence, it follows that

    \[
    \begin{equation*}
        E\left[ S_t-S_{t-1} |\mathcal{F}_{t-1}\right]=E\left[ X_t|\mathcal{F}_{t-1} \right]=E\left[ X_t \right]=0.
    \end{equation*}
    \]

    Furthermore, since

    \[
    \begin{equation*}
        \sum \frac{1}{a_t^2}E\left[ \left( S_t-S_{t-1} \right)^2 \right]=\sum \frac{1}{a_t^2}E\left[ X_t^2 \right]<\infty,
    \end{equation*}
    \]

    Applying the previous theorem yields

    \[
    \begin{equation*}
        \frac{S_t}{a_t}=\frac{1}{a_t}\sum_{s=1}^t X_s\longrightarrow 0 \quad \text{almost surely}
    \end{equation*}
    \]
!!! theorem "Theorem: Strong Law of Large Numbers"

    Let $(X_t)$ be a sequence of integrable, independent, and identically distributed random variables.
    Then it holds

    \[
    \begin{equation*}
        \frac{1}{t}\sum_{s=1}^t X_s\xrightarrow[t \to \infty]{\text{almost surely}}E\left[ X_1 \right].
    \end{equation*}
    \]

!!! note 

    Note that we do not make here the traditional assumption that the sequence shall be square integrable.

!!! proof

    **Step 1:** Define first the countable family $(A_t)$ as $A_t=\{ |X_t|>t\}$ of events in $\mathcal{F}$.
    Using the fact that $X_t\sim X_1$ for every $t$ and Fubini's Theorem, it holds

    \[
    \begin{equation*}
        \sum P\left[ A_t \right]=\sum P\left[ |X_t|>t \right]=\sum P\left[ |X_1|>t \right]\leq \int_{0}^\infty P\left[ |X_1|>\lambda \right]d\lambda=E\left[ |X_1| \right]<\infty.
    \end{equation*}
    \]

    By Borel-Cantelli, it follows that $P[\limsup A_t]=0$ and therefore, for almost all $\omega$ in $\Omega$, there exists $t_0(\omega)$ such that $\omega$ does not belong to $A_t$ for every $t\geq t_0$.
    Hence, defining $Y_t=X_t1_{A_t^c}$, it follows that 

    \[
    \begin{equation*}
        \liminf \frac{1}{t}\sum_{s\leq t} X_s=\liminf \frac{1}{t}\sum_{s\leq t}  Y_s\quad \text{as well as}\quad \limsup \frac{1}{t} \sum_{s\leq t}X_s=\limsup \frac{1}{t}\sum_{s\leq t} Y_s,
    \end{equation*}
    \]

    and so we just have to show that

    \[
    \begin{equation*}
        \frac{1}{t}\sum_{s\leq t} Y_s\xrightarrow[t \to \infty]{\text{almost surely}} E\left[ X_1 \right].
    \end{equation*}
    \]

    **Step 2:** Let $Z_t=Y_t-E[Y_t]$ for every $t$ which is an independent sequence of random variables.
    Furthermore, note that

    \[
    \begin{equation*}
        \sum \frac{E[Z_t^2]}{t^2}=\sum \frac{E\left[ (Y_t-E[Y_t])^2 \right]}{t^2}=\sum \frac{E\left[ Y_t^2 \right]-E\left[ Y_t \right]^2}{t^2}\leq \sum \frac{E[Y_t^2]}{t^2}.
    \end{equation*}
    \]

    By Fubini's theorem, and the fact that $P[|Y_t|>s]=P[|Y_t|>t]=0$ for every $s\geq t$ as well as $P[Y_t>\lambda ]\leq P[X_t>\lambda]=P[X_1>\lambda]$ for every $t$, it holds

    \[
    \begin{equation*}
        E\left[ Y_t^2 \right]=E\left[ \int_{0}^\infty 1_{\{|Y_t|>\lambda\}}2\lambda d\lambda \right]=\int_{0}^\infty P\left[ |Y_t|>\lambda \right]2\lambda d\lambda \leq\int_{0}^t P\left[ |X_1|>\lambda \right]2\lambda d\lambda.
    \end{equation*}
    \]

    The monotone convergence of Lebesgue yields

    \[
    \begin{equation*}
        \sum \frac{1}{t^2}\int_{0}^t P\left[ |X_1|>\lambda \right]2\lambda d\lambda=\int_{0}^\infty \sum \frac{1_{\{t\geq \lambda\}}}{t^2}P\left[ |X_1|>\lambda \right]2\lambda d\lambda.
    \end{equation*}
    \]

    - For $\lambda <1$, it holds

        \[
        \begin{equation*}
          2 \lambda \sum \frac{1}{t^2}=2\lambda\frac{\pi^2}{6}\leq 4\lambda\leq 4.
        \end{equation*}
        \]

    - For $\lambda\geq 1$, it holds

        \[
        \begin{equation*}
          2\lambda \sum_{t\geq \lambda}\frac{1}{t^2}\leq \frac{2}{\lambda}+2\lambda\int_{\lambda}^\infty \frac{1}{x^2}dx\leq 2+2\lambda \frac{1}{\lambda}=4.
        \end{equation*}
        \]

    Hence,

    \[
    \begin{equation*}
        \sum \frac{E\left[ Z_t^2 \right]}{t^2}\leq 4 \int_0^\infty P\left[ |X_1|>\lambda \right]d\lambda=4E\left[ |X_1| \right]<\infty.
    \end{equation*}
    \]

    According to the previous corollary, it follows that $(\sum_{s\leq t} Z_s)/t\to 0$ almost surely.

    **Step 3:** We finally show that $(\sum_{s\leq t} Y_s)/t\to E[X_1]$ almost surely.
    It holds

    \[
    \begin{align*}
        \left| \frac{1}{t}\sum_{s\leq t}Y_s-E[X_1]\right|
            & \leq \left| \frac{1}{t} \sum_{s\leq t}Z_s\right|+\frac{1}{t}\sum_{s\leq t}\left|E\left[Y_s  \right]-E\left[ X_s \right]\right|\\
            & = \left| \frac{1}{t} \sum_{s\leq t}Z_s\right|+\frac{1}{t}\sum_{s\leq t}\left|E\left[X_s1_{\{|X_s|\leq s\}}  \right]-E\left[ X_s \right]\right|\\
            & \leq \left| \frac{1}{t} \sum_{s\leq t}Z_s\right|+\frac{1}{t}\sum_{s\leq t}E\left[|X_s|1_{\{|X_s|> s\}}  \right]\\
            & = \left| \frac{1}{t} \sum_{s\leq t}Z_s\right|+\frac{1}{t}\sum_{s\leq t}E\left[ |X_1|1_{|X_1|>s} \right]\\
            & =\left| \frac{1}{t} \sum_{s\leq t}Z_s\right|+E\left[|X_1|\frac{1}{t}\sum_{s\leq t} 1_{\{|X_1|>s\}}\right]\\
            & =I_t+E[J_t].
    \end{align*}
    \]

    We already shown in the previous step that $I_t\to 0$ almost surely.
    On the other hand, it holds $J_t\leq |X_1|$ with $E[|X_1|]<\infty$ and since $(\sum_{s\leq t} 1_{\{|X_1|>s\}})/t\to 0$ almost surely, it follows that $J_t\to 0$ almost surely.
    Hence, by Lebesgue's dominated convergence theorem, it follows that $E[J_t]\to 0$ which ends the proof.


## $L^1$ Convergence
The $L^1$-case is more delicate.
There we have to make use of uniform integrability in order to show similar results.

!!! theorem "Theorem: $L^1$-Martingale Convergence"

    Let $X$ be a sub-martingale bounded in $L^1$, that is, $\sup E[|X_t|]<\infty$ or equivalently $\lim E[X_t]>-\infty$.
    In particular, by almost sure martingale convergence Theorem, there exists $X_\infty \in L^1$ such that $X_t\to X_\infty$ almost surely.
    Then the following two assertions are equivalent:

    1. $X$ is uniformly integrable;
    2. $X_t\to X_{\infty}$ in $L^1$ and $E[ X_{\infty}|\mathcal{F}_t ]\geq X_t$ for every $t$.

!!! proof

    If $X_t\to X_\infty$ almost surely, uniform integrability of $X$ and $L^1$ convergence are equivalent by means of Uniform Integrability Theorem.
    In particular, by the sub-martingale property, for every event $A$ in $\mathcal{F}_t$, it holds that

    \[
    \begin{equation*}
        E[X_{\infty}1_A]=\lim_{s\geq t}E\left[ X_{s}1_A \right]\geq E[X_t1_A],
    \end{equation*}
    \]

    showing that (i) is equivalent to (ii).

The following corollaries are consequences of this theorem as well as uniform integrability properties.

!!! corollary 

    Let $X$ be a martingale.
    Then the following assertions are equivalent:

    * $X_t=E[\xi|\mathcal{F}_t]$ for some $\xi\in L^1$;
    * $X$ is uniformly integrable;
    * $X_{t}\to X_{\infty}$ in $L^1$.

    ------- 

    Let $\xi$ be an integrable random variable and $\mathcal{F}_\infty=\sigma(\cup \mathcal{F}_t)$.
    Then it follows that 

    \[
    \begin{equation*}
        X_t:=E[\xi|\mathcal{F}_t]\to X_{\infty}:=E[\xi|\mathcal{F}_{\infty}]
    \end{equation*}
    \]

    almost surely and in $L^1$.

!!! proof

    The proof is left as an exercise for the first part of the corollary.

    We show the second part.
    Clearly, $X$ is a martingale which is uniformly integrable.
    Hence, from the previous theorem, it converges to $X_\infty$ almost surely and in $L^1$.
    We are left to show that $X_{\infty}=E\left[ \xi|\mathcal{F}_{\infty} \right]$.
    Let 

    \[
    \mathcal{C}=\{A \in \mathcal{F}_{\infty}\colon E[X_{\infty}1_A]=E[\xi1_A]\}.
    \]

    For every $A \in\mathcal{F}_t$, it holds

    \[
    \begin{equation*}
        E[X_{\infty}1_A]=\lim E[X_t1_A]=\lim E\left[ E[\xi|\mathcal{F}_t]1_A \right]=E[\xi1_A],
    \end{equation*}
    \]

    showing that $\cup \mathcal{F}_t$ is in $\mathcal{C}$.
    Since $\mathcal{C}$ is clearly a $\lambda$-system, by Dynkin's Lemma, it follows that $\mathcal{C}$ contains $\mathcal{F}_{\infty}$, ending the proof.


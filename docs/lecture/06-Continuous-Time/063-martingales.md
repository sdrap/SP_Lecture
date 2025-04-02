# Martingales

The definition of (Super-/Sub-)Martingales does not change in the continuous time.
The martingale properties and theorems extend to the continuous time.
However, some restrictions have to be made in terms of path regularity.
Indeed, as mentioned earlier, the infinite amount of null sets that may add up has to be countably controlled.
!!! definition "Definition: Simple Processes"
    We denote by $\mathcal{S}$ the set of **simple predictable** processes $H$ of the form  

    \[
      H = H_0 1_{\{0\}} + \sum_{k=1}^n H_k 1_{(\tau_{k-1}, \tau_k]}
    \]

    for a finite sequence $0 = \tau_0 \leq \tau_1 \leq \ldots \leq \tau_n$ of stopping times where $\tau_n<\infty$, and $H_k$ is bounded and $\mathcal{F}_{\tau_{k-1}}$ measurable for $k = 0, \dots, n$.

For a progressive process $X$ and $H \in \mathcal{S}$, we denote by $\int H d X$ the process

\[
\int H dX := H_0 X_0 + \sum_{k=1}^n H_k \left( X^{\tau_k} - X^{\tau_{k-1}} \right)
\]

which is the simple definition of a stochastic integral of $H$ with respect to $X$.

!!! theorem
    Let $X$ be a càd stochastic process and $H$ be a simple process.
    The following assertions hold true.

    1. If $X$ is a martingale and then $\int H d X$ is a martingale.
        If $X$ is a super/sub-martingale, and $H$ is positive then $\int Hd X$ is a super/sub-martingale.
        
        In particular, if $\tau$ is a bounded stopping time then $X^\tau$ is a martingale or super/sub-martingale, respectively.

    2. Let $X$ be a submartingale.
        For any $\lambda > 0$ it holds

        \[
        \begin{align*}
          \lambda P\left[ \overline{X}_t \geq \lambda \right] & \leq E\left[ 1_{\{\overline{X}_t < \lambda\}} X_t \right] \leq E\left[ X_t^+ \right]\\
          \lambda P\left[ \underline{X}_t \leq -\lambda \right] & \leq E\left[ 1_{\{\underline{X}_t > -\lambda\}} X_t \right] - E\left[ X_0 \right] \leq E\left[ X_t^+ \right] - E\left[ X_0 \right]
        \end{align*}
        \]


    3. Let $X$ be a positive submartingale and $p > 1$, it holds

        \[
          \left\Vert \sup_{s \leq t} X_s \right\Vert_p \leq \frac{p}{p-1} \left\Vert X_t \right\Vert_p
        \]


    4. Let $X$ be a submartingale.
        Then for every two reals $x < y$, the number of up-crossings of $(x,y)$ by $X$ up to time $t$, $U_{[0,t]}(x,y,X)$ is a random variable and it holds  

        \[
          (y - x) E\left[ U_{[0,t]}(x,y,X) \right] \leq E\left[ \left( X_t - x \right)^+ \right] - E\left[ \left( X_0 - x \right)^+ \right]
        \]

In particular, if $X$ is a càd martingale, and $p > 1$, then $|X|^p$ is a positive càd submartingale and therefore

\[
  \left\Vert X^\ast_t \right\Vert_p \leq \left( \frac{p}{p - 1} \right) \left\Vert X_t \right\Vert_p
\]

for every $p > 1$.

!!! proof
    The inequalities hold true if the process $X$ is sampled on any finite discretization of $[0,t]$ containing $0$ and $t$.
    Hence, passing to the limit, these inequalities hold for $([0,t] \cap \mathbb{Q}) \cup \{0,t\}$ and since the paths of $X$ are càd, the inequalities follow.

    The single thing to check is whether $U_{[0,t]}(x,y,X)$ is a well-defined random variable.
    However, for any finite $F \subseteq [0,t]$, since $X$ is right-continuous, the $\tau^k$ and $\sigma^k$ in the construction of $U_F(x,y,X)$ are stopping times according to the hitting times propositions for continuous processes.
    Therefore $U_F(x,y,X)$ is a random variable.
    It follows that $U_{([0,t] \cap \mathbb{Q}) \cup \{0,t\}}(x,y,X)$ is a random variable.
    Since $X$ is càd, this set takes into account all the up-crossings on $[0,t]$.

!!! theorem
    Any càd sub-martingale is càdlàg, and every sample path is almost surely bounded on any compact interval.

    Furthermore, $X$ is a submartingale with respect to $\mathbb{F}^+$ as well as with respect to the augmentation of $\mathbb{F}$.

!!! proof
    Let $X$ be a càd sub-martingale.
    The boundedness of the sample paths on any compact interval almost surely follows from the previous inequalities.
    As for the càdlàg property, define

    \[
      A = \bigcup_{n \in \mathbb{N}} \bigcup_{p,q \in \mathbb{Q}, p < q} \left\{U_{[0,n]}(p,q,X) = \infty \right\}
    \]

    By means of the up-crossing inequality, it follows that this countable union is of measure $0$.
    However, $A$ contains the set

    \[
    \left\{ \liminf_{s \nearrow t} X_s < \limsup_{s \nearrow t} X_s, \, \text{for some } \right\}
    \]

    Hence $X$ is càdlàg.
    The fact that $X$ is a supermartingale with respect to $\mathbb{F}^+$ is immediate.
    As for the augmentation, observe that null sets do not modify the supermartingale inequalities.

As noticed, the up-crossing inequality shows that sub-martingales have some nice regularity of paths.
However, we assumed from the beginning that these sub-martingales were right-continuous, central to derive Doob's maximal inequalities.
Let us show that up to modification, any sub-martingale has nice properties, however in the right-continuous filtration or in a filtration satisfying the usual conditions.

!!! theorem
    Let $X$ be a sub-martingale, then the following holds true.

    1. Almost surely, the limits  

        \[
        X_{t+} = \lim_{q \searrow t} X_q \quad \text{and} \quad X_{t-} = \lim_{q \nearrow t} X_q
        \]

        exist for every $t$ and thereby define two processes $X_{+}$ and $X_{-}$, respectively.

    2. The process $X_{+}$ is a $\mathbb{F}^+$ sub-martingale and is a martingale if $X$ is.
        Analogously, the process $X_{-}$ is a $\mathbb{F}^-$ submartingale and is a martingale if $X$ is.
        Furthermore  

        \[
        \begin{align*}
            X_t     & \leq E\left[ X_{t+} \,\big|\, \mathcal{F}_{t} \right]\\
            X_{t-}  & \leq E\left[ X_t \,\big|\, \mathcal{F}_{t-} \right]
        \end{align*}
        \]

        with equality in the first if $t \mapsto E[X_t]$ is right-continuous, and equality in the second if $t \mapsto E[X_t]$ is left-continuous.
        In particular, equality holds in both if $X$ is a martingale.

!!! proof
    1. Unlike in the previous proof we can only estimate the up-crossing of $X$ over a countable bounded interval.
        Define  

        \[
        A = \bigcup_{n \in \mathbb{N}} \bigcup_{p < q,\, p,q \in \mathbb{Q}} \left\{ \omega \in \Omega : U_{[0,n] \cap \mathbb{Q}}(p,q,X(\omega)) = \infty \right\}
        \]

        This set is of measure $0$.
        Hence, with the same argumentation as in the previous proof, it follows that

        \[
        \begin{align*} 
          P\left[ \liminf_{q \nearrow t, q \in \mathbb{Q}} X_q < \limsup_{q \nearrow t, q \in \mathbb{Q}} X_q  \text{ for some } t \right] & = 0\\
          P\left[ \liminf_{q \searrow t, q \in \mathbb{Q}} X_q < \limsup_{q \searrow t, q \in \mathbb{Q}} X_q  \text{ for some } t \right] & = 0
        \end{align*}
        \]

        We can then define the processes $X_{-}$ and $X_{+}$ by

        \[
          X_{t+} = \lim_{q \searrow t} X_q, \quad \text{ and } \quad X_{t-} = \lim_{q \nearrow t} X_q
        \]

        with the conventions that $X_{0-} = X_0$.

    2. Clearly $X_{+}$ and $X_{-}$ are $\mathbb{F}^+$- and $\mathbb{F}^-$-adapted processes, respectively.
        Let us show that they are integrable and satisfy the sub-martingale property.
        Let $(q_n) \subseteq \mathbb{Q}$ be a sequence decreasing to $t$.
        From the previous step, $X_{q_n}$ converges $P$-almost surely to $X_{t+}$.
        Further, $E[X_t] \leq E[X_{q_n}] \leq E[X_{q_0}]$ for every $n$, so $(X_{q_n})$ is uniformly bounded in $L^1$, and $E[X_{q_n}]$ is a decreasing sequence converging to $\lim E[X_{q_n}] > E[X_t] > -\infty$.
        Hence, for $\lambda > 0$ and $\varepsilon > 0$, let $n_0$ be such that $E[X_{q_n}] \geq E[X_{q_{n_0}}] - \varepsilon$ for every $n \geq n_0$.
        As $X$ is a submartingale, it follows that  

        \[
        \begin{align}
        E\left[ |X_{q_n}| 1_{\{ |X_{q_n}| > \lambda \}} \right] 
          &= E\left[ X_{q_n} 1_{\{ X_{q_n} > \lambda \}} \right] - E\left[ X_{q_n} 1_{\{ X_{q_n} < -\lambda \}} \right] \\
          &= E\left[ X_{q_n} 1_{\{ X_{q_n} > \lambda \}} \right] - E[X_{q_n}] + E\left[ X_{q_n} 1_{\{ X_{q_n} \geq -\lambda \}} \right] \\
          &\leq E\left[ X_{q_{n_0}} 1_{\{ X_{q_n} > \lambda \}} \right] + \varepsilon - E[X_{q_{n_0}}] + E\left[ X_{q_{n_0}} 1_{\{ X_{q_n} \geq -\lambda \}} \right] \\
          &= E\left[ X_{q_{n_0}} 1_{\{ X_{q_n} > \lambda \}} \right] - E\left[ X_{q_{n_0}} 1_{\{ X_{q_n} < -\lambda \}} \right] + \varepsilon \\
          &\leq E\left[ |X_{q_{n_0}}| 1_{\{ |X_{q_n}| > \lambda \}} \right] + \varepsilon
        \end{align}
        \]

        By Markov's inequality, $P[|X_{q_n}| > \lambda] \leq \sup_n E[|X_{q_n}|]/\lambda = C/\lambda$ for some $C < \infty$, showing that $(X_{q_n})$ is uniformly integrable.
        Together with $P$-almost sure convergence, it follows that $X_{q_n} \to X_{t+}$ in $L^1$.
        Thus $X_{t+}$ is integrable and it holds

        \[
          X_t \leq \lim E\left[ X_{q_n} \,\big|\, \mathcal{F}_t \right] = E\left[ X_{t+} \,\big|\, \mathcal{F}_t \right]
        \]

        Further, for $s < t$ and $q_n \searrow s$ with $q_n < t$, it holds  

        \[
          X_{q_n} \leq E\left[ X_t \,\big|\, \mathcal{F}_{q_n} \right] \leq E\left[ E\left[ X_{t+} \,\big|\, \mathcal{F}_t \right] \,\big|\, \mathcal{F}_{q_n} \right] = E\left[ X_{t+} \,\big|\, \mathcal{F}_{q_n} \right]
        \]

        for every $n$.
        The same arguments as above show that $E\left[ X_{t+} \,\big|\, \mathcal{F}_{q_n} \right]$ is uniformly integrable and converges $P$-almost surely and in $L^1$, and that the limit is $E\left[ X_{t+} \,\big|\, \mathcal{F}_{s+} \right]$.
        Thus $X_{+}$ is a $\mathbb{F}^+$-submartingale.  
        Finally, if $t \mapsto E[X_t]$ is right-continuous, it follows that $E[X_{t+}] = \lim E[X_{q_n}] = E[X_t]$.  
        Hence, the positive random variable $X_t - E[X_{t+} \,|\, \mathcal{F}_t]$ has zero expectation and therefore is zero.

        As for the case of $X_{-}$, a similar argumentation holds using the submartingale convergence theorem for the existence and integrability of $X_{t-}$ and inequality  

        \[
          X_{t-} \leq E[X_t \,|\, \mathcal{F}_{t-}]
        \]

        Furthermore, by $X_{s-} \leq E[X_s \,|\, \mathcal{F}_{s-}] \leq E[E[X_{t-} \,|\, \mathcal{F}_s] \,|\, \mathcal{F}_{s-}] = E[X_{t-} \,|\, \mathcal{F}_{s-}]$ it follows that $X$ is a $\mathbb{F}^-$ submartingale.

        The equality if $t \mapsto E[X_t]$ is left-continuous follows by an analogous argumentation.


!!! theorem
    Let $X$ be a supermartingale with respect to a filtration satisfying the usual assumptions.
    Suppose further that $t \mapsto E[X_t]$ is càd.
    Then $X$ has a càdlàg modification.

!!! proof
    According to the previous theorem, set $Y = X_{+}$ outside the negligible set $A$ up to which $X_{+}$ and $X_{-}$ are defined, and $Y = 0$ on $A$.
    Since $A \in \mathcal{F}_0$, it follows that $Y$ is càdlàg.
    Furthermore, from $t \mapsto E[X_t]$ right-continuous, by the previous theorem it holds that

    \[
    X_t = E[X_{t+} \,|\, \mathcal{F}_t] = E[Y_t \,|\, \mathcal{F}_t]
    \]

    However, since $\mathbb{F}$ is right-continuous, it follows that $Y_t$ is $\mathcal{F}_t$-measurable and so $X_t = Y_t$ almost surely for every $t$.


# Doob-Meyer Decomposition

We already saw in discrete time that any process can be decomposed into the sum of a martingale and a predictable process.
In particular if $X$ is a sub-martingale, the predictable process is increasing.
The proof is relatively straightforward, and one wonders whether it still holds in continuous time.
It turns out that this is way more involved.
In this section, we do not assume continuity of processes.


!!! definition "Definition: Natural Processes"
    An increasing process $A$ is called **natural** if for every bounded right-continuous martingale $M$ and any $t$ it holds

    \[
      E\left[\int_0^t M_s \, dA_s\right] = E\left[ \int_0^t M_{s-} \, dA_s \right]
    \]

!!! remark
    Note that every increasing and continuous process is automatically natural.
    Indeed  

    \[
      \int_0^t (M_s - M_{s-}) \, dA_s = 0
    \]

    almost surely, since every path $s \mapsto M_s$ has only countably many discontinuities and therefore is a set of $dA$-zero measure.

!!! lemma
    The condition for an increasing process to be natural is equivalent to  

    \[
    E\left[ M_t A_t \right] = E\left[ \int_0^t M_{s-} \, dA_s \right]
    \]

!!! proof
    It suffices to show that

    \[
    E[M_t A_t] = \int_0^t M_s \, dA_s.
    \]

    Let $0 = t_0 < t_1 < \cdots < t_n = t$ and define  

    \[
      M^n = \sum_{k=1}^n M_{t_k} 1_{(t_{k-1}, t_k]}.
    \]

    By the martingale property, it follows that  

    \[
    \begin{align}
    E\left[ \int_0^t M^n_s \, dA_s \right] 
      & = \sum_{k=1}^n E\left[ M_{t_k} (A_{t_k} - A_{t_{k-1}}) \right] \\
      & = E[M_t A_t] - \sum_{k=1}^{n-1} E\left[ A_{t_k} (M_{t_{k+1}} - M_{t_k}) \right]\\
      & = E[M_t A_t].
    \end{align}
    \]

    letting the mesh of the subdivision to $0$, yields $M^n \to M$ $P$-almost surely, and by dominated convergence, the claim follows.

Natural processes are the natural pendant to predictable processes in discrete time.

!!! lemma
    In the discrete time context, an increasing process is natural if and only if it is predictable and integrable.

!!! proof
    If an increasing process is predictable and integrable, then clearly it is natural.
    Reciprocally, define the bounded positive martingale $M_s = E[1_B \,|\, \mathcal{F}_s]$ where  

    \[
      B = \{ A_t - E[A_t \,|\, \mathcal{F}_{t-1}] > \varepsilon \}.
    \]

    From $A$ being natural, it holds  

    \[
      E[M_t A_t] = E\left[ \int_0^t M_{s-} \, dA_s \right] = \sum_{1 \leq s \leq t} E\left[ M_{s-1} (A_s - A_{s-1}) \right]
    \]

    for every $t = 1, \ldots$.
    Hence, per induction, it holds  

    \[
    \begin{align}
      0 & = E[(M_t - M_{t-1}) A_t] \\
        & = E[1_B A_t] - E[E[1_B \,|\, \mathcal{F}_{t-1}] A_t] \\
        & \geq \varepsilon P[B] + E[1_B E[A_t \,|\, \mathcal{F}_{t-1}]] - E[1_B E[A_t \,|\, \mathcal{F}_{t-1}]] \\
        & = \varepsilon P[B].
    \end{align}
    \]

    showing that $P[B] = 0$.
    The same holds for $B = \{ A_t - E[A_t \,|\, \mathcal{F}_{t-1}] < -\varepsilon \}$, showing that  

    \[
      A_t = E[A_t \,|\, \mathcal{F}_{t-1}].
    \]

As in the discrete time where a predictable martingale is uniformly constant, the same holds for natural martingales.

!!! proposition
    Let $M$ be a càd martingale which can be written as the difference between two natural increasing processes.
    Then $M$ is indistinguishable from $0$.

!!! proof
    By the identity

    \[
      E[X_t M_t] = E\left[ \int_0^t X_{s-} \, dM_s \right]
    \]

    for every càdlàg bounded martingale $X$, consider the approximation

    \[
    X^n = \sum_{k=1}^n X_{t_{k-1}} 1_{[t_{k-1}, t_k)} + X_t 1_{\{t\}}
    \]

    over a subdivision $0 = t_0 < t_1 < \cdots < t_n = t$, which satisfies  

    \[
      X^n_{-} = X_0 1_{\{0\}} + \sum_{k=1}^n X_{t_{k-1}} 1_{(t_{k-1}, t_k]}.
    \]

    Hence, by the martingale property of $M$ it holds  

    \[
      E\left[ \int_0^t X^n_{s-} \, dM_s \right] = E\left[ \sum_{k=1}^n X_{t_{k-1}} (M_{t_k} - M_{t_{k-1}}) \right] = 0.
    \]

    Letting the mesh of the subdivision to $0$, dominated convergence yields

    \[
      E[X_t M_t] = E\left[ \int_0^t X_{s-} \, dA_s \right] = 0.
    \]

    Let $X = E[1_A \,|\, \mathcal{F}_\cdot]$ where $A = \{M_t > \varepsilon\}$.
    Then $X$ is a bounded martingale, and up to a modification, it is càdlàg.
    It follows that

    \[
      0 = E[X_t M_t] = E[1_A M_t] \geq \varepsilon P[A]
    \]

    so $P[A] = 0$.  
    The same holds for $A = \{M_t < -\varepsilon\}$, showing that $M_t = 0$.  
    Since both $M$ and $0$ are càdlàg, this implies indistinguishability.

We can now address the Doob-Meyer decomposition.

!!! definition
    A càd process $X$ is said to belong to class:

    - **(D)** if the collection $\{X_\tau : \tau \text{ stopping time}, \tau < \infty\}$ is uniformly integrable
    - **(DL)** if the collections $\{X_\tau : \tau \text{ stopping time}, \tau < t\}$ are uniformly integrable for every $t$

!!! theorem "Doob-Meyer Decomposition"
    Let $X$ be a càdlàg sub-martingale of class (DL).
    Then $X$ can be decomposed uniquely &mdash; up to indistinguishability &mdash; into

    \[
      X = M + A
    \]

    where $M$ is a càdlàg martingale and $A$ is a natural increasing process.
    If furthermore, $X$ is of class (D), then $M$ is uniformly integrable and $A$ is integrable.

The proof relies on a deep functional analysis result describing the relatively compacts subsets of $L^1$.

!!! theorem "Dunford-Pettis's Theorem"
    A subset of $L^1$ is $\sigma(L^1, L^\infty)$-relatively compact if and only if it is uniformly integrable.

We do not address the proof of this theorem which involves functional analysis arguments.

Remember that we use the notation $E[\xi \colon A] := E[X 1_A]$.

!!! proof "Proof of Doob-Meyer Decomposition"

    1. **Uniqueness:** Set $X = M + A = M' + A'$.
       It follows that $A - A' = M - M'$ is a càdlàg martingale which is the difference of two increasing natural processes.
       From the previous proposition, $A - A' = M - M'$ is indistinguishable from $0$, hence the uniqueness.

    2. **Decomposition along a discrete partition:**
        Fix $T$ and consider the process on $[0,T]$.
        Assume without loss of generality that $X_0 = 0$ and use the dyadic partitions $\Pi^n = \{t_k^n = kT / 2^n : k = 0, \ldots, 2^n\}$, and $\Pi = \cup \Pi^n$.
        Define

        \[
        A_t^n =
          \begin{cases}
            0 & \text{if } t =0 \\
            \sum_{j=0}^{k-1} E[\Delta_j^n X \,|\, \mathcal{F}_{t_j^n}] & \text{if } t_k^n < t \leq t_{k+1}^n,\; k=1,\ldots,2^n-1
          \end{cases}
        \]

        where we use the notation $\Delta_k^n Y = Y_{t_{k+1}^n} - Y_{t_k^n}$.
        In other terms

        \[
          A^n = \sum_{k=0}^{2^n-2} E[\Delta_k^n X \,|\, \mathcal{F}_{t_k^n}] 1_{[t_k^n, t_{k+1}^n)} +  E[\Delta_{2^{n-1}}^n X \,|\, \mathcal{F}_{t_{2^n-1}^n}] 1_{\{T\}}
        \]

        This defines a càg, piecewise constant, increasing process $A^n$.
        Define $M^n = X - A^n$, so that $X = M^n + A^n$.
        Since $X$ is a sub-martingale, $M^n$ is a martingale on $\Pi^n$.

    3. **Convergence of $(A_T^n)$:**
        For $\lambda > 0$, define the stopping time $\tau_\lambda^n = \inf\{t \colon A_t^n > \lambda\} \wedge T$.
        Since $A^n$ is increasing, càg and piecewise constant over $\Pi^n$, it follows that $\tau_\lambda^n$ takes values in $\Pi^n$ and on $\{\tau^n_{\lambda}<T\}$ it holds that $A_{\tau^n_\lambda}^n \leq \lambda$.
        From optional sampling we have

        \[
        \begin{align}
            E[A_T^n \, \colon \, A_T^n > \lambda]
              & = E[A_T^n - A_{\tau_\lambda^n} \, \colon \, \tau^n_\lambda <T] + E[A_{\tau_\lambda^n}^n \, \colon \, A_T^n >\lambda ]\\
              & = E[X_T - X_{\tau_\lambda^n} \, \colon \, \tau^n_\lambda <T] - \underbrace{E[M^n_T - M^n_{\tau^n_\lambda} \, \colon \, \tau^n_\lambda<T]}_{=0 \text{ Doob optional sampling}} + E[A_{\tau_\lambda^n}^n \, \colon \, A_T^n >\lambda]\\
            &\leq E[X_T^n - X_{\tau_\lambda^n }^n \, \colon\, \tau_\lambda^n < T] + \lambda P[A_T^n>\lambda]
        \end{align}
        \]
        
        On the other hand, for $\tau^n_{\lambda/2}$ with the same doob's optional sampling arguments we get

        \[
          \begin{align*}
             2E[X_T^n - X_{\tau_{\lambda/2}^n \wedge T}^n \, \colon \tau_{\lambda/2}^n < T] 
                & = 2 E[A_T^n -A_{\tau^n_{\lambda/2}} \colon A_T^n\geq \lambda/2]\\
                & \geq 2 E[A_T^n -A_{\tau^n_{\lambda/2}} \colon A_T^n\geq \lambda ]\\
                & \geq \lambda P[A_T^n > \lambda]\\
          \end{align*}
        \]

        Combining both, we get:

        \[
          E[A_T^n \, \colon \, A_T^n > \lambda] \leq E[X_T - X_{\tau_\lambda^n} \, \colon\, \tau_\lambda^n < T] + 2 E[X_T - X_{\tau_{\lambda/2}^n} \, \colon\, \tau_{\lambda/2}^n < T]
        \]

        Since $X$ is of class (DL), the families $(X_T - X_{\tau^n_\lambda})$ and $(X_T - X_{\tau^n_\lambda})$ are uniformly integrable.
        We therefore just need to show that $\{\tau_{\lambda/2}^n<T\}\supseteq \{\tau_\lambda^n\}$ can be made arbitrarily small in $\lambda$ uniformly in $n$ to show that $(A_T^n)$ is uniformly integrable.
        However, by Markov inequality, it holds that

        \[
          P[\tau_{\lambda/2}^n<T] = P[A_T^n > \lambda/2] \leq \frac{2}{\lambda}E[A_T^n]= \frac{2}{\lambda} E[X_T]
        \]

        Thus, $(A_T^n)$ is uniformly integrable.
        By Dunford-Pettis, up to a subsequence, $A_T^n$ converges weakly in $L^1$ to some $A_T$ in $L^1$, that is $E[\xi A_T^n] \to E[\xi A_T]$ for all $\xi$ in $L^\infty$.

    4. **Definition of the limit decomposition:**
        Define $M = E[X_T - A_T \,|\, \mathcal{F}_\cdot]$, a càdlàg martingale, and $A = X^T - M$.
        So $X = M + A$ on $[0,T]$.
        We just remained to show that $A$ is natural.
        Fix $t \in \Pi$, for $n$ large enough such that $t$ is in $\Pi^n$, it holds that for every $\xi$ in $L^\infty$:

        \[
          E[\xi(A_t^n - A_t)] = E[E[\xi \,|\, \mathcal{F}_t](M_t - M_t^n)] = E[E[\xi \,|\, \mathcal{F}_t](A_T^n - A_T)] \to 0
        \]

        Hence $A_t^n \to A_t$ in $\sigma(L^1, L^\infty)$.
        For any $s<t$ with $s$ and $t$ in $\Pi^n$, since $1_{\{A_t<A_s\}}$ is bounded, it holds

        \[
            0\geq E[(A_t-A_s)1_{\{A_t<A_s\}}] = \lim E[(A_t^n - A_s^n)1_{\{A_t<A_s\}}] \geq 0
        \]
        
        showing that $P[A_t\geq A_s] = 1$.
        Since $A$ is càdlàg, we deduce that $A$ is increasing.

        We are left to show that $A$ is natural.
        For a bounded càdlàg martingale $N$

        \[
          \begin{align}
            E[N_T A_T^n] &= E\left[ \int_0^T N_{s-} \, dA_s^n \right] \\
            &= \sum E[N_{t_k^n} \Delta_k^n A] + \sum E[N_{t_k^n} \Delta_k^n(M - M^n)] \\
            &\to E\left[ \int_0^T N_{s-} \, dA_s \right]
          \end{align}
        \]

        so $E[N_T A_T] = E\left[ \int_0^T N_{s-} \, dA_s \right]$, hence $A$ is natural on $[0,T]$.

    5. **Extension to $[0,\infty)$ and case (D):**
        By uniqueness, decompositions on $[0, T+n]$ for each $n$ are consistent, extending the result to $[0,\infty)$.
        If $X$ is of class (D), then $A_T^n$ are uniformly integrable, hence $A_T \in L^1$.
        Also, $\sup_t E[|X_t|] < \infty$ implies:

        \[
        E[M_t 1_{\{M_t > \lambda\}}] \leq E[(X_t - A_T) 1_{\{X_t - A_T > \lambda\}}]
        \]

        By Markov’s inequality and uniform integrability of $X_t - A_T$, $M$ is uniformly integrable.
In the following we will define the stochastic integral with respect to continuous martingale using the Doob-Meyer decomposition.
So one may think that if $X$ is continuous, then the Doob-Meyer decomposition is also continuous.
This is not straightforward a-priori, and is the subject of the following theorem.

!!! theorem
    Let $X$ be a càdlàg sub-martingale such that $E[X_{\tau^n}]\to E[X_\tau]$ for every increasing sequence of stopping times $(\tau^n)$ with $\sup \tau^n=\tau<T$ for some $T>0$.
    Then, the natural increasing process in the Doob-Meyer decomposition of $X$ is continuous.

??? proof
    To be updated

# American Options

So far, even if the outcome of European contingent claims may depend on the sequence of events previous to the maturity, the contract is settled for a given time horizon.
In *American type* of contingent claim, the buyer can claim the payoff at any time before the settlement.

!!! definition
    
    An *American contingent claim* is a non-negative adapted stochastic process:
    
    \[
    C=(C_t)_{0\leq t\leq T}.
    \]
    
    The value $C_t(\omega)$ represents the outcome that a buyer can claim if he/she exercises at time $t$ in state $\omega$.

!!! example

    The most classical example of American contingent claims are the American call and put options:
    
    \[
    C_t^{call}=\left( S_t^i-K \right)^+ \quad \text{and} \quad C_t^{put}=\left( K-S_t^i \right)^+,
    \]
    
    for $t=0,\ldots, T$.

!!! remark

    Note that a European contingent claim $C$ can be viewed as a special case of an American one.  
    Indeed, it would correspond to the stochastic process:
    
    \[
    C_t=
    \begin{cases}
    0 & \text{if } t=0,\ldots, T-1, \\\\
    C & \text{if } t=T.
    \end{cases}
    \]


## Hedging Capital for the Seller

We first consider the problem of a hedging strategy for the seller of an American contingent claim $C$.
Hereby, we denote by $H$ the discounted contingent process, that is:

\[
H_t=\frac{C_t}{B_t}, \quad t=0,\ldots, T.
\]

!!! warning
    We suppose throughout that the financial market is arbitrage-free and, even more, complete.
    This means there exists only one pricing measure $P^\ast$ equivalent to $P$.

We want to compute the minimal amount of capital $U_t$ that the seller at time $t$ should have in order to pay the buyer of the contingent claim in case this person exercises their claim.
We make this computation backward:

- **Time $T$**:
    Suppose that at time $T$, the buyer did not exercise its claim previously.
    Then the discounted amount of capital needed to satisfy the buyer is exactly:

    \[
    U_T=H_T
    \]

- **Time $T-1$**:
    Suppose that we are at time $T-1$. We face two situations.

    Either the buyer decides to exercise now, and we need at least:
  
    \[
    U_{T-1} \geq H_{T-1}
    \]
  
    Or it decides to wait another time period, and we have to hedge against the capital we need in the next period $U_T$.
    Since the market is complete with a value $E^{P^\ast}[U_T|\mathcal{F}_{T-1}]$ at time $T-1$ I can find a strategy $\boldsymbol{\eta}_T$ which will replicate $U_T$, that is

    \[
        E^{P^\ast}[U_T |\mathcal{F}_{T-1}] + \boldsymbol{\eta}_T\cdot \Delta \boldsymbol{X}_T = U_T
    \]

    It follows that the capital required today to hedge this case must be:

    \[
        U_{T-1} \geq E^{P^\ast}\left[ U_T |\mathcal{F}_{T-1} \right]
    \]

    Altogether, this means:
  
    \[
    U_{T-1} = \max\left\{ H_{T-1}, E^{\ast}\left[ U_T | \mathcal{F}_{T-1} \right] \right\} = H_{T-1} \vee E^{P^\ast}\left[ U_T | \mathcal{F}_{T-1} \right].
    \]

- **Time $t \leq T-1$**:
    The same argumentation means we have to reserve at least:
  
    \[
        U_t \geq H_t,
    \]
  
    as well as the minimum amount of capital $U_{t+1}$ needed from tomorrow in expectation under the pricing measure, that is:
  
    \[
    U_t \geq E^{P^\ast}\left[ U_{t+1} | \mathcal{F}_t \right].
    \]
  
    Altogether, it follows that:
  
    \[
    U_t = \max\left\{ H_t, E^{P^\ast}\left[ U_{t+1} | \mathcal{F}_t \right] \right\} = H_t \vee E^{P^\ast}\left[ U_{t+1} | \mathcal{F}_t \right].
    \]

This recursive scheme is called the *Snell Envelope*.

!!! definition "Definition: The Snell Enveloppe"

    Let $H$ be an adapted process, $P^\ast$-integrable.
    The Snell Envelope of $H$ is defined inverse recursively as follows:
    
    \[
    \begin{equation*}
        \begin{cases}
            U_T =H_T\\
            \\
            U_t=H_t \vee E^{P^\ast}\left[ U_{t+1} | \mathcal{F}_t \right] &\text{for } t=T-1,\ldots, 0.
        \end{cases}
    \end{equation*}
    \]

The Snell envelope satisfies the following inequality:

\[
\begin{align*}
   E^{P^\ast}\left[ U_{t+1} | \mathcal{F}_t \right] & \leq  H_t \vee E^{P^\ast}\left[ U_{t+1} | \mathcal{F}_t \right] \\
      & = U_t
\end{align*}
\]

Processes satisfying this inequality are called super-martingales:

!!! definition "Definition: Super/Sub Martingales"

    A process $X$ is called a $P^\ast$-super-martingale if:
    
    1. $X$ is adapted;
    2. $X$ is $Q$-integrable;
    3. $E^{P^\ast}[X_{t+1}|\mathcal{F}_t] \leq X_t$ for every $t=0,\ldots,T-1$.
    
    A process $X$ is called a $Q$-sub-martingale if $-X$ is a $Q$-super-martingale.


The Snell envelope is an example of $P^\ast$-super-martingale with particular property

!!! proposition

    Let $H$ be an adapted and $P^\ast$-integrable process.
    The Snell envelope $U$ of $H$ is a $P^\ast$-super-martingale and the smallest $P^\ast$-super-martingale among those dominating $H$.
    That is, if $V$ is a $P^\ast$ super-martingale such that $V_t \geq H_t$ for all $t$, then $V\geq U$.
    
!!! proof

    From the definition of $U$, it follows immediately that $U$ is a $P^\ast$-super-martingale.
    Let $V$ be another $P^\ast$-super-martingale such that $V_t \geq H_t$ for every $t$.
    By backward induction we show that $V_t \geq U_t$.

    * For $t = T$, by definition we have $V_T \geq H_T = U_T$

    * For $t = T-1$, we have
        * $V_{T-1} \geq H_{T-1}$ since $V$ dominates $H$
        * $V_{T-1}\geq E^{P^\ast}[V_T|\mathcal{F}_{T-1}] = E^{P^\ast}[U_T|\mathcal{F}_{T-1}]$ since $V$ is a super martingale and $V_T \geq U_T$.
        
        All together it follows that $V_{T-1}\geq H_{T-1}\vee E^{P^\ast}[U_T|\mathcal{F}_{T-1}] = U_{T-1}$.

    The argumentation follows the same logic for every other step.


!!! example

    Consider the CRR model where the American contingent claim is path-independent, that is:
    
    \[
    H_t = h_t(S_t),
    \]
    
    for some functions $h_t:\mathbb{R}\to \mathbb{R}$.
    This is particularly the case for American put and call options since $S^0$ does not depend on the states $\omega \in \Omega$.
    The American option scheme for the computation of the Snell envelope $U_t=u_t(S_t)$ reads as follows:
    
    \[
      u_T(x)=h_T(x), \quad \text{and} \quad u_t(x)= h_t(x) \vee \left( u_{t+1}(x(1+u) )p + u_{t+1}(x(1+d))(1-p) \right),
    \]
    
    for $t=0,\ldots, T-1$, where $p=(r-d)/(u-d)$.
   

## Execution Time for the Buyer

The buyer of an American claim is no longer a passive owner of a contract for which he waits until the end of the period the result of the outcome. He can also strategically decide in any state \(\omega\) to exercise its contract at a time \(\tau(\omega)\). In general, this stopping strategy is a set of conditions which triggered, yields the exercise of the claim. However the triggering conditions whether to stop or not at time \(t\) should only rely on the available information at time \(t\).

!!! definition
    A *stopping time* is a random variable \(\tau:\Omega \to \{0,1,\ldots, T\}\cup\{\infty\}\) such that $\{\tau =t\} = \{\omega \in \Omega\colon \tau(\omega)=t\}$ is in $\mathcal{F}_t$ for every \(0\leq t\leq T\).

In other terms, $\{ \tau=t\}$ represents the event on which the buyer will decide to exercise its American contingent claim.
The event $\{\tau=\infty\}$ represents the event where the triggering conditions have not been met before the time horizon, and therefore the buyer will exercise it at time \(T\).

!!! remark
    Note that the following facts hold true (see math suplement on processes):
    
    - *Deterministic times are stopping times:** The constant random variable \(\tau(\omega)=t\) for every \(\omega\) and a given \(t\) is a stopping time;
    - A random variable \(\tau:\Omega \to \{0,1,\ldots,T\}\) is a stopping time if and only if $\{\tau\leq t\}$ is in $\mathcal{F}_t$ for every \(t=0,\ldots, T\).
    - If \(\tau\) is a stopping time, then $\{t\leq \tau\} = \{\tau \leq t-1\}^c$ is in $\mathcal{F}_{t-1}$ for every \(t=1,\ldots, T\);
    - If \(\sigma\) and \(\tau\) are two stopping times, then so are \(\sigma \vee \tau\), \(\tau\wedge \sigma\). In particular $\tau \wedge t$.

!!! example
    Let \(S\) be an adapted process, for instance the price evolution of an asset.
    Given a threshold \(c\), the random variable

    \[
        \tau(\omega)=\inf\left\{ t\colon S_t(\omega)\geq c \right\}
    \]

    is a stopping time.

    ??? proof

        It holds that
    
        \[
          \begin{align*}
            \{\tau \leq t\} & = \left\{\omega \in \Omega\colon S_s(\omega) \geq c \text{ for some }0 \leq s\leq t\right\}\\
                            & = \underbrace{\cup_{s=0}^t \underbrace{\{S_s \geq t\}}_{\in \mathcal{F}_s \subseteq \mathcal{F}_t}}_{\in \mathcal{F}_t}
          \end{align*}
        \]

!!! definition
    Let \(S\) be a stochastic process and \(\tau\) a stopping time.
    We denote by \(S^\tau\) the stopped process

    \[
        \begin{equation*}
          S_t^\tau(\omega)=S_{t\wedge \tau(\omega)}(\omega) =
          \begin{cases}
            S_t(\omega) &\text{if }t< \tau(\omega)\\
            S_{\tau(\omega)}(\omega) & \text{if }\tau(\omega)\leq t
          \end{cases}
        \end{equation*}
    \]

    ![Stopped](./../../images/stopping_dark.svg#only-dark)
    ![Stopped](./../../images/stopping_white.svg#only-light)

!!! theorem "Theorem: Doob's Optional Sampling"
    Let \(M\) be an adapted process and \(Q\) a probability measure such that \(M_t\) is \(Q\)-integrable for all \(t=0,\ldots,T\). The following assertions are equivalent:

    1. \(M\) is a \(Q\)-martingale;
    2. For every stopping time \(\tau\), the process \(M^\tau\) is a martingale;

??? proof

    As for 1. implies 2, we already know that if $M$ is a martingale and $\eta = (\eta_t)_{t=1, \ldots, T}$ is a predictable process, then the portfolio

    \[
      V_t = V_0 + \sum_{s=1}^t \eta_s (M_s - M_{s-1})
    \]

    is a martingale.
    Taking the portfolio $V_0 = M_0$ and the strategy

    \[
      \begin{equation*}
       \eta_t = 1_{\{t\leq \tau\}} = \begin{cases}
        1 & \text{if }t\leq \tau\\
        0 & \text{if }t>\tau
      \end{cases}
      \end{equation*}
    \]

    where you buy and hold $M$ until time $\tau$, it follows that $\eta$ is predictable since $\{t\leq \tau\}=\{\tau \leq t-1\}^c$ is in $\mathcal{F}_{t-1}$.
    Furthermore, by definition 

    \[
      \begin{equation*}
        V_t = \begin{cases}
          M_t & \text{if }t< \tau\\
          M_\tau & \text{if }\tau \leq t
        \end{cases}
        = M_{t\wedge \tau} = M^\tau_t
      \end{equation*}
    \]

    showing that $M^\tau$ is a martingale.

    As for 2. implies 1., it is immediate by considering the stopping time $\tau = T$.

!!! remark

    Note that if $\eta$ is a **positive** predictable process and $M$ is a super-/sub-martingale, then it is easy to show that the portfolio $V_t = V_0 + \sum_{s=1}^t\eta_s (M_s - M_{s-1})$ is a super-/sub-martingale.
    It follows from the proof that Doob's optional sampling theorem also holds for super-/sub-martingales.


Concerning our buyer of an American option. He will choose its exercise strategy among the following set

\[
    \mathcal{T}=\left\{ \tau\colon \tau \text{ stopping time with } \tau \leq T \right\}
\]

Suppose now that the goal of the buyer is to maximize the expectation of its outcome under the pricing measure $P^\ast$, he therefore faces the following optimization problem

\[
    \max\left\{ E^{\ast}\left[ H_{\tau} \right]\colon \tau \in \mathcal{T}\right\}
\]


Its goal is therefore to find an optimal stopping time $\tau^\ast$ such that

\[
E^\ast\left[ H_{\tau^\ast}  \right] \geq E^{\ast}\left[ H_{\tau} \right]
\]

for any other stopping strategy $\tau$.

!!! remark

    Note that such a problem even if intuitive is highly non trivial.
    Indeed, the maximization is done among the set of possible stopping times which is usually infinite dimensional and difficult to describe or parametrize.
    Secondly, the optimization function $\tau \mapsto E^{\ast}[H_{\tau}]$ is nothing close to be something like convex or even smooth (smooth in which sense).
    The classical optimization theory here do not apply at all.

We start by showing that the optimization problem from the buyer's side is always smaller than the minimum hedging capital for the seller.

!!! proposition
    For any stopping time $\tau$ in $\mathcal{T}$, it holds

    \[
        U_0 \geq E^\ast\left[ H_{\tau} \right]
    \]

    In particular,

    \[
        \underbrace{U_0}_{\text{Seller's minimum hedging capital}} \geq \underbrace{\sup \left\{ E^\ast\left[ H_\tau \right] \colon \tau \in \mathcal{T} \right\}}_{\text{Buyer's maximal expected revenue}}
    \]

!!! proof


    Let $\tau$ in $\mathcal{T}$ be any stopping time strategy for the buyer.
    We know that the Snell envelope is a super-martingale such that $U_t\geq H_t$ for every $t$.
    In particular, on the one hand, it holds that $U_\tau \geq H_\tau$ and therefore $E^\ast[U_\tau] \geq E^\ast[H_\tau]$.
    On the other hand, $U^\tau$ is also a super-martingale due to Doob's optional sampling theorem.
    Hence $U_0 \geq E^\ast\left[ U_T^\tau \right] = E^\ast\left[ U_{T\wedge \tau} \right]=E^\ast[U_\tau]$.
    Both together we deduce that
    
    \[
        U_0 \geq E^\ast\left[ H_\tau \right]
    \]

This proposition shows that whatever stopping strategy the buyer is choosing, it will always reach less in (risk-neutral) expectation than what the seller is asking as minimum capital to hedge its contingent claim. If the buyer reaches equality, then it is an optimal strategy. Therefore, the following definition.

!!! definition
    A stopping time $\tau^\ast$ in $\mathcal{T}$ is called optimal if $U_0=E^\ast\left[ H_{\tau^\ast} \right]$.


The question is whether, at least one, optimal stopping time is available to the buyer. Before addressing this question, we can obtain a better characterization of optimal stopping times.

!!! proposition
    A stopping time $\tau^\ast$ is optimal if and only if the two following conditions are satisfied

    1. $U_{\tau^\ast}=H_{\tau^\ast}$;
    2. $U^{\tau^\ast}$ is a $P^\ast$-martingale.

!!! proof

    Suppose that a stopping time $\tau^\ast$ is such that:

    - $U_{\tau^\ast}=H_{\tau^\ast}$
    - $U^{\tau^\ast}$ is a $P^\ast$-martingale
    
    From the second point and Doob's optional sampling theorem, we deduce that
    
    \[
        U_0 = E^\ast\left[ U^\tau_T \right] = E^\ast\left[ U_{\tau^\ast} \right]
    \]
    
    And from the first, we get that $E^\ast[U_{\tau^\ast}] = E^\ast[H_{\tau^\ast}]$.
    Hence $U_0 = E^\ast[H_{\tau^\ast}]$, showing that $\tau^\ast$ is an optimal stopping time.
    
    Reciprocally, suppose that $\tau^\ast$ is an optimal stopping time.
    Since $U$ is a Snell envelope, and $\tau^\ast$ is an optimal stopping time (last equality), we know that
    
    \[
        U_0 \geq E^\ast\left[ U_{\tau^\ast} \right] \geq E^\ast\left[ H_{\tau^\ast} \right] = U_0
    \]
    

    and $U_{\tau^\ast}\geq H_{\tau^\ast}$.
    If $U^{\tau^\ast}$ were a strict martingale, then the first inequality would be strict.
    If $U_{\tau^\ast}$ were strictly greater than $H_{\tau^\ast}$ on a set of positive probability, the second inequality would be strict.
    Since both sides of the inequalities are equal to $U_0$, we conclude that $U^{\tau^\ast}$ is a martingale and $U_{\tau^\ast} = H_{\tau^\ast}$.

This mathematical characterization of optimal stopping times gives us a hint as how to derive an optimal stopping strategy.

Given the Snell envelope $U$ of $H$ under $P^\ast$ with Doob-Meyer decomposition $U = M + A$ where $M$ is a martingale and $A$ is a predictable decreasing process starting at $0$.
On the one hand, according to the first condition we define 

\[
    \tau_{\min}=\inf\left\{ t\colon U_t=H_t \right\}
\]

which is a member of $\mathcal{T}$.
Per definition, it is the smallest stopping time such that $U_{\tau_{\min}}=H_{\tau_{\min}}$.

On the other hand, according to the first condition we define

\[
    \tau_{\max}=\inf \left\{ t\colon E^{\ast}\left[ U_{t+1}-U_t |\mathcal{F}_t \right]\neq 0 \right\}\wedge T=\inf\left\{ t\colon A_{t+1}\neq 0 \right\}\wedge T
\]

which is also a stopping time in $\mathcal{T}$.
By definition is this the largest stopping time for which $U^\tau$ is still a martingale before it starts to be a strict super martingale.

According to the previous proposition, if the buyer is choosing a stopping time that might stop earlier than $\tau_{\min}$ or stop after $\tau_{\max}$ then is has to be sub-optimal.

In other terms, any optimal stopping time $\tau^\ast$ must satisfy

\[
\tau_{\min} \leq \tau^\ast \leq \tau_{\max}
\]

The following proposition shows that eventually $\tau_{\min}$ as well as $\tau_{\max}$, which are explicit, are both optimal stopping times

!!! proposition

    The stopping times $\tau_{\min}$ and $\tau_{\max}$ are optimal stopping times.
    Furthermore, any other optimal stopping time $\tau^\ast$ must satisfy $\tau_{\min} \leq \tau^\ast \leq \tau_{\max}$.

??? proof

    We first show that $\tau_{\min}$ is a optimal stopping time.
    By the characterization, since by definition $U_{\tau_{\min}} = H_{\tau_\min}$ we just need to show that $U^{\tau_\min}$ is a martingale.
    By Doob's optional sampling theorem, the stopped process $U^{\tau_{\min}}_t=U_{t\wedge \tau_{\min}}$ is a $P^\ast$-super-martingale.
    For a fixed $0\leq t\leq T-1$, define $A=\{t<\tau_{\min}\}$. For $\omega\in A$, it holds that $t<\tau_{\min}(\omega)$ and therefore $U_t(\omega)>H_t(\omega)$. Hence,

    \[
        U_t^{\tau_{\min}}(\omega)=U_{t}(\omega)=H_t(\omega)\vee E^{\ast}\left[ U_{t+1}|\mathcal{F}_t \right](\omega)=E^{\ast}\left[ U_{t+1}|\mathcal{F}_t \right](\omega)
        =E^{\ast}\left[ U_{t+1}^{\tau_{\min}}|\mathcal{F}_t \right](\omega)
    \]

    But for $\omega \in A^c$, it holds that $t\wedge \tau_{\min}(\omega)=(t+1)\wedge\tau_{\min}(\omega)=\tau_{\min}(\omega)$ and therefore

    \[
         U_t^{\tau_{\min}}(\omega)=E^{\ast}[U_{t+1}^{\tau_{\min}}|\mathcal{F}_t](\omega)
    \]

    All together with the fact that $A \in \mathcal{F}_t$, it follows that

    \[
        U_{t}^{\tau_{\min}}
        =1_AU_{t}^{\tau_{\min}}+1_{A^c}U_{t}^{\tau_{\min}}
        =1_A E^{\ast}\left[ U_{t+1}^{\tau_{\min}}|\mathcal{F}_t \right]+1_{A^c}E^{\ast}\left[ U_{t+1}^{\tau_{\min}}|\mathcal{F}_t \right]
        =E^{\ast}\left[ U_{t+1}^{\tau_{\min}}|\mathcal{F}_t \right]
    \]

    showing that $U^{\tau_{\min}}$ is a $P^\ast$-martingale.

    We now show that $\tau_{\max}$ is an optimal stopping time.
    By the characterization, since by definition $U^{\tau_\max}$ is a martingale, we just need to show that $U_{\tau_\max} = H_{\tau_\max}$.
    Let $U = M + A$ be the Doob-Meyer decomposition of $U$ into a martingale $M$ and a predictable decreasing process $A$ starting at $0$.
    For $\omega \in \{\tau_{\max}=T\}$ it is clear.
    For $\omega \in \{\tau_{\max}=t\}$ for $t<T$, it follows that $A_t(\omega)=0$ and $A_{t+1}(\omega)>0$. Hence,

    \[
        E^{\ast}\left[ U_{t+1}-U_t|\mathcal{F}_t \right](\omega)=-\left( A_{t+1}(\omega)-A_t(\omega) \right)<0
    \]

    showing that $U_{t}(\omega)>E^{\ast}[U_{t+1}|\mathcal{F}_t](\omega)$ and by the definition of the Snell envelope it follows that $U_t(\omega)=H_t(\omega)\vee E^{\ast}[U_{t+1}|\mathcal{F}_t](\omega) = H_t(\omega)$.
    Hence $H_{\tau_{\max}}=U_{\tau_{\max}}$.

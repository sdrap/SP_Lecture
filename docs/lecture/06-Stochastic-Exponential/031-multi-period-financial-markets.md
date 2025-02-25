# Multi Period Financial Markets

Up to now, we have only considered a static version of a financial market, with a single decision at time \(0\) and a delivery at time \(1\).
This analysis applies to many buy-and-hold investors.
However, as time progresses, more information about the outcomes of contingent claims or portfolios becomes available, allowing investors to adapt their strategies to take advantage of new information.

## Mathematical Model

As always, we consider a probability space \( (\Omega, \mathcal{F}, P) \), which describes the states of the world, the events, and their likelihood.
The market still consists of a bank account \( B \) and \( d \) financial assets \( \boldsymbol{S} = (S^1, \ldots, S^d) \).
Now, we extend the model to \( T+1 \) time periods \( t = 0, \ldots, T \).


* **Bank Account:**
    As in the static case, the bank account \( B \) describes the evolution of one unit of currency over time.
    However the bank now can revise the interest rate it delivers between $t$ and $t+1$ at every time $t$ and this might not be know at time $0$.
    Hence, we define the growth of the bank account as following classical compounding for interest rates:

    \[
      B_0 = 1, \quad B_t(\omega) = B_{t-1}(1+r_t) = \prod_{s=1}^t (1+r_s),
    \]

    where $r_t = (B_t - B_{t-1})/B_t$ is a random variable strictly greater than $-1$.

    In other terms $r_t(\omega)$ represents the interest rate set by the bank at time $t-1$ to remunerate cash deposited in the account at time $t-1$ for the period between $t-1$ and $t$.

* **Financial Assets:**

    We have $d$ of them and as the bank account, their price evolution can be observed at any time $t=0, \ldots, T$.
    Therefore we define the $k$-th financial asset $S^k = (S^k_t){t=0, \ldots, T}$ as a family of random variables

    \[
    \begin{equation*}
      \begin{split}
        S_t^k \colon \Omega & \longrightarrow [0, \infty)\\
                    \omega & \longmapsto S_t^k(\omega) = \text{Price at time $t$ in state $\omega$ of asset $k$}
      \end{split}
    \end{equation*}
    \]

    We assume however that $S_0^k>0$ for the price at time $0$ meaning that the financial asset is not defaulted at time $0$.


In general, a family $Z = (Z_t)_{t=0, \ldots, T}$ where each $Z_t$ is a random variable, is called a **stochastic process**.


* **Portfolio:**

    An investor starts with an initial wealth \( \bar{V}_0 \) and may adjust their holdings over time.
    This strategy is modeled by a \( d \)-dimensional vector \( \boldsymbol{\eta} = (\eta^1, \ldots, \eta^d) \), which is also a ($d$-dimensional) stochastic process:

    \[
    \begin{equation*}
        \begin{split}
            \eta_t^k \colon \Omega &\longrightarrow \mathbb{R}\\
            \omega & \longmapsto \eta_t^k(\omega),
        \end{split}
    \end{equation*}
    \]
    
    for every \( t = 1, \ldots, T \) and \( k = 1, \ldots, d \).  
    The decision about \( \boldsymbol{\eta}_t \) is made at time \( t-1 \) and represents the portfolio held from time \( t-1 \) to \( t \).

    Now given a portfolio value $\bar{V}_{t-1}$ at time $t-1$ and a strategic decision $\boldsymbol{\eta}_{t}$ of holdings until $t$, yields an updated value of the portfolio at time $t$ given by

    \[
    \begin{align*}
        \bar{V}_{t}  & =  \underbrace{\left( \bar{V}_{t-1} - \boldsymbol{\eta}_{t}\cdot \boldsymbol{S}_{t-1} \right)}_{\text{Cash minus cost of holdings}}(1+r_{t}) + \underbrace{\boldsymbol{\eta}_{t}\cdot \boldsymbol{S}_{t}}_{\text{Current holding value}} \\
        &= \bar{V}_{t-1}(1+r_{t}) + \boldsymbol{\eta}_{t}\cdot \left( \boldsymbol{S}_{t} - \boldsymbol{S}_{t-1}(1+r_{t})\right)
    \end{align*}
    \]

* **Discounted Values**
    
    As in the one-period model, it is convenient to work with discounted values.
    The discounted stock prices \( \boldsymbol{X} = (X^1, \ldots, X^d) \) and discounted portfolio value \( V_t \) are defined as:

    \[
        X_t^k = \frac{S_t^k}{B_t} \quad\text{and}\quad  V_t = \frac{\bar{V}_t}{B_t},
    \]

    for \( k = 1, \ldots, d \) and \( t = 0, \ldots, T \).
    Clearly, \( X_0 = S_0 \) and \( V_0 = \bar{V}_0 \).

    Just as in the one period model, it holds that

    \[
        \begin{align*}
            V_t & = \frac{\bar{V}_t}{B_t} \\
            & = \frac{1}{B_{t-1}(1+r_{t})}\left( \bar{V}_{t-1}(1+r_{t}) + \boldsymbol{\eta}_{t}\cdot \left( \boldsymbol{S}_{t} - \boldsymbol{S}_{t-1}(1+r_{t}\right) \right)\\
            & = \frac{\bar{V}_{t-1}}{B_{t-1}} + \boldsymbol{\eta}_t\cdot \left( \frac{\boldsymbol{S}_t}{B_t} - \frac{\boldsymbol{S}_{t-1}}{B_{t-1}} \right)\\
            & = V_{t-1} + \boldsymbol{\eta}_t \cdot  \underbrace{\left(\boldsymbol{X}_t - \boldsymbol{X}_{t-1}\right)}_{:= \Delta \boldsymbol{X}_t}
            = V_0 + \sum_{s=1}^t \boldsymbol{\eta}_s\cdot\Delta \boldsymbol{X}_s
        \end{align*}
    \]

    leading to 

    !!! lemma
        Let \( \boldsymbol{\eta} \) be a strategy and \( V_0 \) the initial value of a self-financing portfolio.
        Then:

        \[
          V_t = V_0 + \sum_{s=1}^t \boldsymbol{\eta}_s \cdot \Delta \boldsymbol{X}_s
        \]
        
        where \( \Delta \boldsymbol{X}_s = \boldsymbol{X}_s - \boldsymbol{X}_{s-1} \).
    
    
## Information

Up to now, we have not considered how decisions are influenced by additional information.
Mathematically, information is represented by collections of events.
A random variable is "known" at a given time if its value is determined by the events available at that time.

!!! definition

    A **filtration** is a family \( \mathbb{F} = (\mathcal{F}_t)_{0 \leq t \leq T} \) of \(\sigma\)-algebras such that:

    \[
    \mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \cdots \subseteq \mathcal{F}_T \subseteq \mathcal{F}.
    \]
    
!!! note

    Throughout, we assume that the initial information \( \mathcal{F}_0 \) is the trivial \(\sigma\)-algebra \( \mathcal{F}_0 = \{\emptyset, \Omega\} \).
    In particular, any $\mathcal{F}_0$ random variable is a constant.(1)
    {.annotate}

    1.  It is a basic exercise to check. Suppose that a random variable $X$ is $\mathcal{F}_0=\{\emptyset, \Omega\}$-measurable then it follows that $X$ is constant. Indeed, if it where not, let $\omega_1$ and $\omega_2$ be two states on which $X(\omega_1) < X(\omega_2)$, let $x$ be such that $X(\omega_1)<x<X(\omega_2)$, it follows that $\omega_1 \in A=\{X\leq x\}$ while $\omega_2 \not \in A$. This is however not possible since the event $A$ is either $\Omega$ or $\emptyset$.

!!! definition

    A collection of random variables indexed by time is called a **stochastic process**.
    A stochastic process \( X = (X_t)_{0 \leq t \leq T} \) is:

    1. **Adapted** if \( X_t \) is \(\mathcal{F}_t\)-measurable for all \( t = 0, \ldots, T \).
    2. **Predictable** if \( X_t \) is \(\mathcal{F}_{t-1}\)-measurable for all \( t = 1, \ldots, T \).


Adapted means that the process at time $t$ only depends on the information up to time $t$ while predictable means that it depends on the information of yesterday.
With this definition in mind, it follows that in a multi-period financial market we have

- The stochastic process modeling financial assets \( \boldsymbol{S} \) is adapted.
- The interest rate process \( r \) is predictable (announced beforehand the next period by the bank)
- Financial strategies \( \boldsymbol{\eta} \) are predictable (decided for the next period).

!!! Multi-Period Financial Market Definition

    A multi-period financial market consists of:
    
    1. A probability space \( (\Omega, \mathcal{F}, P) \).
    2. A filtration \( \mathbb{F} = (\mathcal{F}_t)_{0\leq t\leq T} \).
    3. A $d$-dimensional adapted stochastic process \( \boldsymbol{S} = (\boldsymbol{S}_t)_{0 \leq t \leq T} \) of positive random variables.
    4. A bank account \( B_0 = 1 \), \( B_t = \prod_{s=1}^t (1 + r_s) \), where \( r \) is a predictable process.
    
    Financial strategies \( \boldsymbol{\eta} = (\boldsymbol{\eta}_t)_{0 \leq t \leq T} \) are \( d \)-dimensional predictable processes.


## Arbitrage, Pricing Measure

The primary notion of arbitrage in the static case is given by the fact that one can find a strategy such that it is possible to make strict positive gain without losing any money for sure.
The same notion holds in the multi-period case.

!!! definition "Definition: Arbitrage"

    Given a financial market, a self-financing portfolio \(\bar{V}\) with start value \(\bar{V}_0\) and strategy \(\boldsymbol{\eta}\) is called an arbitrage opportunity if

    \[
        P\left[ \bar{V}_T \geq \bar{V}_0 B_T \right] = 1 \quad \text{and} \quad P\left[ \bar{V}_T > \bar{V}_0 B_T \right] > 0.
    \]

Note that as in the one-period model, this definition is independent of discounting and start since it is equivalent to

\[
  P\left[ V_T \geq V_0 \right] = 1 \quad \text{and} \quad P\left[ V_T > V_0 \right] > 0
\]

and  

\[
  P\left[ \sum_{s=1}^T \boldsymbol{\eta}_s \Delta \boldsymbol{X}_s \geq 0 \right] = 1 \quad \text{and} \quad P\left[ \sum_{s=1}^T \boldsymbol{\eta}_s \cdot \Delta \boldsymbol{X}_s > 0 \right] > 0
\]  

for a strategy \(\eta\).

This definition is global between \(0\) and \(T\) in the sense that along the way an arbitrage can be constructed.
However, the following proposition shows that it is equivalent to a local definition where an arbitrage must exist between two consecutive times.

!!! proposition

    Given a financial market, the following assertions are equivalent:

    1. *Global arbitrage*: There exists an arbitrage opportunity.
    2. *Local arbitrage*: There exists some time \(t\) between $1$ and $T$ and an \(\mathcal{F}_{t-1}\)-measurable random variable \(\boldsymbol{\mu} \colon \Omega \to \mathbb{R}^d\) such that

    \[
      P[\boldsymbol{\mu} \cdot \Delta \boldsymbol{X}_t \geq 0] = 1 \quad \text{and} \quad P\left[ \boldsymbol{\mu} \cdot \Delta \boldsymbol{X}_t > 0 \right] > 0.
    \]

??? proof

    1. We show that the second assertion implies the first with some $\mathcal{F}_{t-1}$-measurable strategy $\boldsymbol{\mu}$ which is an arbitrage between $t-1$ and $t$.
        Let \(\boldsymbol{\eta}\) be the \(\mathbb{R}^d\)-valued process given by

        \[
          \eta_s =  
            \begin{cases}  
              \mu & \text{if } s = t \\  
              0 & \text{otherwise.}  
            \end{cases}
        \]  

        By definition, \(\boldsymbol{\eta}\) is predictable, for which holds $\sum_{s=1}^T \boldsymbol{\eta}_s \cdot \Delta \boldsymbol{X}_s = \boldsymbol{\mu}\cdot \Delta \boldsymbol{X}_t$ showing that $\boldsymbol{\eta}$ is an arbitrage globally.

    2. Conversely, let \(\boldsymbol{\eta}\) be a global arbitrage strategy strategy with the corresponding discounted value process \(V\), and define

        \[
          t := \min\left\{s = 0, \ldots, T : V_s \geq V_0 \text{ and } P\left[ V_s > V_0 \right] > 0 \right\}.
        \]
      
        being the first time where an arbitrage kicks in your portfolio.
        By assumption, \(t \leq T\) and by definition, it follows that \(V_{t-1} = V_0\) or \(P[V_{t-1} < V_0] > 0\).

        In the first case, since

        \[
          \boldsymbol{\eta}_t \cdot \Delta \boldsymbol{X}_t = V_t - V_{t-1} = V_t - V_0 \geq 0,
        \]

        it follows that \(\boldsymbol{\mu} = \boldsymbol{\eta}_t\), which is \(\mathcal{F}_{t-1}\)-measurable and fulfills the assumptions of the local arbitrage.

        In the second case, let \(\boldsymbol{\mu} = \boldsymbol{\eta}_t 1_{\{V_{t-1} < V_0\}}\), which is \(\mathcal{F}_{t-1}\)-measurable.
        It follows that

        \[
          \boldsymbol{\mu} \cdot \Delta \boldsymbol{X}_t = \left(V_t - V_{t-1}\right)1_{\{V_{t-1} < V_0\}} \geq \left(V_0 - V_{t-1}\right)1_{\{V_{t-1} < V_0\}} \geq 0,
        \]

        and since \(P[V_{t-1} < V_0] > 0\), this inequality holds strictly with a strict positive probability showing that $\boldsymbol{\mu}$ is a local arbitrage.


In the first section, we saw that a market is fair if and only if there exists a pricing measure \(P^\ast\) such that

\[
  E^{P^\ast}\left[\boldsymbol{X}_1\right] = \boldsymbol{X}_0
\]

In a multiperiod setting, this equation translates into:

\[
E^{P^\ast}\left[\boldsymbol{X}_{t+1}|\mathcal{F}_{t}\right] = \boldsymbol{X}_{t}
\]  

saying that under the pricing measure, the expected discounted value of every asset at time \(t+1\) conditioned on the information available at time \(t\) is equal to the discounted value of those assets at time $t$.
This statement brings us to the following important notion in the theory of stochastic processes.


!!! definition "Definition: Martingale"

    Given a probability measure \(Q\), a stochastic process \(M = (M_t)_{0 \leq t \leq T}\) is called a \(Q\)-martingale if:

    1. \(M\) is an adapted process.
    2. \(M\) is \(Q\)-integrable.  
    3. \(M\) satisfies the \(Q\)-martingale property, that is,  

        \[
          E^Q\left[M_{t+1}|\mathcal{F}_t\right] = M_t,
        \]  
    
        for every \(t = 0, \ldots, T-1\).


!!! note

    Given a probability $Q$, the most simple example of a martingal is the expectation of a given (integrable random variable).
    Indeed, let $C$ be an (integrable) random variable and define 

    \[
      M_t = E^Q\left[ C | \mathcal{F}_t \right]
    \]

    By definition $M = (M_t)$ is an adapted and integrable process.
    Furthermore, by the tower property of the conditional expectation we get

    \[
      E^Q\left[ M_{t+1} |\mathcal{F}_t\right] = E^{Q}\left[ E^Q\left[ C|\mathcal{F}_{t+1} \right] |\mathcal{F}_t\right] = E^Q\left[ C|\mathcal{F}_t \right] = M_t
    \]



which leads to the definition of a pricing measure

!!! definition

    A probability measure $P^\ast$ is called a **pricing measure** if the discounted price process $\boldsymbol{X}$ is a $d$-dimensional $P^\ast$-martingale.


!!! proposition

    Let $P^\ast$ be a probability measure.
    The following conditions are equivalent

    * $P^\ast$ is a pricing measure;
    * Any (discounted) portfolio $V = V_0 + \sum \boldsymbol{\eta}_s \cdot \Delta \boldsymbol{X}_s$ for some (bounded) strategy $\boldsymbol{\eta}$ is a $P^\ast$-martingale;

!!! proof

    As for the first assertion implying the second, let $P^\ast$ be a risk pricing measure and $\boldsymbol{\eta}$ a bounded strategy, then $V$ is a $P^\ast$-martingale.(1) Since $\boldsymbol{\eta}$ is predictable, it follows that
    {.annotate}

    1.  In your context you just need to check the martingale property, however the other two assumption shall be checked too. Adaptiveness is usually given right away, in our case it follows from the fact that $V$ is an adapted process as a scalar product between a predictable and an adapted process. Integrability is usually also straightforward, yet mathematically should be checked. In our case since $\boldsymbol{\eta}$ is uniformly bounded, it follows that
        \[
          \begin{equation*}
            |V_t|\leq |V_0|+\sum_{s=1}^t\sum_{k=0}^d|\eta_s^k||\Delta X_s^k|\leq |V_0|+C\sum_{s=1}^t\sum_{k=0}^d|\Delta X_s^k|
          \end{equation*}
        \]

        for every $t$, where $C$ is the constant such that $|\eta_s^k|\leq C$ for every $k=0,\ldots,d$ and $s=0,\ldots ,T$.
        Since $\boldsymbol{X}$ is $P^\ast$ integrable, it follows that $V$ is also too.


    \[
      \begin{equation*}
          E^{P^\ast}\left[ V_{t+1}|\mathcal{F}_{t} \right]=E^{P^\ast}\left[ V_{t} + \boldsymbol{\eta}_{t+1}\cdot \Delta \boldsymbol{X}_{t+1}|\mathcal{F}_{t} \right]=V_t + \boldsymbol{\eta}_{t+1}\cdot E^{P^\ast}\left[ \Delta \boldsymbol{X}_{t+1}|\mathcal{F}_{t} \right]=0
      \end{equation*}
    \]

    Hence, $V$ is a $P^\ast$-martingale.

    Reciprocally, if every discounted portfolio is a $P^\ast$ martingale, fix $k$ in $\{1,\ldots,d\}$, and define
    
    \[
    \begin{equation*}
        \eta_t^i=
        \begin{cases}
            1 &\text{if }i=k\\
            0 &\text{otherwise}
        \end{cases}
    \end{equation*}
    \]
    
    for any $t=1,\ldots,T$ and $i=1,\ldots, d$ which defines a uniformly bounded strategy $\boldsymbol{\eta}$.
    Furthermore, by definition, it holds that $V = X^k$.
    Hence $V$ being a $P^\ast$ martingale implies that $X^k$ is a $P^\ast$ martingale too.
    Hence $P^\ast$ is a pricing measure.


## Fundamental Theorem of Asset Pricing

As exposed before, the multi period setting can be cast as a sequence of pasted successive one period models.
Hence, it is not a surprise that all the results derived in one period model do extend into the multiperiod one.
The intuition is the same, it just requires the infinite dimensional extension of the separation Theorem of Hahn-Banach which is beyond the scope of this lecture.

!!! theorem "Fundamental Theorem of Asset Pricing"

    The financial market model is arbitrage free if, and only if, there exists a pricing measure $P^\ast$ equivalent to $P$.

    This risk pricing neutral pricing measure can be chosen such that $dP^\ast/dP$ is bounded.

Super- and sub-hedging results carries over the same way.
In particular, given a contingent claim $C$ paying off at maturity $T$, a fair price $\pi(C)=(\pi_t(C))$ is a stochastic process given by

\[
\pi_t(C) = B_t E^{P^\ast}\left[ \frac{C}{B_T} | \mathcal{F}_t \right]
\]

As in the one period model you have the price at time $0$ given by $\pi_0(C) = E^{P^\ast}[C/B_T]$ which is the discounted expectation of the contingent claim, while $\pi_T(C) = B_T E^{P^\ast}[C/B_T |\mathcal{F}_T] = C$ is the contingent claim itself at time $T$.



## Exotic Derivatives


European derivatives (Put/Call, butterfly, Straddle, Forward) definition follows directly from the one period.
However, since we have now several periods, new class of options can be defined where intermediary conditions depending on time can be part of the contract.
Those options are typically called exotic derivatives.

* **European Options**:

    As mentioned it is a straight forward extension, where the horizon $T$ is called *maturity*.
    For instance European call and put options

    \[
    \begin{align*}
      C^{call} & = (S_T - K)^+ \\
      C^{put} & = (K-S_T)^+ 
    \end{align*}
    \]

* **Asian Option**: Asian option typically depends on the time average of an underlying.

    We define the **rolling time average** between $1$ and $t$ of an asset $S$ as follows

    \[
        S^{av}_t = \frac{1}{t} \sum_{s=1}^t S_s
    \]

    Asian options, are contracts written on this time average, for instance an Asian call or put option

    \[
    \begin{align*}
      C^{asian\,call} & = (S^{av}_T - K)^+ = \left( \frac{1}{T}\sum_{t=1}^T S_t -K \right)^+\\
      C^{asian\,put} & = (S^{av}_T - K)^+ = \left( K-\frac{1}{T}\sum_{t=1}^T S_t \right)^+
    \end{align*}
    \]

    In the following illustration thick lines stands for paths while dashed stands for exanding average.
    For an asian call, only the red scenario returns a positive outcome.
    In contrast, for the standard call, only the red scenario is void.


    ![Asian](./../../images/asian_dark.svg#only-dark){align = right}
    ![Asian](./../../images/asian_white.svg#only-light){ align = right}




* **Barrier Options**: Barrier options are options that depends on the path of the underlying hitting or not a given barrier at a given previous time.

    To do so, for a financial asset $S$, we define the **rolling maximum** $\overline{S}$ and **minimum** $\underline{S}$ as

    \[
      \begin{align*}
        \overline{S}_t & =\max_{s\leq t} S_s\\
        \underline{S}_t & =\min_{s\leq t} S_S
      \end{align*}
    \]

    With these rolling maximum and minimum, we can define several conditions for a standard contract to hold

    * *knocked up and in*: The contract hold only if $\overline{S}_T \geq B$;
    * *knocked up and out*: The contract is void if $\overline{S}_T \geq B$;
    * *knocked down and in*: The contract hold only if $\underline{S}_T \leq B$;
    * *knocked down and out*: The contract is void if $\underline{S}_T \leq B$;

    With these conditions at hand, myriad of options can be defined starting from European or Asian options.
    For instance

    \[
      \begin{align*}
        C^{call}_{up\&in} & 
        = (S_T - K)^+ 1_{\{ \overline{S}_T\geq B \}}
        = 
        \begin{cases}
          (S_T-K)^+ & \text{if }\overline{S}_T \geq B \\
          0 & \text{otherwize}
        \end{cases}\\
        C^{call}_{down\&out} & 
        = (S_T - K)^+ 1_{\{ \underline{S}_T > B \}}
        = 
        \begin{cases}
          (S_T-K)^+ & \text{if }\underline{S}_T > B \\
          0 & \text{otherwize}
        \end{cases}
      \end{align*}
    \]

    In the following illustration thick lines stands for paths while dashed stands for the running maximum.
    For an up and out call, only the orange scenario returns a positive outcome.
    The blue scenario is above the strike however knocked the barrier before $T$.


    ![Barrier](./../../images/barrer_dark.svg#only-dark){align = right}
    ![Barrier](./../../images/barrer_white.svg#only-light){ align = right}




!!! note "Computational Issues"
    Given a contingent claim \(C\), any fair price of this contingent claim is given as \(E^{P^\ast}[C/B_T]\).
    Setting the discounting factor to \(1\), if \(C = f(S_T)\) for some function, such as a plain European option, it follows that the price can be computed as:

    \[
      E^{P^\ast}\left[ f(C) \right] = E^{P^\ast}\left[ f(S_T) \right] = \int_{\mathbb{R}} f(s) dF^\ast_{S_T}(s)
    \]

    However, if the contingent claim is of Asian or barrier type, the payoff does not only depend on the last value of the financial asset but on the whole path.
    In other terms, \(C = f(S_1, \ldots, S_T)\), such as \(f(s_1, \ldots, s_T) = \left(\frac{\sum s_t}{T} - K\right)^+\), meaning that the contingent claim depends on the multidimensional distribution of the price over time.
    Suppose that this price has a density, that is:

    \[
    dF^{\ast}(S_1, \ldots, S_T)(s_1, \ldots, s_T) = \phi(s_1, \ldots, s_T) ds_1 \ldots ds_T.
    \]

    It follows that:  

    \[
      E^{P^\ast}\left[ f(C) \right] = E^{P^\ast}\left[ f(S_1, \ldots, S_T) \right] = \int_{\mathbb{R}} \int_{\mathbb{R}} \ldots \int_{\mathbb{R}} f(s_1, \ldots, s_T) \varphi(s_1, \ldots, s_T) ds_1 \ldots ds_T
    \]

    which is a high-dimensional integration.

    Classical integration becomes unusable beyond 2-3 dimensions as it suffers from the curse of dimensionality.
    Monte Carlo methods are then the way to go, but reasonable accuracy requires very large samples.
    This is one drawback of those exotic options.

    However, for barrier options, it turns out that in specific contexts, regardless of the horizon \(T\), the integration can be reduced to a two-dimensional one, which is tractable.
    Therefore, the popularity of barrier options (or similarly, snowball options).

  


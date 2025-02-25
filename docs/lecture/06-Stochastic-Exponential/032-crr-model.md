# Binomial Model aka Cox Ross Rubinstein Model

The Cox Ross Rubinstein model can litteraly be considered as the discrete time full analog to the Black-Scholes-Merton model.
The dynamic is entirely determined by the result of a coin toss every day, hence the following model:

## Probability Model

The space of coint toss sequences is given by \(\Omega = \{\omega = (\omega_1, \ldots, \omega_T) : \omega_t = \pm 1\}\) where $\omega=(\omega_1, \ldots, \omega_T)$ represents each sequence of $\pm1$ as result of the coin toss.
As for the $\sigma$-algebra of events we consider $\mathcal{F}=2^\Omega$.
We also consider a probability measure $P$ such that \(P[\{\omega\}] > 0\) for every \(\omega\).

As for the information we consider the stochastic process $Y=(Y_t)_{t=1, \ldots T}$ given by

\[
\begin{equation*}
  \begin{split}
    Y_t\colon \Omega & \longmapsto \{-1, 1\}\\
              \omega & \longrightarrow Y_t(\omega) = \omega_t =  \text{result of coin toss at time }t
  \end{split}
\end{equation*}
\]

In other terms the stochastic process $Y$ provides information about the result of the coin toss at each time.
We therefore define the filtration

\[
\mathcal{F}_0 = \{\emptyset, \Omega\} \quad \text{and}\quad \mathcal{F}_t = \sigma\left( Y_s\colon s\leq t \right)
\]

In other terms, $\mathcal{F}_t$ is the set of events which have been revealed by all coin tosses up to time $t$.
It can be shown that if $\xi$ is a $\mathcal{F}_t$-measurable random variable, then this random variable only depends on the coin tosses up to time $t$, that is 

\[
\xi(\omega) = \xi( \underbrace{\omega_1, \ldots, \omega_t}_{\text{Information up to $t$}}, \underbrace{\omega_{t+1}, \ldots, \omega_T}_{\text{Information after $t$}} ) = \xi( \omega_1, \ldots, \omega_t )
\]


## Market Model

* **Bank account** $B=(B_t)_{t=0, \ldots, T}$ whith

    \[
      B_0 = 1, \quad \text{and}\quad B_t = B_{t-1}(1+r) = (1+r)^t
    \]

    for a fixed interest rate $r>-1$.
    Clearly, the bank account is predictable since the interest rate is constant.

* **Single risky asset** $S = (S_t)_{t=0, \ldots, T}$ where

    \[
      S_0>0 \quad \text{and}\quad S_t = S_{t-1}\left( 1+R_t\right)
    \]

    where the returns of the stock $R=(R_t)_{t=1, \ldots, T}$ is a stochastic process given by

    \[
      \begin{align*}
        R_t(\omega) & = 
        \begin{cases}
          u & \text{if }\omega_t = 1\\
          d & \text{if }\omega_t = -1
        \end{cases}
    \end{align*}
    \]

    where $-1<d<u$ are constants.
    Clearly, $R_t$ only depends on the result of the coin toss at time $t$, which can also be seen from

    \[
        R_t = u 1_{\{Y_t = 1\}} + d 1_{\{Y_t = -1\}} = (u-d)1_{\{Y_t = 1\}} +d
    \]

    showing that $S$ is an adapted process.

## No arbitrage and Pricing Measure

This financial model is called the binomial model or Cox, Ross, and Rubinstein model (CRR for short).

!!! proposition

    The CRR model is arbitrage-free if and only if \(d < r < u\).
    In this case, the CRR model is complete with unique pricing measure \(P^\ast\) equivalent to \(P\).
    This risk pricing measure is characterized by the fact that the random variables \(R_1, \ldots, R_T\) are iid with common distribution:

    \[
      P^\ast[R_t = u] = p = \frac{r - d}{u - d}, \quad t = 1, \ldots, T
    \]

!!! proof

    By the FTAP, arbitrage-free is equivalent to the existence of a pricing measure \(P^\ast\) equivalent to \(P\).
    Under such \(P^\ast\), the discounted price process is a martingale.
    In particular, it holds:

    \[
      0 = E^\ast\left[ \Delta X_t \mid \mathcal{F}_{t-1} \right] = E^\ast\left[ X_{t-1} \left( \frac{1 + R_t}{1 + r} - 1 \right) \mid \mathcal{F}_{t-1} \right] = X_{t-1} E^\ast\left[ \frac{R_t - r}{1 + r} \mid \mathcal{F}_{t-1} \right]
    \]

    Since \(X_{t-1} > 0\) and \(R_t = (u-d)1_{\{Y_t = 1\}} +d\), it follows that

    \[
    r = E^\ast[R_t \mid \mathcal{F}_{t-1}] = (u - d) P^\ast\left[ Y_t = 1 \mid \mathcal{F}_{t-1} \right] + d
    \]
    
    Showing that
    
    \[
    P^\ast\left[ Y_t = 1 \mid \mathcal{F}_t \right] = \frac{r - d}{u - d}
    \]
    
    for every \(t = 0, \ldots, T\).
    
    From this relation, we conclude three facts:
    
    - The conditional distribution of \(P^\ast\) under \(\mathcal{F}_{t-1}\), that is, \(P^\ast[\cdot \mid \mathcal{F}_{t-1}]\), is constant for every \(t = 0, \ldots, T-1\).
        Hence,
        \[
          P^\ast\left[ Y_t = 1 \mid \mathcal{F}_t \right] = P^\ast\left[ Y_t = 1 \right] = P^\ast\left[ Y_1 = 1 \right]
        \]
    - Since \(P^\ast\) is a probability measure equivalent to \(P\), it follows that

        \[
          0 < \frac{r - d}{u - d} < 1
        \]
      
        That is, \(d < r < u\).

    - The formula for the probability \(P^\ast\) is uniquely determined, and therefore, if the market is arbitrage-free, it has to be complete.
    
    As for the independence of \(R\), it follows readily from the definition of \(P^\ast\).

!!! remark

    Note that the distribution of the pricing measure $P^\ast$ is entirely given by $P^\ast[R_t = u] = p$.
    Indeed, since $\{Y_t = 1\} =\{R_t=u\}$ as well as $\{Y_t = -1\} = \{R_t = d\}$ it follows that $(Y_1, \ldots, Y_T)$ are iid.
    Hence, for $\omega = (\omega_1, \ldots, \omega_T)$ it holds that

    \[
        \begin{align*}
          P^\ast\left[ \{\omega\} \right] & = P^\ast\left[ Y_1 = \omega_1, \ldots, Y_T = \omega_T \right]\\
          & = P^\ast\left[ \cap_{t=1}^T \{Y_t = \omega_t\} \right]\\
          & = \prod_{t=1}^T P^\ast[Y_t = \omega_t] & & \text{Independence of }Y_1, \ldots, Y_T\\
          & = \prod_{t=1}^T P^\ast[Y_1 = \omega_t] & & \text{Identical distribution of }Y_1, \ldots, Y_T\\ 
          & = p^l (1-p)^{T-l}
        \end{align*}
    \]

    where $l = \# \{t \colon \omega_t = 1\}$ is the number of $1$ in the sequence of coin tosses $\omega = (\omega_1, \ldots, \omega_T)$.


Since the market is complete, we can therefore:

- **Price** any European contingent claim \(C\) uniquely by means of

    \[
      \pi(C) = E^\ast\left[ \frac{C}{(1 + r)^T} \right]
    \]

- **Replicate** (or hedge) the claim by means of a strategy \(\eta\) such that

    \[
      \pi(C) + \sum_{s=1}^T \eta_s \Delta X_s = \frac{C}{(1 + r)^T}
    \]

In particular, given the replicating strategy \(\eta\), we can even provide the (discounted) price at any time by means of

\[
    V_t = \pi(C) + \sum_{s=1}^t \eta_s \Delta X_s = E^\ast\left[ \frac{C}{(1 + r)^T} \mid \mathcal{F}_t \right]
\]

**Pricing** (i.e., computing \(\pi(C)\)) and **Hedging** (i.e., finding \(\eta\)) are two of three (managing risk is a fundamental component) main activities of financial institutions engaging in derivative trading.

Before any further assumptions, as for the price, since we have an explicit expression for $P^\ast$, it holds that

\[
\pi(C) = \sum_{\omega \in \Omega} \frac{C(\omega)}{(1+r)^T} P^\ast[\{\omega\}] = \sum_{\omega \in \Omega}\frac{C(\omega)}{(1+r)^T}p^{l(\omega)}(1-p)^{T-l(\omega)}
\]

where $l(\omega) = \# \{t \colon \omega_t = 1\}$.

!!! warning
    This simple expression that can be implemented easily programatically hides however a very important fact.
    The sum is processed over all possible paths of coin tosses, and the cardinality of which is equal to $2^T$.
    Even with such a very simple market, if we consider one year maturity by daily trading, it amounts for $2^{260}$ paths which largely outmatch any computational power.
    Hence, it is not efficiently implementable, and without further assumptions, this curse of dimensionality can only be overcome through Monte-Carlo methods, sampling a large number, though less than $2^{260}$ of paths and approximating the expectation.
    

## Reducing Complexity: Vanilla Derivatives

Many of the derivatives are plain vanilla European options, that is derivatives which discounted value only depends on the last value of the underlying:

\[
H = \frac{C}{(1+r)^T} = h(S_T)
\]

where $h\colon \mathbb{R} \to \mathbb{R}$.
For instance $h(x) = (x-K)^+/(1+r)^T$ the discounted profile of a call option.
However this option can only take $T+1$ values $S_0(1+u)^l(1+d)^{T-l}$ for $l = 0, \ldots, T$ with each values corresponding to $C_T^l=T!/(l!(T-l)!)$ different possible paths.
The computation of the price at time $0$ therefore simplifies to

\[
\begin{align*}
  \pi(C) & = \sum_{\omega \in \Omega} H(\omega)P^\ast[\{\omega\}]\\
         & = \sum_{l=0}^T  h\left(S_0 (1+u)^l(1+d)^{T-l}\right) C_T^l p^l (1-p)^{T-l}
\end{align*}
\]

which turns the computation of the price from a $2^T$ to a $T+1$ sum.

### Dynamic Pricing

A further particularity of those options, is that the value of the discounted portfolio can also be computed explicitely through a simple backward technique.
This relies on the following mathematical result

!!! proposition

    Let $X$ and $Y$ be two random variable where $X$ is $\mathcal{F}_t$-measurable and $Y$ is independent of $\mathcal{F}_t$.
    Then for every function $h:\colon \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ it holds (modulo integrability)

    \[
      E^{P^\ast}\left[ h(X, Y) |\mathcal{F}_t \right](\omega) = v(X(\omega))
    \]

    where $v\colon \mathbb{R} \to \mathbb{R}$ is a function defined as

    \[
      v(x) = E^{P^\ast}\left[ h(x, Y) \right]
    \]

!!! remark

    This proposition basically says that since $Y$ is independent of $\mathcal{F}_t$ and $X$ is $\mathcal{F}_t$ measurable, then computing the conditional expectation corresponds to freezing $X(\omega)$ and computing the expectation.
    In not so adequate notations, 

    \[
      E^{P^\ast}\left[ h(X, Y) | \mathcal{F}_t \right](\omega) = E^{P^\ast}\left[ h(x, Y) | x = X(\omega) \right]
    \]


This allows us to state the discrete formulation of partial differential equation type for the portfolio value:

!!! proposition

    For a european vanilla option $H = h(S_T)$, it holds that that the discounted value of the hedging portfolio is equal to

    \[
      V_t = v_t(S_t)
    \]

    where $v_t \colon \mathbb{R} \to \mathbb{R}$ for $t=T, \ldots, 0$ is recursively defined as

    \[
      \begin{equation*}
        \begin{cases}
          v_T(x)  = h(S_T)\\
          \\
          v_t(x)  = p v_{t+1}(x(1+u)) + (1-p)v_t(x(1+d)) & \text{for }t = T-1, \ldots, 0
        \end{cases}
      \end{equation*}
    \]

!!! proof

    By finite inverse induction.

    * For $t=T$ it holds that $V_t = H = h(S_T) = v_T(S_T)$ by definition.
    * For $t=T-1$, by the martingale property, it holds that $V_{T-1} = E^{P^\ast}[V_T |\mathcal{F}_{T-1}] = E^{P^\ast}[v_T(S_T)|\mathcal{F}_{T-1}]$.
        Now using the proposition above, since $S_{T-1}$ is $\mathcal{F}_{T-1}$-measurable and $R_T$ is independent to $\mathcal{F}_{T-1}$ we get

        \[
          \begin{equation*}
            V_T  = E^{P^\ast}\left[ v_T(S_{T-1}(1+R_T)) |\mathcal{F}_{T-1} \right] = v_{T-1}(S_{T-1}) 
          \end{equation*}
        \]
        
        for

        \[
          \begin{align*}
            v_{T-1}(x) & = E^{P^\ast}\left[ v_T(x (1+R_T)) \right]\\
                       & = E^{P^\ast}\left[ v_T(x(1+R_1)) \right] && R_1, \ldots, R_T \text{ are iid}\\
                       & = pv_T(x(1+u)) + (1-p)v_T(x(1+d))
          \end{align*}
        \]

    The next steps $T-2, \ldots, 0$ follows the same argumentation.


### Dynamic Hedging

As for the second part of the job, hedging, we know that there exists a predictable strategy $\eta = (\eta_t)_{t=1, \ldots, T}$ that will hedge the claim.
Again, in the setting of plain vanilla european option, these ones can be computed backwardly as soon as you computed the sequence of functions $v_0, \ldots, v_T$.

!!! proposition

    For a european vanilla option $H= h(S_T)$ the hedging strategy $\eta = (\eta_t)_{t=1, T}$ is given by

    \[
      \eta_t = \Delta_t(S_{t-1})
    \]

    where $\Delta_t \colon \mathbb{R} \to \mathbb{R}$ for $t=1, \ldots, T$ are functions recursively computed as follows

    \[
        \displaystyle \Delta_t(x) = (1+r)^t \frac{v_t(x(1+u)) - v_t(x(1+d))}{x(1+u) - x(1+d)}
    \]

!!! remark

    The function $\Delta_t$ is called the **delta** hedge in finance.
    The notation is a bit unfortunate in regards to our notation for difference, but is makes sense if you notice that this is the discrete version of the derivative of the portfolio value with respect to the underlying asset $\partial v_t/\partial S_t$ coinciding with the Black and Sholes framework.


!!! proof

    Let us consider a given time $1\leq t\leq T$.
    The hedging strategy $\eta = (\eta_t)_{t=1, \ldots, T}$ is such that

    \[
        V_{t} - V_{t-1} = \eta_t (X_t - X_{t-1}) 
    \]

    On the one hand, knowing $S_0, \ldots, S_{t-1}$, since $\eta_t$ is predictable the right hand side can only take two values

    \[
      \begin{align*}
        \eta_t (X_t - X_{t-1}) & = \displaystyle \eta_t \frac{S_{t-1}}{(1+r)^t}\left( R_t - r  \right)
        \\
        & =\displaystyle \eta_t \frac{S_{t-1}}{(1+r)^t}
          \begin{cases}
            u-r & \text{if } \omega_t = 1\\
            \\
            d-r & \text{if } \omega_{t} = -1
          \end{cases}
      \end{align*}
    \]

    On the other hand, since $V_t = v_t(S_t) = v_t(S_{t-1}(1+R_t))$ as well as $V_{t-1} = v_{t-1}(S_{t-1}) = p v_t(S_{t-1}(1+u)) + (1-p) v_t(S_{t-1}(1+d))$, it follows that the left hand side can only take two values given $S_0, \ldots, S_{t-1}$.

    \[
      \begin{align*}
        V_t - V_{t-1} & = \displaystyle v_t(S_{t-1}(1+R_t)) - p v_t(S_{t-1}(1+u)) - (1-p) v_t(S_{t-1}(1+d))\\
        \\
                      & = \displaystyle
        \begin{cases}
         (1-p) \left(v_t(S_{t-1}(1+u)) - v_t(S_{t-1}(1+d))\right) & \text{if }\omega_t =1\\
        \\
         p \left(v_t(S_{t-1}(1+u)) - v_t(S_{t-1}(1+d))\right) & \text{if }\omega_t =-1\\
        \end{cases}
      \end{align*}
    \]

    Puting these two equation together and solving for $\eta_t$, knowing that $p = (r-d)/(u-d)$ yields that knowing $S_0, \ldots, S_{t-1}$ we have

    \[
      \eta_t = (1+r)^t \frac{v_t(S_{t-1}(1+u)) - v_t(S_{t-1}(1+d))}{S_{t-1}(1+u) - S_{t-1}(1+d)} = \Delta_t(S_{t-1})
    \]

!!! remark

    The derivation of the functions $v_t$ and $\Delta_t$ for $t=0, \ldots, T$ can be extended to the general case of options depending on the full path, that is with discounted formulation $H = h(S_0, \ldots, S_T)$ for some function $h:\mathbb{R}^{T+1} \to \mathbb{R}$ following the same argumentation where

    \[
        \begin{equation*}
            \begin{cases}
                v_T(x_0, \ldots, x_{T}) & = h(x_0, \ldots, x_T)\\
                \\
                v_t(x_0, \ldots, x_t) & = p v_{t+1}(x_0, \ldots, x_{t}, x_t(1+u)) + (1-p)v_{t+1}(x_0, \ldots, x_{t}, x_t(1+d))
            \end{cases}
        \end{equation*}
    \]

    as well as

    \[
        \Delta_t(x_0, \ldots, x_{t-1}) = (1+r)^t \frac{v_{t}(x_0, \ldots, x_{t-1}, x_{t-1}(1+u)) - v_{t}(x_0, \ldots, x_{t-1}, x_{t-1}(1+d))}{x_{t-1}(1+u) - x_{t-1}(1+d)}
    \]

    Though those expression are valid and simple to write down mathematically, to solve those numerically hits the problem of the curse of dimensionality, since those depends on every possible combinations of paths for the price $(x_0, \ldots, x_t)$ at each time $t$, which amounts to $2^T$.

### Implementation

The implementation in a binomial model(1) for plain vanilla options is classical and relatively straightforward after reformulating the problem in terms of matrices. 
{.annotate}

1.  the BS model turns into resolving pde which unless you have an explicit expression turns into finite difference methods or alike kinds which are similar.


The main computational issue is to derive $v_t(x)$ for every attainable $x=S_t$ and every $t$.
To do so as in numerical methods for PDE we consider matrix/vector notations(1) of values
{.annotate}

1.  In terms of computer memory and efficiency, this certainly not the best approach. But in that case you don't use python but rather low level programming languages like rust or C and look at structures like Btreemaps and the likes. In python `numpy` does just fine and the dimension is no longer an issue for modern computers.

We will store the value of the portfolio and the delta hedging into a diagonal matrices $(T+1)\times (T+1)$ and $T\times T$ with column vectors $\boldsymbol{v}_t$ in $\mathbb{R}^{T+1}$ and $\boldsymbol{\Delta}_t$ as follows

\[
\begin{equation*}
\boldsymbol{v}_t = 
\begin{bmatrix}
    v_t(S_0(1+u)^t)\\
    v_t(S_0(1+u)^{t-1}(1+d))\\
    \vdots 
    \\
    v_t(S_0(1+d)^t)\\
    0
    \\
    \vdots
    \\
    0
\end{bmatrix}
\quad \text{and}\quad
\boldsymbol{\Delta}_t = 
\begin{bmatrix}
\Delta_t(S_0(1+u)^{t-1})\\
\Delta_t(S_0(1+u)^{t-2}(1+d))\\
\vdots
\\
\Delta_t(S_0(1+d)^{t-1})
\\
0
\\
\vdots
0
\end{bmatrix}
\end{equation*}
\]

for $t=0, \ldots, T$. 
and we apply the recursion up to $0$.
Once $\boldsymbol{v}_t$ are calculated, and stored, the heding strategy can be computed directly.

```python
import numpy as np

# Computation of the discounted portfolio value
# claim is the function C = f(S_T)
# not efficient in this form (python is bad with loops) but clear in terms of loops
# does not verify if -1 < d< r< u!!!
def portfolio_value(claim, S0, r, u, d, T):
    # value of the portfolio
    v = np.zeros((T+1, T+1))
    # stock prices tree
    s = np.zeros((T+1, T+1))
    # hedging strategy
    delta = np.zeros((T, T))

    # initialize the stock tree
    s[0, 0] = S0
    for t in range(1, T+1):
        for l in range(t+1):
            s[t, j] = S0 * (1+u)**(t-l) * (1+d)**l
    
    # risk neutral probability
    p = (r - d)/(u - d)

    # initialization of the portfolio value at time T
    v[T, :] = claim(s[T,:]) / (1+r) ** T

    # Compute backwardly the discounted portfolio value and the hedging
    for t in range(T-1, -1, -1):
        for l in range(t+1):
            vup = v[t+1, l]
            vdown = v[t+1, l+1]
            sup = s[t, l] * (1+u)
            sdown = s[t,l] * (1+d)
            # delta hedging
            delta[t, l] = (1+r) ** t * (vup - vdown) / (sup - sdown)
            # portfolio value
            v[t,j] = p * vup + (1-p) * vdown

    return {
        "Stock": s,
        "portfolio": v,
        "delta": delta
    }

```

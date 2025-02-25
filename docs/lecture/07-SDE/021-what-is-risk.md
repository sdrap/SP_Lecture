# What is Risk

Even if the notion of risk is colloquial and everyone intuitively understands it, it is far from clear what it is the exact definition.

We saw in the previous chapter how to price contingent claims in a "risk-neutral way" ensured by an arbitrage-free financial market. However, such pricing does not tell us much about the amount of "risk" one undertakes when investing in one product or another.

Let us consider the following example.


!!! example


    Let $\Omega=\{\omega_1,\omega_2,\omega_3\}$, $\mathcal{F}=2^\Omega$, and the "objective probability" measure $P$ given by $P[\{\omega_1\}]=0.1$, $P[\{\omega_2\}]=0.85$, and $P[\{\omega_3\}]=0.05$. Our bank account $B_0=1$ and $B_1=(1+r)$. We have two stocks with the same start price $S_0^1=S_0^2=100$ and prices tomorrow:
    
    \[
    S_1^1(\omega)=
    \begin{cases}
        110 & \text{if } \omega = \omega_1 \\
        105 & \text{if } \omega = \omega_2 \\
        100 & \text{if } \omega = \omega_3
    \end{cases}
    \quad \text{and} \quad
    S_1^2(\omega)=
    \begin{cases}
        160 & \text{if } \omega = \omega_1 \\
        110 & \text{if } \omega = \omega_2 \\
        0   & \text{if } \omega = \omega_3
    \end{cases}
    \]
    
    Simple computation shows that for $r=\frac{1}{15} \approx 6.66\%$, there exists a unique risk-neutral pricing measure $P^\ast$ given by:
    
    \[
    P^\ast[\{\omega_1\}] = p_1^\ast = \frac{2}{3}, \quad P^\ast[\{\omega_3\}] = p_3^\ast = \frac{1}{3}, \quad \text{and} \quad P^\ast[\{\omega_2\}] = p_2^\ast = 0
    \]
    
    Now, as a portfolio manager, you face the dilemma of which stock you would choose or what proportion you would allocate to one or the other. If the only rationale underlying your decision process is given in terms of the risk-neutral pricing, there is no difference between the two stocks, and you are indifferent.
    
    However, you intuitively see that the first stock is a blue chip, whereas the second one is rather the hot but "risky" kid on the playground—a startup or so. Your decision process would likely be driven by a "risk/reward" analysis in the face of "uncertainty," whatever that means.


We make the analysis even simpler with the following second example.

!!! example

    You own 1,000 RMB and have the choice between the following games:
    
    1. Pay 1,000 and get immediately:

        \[
        \begin{cases}
            2,000 & \text{with probability } 50\% \\
            0     & \text{otherwise}
        \end{cases}
        \]

    2. Pay 1,000 and get immediately:
    
        \[
         \begin{cases}
             1,200 & \text{with probability } \frac{5}{6} \approx 83.33\% \\
             0     & \text{otherwise}
         \end{cases}
        \]

    3. Pay 1,000 and get immediately:
      
        \[
         \begin{cases}
             1,300 & \text{with probability } 25\% \\
             900   & \text{otherwise}
         \end{cases}
        \]

    4. Pay 1,000 and get immediately:

        \[
         \begin{cases}
             1,100 & \text{with probability } 50\% \\
             900   & \text{otherwise}
         \end{cases}
        \]
    
    5. Do nothing and keep your 1,000.
    
    All these games have an expected return of 0. However, you would likely have a preference regarding which one is the best. Considering their standard deviations—that is, $E[(X - E[X])^2]^{1/2}$—it holds:
    
    \[
      \begin{aligned}
          \mathrm{STD}(\text{game 1}) & \approx 1,000, \\
          \mathrm{STD}(\text{game 2}) & \approx 447.21, \\
          \mathrm{STD}(\text{game 3}) & \approx 173.21, \\
          \mathrm{STD}(\text{game 4}) & \approx 100, \\
          \mathrm{STD}(\text{game 5}) & \approx 0.
      \end{aligned}
    \]


!!! remark

    Risk perception is a subjective view of how you assess uncertain prospective outcomes.
    This may differ from one person to another as well as from one context to another.
    How can we model this fact mathematically?


## Two Examples for Risk Assessment Instruments

### Markowitz Mean Variance
The deviation from the mean appears to be a good indicator of our aversion to uncertainty. This is why Markowitz introduced the following criterion to assess the trade-off between risk and rewards in terms of variance and means.

!!! definition

    Given a square integrable random variable \( X \)—modeling some payoff such as a portfolio strategy, industrial projects, or any management decision—the *Markowitz mean/variance* measure is defined as:
    
    \[
    MV_{\alpha}(X) = E[X] - \frac{\alpha}{2} \text{VAR}(X)
    \]
    
    where:
    
    \[
    \text{VAR}(X) = E\left[(X - E[X])^2\right]
    \]
    
    is the variance of the random variable, and \( \alpha \) is a positive number.

For any value of \( \alpha \), you can check that assessing previous games in terms of mean and variance will rank them, with the largest standard deviation corresponding to the worst game and the smallest standard deviation corresponding to the best game. 

The Markowitz mean-variance approach was a highly successful instrument for finding optimal portfolio strategies.
It can also be used as a risk assessment measure.
However, since we are more interested in the downside risks, we consider risk measures defined for the random variable \( L = -X \), where \( X \) represents returns.

!!! definition

    The *Markowitz risk measure* is defined as:

    \[
      RMV_{\alpha}(L) = E[L] + \frac{\alpha}{2} \text{VAR}(L)
    \]

    where \( L \) is a square integrable loss profile.

!!! proposition

    The Markowitz risk measure satisfies the following properties:

    1. **Cash-invariance**: For every loss profile \( L \) and \( m \in \mathbb{R} \),

        \[
          RMV_{\alpha}(L - m) = RMV_{\alpha}(L) - m.
        \]
    
    2. **Convexity**: For any two loss profiles \( L_1, L_2 \) and \( \lambda \in [0, 1] \),
       
        \[
          RMV_{\alpha}(\lambda L_1 + (1 - \lambda)L_2) \leq \lambda RMV_{\alpha}(L_1) + (1 - \lambda)RMV_{\alpha}(L_2) \leq \max \left\{ RMV_{\alpha}(L_1), RMV_{\alpha}(L_2)\right\}.
        \]
    
    3. **Law Invariance**: If two loss profiles \( L_1 \) and \( L_2 \) have the same CDF, then:
       
        \[
          RMV_{\alpha}(L_1) = RMV_{\alpha}(L_2).
        \]
    
  

??? proof 

    1. **Cash-invariance:** For every \( m \in \mathbb{R} \), and loss \( L \), it holds:

        \[
          \begin{align*}
             RMV_{\alpha}(L-m) & = E[L-m] + \frac{\alpha}{2} E\left[\left(L-m-E[L-m]\right)^2\right]\\
                               & = E[L] + \frac{\alpha}{2} E\left[\left(L - E[L]\right)^2\right] - m = RMV_{\alpha}(L) - m
          \end{align*}
        \]
       
    2. **Convexity:** Let \( 0 \leq \lambda \leq 1 \) and \( L_1 \) and \( L_2 \) be two loss profiles. 

        Since the function \( x \mapsto x^2 \) is convex, it follows that:

        \[
          \begin{align*}
             \left(\lambda L_1 + (1-\lambda)L_2 - E[\lambda L_1 + (1-\lambda)L_2]\right)^2 
              &=\left(\lambda(L_1 - E[L_1]) + (1-\lambda)(L_2 - E[L_2])\right)^2\\
              &\leq \lambda \left(L_1 - E[L_1]\right)^2 + (1-\lambda)\left(L_2 - E[L_2]\right)^2
          \end{align*}
        \]
       
        Taking expectation, it follows that:
       
        \[
          \text{VAR}(\lambda L_1 + (1-\lambda)L_2) \leq \lambda \text{VAR}(L_1) + (1-\lambda) \text{VAR}(L_2)
        \]
       
        showing that:
        
        \[
          \begin{align*}
             RMV_{\alpha}(\lambda L_1 + (1-\lambda)L_2) & = \lambda E[L_1] + (1-\lambda)E[L_2] + \frac{\alpha}{2} \text{VAR}(\lambda L_1 + (1-\lambda)L_2)\\
              &\leq \lambda\left(E[L_1] + \frac{\alpha}{2} \text{VAR}(L_1)\right) + (1-\lambda)\left(E[L_2] + \frac{\alpha}{2} \text{VAR}(L_2)\right)\\
              & = \lambda RMV_{\alpha}(L_1) + (1-\lambda)RMV_{\alpha}(L_2)\\
              & \leq \max \left\{ RMV_{\alpha}(L_1), RMV_{\alpha}(L_2) \right\}
          \end{align*}
        \]
    
    3. **Law Invariance:** For the last assertion, let \( L_1 \) and \( L_2 \) be such that \( F_{L_1} = F_{L_2} \).
      It follows that:
      
        \[
        \begin{align*}
           RMV_{\alpha}(L_1) & = \int_{\mathbb{R}} x dF_{L_1}(x) + \frac{\alpha}{2}\int_{\mathbb{R}} \left[x - \int_{\mathbb{R}}x dF_{L_1}(x)\right]^2 dF_{L_1}(x) \\
              & = \int_{\mathbb{R}} x dF_{L_2}(x) + \frac{\alpha}{2}\int_{\mathbb{R}} \left[x - \int_{\mathbb{R}}x dF_{L_2}(x)\right]^2 dF_{L_2}(x) \\
              & = RMV_{\alpha}(L_2)
        \end{align*}
        \]
    


### Value at Risk (V@R)

The value at risk (V@R) is a widely used risk assessment measure introduced in the finance industry by JP Morgan around 1995.
However as an instrument for measuring risk, it has been used for centuries in insurrance industry and turns out to be a very well known mathematical concept.
It measures downside risk as follows:


!!! definition

    Let \( L \) be a loss profile. The value at risk (\( V@R_{\alpha} \)) with parameter \( 0 < \alpha < 1 \) is defined as:

    \[
      V@R_{\alpha}(L) = \inf\{m \in \mathbb{R} : P[L > m] \leq \alpha\}.
    \]


This can also be expressed as:

\[
  \begin{align*}
    V@R_{\alpha}(L) & = \inf\{m \in \mathbb{R} : P[L > m] \leq \alpha\}\\
                    & = \inf\{m \in \mathbb{R} : 1-P[L\leq m] \leq \alpha\}\\
                    & = \inf\{m \in \mathbb{R} : F_L(m) \geq 1-\alpha\}
  \end{align*}
\]

where \( F_L(m):= P[L\leq m] \) is the cumulative distribution function (CDF) of \( L \).


![Value at Risk](./../../images/var_dark.svg#only-dark)
![Value at Risk](./../../images/var_white.svg#only-light)


!!! note "Note: Quantile Function"

    Note that the CDF $F_L$ is an increasing function from $0$ to $1$.
    Furthermore, it is right continuous meaning that $F_L(m_n)\downarrow F_L(m)$ for any sequence $m_n \downarrow m$.
    Indeed, let $A_n = \{L \leq m_n\}$ and $A =\{L\leq m\}$, it follows that $A_1\supseteq A_2 \ldots \supseteq A_n \supseteq \ldots$ with $\cap A_n =A$.
    As a consequence of the $\sigma$-additivity of the probability measure, it follows that $P[A_n]\downarrow P[A]$.

    Now, if $F_L$ is strictly increasing and continuous, it has an inverse $F_L^{-1}\colon (0, 1)\to \mathbb{R}$ which is also strictly increasing and continuous.
    Such an inverse is called the quantile of $L$ and denoted by $q_L\colon (0,1)\to \mathbb{R}$.
    It follows that we can write the value at risk in terms of quantile:

    \[
      \begin{align*}
        V@R_{\alpha}(L) & = \inf\{m \in \mathbb{R} : F_L(m) \geq 1-\alpha\}\\
                        & = \inf\{m \in \mathbb{R} : F^{-1}_L(F_L(m)) \geq F^{-1}_L(1-\alpha)\}\\
                        & = \inf\{m \in \mathbb{R} : m \geq F^{-1}_L(1-\alpha)\}\\
                        & = F^{-1}_L(1-\alpha)
      \end{align*}
    \]
    
    In other terms, $V@R_{\alpha}(L)=q_L(1-\alpha)$ is the $1-\alpha$ quantile of the distribution.

    In the case where $F_L$ is not strictly increasing and continuous, we can still define the so called (left) pseudo-inverse or quantile as

    !!! definition "Definition: Quantile"

        The quantile of the random variable $L$ is defined as

        \[
        \begin{equation*}
          \begin{split}
            q_L \colon (0,1) & \longrightarrow \mathbb{R}\\
                        s & \longmapsto q_L(\alpha) = \inf\left\{ m \in \mathbb{R}\colon P\left[ L\leq m \right] \geq s\right\}
          \end{split}
        \end{equation*}
        \]

    The quantile is an increasing and left continuous function for which holds

    \[
      F_L(q_L(s)-) \leq s\leq F_L(q_L(s))  
    \]

The value at risk indicates the amount of cash or liquidity needed to reduce the loss size so that the probability of making losses exceeds \( \alpha \) is small.
Typical values for \( \alpha \) are 5%, 1%, or 0.5%, depending on the horizon.





!!! example

    Let \( \Omega = \{\omega_1, \omega_2, \omega_3, \omega_4\} \) with probabilities \( p = (0.7\%, 3.3\%, 46\%, 50\%) \), and let \( L \) be a loss profile defined as:
    
    \[
    L(\omega) =
    \begin{cases}
    10,000 & \text{if } \omega = \omega_1, \\
    -50    & \text{if } \omega = \omega_2, \\
    -200   & \text{if } \omega = \omega_3, \\
    -1,000 & \text{if } \omega = \omega_4.
    \end{cases}
    \]
    
    The corresponding CDF \( F_L(m) \) is:
    
    \[
    F_L(m) =
    \begin{cases}
    0       & \text{if } m < -1,000, \\
    50\%    & \text{if } -1,000 \leq m < -200, \\
    96\%    & \text{if } -200 \leq m < -50, \\
    99.3\%  & \text{if } -50 \leq m < 10,000, \\
    1       & \text{if } m \geq 10,000.
    \end{cases}
    \]
    
    From this, the quantile function is:
    
    \[
    q_L(x) =
    \begin{cases}
    -1,000 & \text{if } 0 < x \leq 50\%, \\
    -200   & \text{if } 50\% < x \leq 96\%, \\
    -50    & \text{if } 96\% < x \leq 99.3\%, \\
    10,000 & \text{if } 99.3\% < x \leq 1.
    \end{cases}
    \]
    
    Thus:
    \[
    V@R_{5\%} = q_L(95\%) = -200, \quad V@R_{1\%} = q_L(99\%) = -50, \quad V@R_{0.5\%} = q_L(99.5\%) = 10,000.
    \]


!!! note "Note: Practical Computation of Value at Risk"

    Unlike mean-variance risk measures, which involve computing expectations (analytical or via Monte Carlo methods, for instance), the computation of Value at Risk (VaR) is slightly more complex. 
    Even when a random variable has a probability density function, there is generally no analytical form for its quantile function. In cases where the cumulative distribution function (CDF) is strictly increasing and continuous, computing VaR requires inverting the function \( m \mapsto F_L(m) \). This involves solving the equation:

    \[
      F_L(m^\ast) = s
    \]

    where \( m^\ast \) is the quantile we are seeking. This is a classical root-finding problem.

    Most scientific libraries provide methods for root finding, such as Newton's method, the secant method, or more advanced mixed approaches like Brent's method. 
    It is important to note, however, that VaR often focuses on high quantiles (e.g., 0.99 or 0.999) of the CDF, which lie near the boundary of the inverse. This makes the problem particularly challenging, as the derivative of the CDF approaches zero near these limits, testing the bounds of numerical precision. 
    Fortunately, most scientific libraries with statistical functions provide predefined and highly optimized methods for quantile computation. 

    Below, we illustrate this using Python, specifically with `scipy.optimize` and `scipy.stats`.

    ```python title="Computation of value at risk"
    # import libraries
    import numpy as np
    from scipy.stats import norm, t             # Normal and Student distribution
    from scipy.optimize import root, brentq     # root->newton method, brentq->bissecant flavor
    import plotly.graph_objs as go              # professional but easy plotting
    
    # Straightforward quantile computation implementation
    def quantile(cdf, s):
      # definition of the root function(1) 
      def fun(m):
        result = cdf(m) - s
        return result

      # return the root(2)
      result = root(fun, 0)
      return result.x[0]

    # Define two random variables
    X = norm()      # standard normal
    Y = t(df = 2)   # student with 2 as degree of freedom

    # plot the cdf of both

    x = np.linespace(-4, 4, 100)
    y1 = X.cdf(x)
    y2 = Y.cdf(x)

    fig = go.Figure()
    fig.add_scatter(x=x, y=y1, name="normal distribution")
    fig.add_scatter(x=x, y=y2, name="student distribution")
    fig.update_layout(title = 'CDF of normal and student')
    fig.show()

    # compute the var 0.01 and 0.01 for each

    print(f"""
    1% V@R for Normal:\t{quantile(X.cdf, 0.99)}
    0.01% V@R for Normal:\t{quantile(X.cdf, 0.999)}
    1% V@R for Student:\t{quantile(Y.cdf, 0.99)}
    0.01% V@R for Student:\t{quantile(Y.cdf, 0.999)}
    """)


    # using the pre programmed `ppf` functions
    print(f"""
    1% V@R for Normal:\t{X.ppf(0.99)}
    0.01% V@R for Normal:\t{X.ppf(0.999)}
    1% V@R for Student:\t{Y.ppf(0.99)}
    0.01% V@R for Student:\t{Y.ppf(0.999)}
    """)

    # You can compare the speed between your implementation and the pre programmed using %timeit
    ```
    {.annotate }

    1.  Find `m` such that `F(m) = s` is equivalent to finding `m` such that `F(m) - s = 0` which is the usual implementation.
    2.  We use here the Newton variant of root optimization problem. It only requires a start point and is usually fast. 
        However it might not converge if the derivative is quite close to `0` so it might not always be adequate.
        Using `brentq`, as a bissecant type, requires to provide two bounds `a<b` within which that root shall be found. In particular it should hold that `fun(a)` has a different sign as `fun(b)`.
        Both have advantages and inconvenience.


As for mean-variance, value at risk also fulfills some properties

!!! proposition

    The Value at Risk V@R satisfies the following properties:

    1. **Cash-invariance**: For every loss profile \( L \) and \( m \in \mathbb{R} \),

        \[
          V@R_{\alpha}(L - m) = V@R_{\alpha}(L) - m.
        \]
    
    2. **Monotonicity**: For any two loss profiles \( L_1, L_2 \) with \(L_1(\omega) \leq L_2(\omega)\) it holds,
       
        \[
          V@R_{\alpha}(L_1) \leq V@R_{\alpha}(L_2).
        \]
    
    3. **Law Invariance**: If two loss profiles \( L_1 \) and \( L_2 \) have the same CDF, then:
       
        \[
          V@R_{\alpha}(L_1) = V@R_{\alpha}(L_2).
        \]
    
??? proof

    1. **Cash-invariance:** For every \( m \in \mathbb{R} \), and loss \( L \), it holds with variable change $\hat{m} = \tilde{m} - m$:

        \[
          \begin{align*}
             V@R_{\alpha}(L-m) & = \inf\left\{ \tilde{m} \in \mathbb{R} \colon P[L-m>\tilde{m}] \leq \alpha \right\}\\
                            & = \inf \left\{ \hat{m} - m \colon P[L>\hat{m}] \leq \alpha  \right\}\\
                            & = \inf \left\{ \hat{m} \colon P[L>\hat{m}] \leq \alpha  \right\} - m = V@R_{\alpha}(L) - m
          \end{align*}
        \]
       
    2. **Monotonicity:** Let \( L_1 \leq L_2 \) be two loss profiles.

        For any $m$, it holds

        \[
            \left\{ \omega \colon L_1(\omega)\leq m \right\} \supseteq \left\{ \omega \colon L_2(\omega)\leq m \right\}
        \]

        showing that for every $m$ we have $P[L_1\leq m] \geq P[L_2 \leq m]$.
        Hence, we have

        \[
            \left\{ m \in \mathbb{R} \colon P\left[ L_1\leq m \right]\geq 1-\alpha \right\} \subseteq  \left\{ m \in \mathbb{R} \colon P\left[ L_2\leq m \right]\geq 1-\alpha \right\}
        \]

        showing that the infimum of the the left handside is smaller than the infimum of the right hand side, that is $V@R_{\alpha}(L_1)\leq V@R_{\alpha}(L_2)$. 

    
    3. **Law Invariance:** This follows immediately since the value at risk depends only on the CDF.
    


## Sound Properties?

Both risk assessments make sense and have a certain appeal. Let us discuss some of the properties they fulfill:

* **Cash Invariance:** Given a risk assessment instrument \( L \mapsto R(L) \), being cash invariant means that \( R(L - m) = R(L) - m \).
    This property is appreciated by economists and regulators as it confers a clear monetary interpretation to risk assessment.
    Regulators typically require financial institutions to maintain their total risk below zero.
    For a financial institution with a loss exposure \( L \), the question is how much liquidity (or cash) must be held to reduce the overall risk to below zero.
    With cash \( m \) and risky exposure \( L \), the resulting loss profile is \( L - m \), with a risk equal to \( R(L - m) \).
    A risk assessment below zero implies that \( m \geq R(L) \). In other words, the minimal cash requirement to make the risky exposure acceptable is \( m = R(L) \).

* **Law Invariance:** Law invariance is important because, even though we work with random variables, in practice we observe only their realizations and approximate their CDF.
    Hence, a risk assessment instrument should depend solely on the CDF of the loss profile.

* **Monotonicity:** Monotonicity means that if the loss profile of one position is always greater than another, i.e., it results in higher losses in all scenarios, then its risk should also be higher.

* **Diversification (Convexity):** Diversification implies that combining two risky assets (a convex combination) should result in a risk lower than the worst of the two individual risks.


| Property        | \( MVR_{\alpha} \) | \( V@R_{\alpha} \) |
|:----------------|:------------------:|:------------------:|
| Cash Invariance | :material-check-all: | :material-check-all: |
| Law Invariance  | :material-check-all: | :material-check-all: |
| Monotonicity    | :material-close:    | :material-check-all: |
| Diversification | :material-check-all: | :material-close:    |

!!! warning "Warning: Value at Risk might lead to Concentration"

    Value at Risk (VaR) can, in some cases, counteract diversification.
    The primary reason is that the quantile is just a single point on the CDF of the loss distribution and does not account for the full risk in the tail.
    The following example illustrates this concentration issue:

    In the first scenario, you lend \( 1000 \) RMB to a friend, expecting repayment in one year with \( 4\% \) interest.  
    - If the friend repays the loan, you gain \( 40 \) RMB.  
    - If the friend defaults, you lose \( 1000 \) RMB.  
    - Assume the probability of default is \( 4\% \).  

    The loss profile can be represented as:  
    
    \[
        L = 
        \begin{cases}
            -40 & \text{with probability } 96\% \\
            1000 & \text{with probability } 4\%
        \end{cases}
    \]

    This results in the following CDF and quantile function:  
    
    \[
        \begin{align*}
            F_L(m) & = \begin{cases}
                0 & \text{for } m < -40 \\
                96\% & \text{for } -40 \leq m < 1000 \\
                100\% & \text{for } m \geq 1000
            \end{cases} \\
            q_L(s) & = \begin{cases}
                -40 & \text{for } 0 < s \leq 96\% \\
                1000 & \text{for } s > 96\%
            \end{cases}
        \end{align*}
    \]

    The Value at Risk at the \( 5\% \) level is:  
    
    \[
        V@R_{5\%}(L) = q_L(95\%) = -40
    \]

    Now, consider diversifying your exposure by lending \( 500 \) RMB to two independent friends:  
    
    \[
        L = 
        \begin{cases}
            -40 & \text{with probability } 92.16\% \\
            480 & \text{with probability } 7.68\% \\
            1000 & \text{with probability } 0.16\%
        \end{cases}
    \]

    This diversification reduces the probability of large losses to \( 0.16\% \), but introduces a medium loss of \( 480 \) RMB with a \( 7.68\% \) probability.  

    The CDF and quantile function for this case are:  
    
    \[
        \begin{align*}
            F_L(m) & = \begin{cases}
                0 & \text{for } m < -40 \\
                92.16\% & \text{for } -40 \leq m < 480 \\
                99.84\% & \text{for } 480 \leq m < 1000 \\
                100\% & \text{for } m \geq 1000
            \end{cases} \\
            q_L(s) & = \begin{cases}
                -40 & \text{for } 0 < s \leq 92.16\% \\
                480 & \text{for } 92.16\% < s \leq 99.84\% \\
                1000 & \text{for } s > 99.84\%
            \end{cases}
        \end{align*}
    \]

    The Value at Risk at the \( 5\% \) level is:  
    
    \[
        V@R_{5\%}(L) = q_L(95\%) = 480
    \]

    In this case, the Value at Risk increases from \( -40 \) to \( 480 \), contradicting the expectation that diversification reduces risk.
    The primary reason is that, in the non-diversified scenario, all potential losses are concentrated in the tail of the distribution beyond the chosen quantile. In other words, Value at Risk is *blind* to the magnitude of losses beyond the selected quantile level.

Even though both instruments (mean-variance risk and Value at Risk) have intuitive appeal and practical applications, closer scrutiny reveals that each violates one or more fundamental properties expected of a robust risk measure.


# Itô's Formula

This Section is dedicated to the celebrated Itô's Formula.
To begin with, let us state a result about an analogue to Lebesgue's dominated convergence for stochastic integral.

!!! proposition "Proposition: Lebegue's Stochastic Dominated Convergence"
    Let $X$ be a semi-martingale.
    For $(H^n)$ sequence in $\mathcal{L}^{loc}(X)$ converging point-wise to $0$, if $\left\vert H^n\right\vert\leq H$ for $H \in \mathcal{L}^{loc}(X)$, then it follows that $\int_{}^{} H^n d X \to 0$ in ucp.

    In particular, if $H$ is a continuous adapted process, then, $\int_{}^{} H^n d X$ converges uniformly in probability on $[0,t]$ to $\int_{}^{} HdX$ for $H^n=H_0+\sum H_{t^n_{k-1}}1_{(t_{k-1}^n,t^n_{k}]}$ and for a subdivision $\Pi^n=\{0=t_0^n< \cdots< t_{k_n}^n\nearrow \infty\}$ whose mesh is converging to $0$.


!!! proof
    Let $X=M+A$.
    It is enough to show the convergence to zero uniformly on compact in probability for both $\int_{}^{} H^n dM$ and $\int_{}^{} H^ndA$.
    Defining $\tau^m = \inf\{t \colon |M_t|>m \text{ or }\int_{0}^{t} |H| d|A| >m \text{ or } \int_{0}^{t} H^2 d\langle M\rangle >m\}$ provides a localizing sequence of stopping times.
    Hence according to the localization's Lemma, we may show the theorem by assuming that $M$, $\int |H| d|A|$ and $\int H^2 d\langle M\rangle$ are all uniformly bounded.
    By the fact that $|H^n|\leq H$, the same holds uniformly for $\int_{}^{} |H^n| d|A|$ and $\int_{}^{} (H^n)^2 d\langle M\rangle$.
    By Lebesgue's dominated convergence and Itô's isometry, it follows that

    \[ 
    \begin{equation*}
        \int_{0}^{t}H^n dM \xrightarrow[ n\to \infty]{L^2}0 \quad \text{and} \quad \int_{0}^{t}H^n dA \xrightarrow[ \to \infty]{L^1} 0 
    \end{equation*}
    \]

    From Doob's maximal inequalities, follows that $\sup_{s\leq t}(\int_{0}^{s}H^n dM)^2 \to 0$ in $L^1$ and therefore $P$-almost surely.
    Since $|\int_{0}^{s}H^n dA|\leq \int_{0}^{s}|H^n|d|A|\leq \int_{0}^{t}|H^n|d|A|\to 0$ in $L^1$, it follows that $\sup_{s\leq t}\int_{0}^{s}H^n dA\to 0$ $P$-almost surely, hence in probability for every $t$, ending the proof.

!!! theorem "Theorem: Product Rule"
    Let $X$ and $Y$ be semi-martingales, then it holds

    \[ 
    \begin{equation}\label{eq:itomonome}
        \begin{split}
            XY&=X_0Y_0+\int XdY+\int YdX+\int d\langle X,Y\rangle\\
              &=X_0Y_0+\int XdY+\int YdX+\langle X,Y\rangle
        \end{split}
    \end{equation}
    \]

    In particular

    \[ 
    \begin{equation}\label{eq:itoquadrat}
        \begin{split}
            X^2&=X_0+2\int X dX+\int d\langle X\rangle=X_0+2\int X dX+\langle X\rangle
        \end{split}
    \end{equation}
    \]

    Furthermore, for any $n\geq 2$ it holds

    \[
      X^n = X_0^n + \int n X^{n-1}dX + \frac{1}{2}\int n(n-1)X^{n-2}d\langle X \rangle
    \]

!!! proof
    Note that from the polar relation $XY=((X+Y)^2-(X-Y)^2)/4$ and the linearity of the relation \eqref{eq:itoquadrat}, it is enough to show \eqref{eq:itoquadrat}.
    Let $(\Pi^n)$ be a sequence of subdivisions whose mesh is converging to $0$.
    It follows that

    \[ 
    \begin{equation*}
        \begin{split}
            X^2-X_0^2 & = 2\sum X_{t_{k-1}}\left( X_{t_k\wedge t}-X_{t_{k-1}\wedge t} \right)+ \sum \left( X_{t_{k}\wedge t}-X_{t_{k-1}\wedge t} \right)^2\\
                      & = 2\int_{}^{} X^n dX+\left[ X \right]^{\Pi^n}
        \end{split}
    \end{equation*}
    \]

    where $X^n=X_0+\sum X_{t_{k-1}}1_{(t_{k-1},t_k]}$.
    Since $X$ is continuous, according to Lebesgue's stochastic dominated convergence, it follows that $2\int X^n dX\to 2\int_{}^{}X dX$ in ucp.
    On the other hand, according to the quadratic variation proposition, it holds that $[X]^{\Pi^n}\to \langle X\rangle$ in ucp.
    Hence, up to a rapid subsequence, we get the result point-wise.

    We show per induction on $n\geq 2$ the product formula.
    For $n=2$, this is the previous result.
    Assume that it holds for any $m \leq n$ and we show it for $n\geq 3$.
    Define $Y = X^{n-1}$.
    According to the product rule it holds 

    \[
      X^n = XY = X_0^n + \int X dX^{n-1} + \int X^{n-1}dX + \langle X, Y\rangle
    \]

    However by induction assumption it holds 

    \[ 
    \begin{align*}
        \int XdX^{n-1} & = \int Xd\left( X_0+(n-1)\int X^{n-2}dX+\frac{(n-1)(n-2)}{2}\int X^{n-3}d\langle X\rangle \right)\\
                       & = (n-1)\int X^{n-1}dX+\frac{(n-1)(n-2)}{2}\int X^{n-2}d\langle X\rangle
    \end{align*}
    \]
    
    and since the covariation where one of the process is of bounded variation is $0$, for the covariation we get
    
    \[ 
    \begin{align*}
        \langle X,X^{n-1}\rangle&=\left\langle X,X_0+(n-1)\int X^{n-2}dX+\frac{(n-1)(n-2)}{2}\int X^{n-3}d\langle X\rangle\right\rangle\\
        & = (n-1)\langle \int dX, \int X^{n-2}dX \rangle\\
        &=(n-1)\int_{}^{}X^{n-2}d\langle X\rangle.
    \end{align*}
    \]

    Substituting these two relations in the product formula yields the result.


!!! remark

    Note that a similar proof also shows 

    \[ 
      \begin{align}
        X^nY^m & = X_0^nY_0^m+n\int_{}^{}X^{n-1}Y^m dX+m\int X^nY^{m-1}dY\\
          & \quad \quad \quad +\frac{n(n-1)}{2}\int_{}^{} X^{n-2}Y^m d\langle X\rangle+nm\int_{}^{} X^{n-1}Y^{m-1}d\langle X,Y\rangle+\frac{m(m-1)}{2}\int_{}^{} X^{n}Y^{m-2}d\langle Y\rangle
      \end{align}
    \]


The product rule formula can immediately be reformulated into Ito's formula.

!!! theorem
    Let $X$ and $Y$ be semi-martingale, and $f:\mathbb{R}^2\to \mathbb{R}$ be a twice continuously differentiable function.

    Then it holds

    \[ 
    \begin{align}
        f(X,Y) & = f(X_0,Y_0)+\int_{}^{}\partial_x f(X,Y)dX+\int_{}^{} \partial_y f(X,Y) dY \\
          & \quad \quad \quad +\frac{1}{2}\int_{}^{} \partial_{xx} f(X,Y)d\langle X\rangle +\int_{}^{} \partial_{xy}f(X,Y)\langle X,Y\rangle+\frac{1}{2}\int_{}^{} \partial_{yy}f(X,Y) d\langle Y\rangle
    \end{align}
    \]

    In particular, if $f$ only depends on $x$, we get the more classical version

    \[ 
    \begin{equation}\label{eq:ito}
        f(X)=f(X_0)+\int_{}^{} f^\prime (X)dX+\frac{1}{2}\int_{}^{} f^{\prime\prime}(X)d\langle X\rangle
    \end{equation}
    \]

!!! proof

    Obviously, Itô's formula holds in the case where $f(x,y) = x^n y^m$ and by linearity for any multivariate polynomials $f(x,y) = \sum_{0\leq n\leq N, 0\leq m\leq M} a_{n,m} x^n y^m$.
    We will show the unidimensional case, the argumentation for the two or $n$-dimensional case is just a simple adaptation of the argumentation.
    Note that by localization, we can show the statement for $X$ uniformly bounded by $K$.
    We denote by $\|\cdot \|_{K}$ the supremum norm on $[-K, K]$.
    By density of polynomials in the set of $C^2$ functions on compact, for any $n$ we can find a polynomial $P_n$ such that

    \[
      \left\Vert P_n-f\right\Vert_K+\left\Vert P^\prime -f^\prime\right\Vert_K+\left\Vert P^{\prime\prime}-f^{\prime \prime}\right\Vert_K<1/n
    \]

    It follows that

    \[
      \begin{multline*}
        \left|f(X) - f(X_0) - \int f^\prime(X)dx - \frac{1}{2}\int f^{\prime\prime}(X) d\langle X\rangle\right| \\
        \leq \left| f(X) - P_n(X)\right| + \left|f(X_0) - P_n(X_0)\right| + \left|\int \left( f^\prime(X) - P_n^\prime(X) \right)dX\right| + \int \left| f^{\prime\prime}(X) - P_n^{\prime\prime}(X)\right| d\langle X\rangle
      \end{multline*}
    \]

    The first two differences can be made arbitrarily small.
    As for the stochastic integral difference, the uniform convergence on compact in probability follows from Lebesgue's stochastic dominated convergence.
    Hence, up to a rapid subsequence, we have almost sure convergence.
    Finally the Lebesgues-Stieltjes integral converges to $0$ due to Lebesgues' dominated convergence.


Ito's formula as we will see later is the door to stochastic differential equations as well as the link between stochastic analysis and partial differential equations.
Note that we often use the differential notation

\[
  \begin{align*}
    df(X) & = f^\prime(X) dX + \frac{1}{2}f^\prime\prime(X) d \langle X \rangle\\
          & = f^\prime dX + \frac{1}{2}f^{\prime\prime}d\langle X\rangle\\
    df(X,Y) & = \partial_x f(X,Y)dX + \partial_y f(X,Y) dY \\
            & \quad \quad \quad + \frac{1}{2}\partial_{xx}f(X,Y)d \langle X \rangle + \partial_{xy}f(X,Y)d \langle X,Y \rangle + \frac{1}{2}\partial_{yy}f(X,Y)d \langle Y\rangle\\
            & = \partial_x f dX + \partial_y fdY + \frac{1}{2}\partial_{xx} f d\langle X\rangle +\partial_{xy}f d\langle X,Y\rangle + \frac{1}{2}\partial_{yy}f d\langle Y \rangle
  \end{align*}
\]


Note also that by taking $Y_t = t$ which is a semi-martingale without local martingale term where $dY = dt$ and $d\langle Y\rangle = d\langle X, Y\rangle =0$ we obtain a very common version of Itô's formula for $f:[0, \infty)\times \mathbb{R} \to \mathbb{R}$ which is $C^{1,2}$ as follows

\[
  df(t, X) = \partial_t f dt + \partial_x f dX + \frac{1}{2}\partial_{xx} f d\langle X\rangle
\]


!!! example 

    Let us have a look at a classical situation that provides a hint as to the relation between PDEs and Stochastics.
    Let $\mu, \sigma \colon \mathbb{R}\to \mathbb{R}$ be two smooth functions and suppose that there exists a semi martingale $X$ such that
    
    \[
    X = X_0 + \int \mu(X) dt + \int \sigma(X) dW
    \]
    
    where $W$ is the Brownian motion.
    In other terms, $X$ solves the stochastic differential equation 
    
    \[
     dX = \mu(X) dt +\sigma(X) dW
    \]

    Note that

    \[
        d\langle X\rangle = \sigma^2(X)d\langle W\rangle = \sigma^2(X)dt
    \]

    Given a $C^{1,2}$ function $u \colon [0, \infty) \times \mathbb{R}$, using Itô's formula we get

    \[
        \begin{align*}
            du(t, X_t) 
                & = \partial_t u(t, X_t)dt + \partial_x u(t, X_t)dX_t + \frac{1}{2}\partial_{xx}u(t, X_t)d\langle X\rangle_t\\
                & = \partial_t u(t, X_t)dt +\partial_x u(t, X_t)\left(\mu(X_t)dt + \sigma(X_t)dW_t\right) + \frac{\sigma^2(X_t)}{2}\partial_{xx}u(t, X_t) dt\\
                & = \left(\partial_t +\underbrace{\mu(X_t)\partial_x +\frac{\sigma^2(X_t)}{2}\partial_{xx}}_{=: \mathcal{L}^X(X_t)}\right)u(t, X_t)dt + \sigma(X_t)\partial_x u(t, X_t)dW
        \end{align*}
    \]

    Defining the differential operator $\mathcal{L}^X(x)$ &mdash; also called **infinitesimal generator** of $X$ &mdash; on $C^{1,2}$ functions $f$:

    \[
        \mathcal{L}^X(x) f(t, x) := \mu(x)\partial_x f(t,x) + \frac{\sigma^2(x)}{2}\partial_{xx}f(t,x)
    \]

    We can rewrite the result of the Itô's formula as follows

    \[
        du = \underbrace{\left(\partial_t + \mathcal{L}^X\right) u dt}_{\text{Bounded variations}} + \underbrace{\sigma \partial_x u dW}_{\text{Local martingale}}
    \]

    Suppose that $u$ is in particular a solution of the following PDE

    \[
        \begin{equation*}
            \begin{cases}
                \begin{aligned}
                \partial_t u(t, x) + \mathcal{L}^X(x) u(t, x) & = 0\\
                \\
                u(0, x) & = X_0
                \end{aligned}
            \end{cases}
        \end{equation*}
    \]

    then it follows that

    \[
        du = \left(\partial_t + \mathcal{L}^X\right) u dt +\sigma \partial_x u dW = \sigma \partial_x dW
    \]

    and therefore $u(t, X_t)$ is a local martingale.

!!! example "Geometric Brownian Motion"

    In finance, the bank account $B$ pays interest $r \Delta$ over the period $\Delta$.
    It follows that the value of the bank account at time $t+\Delta$ is given by $B_{t+\Delta} = B_t (1+ r\Delta)$.
    In differential form it follows that

    \[
        dB_t \approx B_{t+\Delta} - B_t = B_t r \Delta \approx B_t r dt
    \]

    With one RMB at time $0$, that is, $B_0 = 1$, this stochastic differential equation is a simple (eventually stochastic) ODE $dB = B r dt$ with solution

    \[
        B = B_0 \exp\left(\int r dt\right) = e^{\int r dt}
    \]

    On the other hand, looking at a risky asset $S$, such as a stock price,, the return between $t$ and $t+\Delta$ might be subject to uncertainty.
    In this case, the stock price $S_{t+\Delta} = S_t(1+R_{t+\Delta})$ where

    \[
        R_{t+\Delta} = \mu \Delta + \sigma \sqrt{\Delta} \xi_t
    \]

    where $\xi_t \sim \mathcal{N}(0, 1)$ is some random noise, $\mu$ is the certain return on the asset over the short period while $\sigma$ is the volatility, or amount of uncertainty.
    For the differential form we have a problem as how $\sigma \sqrt{\Delta}\xi_t$ scales as $\Delta$ is infinitesimaly small.
    However, from the properties of the brownian motion, it hodls that $\sqrt{\Delta}\xi_t \sim \mathcal{N}(0, \Delta) \sim W_{t+\Delta} - W_t$.
    We can therefore reformulate the differential evolution of the stock price as

    \[
        dS = S\left(\mu dt + \sigma dW\right)        
    \]

    In this case we are no longer facing an ODE but a stochastic differential equation as for the $dW$ term.
    It is not clear as if there exists a solution $S$ that satisfies this stochastic differential equation.
    However in this case, we can guess the solution as follows.
    Let $X$ be the semi martingale defined as

    \[
        X = \int \left( \mu -\frac{\sigma^2}{2}\right)dt + \int \sigma dW
    \]

    Applying Itô's formula to $f(X) = \exp(X)$, knowing that $f = f^\prime= f^{\prime\prime}$ we get

    \[
        \begin{align*}
            df(X) 
                & = f^\prime(X)dX + \frac{1}{2}f^{\prime \prime}(X)d\langle X\rangle\\
                & = f(X)\left(\underbrace{dX}_{=(\mu-\sigma^2/2) dt + \sigma dW} + \frac{1}{2}\underbrace{d\langle X\rangle}_{= \sigma^2 dt}\right)\\
                & = f(X)\left(\left(\mu dt - \frac{1}{2}\sigma^2 + \frac{1}{2}\sigma^2\right)dt + \sigma dW\right)\\
                & = f(X)(\mu dt + \sigma dW)
        \end{align*}
    \]

    We deduce that 

    \[
        S_t = S_0 \exp \left( \int \left(\mu - \frac{\sigma^2}{2}\right)dt + \int \sigma dW\right)
    \]

    satisifies the stochastic differential equation of the stock price evolution.

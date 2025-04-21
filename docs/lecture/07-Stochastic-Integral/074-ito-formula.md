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

!!! example "Example: Financial Market"
    The financial market is modeled by a bank account $B$ and stock prices $S$.
    To simplify, we consider that we only have one stock price.
    Hereby $B_t$ represents the value at time $t$ of one RMB at time $t$ after interest rate and $S_t$ represents the value of the stock price at time $t$.
    The most simple model of dynamic evolution of the bank account and the stock price are given by the stochastic differential equations

    \[
    \begin{equation}
        dB=r B dt\text{, with }B_0=1 \quad \text{and}\quad dS=S(\mu dt+\sigma dW)\text{, with }S_0>0
    \end{equation}
    \]

    where $r$ represents the evolution of the interest rate in the bank and $\mu$ and $\sigma>0$ represent the drift and volatility of the stock price respectively.
    The basic intuition behind these stochastic evolutions is that over a small interval $[t,t+\Delta]$ for a value $B_t$ on the bank account, the bank will pay out an interest $r_t$ so that after $\Delta$ amount of time you will own $B_t(1+r_t \Delta)$.
    In other terms, the value of the bank account evolves like

    \[
    B_{t+\Delta}=B_t(1+r_t \Delta) \quad \text{that is}\quad B_{t+\Delta}-B_t=r_t B_t \Delta 
    \]

    As for the stock price, if we denote $R_{t+\Delta}=(S_{t+\Delta}-S_t)/S_t$ the returns of the stock over a small interval, it holds $S_{t+\Delta}=S_{t}(1+R_{t+\Delta})$ or $(S_{t+\Delta}-S_t)=S_tR_{t+\Delta}$.
    So the idea is to model the returns by assuming that they are iid and such that 

    \[
    R_{t+\Delta}=\mu_t \Delta +\sigma_t\sqrt{\Delta} Z, \quad \text{where}\quad Z\sim \mathcal{N}(0,1)
    \]

    In other terms the stock price, as the bank account, has a predictable evolution or drift given by $\mu_t$ over the interval.
    However, it is also subject to random movement around this mean given by a normal distribution scaled by the volatility of the market $\sigma_t$ as well as the time interval considered.
    Recasting, it follows that

    \[
    S_{t+\Delta}-S_t=S_t(\mu_t \Delta+\sigma_t \Delta Z)=S_t\left( \mu_t\Delta+\sigma_t\left(W_{t+\Delta}-W_t \right)\right)
    \]

    The main question though, is whether the stochastic differential equations describing the financial market do have a solution.

    !!! proposition
        Suppose that $r$, $\mu$ and $\sigma$ are locally bounded processes with $\sigma>0$.
        Then, the stochastic differential equations
        
        \[
          \begin{align*}
            dB & = B rdt\\
            dS & = S(\mu dt + \sigma dW)
          \end{align*}
        \]

        have solutions explicitly given by

        \[
        \begin{align}
            B & = \exp\left( \int r dt  \right) \\
            S & = S_0\exp\left( \int \left( \mu-\frac{\sigma^2}{2} \right)dt+\int \sigma dW   \right)
        \end{align}
        \]

    !!! proof
        We just have to check that the process 

        \[
        \begin{align}
            B & = \exp\left( \int r dt  \right) \\
            S & = S_0\exp\left( \int \left( \mu-\frac{\sigma^2}{2} \right)dt+\int \sigma dW   \right)
        \end{align}
        \]

        satisfy the corresponding stochastic differential equations.

        Define $Y=\int r dt$ and $X=\int (\mu-\sigma^2/2)dt+\int \sigma dW$ which are well defined semi-martingales by the assumptions on $r$, $\mu$ and $\sigma$.
        For $f(x)=\exp(x)$, since $f=f^\prime=f^{\prime\prime}$, it follows that $B=f(X)=f^\prime(X)=f^{\prime\prime}(X)$ and $S=S_0f(Y)=S_0f^{\prime}(Y)=f^{\prime\prime}(Y)$.
        Furthermore $dX=rdt$ and $d\langle X\rangle =0$, as well as $dY=(\mu-\sigma^2/2) dt+\sigma dW$ and $d\langle Y\rangle=d\langle \sigma W\rangle=\sigma^2 d\langle W\rangle=\sigma^2 dt$.
        Applying Itô's formula yields

        \[
        \begin{aligned}
            dB = df(X) & = f^\prime(X)dX+\frac{1}{2} f^{\prime\prime}(X)d\langle X\rangle\\
                       & = f(X)rdt\\
                       & = B r dt\\
            dS = S_0df(Y) & = S_0f^{\prime}(Y)dY+\frac{1}{2}S_0 f^{\prime\prime}(Y)d\langle Y\rangle\\
                         & = S_0f(Y)\left(\left( \mu-\frac{\sigma^2}{2} \right)dt+\sigma dW\right)+\frac{1}{2}S_0f(Y)\sigma^2 dt\\
                         & = S_0f(Y)\left( \mu dt+\sigma dW \right)\\
                         & = S\left( \mu dt+\sigma dW \right)
        \end{aligned}
        \]

        which ends the proof.

    In particular, if $\mu=0$, it follows that $dS = \sigma S dW$ showing that

    \[
      \exp \left( \int \sigma dW - \frac{1}{2}\int \sigma^2 dt\right)
    \]

    is a local martingale.

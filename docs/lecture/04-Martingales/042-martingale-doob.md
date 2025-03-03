# Martingales and Doob's Optional Sampling


## Martingales


!!! definition "Definition: Martingale (Sub/Super)"

    A stochastic process $X$ is called a **martingale** if:

    1. $X$ is adapted;
    2. $X$ is integrable, that is, $X_t$ is integrable for every $t$;
    3. $X_s=E[X_t\,|\, \mathcal{F}_s]$ whenever $s\leq t$.

    A process $X$ is called a **super-martingale** if instead of (3) we require:

    3'. $X_s\geq E[X_t\,|\, \mathcal{F}_s]$ whenever $s\leq t$.

    A process $X$ is called a **sub-martingale** if instead of (3) we require:

    3''. $X_s\leq E[X_t\,|\, \mathcal{F}_s]$ whenever $s\leq t$.


!!! remark
    Note that a martingale is, in particular, both a super-martingale and a sub-martingale at the same time.

    Note that since we are working in discrete time, the martingal (sub/super) property can be checked only on each increment, that is $E[\Delta X_t |\mathcal{F}_{t-1}]=E[X_t - X_{t-1}|\mathcal{F}_{t-1}] =0$.



!!! example

    * Given and integrable random variable $\xi$, the process $X = (E[\xi|\mathcal{F}_t])$ defines a martingale.

    * Consider the random walk $S$ from the example in the previous section.
        show that 

        - $p=1/2$, then $S$ is a martingale;
        - $p\geq 1/2$, then $S$ is a sub-martingale;
        - $p\leq 1/2$, then $S$ is a super-martingale.

!!! proposition
    Let $X$ be an adapted process and $\varphi:\mathbb{R}\to \mathbb{R}$ be a measurable function such that $\varphi(X_t)$ is integrable for every $t$.

    - If $X$ is a martingale and $\varphi$ is convex, then $Y=(\varphi(X_t))$ is a sub-martingale.
    - If $X$ is a martingale and $\varphi$ is concave, then $Y=(\varphi(X_t))$ is a super-martingale.
    - If $X$ is a sub-martingale and $\varphi$ is convex and increasing, then $Y=(\varphi(X_t))$ is a sub-martingale.

!!! proof
    Since a process $Y$ is a sub-martingale if and only if $-Y$ is a super-martingale, and $\varphi$ is convex if and only if $-\varphi$ is concave, we only need to prove the first point to get the second.
    Clearly, $Y$ is adapted.
    By assumption, $Y_t$ is integrable for every $t$.
    Finally, using Jensen's inequality for conditional expectation and the martingale property $X_s=E[X_t|\mathcal{F}_s]$, it follows that:

    \[
      E[Y_t|\mathcal{F}_s]=E[\varphi(X_t)|\mathcal{F}_s]\geq \varphi(E[X_t|\mathcal{F}_s])=\varphi(X_s)=Y_s.
    \]

    If $X$ is a sub-martingale and $\varphi$ is convex and increasing, then:

    \[
    E[Y_t|\mathcal{F}_s]=E[\varphi(X_t)|\mathcal{F}_s]\geq \varphi(E[X_t|\mathcal{F}_s])\geq \varphi(X_s)=Y_s,
    \]

    showing the sub-martingale property and therefore proving the third point.


Clearly the notion of martingale is very minimal.
A martingale can be seen as a *noise* process (in a vague sense) in so far that it moves in any possible direction but in average like now.
Sup-martingale are trending downwards while sub-martingales are trending upwards.
This intuitive notion and the centrality of this fact can be inspected in the following Doob Meyer Theorem.

!!! theorem "Theorem: Doob Meyer Decomposition"

    Let $X$ be an adapted and integrable process.
    Then there exists a unique decomposition:

    \[
      X=M+A,
    \]

    where $M$ is a martingale and $A$ is a predictable process with $A_0=0$.
    This decomposition is called the *Doob decomposition*.

    Furthermore, $X$ is a sub-martingale or super-martingale if and only if $A$ is increasing or decreasing respectively.

!!! proof

    Assume that we had such a decomposition, then it follows that $M = X - A$ is a martingale.
    By the martingale property and predictability of $A$ we get

    \[
      0= E[\Delta M_{t+1}|\mathcal{F}_t] = E[\Delta X_{t+1}|\mathcal{F}_t] - E[\Delta A_{t+1}|\mathcal{F}_t] =  E[\Delta X_{t+1}|\mathcal{F}_t] -(A_{t+1} - A_t)
    \]

    This provides us a recursive way to define $A$ as follows

    \[
      \begin{equation*}
        \begin{cases}
            A_0 &= 0\\
            A_t &=A_{t-1}+ E[X_t-X_{t-1}|\mathcal{F}_{t-1}] \quad \text{for}\quad t\geq 1
        \end{cases}
      \end{equation*}
    \]

    It is immediate to check by induction that $A$ is predictable and by definition $M:=X - A$ is a martingale providing the decomposition.

    As for the uniqueness, let $X = M+A = \tilde{M}+\tilde{A}$ where $M$ and $\tilde{M}$ are martingales and $A$ and $\tilde{A}$ are predictable processes starting at $0$.
    It follows that $M - \tilde{M} = \tilde{A}-A$ is a predictable martingale.
    Hence by martingale property and then predictability it holds that $M_{t_1}-\tilde{M}_{t-1} = E[M_t - \tilde{M}_{t} |\mathcal{F}_{t-1}] = M_t - \tilde{M}_{t}$ showing that 

    \[
      M_t - \tilde{M}_{t} = M_{t-1} - \tilde{M}_{t-1} = \cdots = M_0 - \tilde{M}_0 = \tilde{A}_0 - A_0 = 0
    \]

    We deduce that $M=\tilde{M}$ and $A = \tilde{A}$.

    The assertions about super and sub martingales are immediate to get.


## Stochastic integration with respect to a martingale

!!! theorem "Doob's Optional Sampling Theorem, Modern Version"

    Let $H$ be a predictable process.
    The following holds true:

    1. If $X$ is a martingale and $H\bullet X_t$ is integrable for every $t$, then $H\bullet X$ is a martingale.
    2. If $X$ is a super-martingale or sub-martingale, $H\geq 0$, and $H\bullet X_t$ is integrable for every $t$, then $H\bullet X$ is a super-martingale or sub-martingale.

!!! proof
    Suppose that $X$ is a martingale and $H$ is such that $H\bullet X$ is integrable.
    Adaptiveness is immediate.
    From $H$ being predictable, that is, $H_{t+1}$ is $\mathcal{F}_t$-measurable, and $X$ being a martingale, that is, $E[X_{t+1}-X_t|\mathcal{F}_t]=E[X_{t+1}|\mathcal{F}_t]-X_t=0$, it follows that:

    \[
      E\left[ \Delta H\bullet X_{t+1}|\mathcal{F}_t \right]=E\left[ H_{t+1} \Delta X_{t+1}|\mathcal{F}_t \right]= H_{t+1}E\left[ \Delta X_{t+1}|\mathcal{F}_t \right]= 0.
    \]

    The argument in the sub-martingale case is similar, using the fact that $H_{t+1}\geq 0$ and $E[X_{t+1}-X_t|\mathcal{F}_t]=E[X_{t+1}|\mathcal{F}_t]-X_t\geq 0$ and similarly for the super-martingale case.


!!! remark
    Note that in this theorem, if there exists a constant $C>0$ such that $|H_t|<C$ for every $t$, then $H\bullet X_t$ is integrable for every $t$ as soon as $X$ is integrable.
    Indeed,

    \[
      E\left[ |H\bullet X_t| \right]\leq E\left[ |H_0 X_0| \right]+\sum_{s=1}^tE\left[ |H_t||X_{t}-X_{t-1}| \right]\leq 2C\sum_{s=0}^t E[|X_t|]<\infty.
    \]

    So the assumption that $|H\bullet X_t|$ is integrable for every $t$ can be replaced by $H$ being uniformly bounded.

This remark allows us to formulate the original Doob's sampling theorem.

!!! theorem "Doob's Optional Sampling Theorem"
    Let $X$ be a (super/sub-)martingale and $\tau$ a stopping time.
    Then $X^\tau$ is a (super/sub-)martingale.

!!! proof
    Let $\tau$ be a stopping time.
    It holds that $X^\tau=H\bullet X$ for the process $H=1_{\{\cdot \leq \tau\}}$.  
    However, $H$ is predictable, uniformly bounded since $|H_t|\leq 1$, and positive.
    By the property of the stochastic integral $1_{\{\cdot \leq \tau\}}\bullet X = X^\tau$.
    Hence, according to Doob's optional sampling theorem (modern version), it follows that $X^\tau$ is a (super/sub-)martingale.

!!! proposition

    If $X$ is a martingale or sub-martingale, then:

    \[
      E[X_\tau \,|\, \mathcal{F}_\sigma]=X_{\sigma} \quad \text{or} \quad E[X_\tau \,|\, \mathcal{F}_\sigma]\geq X_{\sigma},
    \]

    respectively, for every pair of bounded stopping times $\sigma\leq \tau \leq T$ for some $T$.

!!! proof
    Since $\tau \leq T$ for some $T$, it follows that:

    \[
    \left\vert X_\tau \right\vert\leq \left\vert X_0\right\vert+\cdots +\left\vert X_t\right\vert.
    \]

    Thus, $X_\tau$ is integrable.
    Furthermore, $X^\tau$ is a martingale from Doob's optional sampling theorem and $X^\tau_T = X_\tau$.
    For $A \in \mathcal{F}_{\sigma}$, it holds that $A\cap \{\sigma=s\}$ is an event in $\mathcal{F}_s$.
    Hence,

    \[
      E\left[ (X_{t}-X_{\sigma})1_{A} \right] =\sum_{s\leq k}E\left[ (X_{t}-X_{s})1_{A\cap \{\sigma =s\}} \right]=\sum_{s\leq k}E\left[ E\left[X_{t}-X_{s}\,|\, \mathcal{F}_{s}\right]1_{A\cap \{\sigma =s\}} \right]=0,
    \]

    showing that $E[X_t\,|\, \mathcal{F}_{\sigma}]=X_{\sigma}$.
    Applying this to the stopped process $X^\tau$ yields the result.
    The proof in the sub-martingale case follows the same argumentation.


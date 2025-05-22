# Girsanov Transformation

The density process of a measure $Q\ll P$ is given by the càdlàg version $Z$ of $Z_t:=E[Z_{\infty}|\mathcal{F}_t]$ where $Z_{\infty}=dQ/dP$.

!!! proposition
    Let $Q$ be an equivalent probability measure to $P$.
    Then it follows that the density process $Z$ is — up to a modification — a càdlàg strictly positive uniformly integrable martingale and the density process of $dP/dQ$ is $1/Z$.
    Reciprocally, let $Z$ be a càdlàg strictly positive uniformly integrable martingale.
    Then $dQ/dP=Z_{\infty}$ defines a probability measure $Q$ equivalent to $P$.

    Furthermore, for every integrable random variable $\xi$ it holds

    \[
    E^Q\left[ \xi|\mathcal{F}_t \right]=E\left[ \frac{Z_\infty}{Z_t}\xi|\mathcal{F}_t \right]
    \]

    Finally, if the density process $Z$ of $Q\sim P$ is continuous, then $X$ is a $Q$-local martingale if and only if $ZX$ is a $P$-local martingale.

!!! proof
    By Radon-Nikodym, it holds that $dQ/dP$ is in $L^1$ with $E[dQ/dP]=1$ and is strictly positive since $Q\sim P$ and it holds $dP/dQ=(dQ/dP)^{-1}$.
    By standard arguments $Z$ is also a uniformly integrable martingale with $Z_{t}\to Z_{\infty}=E[dQ/dP|\mathcal{F}_{\infty}]$ almost surely and in $L^1$ according to the martingale convergence theorem for uniformly integrable martingales.
    The fact that $Z$ is strictly positive follows from the fact that $Z$ is a martingale and $dQ/dP>0.

    Let now $X$ be a $Q$ integrable random variable and $A \in \mathcal{F}_t$.
    It follows that

    \[
    \begin{aligned}
    E^Q\left[ E\left[\frac{Z_\infty}{Z_t} \xi|\mathcal{F}_t\right]1_A\right]
    &=E\left[ \frac{Z_{\infty}}{Z_t}E\left[ Z_{\infty}\xi 1_A|\mathcal{F}_t \right] \right]\\
    &= E\left[ E\left[ \frac{Z_{\infty}}{Z_t}|\mathcal{F}_t\right]E\left[ Z_{\infty}\xi 1_A|\mathcal{F}_t \right] \right]\\
    &= E\left[Z_{\infty}\xi1_A  \right]=E^Q[\xi1_A]
    \end{aligned}
    \]

    showing the last assertion.

    Let $X$ be an adapted continuous process.
    Without loss of generality we may assume up to localization that both $X$ and $ZX$ are uniformly bounded.
    If $ZX$ is a $P$-martingale, then for every bounded stopping time $\tau$ it holds

    \[
    E^Q\left[X_{\tau}  \right]=E\left[ Z_{\infty}X_{\tau} \right]=E\left[ Z_{\tau}X_{\tau} \right]=E\left[ Z_0 X_0 \right]=E\left[ Z_{\infty}X_0 \right]=E^Q\left[ X_{0} \right]
    \]

    showing that $X$ is a $Q$-martingale.
    The reciprocal follows the same argumentation.

!!! theorem
    Suppose that $Q\sim P$ and has a density process $Z$ which — up to modification — is continuous.
    Every semi-martingale $X$ under $P$ is a semi-martingale under $Q$.
    More precisely, a process $X$ is a $P$-local martingale if and only if $\tilde{X}=X-\int \frac{d\langle X,Z\rangle}{Z}$ is a $Q$-local martingale.
    If $Y$ is another $P$-local martingale, then $\langle \tilde{X}, \tilde{Y}\rangle =\langle X,Y\rangle$.
    Also, $\mathcal{L}^{loc}(X,P)=\mathcal{L}^{loc}(X,Q)$ and $\int HdX$ is the same under $P$ and $Q$.
    In particular $\int H dX$ is the same under $P$ and under $Q$.

!!! proof
    Note first that since the quadratic variations $[ \cdot ]$ are defined as a limit in probability, quadratic variations and co-variations of a process do not change under equivalent change of measure.
    The same holds for processes of bounded variations.
    Hence it is enough to check that for a $P$-local martingale $X$, then $\tilde{X}=X-\int \frac{d\langle X,Z\rangle}{Z}$ is a $Q$-local martingale, that is, according to the previous Proposition, that $Z\tilde{X}$ is a $P$-local martingale.
    By Itô's formula under $P$, since $\int \frac{d\langle X,Z\rangle}{Z}$ is of bounded variations, it follows that

    \[
    \begin{aligned}
    dZ\tilde{X}&=\tilde{X} dZ + Z d\tilde{X}  + d\langle Z,\tilde{X} \rangle\\
    &=\tilde{X} dZ + ZdX - d\langle X,Z \rangle + d\langle X,Z \rangle\\
    &= \tilde{X}dZ+ZdX
    \end{aligned}
    \]

    Since $Z$ and $X$ are both $P$-local martingales, it follows that $Z\tilde{X}$ is a $P$-local martingale.
    The relation $\langle \tilde{X},\tilde{Y}\rangle = \langle X,Y\rangle$ is immediate by the formula.

    Finally, if $H$ is locally bounded under $P$ then it is locally bounded under $Q$.
    For such an $H$, let $X=M+A$ where $M$ is a $P$-local martingale.
    It has a decomposition $X=\tilde{M}-\int \frac{d\langle M,Z\rangle}{Z} +A$ under $Q$.
    Hence under $Q$, it holds

    \[
    \int H dX =\int H d\tilde{M}-\int H\frac{d\langle Z,M\rangle}{Z}+\int H dA=\int H dM+\int H dA
    \]

    the right-hand side being the stochastic integral of $H$ with respect to $X$ under $P$.

A continuous density process of $Q$ equivalent to $P$ can be expressed in terms of stochastic exponential and therefore we get the more traditional version of Girsanov theorem.

!!! corollary
    A probability $Q$ equivalent to $P$ admits a continuous density process $Z$ if and only if $Z = \mathcal{E}(M)$ for some local martingale $M$ such that $\mathcal{E}(M)$ is uniformly integrable and strictly positive.
    In that case, if $X$ is a $P$-local martingale then $\tilde{X}=X-\langle M,X\rangle$ is a $Q$-local martingale.

!!! proof
    If $Z=\mathcal{E}(M)$ is uniformly integrable, we already saw that $Q$ is a probability measure.
    As for the reciprocal, since $Z$ is strictly positive, applying Itô's formula to $\ln(Z)$, we get

    \[
    d\ln(Z)=\frac{dZ}{Z}-\frac{1}{2}\frac{d\langle Z\rangle}{Z^2}=dM-\frac{1}{2}d\langle M\rangle
    \]

    where $M:=\int dZ/Z$ showing that $Z=\mathcal{E}(M)$.

    Further, $X$ is a $P$-local martingale, if and only if $X-\int \frac{d\langle Z,X\rangle}{Z}$ is a $Q$-local martingale.
    However $d\langle Z,X\rangle /Z=d\langle M, X\rangle$ which ends the proof.


!!! example
    Pursuing our example, our small argumentation for the arbitrage is now better founded.
    The details are a bit more tricky but the bottom line is there.
    Though, we are not sure if there exists an equivalent probability measure $Q$ such that $X$ is a $Q$-local martingale.
    However, Girsanov theorem comes here handily.
    Recall that the stochastic evolution of the discounted stock price $X$ is given by

    \[
    dX=\sigma X\left( \theta dt+dW \right)
    \]

    where $\theta = (\mu-r)/\sigma$.
    In other terms, we want to find a probability measure $Q$ such that $W+\int \theta dt$ is a local martingale under $Q$.
    Following Girsanov theorem, we define $M=-\int \theta dW$.
    We suppose that $M$ satisfies the Novikov condition so that $dQ/dP=\mathcal{E}_{\infty}(M)$ defines a probability measure $Q$ equivalent to $P$.
    Since $W$ is a local martingale under $P$, by Girsanov, it follows that $W-\langle M,W\rangle$ is a local martingale under $Q$.
    However, $\langle M,W\rangle =-\int \theta d\langle W,W\rangle=-\int \theta dt$ showing that $X$ is a local martingale under $Q$.

    We finish the study of this chapter with an additional comment on this example.
    You will see in exercises that the price of European options, for instance a call option $C = (S_T-K)^+$ where $T$ is the *maturity* and $K$ the *strike price*, is given by

    \[
    \Pi(C)=E^{Q}\left[ \frac{C}{B_T} \right]=E^Q\left[ \left( X-\frac{K}{B_T} \right)^+ \right]
    \]

    In the case of the call option, it means that even if we know the distribution of $X$ under $P$, we are not so clear about its distribution under $Q$.
    In other terms, we are interested in the distribution of $\tilde{W}=W+\int \theta dt$ under $Q$.
    It turns out that it is astonishingly a Brownian motion due to the following characterization of Lévy.

!!! theorem
    A stochastic process $X$ is a Brownian motion if and only if it is a continuous local-martingale with $\langle X\rangle =t$.

!!! proof
    If $X$ is a Brownian motion then it is clear that it is a semi-martingale with quadratic variations equal to $t$.
    Reciprocally, let $X$ be a local martingale with quadratic variations equal to $t$.
    We define $F(t,x)=\exp(iux+u^2 t/2)$ for every $u \in \mathbb{R}$.
    Though being complex valued, nothing changes — you apply everything component by component.
    Applying Itô's formula, since $d\langle X\rangle = dt$ by assumption, it holds

    \[
    dF(t,X)=\frac{u^2}{2}F(t,X)dt+iuF(t,X)dX-\frac{u^2}{2}F(t,X_t)d\langle X\rangle=iuF(t,X)dX
    \]

    In particular, $F(t,X)$ is a local martingale, which is uniformly bounded on compact intervals.
    Hence it is a true martingale.
    For every $s\leq t$, it holds

    \[
    E\left[ \exp\left( iu(X_t-X_s)\right)|\mathcal{F}_s \right]=e^{-\frac{u^2}{2}(t-s)}E\left[ \frac{F(t,X_t)}{F(s,X_s)}|\mathcal{F}_s \right]=  e^{-\frac{u^2}{2}(t-s)}
    \]

    which is the conditional characteristic function of the increment of $X$.
    Since it holds for every $u$, is independent of $\mathcal{F}_s$, it follows that $X_t-X_s$ is independent of $\mathcal{F}_s$ and $X_t-X_s \sim \mathcal{N}(0,t-s)$ showing that $X$ is a Brownian motion.

!!! example
    In our financial case where $Q=\mathcal{E}(-\int \theta dW)$, it follows that $\tilde{W}=W+\int \theta dt$ is a local martingale under $Q$ with quadratic variations according to Girsanov Theorem equal to $\langle \tilde{W}\rangle =\langle W\rangle =t$ showing that $W+\int \theta dW$ is a Brownian motion under $Q$.


# Default (Ruin) Probability

We saw that the random walk often generates the evolution of the stock prices in the CRR model. In this section, we are interested in finding the probability of the ruin event. During the study of American Options, we introduced the concept of stopping times. Stopping times are also used to define ruin events, and the martingales with the help of Doob's Optional Sampling Theorem will provide a very elegant way to study the properties of this ruin event.

We consider the following random walk of the CRR model starting at $0$:

\[
    Z_0=0\quad \text{and}\quad Z_t=\sum_{s=1}^t Y_s,\quad t\geq 1
\]

where $Y$ are i.i.d. with $P[Y_t = 1] = p$ and $P[Y_t = -1] = 1 - p = q$.

As for the filtration, we take

\[
    \mathcal{F}_0=\{\emptyset,\Omega\}\quad \text{and}\quad \mathcal{F}_t=\sigma(Z_s\colon 1\leq s\leq t),\quad t\geq 1
\]

We define $\tau_{a}=\inf\left\{ t\colon Z_t=a \right\}$, $\tau_{b}=\inf\left\{ t\colon Z_t =-b \right\}$, and $\tau=\tau_a\wedge \tau_b =\inf\{t\colon Z_t=a\text{ or }Z_t=-b\}$ for two integers $a,b$.

!!! remark
    As we saw in the CRR model, we often describe the stock price as:

    \[
        S_t=S_0(1+u)^{Z_t}
    \]

    so that the stopping time $\tau$ can be interpreted as the first time that the stock price reaches the level $S_0(1+u)^a$ or drops to the level $S_0/(1+u)^{b}$.

We are interested in the following probabilities:

\[
    P\left[ Z_{\tau}=a \right], \quad \text{and}\quad P \left[ Z_{\tau}=-b \right]
\]

which are, respectively, the probability that $Z$ reaches the level $a$ before running bankrupt at level $-b$, and the probability of running bankrupt at level $-b$ before reaching level $a$.

### Symmetric Random Walk
Suppose first that $p=q=1/2$, the case of the symmetric random walk. It follows that $Z$ is a martingale. Hence, due to the Optional Sampling Theorem, the stopped process $Z^\tau$ is a martingale, showing that:

\[
    0=Z_0=E\left[ Z_t^\tau \right]=E\left[ Z_{t\wedge \tau} \right]
\]

for every $t$. An intuitive inspection shows that for almost all $\omega$, the hitting time of one of the barriers will occur in a finite amount of time almost surely, that is $P[\tau <\infty]=1$. Hence,

\[
    \lim_{t\to \infty}Z_{t\wedge \tau}=Z_\tau
\]

$P$-almost surely. Furthermore, $|Z^\tau_t|\leq a\wedge b$ for every $t$, and therefore, by Lebesgue's Dominated Convergence Theorem, it follows that:

\[
    0=\lim_{t\to \infty}E\left[ Z_t^\tau \right]=E\left[ \lim_{t\to \infty} Z_{t\wedge \tau} \right]=E[Z_{\tau}]
\]

On the other hand, it holds:

\[
    Z_{\tau}=a1_{\{Z_\tau =a\}}-b1_{\{Z_\tau=-b\}}=a1_{\{Z_\tau=a\}}-b(1-1_{\{Z_\tau=a\}})
\]

showing that:

\[
    E\left[ Z_\tau \right]=(a+b)P\left[ Z_\tau=a \right]-b
\]

Together with the fact that $E[Z_\tau]=0$, it follows that:

\[
    P\left[ Z_\tau=a \right]=\frac{b}{a+b}, \quad \text{and}\quad P\left[ Z_\tau=-b \right]=\frac{a}{a+b}
\]

### Asymmetric Random Walk
Suppose now that $1>p>1/2$. Then, $Z$ is no longer a martingale, but a sub-martingale. Indeed, $Y$ being independent and identically distributed, it follows that:

\[
    E\left[ Z_{t+1}-Z_t|\mathcal{F}_t \right]=E\left[ Y_{t+1}|\mathcal{F}_t \right]=E\left[ Y_{1} \right]= P\left[ Y_1=1 \right]-P\left[ Y_1=-1 \right]=2p-1>0
\]

We can therefore no longer apply the same strategy as before. However, a similar inspection as in the previous case shows that $\tau(\omega)<\infty$ for $P$-almost all $\omega \in \Omega$. Despite the fact that $Z$ is no longer a martingale, the process:

\[
    M_t=\left(\frac{q}{p}\right)^{Z_t}, \quad t=0,1,\ldots
\]

is a martingale where $q = 1-p$. Indeed, it is clearly adapted and integrable. Furthermore, using the independent and identically distributed assumption for $Y$, it holds:

\[
    E\left[ M_{t+1}-M_t|\mathcal{F}_t \right]
    =M_tE\left[ \left( \frac{q}{p} \right)^{Y_{t+1}}-1|\mathcal{F}_t \right]
    =M_tE\left[ \left( \frac{q}{p} \right)^{Y_{1}}-1 \right]
    =M_t\left( p\frac{q}{p}+q\frac{p}{q}-1 \right)=0
\]

Considering the stopped process $M^\tau$, it follows from Doob's Optional Sampling Theorem that:

\[
    1=M_0=E\left[M_{t}^\tau  \right]=E\left[ M_{t\wedge \tau} \right]
\]

for every $t$. However, since $\tau(\omega)<\infty$ for every $\omega$, it follows that $\lim_{t\to \infty}M_{t\wedge \tau}=M_{\tau}$ $P$-almost surely. Furthermore $|M_{t\wedge \tau}|\leq 1$, allowing us to apply Lebesgue's Dominated Convergence:

\[
    1=\lim_{t\to \infty}E\left[ M_{t\wedge \tau} \right]=E\left[ \lim_{t\to \infty}M_{t\wedge \tau} \right]=E\left[ M_\tau \right]
\]

On the other hand, it holds:

\[
    E\left[ M_\tau \right]
    =\left(\frac{q}{p}\right)^aP\left[ Z_\tau=a \right]+\left( \frac{q}{p} \right)^{-b} P\left[ Z_\tau=-b \right]
    =\left(\frac{q}{p}\right)^{-b}\left(\left(\frac{q}{p}\right)^{a+b}P[Z_\tau=a]+(1-P[ Z_\tau=a]) \right)
\]

Combined with $E[M_\tau]=1$, it yields:

\[
    P\left[ Z_\tau=a \right]=\frac{(q/p)^b-1}{(q/p)^{a+b}-1}, \quad \text{and}\quad P\left[ Z_{\tau}=-b \right]=\frac{(q/p)^{a}-1}{(q/p)^{a}-(q/p)^{-b}}
\]

### Application to Credit Rating
Given a company, we want to estimate its probability to default at some point. In our simple framework, we define:

\[
    \inf\left\{ t: b+Z_t =0 \right\}=\inf\left\{ t \colon Z_t = -b \right\}=\tau_b
\]

which is the first time that a firm with cumulative returns $Z$ and start capital $b$ reaches bankruptcy. We also assume here that $1/2 <p<1$. We want to estimate:

\[
    P\left[ \tau_b <\infty \right]
\]

which is the probability that the firm goes bankrupt at some point in time. Since $\tau_a \to \infty$ as $a\to \infty$, it follows that:

\[
    P\left[ \tau_b<\infty \right]=\lim_{a \to \infty}P\left[ Z_{\tau}=-b \right]=\lim_{a\to \infty}\frac{(q/p)^{a}-1}{(q/p)^{a}-(q/p)^{-b}}=\left( \frac{q}{p} \right)^b
\]

We see therefore two factors impacting the probability of default of the company:

- **The returns of the company** ($p$): Since $E[Z_{t+1}-Z_t|\mathcal{F}_t]=2p-1>0$, if $p$ is very close to $1$, that is strong returns, then $q/p$ is very small and so is the probability of default $(q/p)^b$.
- **The present capital of the company** ($b$): Since $0<q/p<1$, it follows that the higher $b$, the smaller $(q/p)^b$ in an exponential way.


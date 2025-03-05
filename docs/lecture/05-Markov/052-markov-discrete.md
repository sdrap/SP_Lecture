# Markov Chains

In this subsection we treat discrete time Markov processes chains with a finite or eventually countable state space $S$, also called **Markov Chains**.
Recall that we only consider time homogenous Markov processes.
Defining

\[
\begin{align*}
    \mu_x:=P[X_0=x] \quad p_{xy}:=P\left[X_{t+1}=y|X_t=x\right]=P[X_1=y|X_0=x]
\end{align*}
\]

it follows that $0\leq \mu_x, p_{xy}\leq 1$ and $\sum \mu_x=1$, as well as $\sum_y p_{xy}=1$ for every $x$.
In other terms, the initial distribution $\mu:=(\mu_x)$ is a random vector and the one step transition probability can be represented by the stochastic matrix $P=(p_{xy})$.
For $B\subseteq S$, it holds

\[
\begin{equation*}
    P_1(x,B)=\sum_{y \in B}p_{xy}
\end{equation*}
\]

By Chapman Kolmogorov relation, we have $P_t=P_{t-1}P_1$, hence, defining recursively

\[
\begin{equation}\label{eq:repetition_markov}
    p^t_{xy}=\sum_{z}p^{t-1}_{xz}p_{zy}
\end{equation}
\]

we have

\[
\begin{equation*}
    P_t(x,B)=\sum_{y \in B}p^t(x,y)
\end{equation*}
\]

In the discrete case the following strong Markov property holds.

!!! theorem "Strong Markov Property"
    Let $Z$ be a bounded random variable and $\tau$ a stopping time.
    Then it holds

    \[
    \begin{equation*}
        1_{\{\tau<\infty\}}E^{\mu}\left[ Z\circ\theta_{\tau}|\mathcal{F}_\tau \right]=1_{\{\tau<\infty\}} E^{X_{\tau}}\left[ Z \right].
    \end{equation*}
    \]

!!! proof
    For every $A \in \mathcal{F}_\tau$ we get by Theorem \ref{thm:markov property} and the fact that $A\cap \{\tau=t\}\in \mathcal{F}_t$ for every $t$,

    \[
    \begin{align*}
        E^{\mu}\left[1_A1_{\{\tau<\infty\}} Z\circ\theta_\tau\right]
        &=\sum_{t} E^\mu \left[1_A1_{\{\tau=t\}} Z\circ\theta_t\right]\\
        &= \sum_{t} E^{\mu}\left[1_A1_{\{\tau=t\}} E^{X_t}\left[Z\right]\right]\\ 
        &=E^\mu\left[1_A1_{\{\tau<\infty\}} E^{X_\tau}\left[Z\right]\right],
    \end{align*}
    \]

    from which the claim follows.

Markov chains are defined locally:
The next step is entirely defined by the place where you are now and the transition probability.
The natural question therefore is whether you will come back or not.
Given a state $y$ in $S$, define recursively 

\[
\begin{align*}
    \tau^0_y  & :=0\\
    \tau^1_y & := \inf\left\{ t> \tau^0_y\colon X_t=y \right\}\\
    \vdots\\
    \tau^k_y & := \inf\left\{ t>\tau^{k-1}_y\colon X_t=y \right\}\\
    \vdots
\end{align*}
\]

Here $\tau^k_y$ denotes the $k$-th return time to the state $y$.
Let further 

\[
\begin{equation*}
    \rho_{xy}:=P^{x}\left[ \tau_y<\infty \right]
\end{equation*}
\]

be the probability that starting from $x$, the Markov chain visits the state $y$ at least once, 
where we denote the first return time as $\tau_y = \tau^1_y$.

!!! definition
    We say that a time homogeneous Markov chain is 
    
    - **recurrent**: if $\rho_{xx}=1$;
    - **transient**: if $\rho_{xx}<1$.

!!! theorem 

    For any two states $x$ and $y$ in $S$, it holds

    \[
    \begin{equation*}
        P^x[\tau_y^k < \infty] = \rho_{xy}\rho_{yy}^{k-1}.
    \end{equation*}
    \]

!!! proof
    We show it per induction.
    Per definition, it holds $P^x[\tau_y^1 < \infty]= \rho_{xy}$.
    Suppose therefore that the claim holds for every $l=1,\ldots,k-1$ and we show it for $k$.
    
    Define $\tau=\tau_y^{k-1}$ and $Z:=1_{\{\tau_y < \infty \}}$.
    It follows that $\{ \tau_y^k < \infty \} = \{ \tau_y \circ \theta_\tau < \infty \}$.
    Furthermore, from $1_{\{\tau<\infty\}}$ bounded and $\mathcal{F}_{\tau}$-measurable and $X_{\tau}=y$ on $\{\tau<\infty\}$, using the strong Markov property it follows that

    \[
    \begin{align*}
        P^{x}[\tau_y^k < \infty ] &= P^{x}[\tau_y \circ \theta_\tau < \infty ]\\
                                  &= E^x\left[1_{\{\tau < \infty\}}  (Z \circ \theta_\tau) \right]\\
                                  &= E^x\left[1_{\{\tau < \infty\}}  E^x\left[Z \circ \theta_\tau| \mathcal{F}_\tau\right]\right]\\
                                  &= E^x\left[1_{\{\tau < \infty\}}  E^{X_\tau}\left[Z\right] \right]\\
                                  &= E^x\left[1_{\{\tau < \infty\}}  P^y[\tau_y<\infty]\right]\\
                                  &= \rho_{yy} P^x[\tau_y^{k-1} < \infty]\\
                                  &= \rho_{yy} \rho_{xy} \rho_{yy}^{k-2}\\
                                  &= \rho_{xy} \rho_{yy}^{k-1}.
    \end{align*}
    \]

!!! theorem
    Let $x$ and $y$ be two states in $S$, where $x$ is recurrent and $\rho_{xy}>0$.
    Then $y$ is recurrent and $\rho_{yx}=1$.

!!! proof
    Let us first show that $\rho_{yx}=1$.
    Since $x$ is recurrent, it follows that $\tau_x(\omega)<\infty$ for almost all $\omega \in \Omega$.
    Hence, for almost all $\omega \in \Omega$ such that $\tau_y(\omega)<\infty$ we get $\tau_x \circ \theta_{\tau_y}(\omega) <\infty$.
    
    Thus with $H:=1_{\{\tau_x=\infty\}}$, the strong markov property, and the fact that $X_{\tau_y}=y$, we get

    \[
    \begin{align*}
        0 & =P^x[\tau_y < \infty, \tau_x \circ \theta_{\tau_y} = \infty]\\
          & =E^x\left[1_{\{\tau_y<\infty\}} 1_{\{\tau_x \circ \theta_{\tau_y} = \infty\}} \right]\\
          & =E^x\left[1_{\{\tau_y<\infty\}} E^{X_{\tau_y}}\left[H\right] \right]\\
          & =E^x\left[1_{\{\tau_y<\infty\}} P^y[\tau_x=\infty]\right] \\
          & =\rho_{xy}(1-\rho_{yx}).
    \end{align*}
    \]

    Since $\rho_{xy} > 0$, it must be that $\rho_{yx}=1$.

    Let us finally show that $y$ is recurrent.
    Let $i$ and $j$ be two states in $S$ and $k$ in$\mathbb{N}$.
    Then by Chapman-Kolmogorov relation and an induction we get $P_i[X_k=j]=p^k_{ij}$.
    Since $\rho_{xy}>0$ and $\rho_{yx}>0$, there exist $k_1$ and $k_2$ in $\mathbb{N}$ with $p_{xy}^{k_1}>0$ and $p_{yx}^{k_2}>0$.
    By the Chapman-Kolmogorov relation we get

    \[
    p_{yy}^{k_1+t+k_2} \geq p_{yx}^{k_2} p_{xx}^t p_{xy}^{k_1}
    \]

    so that

    \[
    E^y\left[N_y\right] =p_{yx}^{k_2} E^x\left[N_x\right]p_{xy}^{k_1} =\infty.
    \]

    Recurrence/Transience Theorem implies that $y$ is recurrent.


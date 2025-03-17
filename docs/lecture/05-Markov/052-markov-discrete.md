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
!!! definition
    A set $C \subseteq S$ is called

    - **closed**, if for $x\in C$, $y\in S$ and $\rho_{xy}>0$ it holds $y \in C$,
    - **irreducible**, if $\rho_{xy}>0$ for all $x,y\in C$.

!!! theorem
    Suppose $C \subset S$ is finite and closed.

    - There exists $x\in C$ such that $x$ is recurrent.
    - If $C$ is irreducible, then all its states are recurrent.

!!! proof
    - By contradiction, assume that all states are transient, that is $E^x[N_y] < \infty$ for all $x$ and $y$ in $C$ by the recurrent/transient Theorem.
        But then, since $C$ is finite we get with Tonelli's theorem

        \[
        \sum_{y\in C} E^x[N_y] =\sum_{y\in C} \sum_{t} P^x [X_t=y] =\sum_{t}\sum_{y\in C} P^x[X_t=y]
        =\sum_{t} P^x [ X_t\in C] =\sum_{t} 1=\infty.
        \]

        Indeed, if $P^x [X_t\in C] < 1$, then there is $y$ in $C^c$ with $P^x[X_t=y] >0$, that is $\rho_{xy} >0$.
        Since $C$ is closed, it follows $y \in C$, a contradiction.

    - If $x \in C$ is recurrent and $\rho_{xy}>0$, then $y$ is recurrent by Theorem the previous theorem.

!!! theorem
    Let $R:=\{ x \in S \colon \rho_{xx} =1  \}$ be the set of recurrent states.
    Then $R$ is a disjoint union of closed and irreducible sets.

!!! proof
    Fix $x$ in$ R$ and let $C_x :=\{ y\in R \colon \rho_{xy} >0 \} $.

    - For $x$, $y$ and $z$ in $R$ it holds $\rho_{xy} \geq \rho_{xz} \rho_{zy}$.
        Indeed, with $H:=1_{\{\tau_y < \infty\}}$ and the strong Markov property using the same argument as in recurrence Theorem we obtain

        \[
        \begin{align*}
           \rho_{xy}  & =P^x[\tau_y<\infty]\\
                      & \geq P^x[\tau_z<\infty, \tau_y \circ \theta_{\tau_z} < \infty]\\
                      & =E^x[1_{\{\tau_z < \infty\}} E^x[H \circ \theta_{\tau_z} | \mathcal{F}_{\tau_z}]]\\
                      & =E^x[1_{\{\tau_z < \infty\}}] E^z[1_{\{\tau_y < \infty\}}]]\\
                      & =\rho_{xz}\rho_{zy}.
        \end{align*}
        \]

    - $C_x$ is irreducible and closed.
        Indeed, for $y$ in $C_x$ and $\rho_{yz} >0$, since $y$ is in $C_x$ we have $\rho_{xy}>0$ and therefore by the previous step $\rho_{xz} >0$, that is $z$ belongs to $C_x$.
        Furthermore, for $y$ and $z$ in $C_x$, it implies that $\rho_{xy} >0$, $\rho_{xz}>0$.
        Recurrence Theorem yields $\rho_{yx}>0$ and therefore $\rho_{yz}>0$.

    - We now show that $C_x \cap C_y \neq \emptyset$ implies $C_x=C_y$.
        Let $z$ be in $C_x \cap C_y$ and $y^\prime$ in $C_y$.
        Therefore $\rho_{xz}>0$, $\rho_{yz}>0$, $\rho_{yy^\prime}>0$ and by recurrence Theorem $\rho_{zy}>0$.
        This means $\rho_{xy^\prime} >0$ which yields $y^\prime\in C_x$, hence $C_y \subset C_x$.
        Analogously, $C_x \subset C_y$.

!!! definition
    A measure $\mu$ on is called **stationary**&mdash;or **invariant**&mdash;if

    - $\mu(y)< \infty$ for all $y \in S$,
    - $\mu(y)=\sum_{x\in S} \mu(x)p_{xy}$.

    If $\mu$ is a probability measure, then $\mu$ is called a stationary distribution.

!!! remark
    Suppose that $\mu$ is a stationary distribution, and let $P^\mu$ the measure such that $X$ is Markov with start distribution $\mu$.
    Then

    \[
      \begin{align*}
         P^\mu[X_1=y] & = \sum_{x\in S}P^\mu[X_1=y | X_0=x] P^\mu[X_0=x]\\
                      & =\sum_{x\in S} \mu(x) p_{xy}\\
                      & =\mu(y)
      \end{align*}
    \]

    By induction, we assume that $P^\mu[X_t=y]=\mu(y)$.
    Then

    \[
      \begin{align*}
         P^\mu[X_{t+1}=y] & =\sum_{z\in S} P^\mu[X_{t+1}=y|X_t=z]P^\mu[X_t=z]\\
                          & =\sum_{z\in S} \mu(z) p_{zy}\\
                          & =\mu(y)
      \end{align*}
    \]

    This shows $P^\mu(X_t=y) = \mu(y)$ for every $t$.

!!! example "Example: Randomw Walk"

    Let $X_t:=X_0+\sum_{s=1}^{t} Y_s$ and $\mathcal{F}_t:=\sigma(X_0,\dots,X_t)$.
    Then

    \[
      \begin{align*}
         p_{xy} & = P[X_{t+1}=y | X_t=x]=P[\xi_{t+1}=y-X_t | X_t=x]\\
                & =P[\xi_1=y-x]\\
                & =f(y-x)
      \end{align*}
    \]

    where $f \colon S \to [0,1]$ is such that $\sum_{y\in S}f(y)=1$, that is $f(y):=P[\xi_1=y]$.
    In this case $\mu \equiv 1$ is a stationary measure.
    Indeed,

    \[
      \begin{align*}
         \sum_{x\in S} \mu(x)p_{xy}   & = \sum_{x\in S} p_{xy}\\
                                      & = \sum_{x\in S} f(y-x) \\
                                      & =\sum_{x^\prime\in S} f(x^\prime) \\
                                      & =1\\
                                      & =\mu(y)
      \end{align*}
    \]

!!! remark
    Let $x\in S$ be transient and $\pi$ a stationary distribution.
    Then $\pi(x)=0$.


!!! proof
    Exercise.

!!! theorem
    Suppose $x$ is recurrent and $\tau:=\inf\{ t\colon X_t = x \}$.
    Define

    \[
    \mu(y)=E^x\left[\sum_{t=0}^{\tau-1}1_{\{X_t=y\}}\right]=\sum_{t} P^x[X_t=y, t<\tau]
    \]

    for all $y\in S$.
    Then $\mu$ is a stationary measure.

!!! proof
    For $z$ in $S$ and $t$ let $\bar{p}_t(x,z):=P^x[X_t=z,\tau>t]$.
    We claim that $\sum_{t} \bar{p}_t(x,\cdot)$ is a stationary measure.

    - For $z\neq x$ we have

        \[
          \begin{align*}
             \sum_{y\in S} \bar{p}_t(x,y) p_{yz} 
              & = \sum_{y\in S} P^x[X_t=y, \tau>t] p_{yz} \\
              & = \sum_{y\in S} P^x(X_t=y,\tau>t,X_{t+1}=z]\\
              & = P^x[\tau>t+1,X_{t+1}=z]\\
              & =\bar{p}_{t+1}(x,z)
          \end{align*}
        \]

        Hence,

        \[
          \begin{align*}
             \sum_{y\in S}\sum_{t} \bar{p}_t(x,y)p_{yz} 
                & = \sum_{t}\sum_{y\in S} \bar{p}_t(x,y)p_{yz}\\
                & = \sum_{t} \bar{p}_{t+1}(x,z)\\
                & = \mu(z)
          \end{align*}
        \]

        since $\bar{p}_0(x,z)=0$.

    - For $z=x$ we have

        \[
        \sum_{y\in S} \bar{p}_t(x,y) p_{yx} = \sum_{y\in S} P^x[X_t=y,\tau>t,X_{t+1}=x] = P^x[\tau=t+1].
        \]

        Hence,

        \[
        \sum_{t}\sum_{y\in S} \bar{p}_t(x,y)p_{yz} = \sum_{t} P^x[\tau=t+1] = 1 = \mu(x).
        \]

    - Finally we show that $\mu(y)<\infty$ for any $y$ in $S$.
        We have $\mu(x)=1$, and $\mu p^t=\mu$, showing that $\mu(y)<\infty$ if $p^t_{xy}>0$ for some $t$.

        - If $P^x[\tau_y<\infty]=0$, then $\mu(y)=0$.
        - If $P^x[\tau_y<\infty]>0$, then by recurrence Theorem we have $P^y[\tau_x<\infty]>0$ so that $p_{yx}^t>0$ for some $t$, hence $\mu(y)<\infty$.


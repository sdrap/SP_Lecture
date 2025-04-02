# Continuous Time Processes: Regularity, Filtration, Stopping Times

!!! warning

    Unless otherwize specified, the letters $q$ and $r$ used for time means that they are rational.


!!! definition
    Let $X$ and $Y$ be two processes.
    We say that

    - $X$ is a **modification** of $Y$ if $X_t=Y_t$ $P$-almost surely for every $t$, that is

    
    \[
    P[X_t=Y_t]=1,\quad \text{for every }t.
    \]

    - $X$ is indistinguishable from $Y$ if $X_t=Y_t$ for all $t$, $P$-almost surely, that is

    
    \[
    P[X_t=Y_t; \text{ for every }t]=1.
    \]

In the case where the stochastic process is indexed by a countable set, these two notions are equivalent.
However, if it is indexed by $t$ in $[0, \infty)$ of any uncountable directed set, modification and indistinguishability are different in that we may have to take into account uncountably many null sets as the following example shows.

!!! example
    Set $(\Omega, \mathcal{F},P):=([0,1], \mathcal{B}([0,1]),dt)$, where $dt$ is the Lebesgue measure and $\mathcal{B}([0,1])$ is the Borel $\sigma$-algebra.
    Define the processes $X$ and $Y$ by

    
    \[
    X_t=0\quad\text{and}\quad
    Y_t=
    \begin{cases}
        Y_t(\omega)=1& \text{if }\omega = t\\
        Y_t(\omega)=0 & \text{otherwise}
    \end{cases}
    \]

    for every $0\leq t\leq 1$.
    It follows that 

    \[
      P[X_t=Y_t]=P[ \{\omega\in [0,1]\colon \omega\neq t\}]=1
    \]

    whereas 

    \[
      P[X_t=Y_t\colon\text{ for every }t]=P[\{\omega \in [0,1]\colon \omega\neq t\text{ for every }t\}]=P[\emptyset]=0
    \]

We see that uncountably many sets of measure zero can add up to something that may no longer have measure zero.
However, if we can infer from the structure of the trajectories that it is sufficient to consider countably many times, then these two conditions will coincide again.

We say that a process $X$ has

- **des limites à gauche**(1) (làg) if 

    
    \[
    P\left[\liminf_{s\nearrow t}X_s=\limsup_{s\nearrow t}X_s: \text{ for every }t>0\right]=1,
    \]

- **des limites à droite** (làd) if

    
    \[
    P\left[\liminf_{s\searrow t}X_s=\limsup_{s\searrow t}X_s:\text{ for every }t\right]=1,
    \]

- **continue à gauche** (càg) if

    
    \[
    P\left[\lim_{s\nearrow t}X_s=X_t: \text{ for every }t>0, t\in \mathbf{T}\right]=1,
    \]

- **continue à droide** (càd) if

    
    \[
    P\left[\lim_{s\searrow t}X_s=X_t:\text{ for every }t<T, t \in \mathbf{T}\right]=1,
    \]


!!! note

    The notations làg, làd, càd, or càg comes from french where "gauche" stands for "left", "droite" stands for "right", "limites" stands for "limits" and "continue" stands for "continuous".
    In some Americanized textbooks, "ll" stands for "làg", "lr" stands for "làd", "rc" stands for "càd", or "lc" stands for "càg".

A process $X$ is said to be càdlàg, càglàd, or làdlàg, if it is “continue à droite avec des limites à gauche”, “continue à gauche avec des limites à droite” or “limites à gauche et limites à droite”, respectively.

!!! lemma
    Suppose that $X$ and $Y$ are modifications of each other and both are either càd or càg.
    Then $X$ and $Y$ are indistinguishable.

!!! proof
    Let $X$ and $Y$ both be càd and modifications of each other.
    Since $X$ and $Y$ are càd, it follows that

    
    \[
    \begin{align*}
      P\left[ X_t\neq Y_t:\text{for some }t\right] 
        & = P\left[ \lim_{ q\searrow t}X_q\neq \lim_{ q\searrow t}Y_q: \text{ for some }t \right]\\
        & = P\left[X_q \neq Y_q: \text{for some }q \in \mathbb{Q} \right]\\
        & = P\left[ \cup_{q \in \mathbb{Q}}\{X_q\neq Y_q\} \right]\\
        & \leq \sum P[X_q\neq Y_q]=0
    \end{align*}
    \]

    Hence, $P\left[ X_t=Y_t\colon \text{for every }t \right]=1$ showing that $X$ and $Y$ are indistinguishable.

!!! note
    The assumption of left- or right-continuity is central.
    The counter example provided for distinction between version and indistinguishable are two làdlàg processes modification of each others while not indistinguishable.


The definition of a filtration $\mathbb{F}=(\mathcal{F}_t)$ does not change as an increasing family of $\sigma$-algebra indexed by time.
However, in continuous time, we can also define the right and left filtration $\mathbb{F}^+=(\mathcal{F}_t^+)$ and $\mathbb{F}^-=(\mathcal{F}^-_t)$ as follows(1)
{.annotate}

1.  Clearly for the left continuous version we have to assume $t>0$ and set as convention $\mathcal{F}_0^- = \mathcal{F}_0$. If the time index is $[0, T]$, then also for the right continuous version we set $\mathcal{F}_T^+ = \\mathcal{F}_T$.

\[
  \mathcal{F}_t^+=\bigcap_{s>t}\mathcal{F}_s\quad \text{and}\quad \mathcal{F}_{t}^-=\bigvee_{s<t}\mathcal{F}_s:=\sigma\left( \mathcal{F}_s: s<t \right)
\]

We say that the filtration is left- or right-continuous if $\mathbb{F}=\mathbb{F}^-$ or $\mathbb{F}=\mathbb{F}^+$, and continuous if it is both.


!!! remark
    From the definition, $\mathbb{F}^\pm$ are themselves filtrations and it holds $\mathcal{F}_t^-\subseteq \mathcal{F}_t\subseteq \mathcal{F}_t^+$ as well as $\mathcal{F}^+_s\subseteq \mathcal{F}_t^-$ whenever $s<t$.
    Hence $(\mathbb{F}^-)^+=(\mathbb{F})^+=(\mathbb{F}^+)^+$ as well as $(\mathbb{F}^+)^-=(\mathbb{F})^-=(\mathbb{F}^-)^-$.

As such, a process is nothing else than an arbitrary family of random variables indexed by the time.
It can also be seen as a mapping $X:\Omega \times [0, \infty)\to \mathbb{R}$.

!!! definition
    Given a filtration $\mathbb{F} = (\mathcal{F}_t)$, we say that a process $X$ is

    * **measurable** if $X\colon \Omega\times [0, \infty) \to \mathbb{R}$ is measurable with respect to the product $\sigma$-algebra $\mathcal{F}\otimes \mathcal{B}([0, \infty))$.

    * **adapted** if $X_t$ is $\mathcal{F}_t$-measurable for every $t$.

    * **progressively measurable** if for every $t$, the function $X\colon \Omega \times [0, t]\to \mathbb{R}$, $(\omega, s) \mapsto X_s(\omega)$ is measurable with respect to the product $\sigma$-algebra $\mathcal{F}\otimes \mathcal{B}([0, t])$


In particular, progressively measurable processes are automatically adapted.
The reciprocal is true if the paths of the process are regular enough.

!!! proposition
    Let $X$ be a càd or càg $\mathbb{F}$-adapted process.
    Then $X$ is progressively measurable.

!!! proof
    Suppose that $X$ is càd and fix $t$.
    Define

    
    \[
        X^n_s=X_{\frac{k+1}{2^n}t}, \quad \text{for} \quad \frac{k}{2^n}t \leq  s < \frac{k+1}{2^n}t
    \]

    It follows that $X^n$ is also càd as $X$, hence $\lim X^n =X$ on $\Omega \times [0,t]$ up to the null set of those $\omega$ on which $X$ does not have right-continuous paths.
    Furthermore, since $X$ is adapted, it follows that the piecewise constant process $X^n$ is $\mathcal{F}_t\otimes \mathcal{B}([0,t])$-measurable.
    Hence $X$ is progressively measurable.

The previous result makes use of the regularity of paths to derive progressive measurability from adaptiveness.
The following result goes a step further by showing that measurability together with adaptiveness yields progressive measurability, up to a modification though.

!!! theorem
    Any measurable and adapted process admits a progressive modification.

The proof of this theorem is clearly not trivial, somewhat lengthy and often just mentioned like here without proof. If you are interested you can see Delacherie and Meyer[@Dellacherie1978][@Dellacherie1982].

The notion of stopping times also has to be slightly modified in the continuous time.

!!! definition
    On a probability space, a *random time* is a measurable mapping $\tau :\Omega \to [0, \infty)\cup \{\infty\}$.
    Given a filtration, a random time is

    - an **optional time** if $\{\tau <t\}$ is in $\mathcal{F}_t$ for every $t$.
    - a **stopping time** if $\{\tau \leq t\}$ is in $\mathcal{F}_t$ for every $t$.

!!! proposition
    Every stopping time is an optional time, and every optional time is a stopping time for the right-filtration.
    In particular, the two notions coincide if the filtration is right-continuous.

!!! proof
    The first assertion is trivial.
    As for the second, let $\tau$ be an optional time and fix $t$.
    It follows that $\{\tau \leq t\}=\cap_n\{\tau < t+ 1/n\}$ which is an event in $\mathcal{F}_{t}^+$.

For a process $X$ and a subset $V$ of the state space we define the **hitting time** of $X$ in $V$ as

\[
\tau_V(\omega)=\inf\{t\colon X_t(\omega)\in V\}.
\]

This function is not necessarily measurable even if $X$ is adapted, however we have the following.

!!! proposition
    If $X$ adapted and càd and $V$ is open, then $\tau_{V}$ is an optional time.
    If $X$ is adapted and continuous and $V$ is closed, then $\tau_{V}$ is a stopping time.

!!! proof
    It holds $\{\tau_V <t\}=\{\omega \in \Omega: X_s(\omega)\in V, s<t\}$.
    Since $X$ is càd and $V$ is open, $X_s(\omega)$ being in $V$ implies the existence of a rational $q<t$ such that $X_q(\omega)$ is already in $V$.
    Hence 

    \[
      \{\tau_V<t\}=\{X_q \in V:  q<t\}=\cup_{ q<t}\{X_q \in V\}\in \mathcal{F}_t
    \]
    
    For the case of $X$ being continuous and $V$ closed, define the open sets $V_n=\{x: d(x,V)<1/n\}\supseteq V$.
    Then by continuity of $X$ we obtain

    
    \[
      \{\tau_V \leq t\}=\{X_t \in V\}\cup \left( \cap_n \cup_{ q<t}\{X_q \in V_n\} \right) \in \mathcal{F}_t.
    \]

Let us collect some standard properties of optional and stopping times.

!!! proposition
    The following assertions hold:

    - Every constant $t$ is a stopping time;
    - $\tau+\sigma$, $\tau \vee \sigma$ and $\tau\wedge \sigma$ are stopping/optional times as soon as $\tau,\sigma$ are stopping/optional times;
    - $\lim \tau^n$ is a stopping time as soon as $(\tau^n)$ is an increasing sequence of stopping times;
    - $\lim \tau^n$ is an optional time as soon as $(\tau^n)$ is a decreasing sequence of optional times;
      It is a stopping time if $(\tau^n)$ are stationary stopping times, that is, $\tau^m(\omega)=\tau^n(\omega)$ for all $m$ greater than a given $n$, for $P$-almost all $\omega \in \Omega$;
    - If $\tau$ is a stopping time, then the collection $\mathcal{F}_\tau=\{A \in \mathcal{F}: A\cap \{\tau\leq t\}\in \mathcal{F}_t\}$ is a $\sigma$-algebra and $\tau$ is $\mathcal{F}_{\tau}$-measurable;
    - For any two stopping times, it holds $\mathcal{F}_{\sigma}\cap \mathcal{F}_{\tau}=\mathcal{F}_{\sigma \wedge \tau}$.
      In particular, $\mathcal{F}_{\sigma}\subseteq \mathcal{F}_{\tau}$, if $\sigma \leq \tau$.
      For every integrable random variable $\xi$, it holds $E[E[\xi|\mathcal{F}_{\sigma}]| \mathcal{F}_{\tau}]=E[\xi| \mathcal{F}_{\sigma \wedge \tau}]$.

!!! proof
    The proof follows the same argumentation as in the discrete time since $\mathbb{Q}$ is a countable dense subset of $[0, \infty)$.
    Only the following two points need a certain care.

    - Let $\tau$ and $\sigma$ be two stopping times, let us show that the sum is still a stopping time.
        Noting that $\tau$ is a stopping time if and only if $\{\tau >t \}=\{\tau\leq t\}^c$ is in $\mathcal{F}_t$ for every $t$, the following decomposition holds

      
        \[
        \{\tau+\sigma >t\}=\{\tau=0, \sigma > t\}\cup \{\sigma=0,\tau > t\}\cup \{\tau \geq t, \sigma>0 \}\cup\{\sigma+\tau>t,0<\tau<t\}
        \]

        Noting that $\{\tau=0\}=\{\tau\leq 0\}$ is in $\mathcal{F}_0\subseteq \mathcal{F}_t$, the same for $\{\sigma=0\}$ being in $\mathcal{F}_t$, it follows immediately that the first two sets are in $\mathcal{F}_t$.
        Further, $\{\tau \geq t\}=\cap_{n}\{\tau>t-1/n\}$ is in $\mathcal{F}_{t-}\subseteq \mathcal{F}_t$ and $\{\sigma>0\}$ is in $\mathcal{F}_0$ showing that the third set in this decomposition is in $\mathcal{F}_t$.
        As for the last one, note that

      
        \[
          \{\sigma+\tau>t,0<\tau<t\}=\cup_{0<q<t}\{\sigma>t-q\}\cap\{t>\tau>q\}=\cup_{0<q<t}\{\sigma>t-q\}\cap \{\tau>q\}\cap \{\tau<t\}
        \]

        which is for the same reason as before in $\mathcal{F}_t$ since $0<q<t$.

    - Suppose that $\tau^n$ is a decreasing sequence of optional times.
      It follows from $\{\lim \tau^n <t\}=\{\tau^n <t: \text{ for some }n\}=\cup_n\{\tau^n <t\}$ is in $\mathcal{F}_t$ that $\lim \tau^n$ is an optional time.
      If $\tau^n$ are stopping times, it only holds $\{\lim \tau^n \leq t\}=\cap_{q>0}\{\tau^n \leq t+q: \text{for some }n\}$ is in $\mathcal{F}^+_t$ and therefore $\lim \tau^n$ is optional.
      However, defining $A_n=\{\tau^n=\tau^m: \text{for all }m\geq n\}$, it follows from stationarity that $A_n$ is increasing to $\Omega$.
      Furthermore, $A_n$ is an event in $\mathcal F_{\tau^n}$ and hence $\{\lim \tau^n \leq t\}=\cup_n \{\tau^n\leq t\}\cap A_n$ is in $\mathcal{F}_t$.

!!! proposition
    Let $X$ be a progressively measurable process and $\tau$ a stopping time with $\tau <\infty$.
    Then $X_\tau(\omega):=X_{\tau(\omega)}(\omega)$ is an $\mathcal{F}_{\tau}$-measurable random variable.
    Furthermore, $X^\tau:=(X_{\cdot\wedge \tau})$ is a progressive process.

!!! proof
    First, $\tau$ being a stopping time implies that $(\omega,s)\mapsto h(\omega,s):= (\omega, \tau(\omega)\wedge s)$ from $\Omega \times [0,t]$ onto itself is $\mathcal{F}_t\otimes \mathcal{B}([0,t])$-measurable for every $t$.
    Since $X$ is progressive and $X^\tau_s(\omega)=X\circ h(\omega, s)$ for every $s\leq t$, it follows that $(s,\omega)\mapsto X^\tau_s(\omega)$ is also $\mathcal{F}_t\otimes \mathcal{B}([0,t])$-measurable.
    Thus $X^\tau$ is progressive and, in particular, $X_{\tau}$ is $\mathcal{F}_{\tau}$-measurable.

The null sets on a probability space play a central role.
They allow to identify random variables in the almost sure sense.
With regard to a filtration indexed by an uncountable time set, this may yield some tricky problems — this is mainly due to the problem of right-continuous version of processes not further discussed here, see Theorem III-44 p.~64, Theorems IV-32-33 pp.~102--103 From Delacherie-Meyer[@Dellacherie1978].
In order to get rid of these problems and the identification between optional and stopping times we will work with the following assumption.

!!! definition
    A filtration $\mathbb{F}$ is said to 

    - be **complete** if $\mathcal{F}_0$ contains all the $P$-negligible sets of $\mathcal{F}$;

    - satisfy the **usual conditions** if it is complete and right-continuous, that is $\mathbb{F}^+=\mathbb{F}$.

From now on, unless otherwise specified:

\[
\mathbb{F}=\mathbb{F}^+\quad \text{and}\quad \mathcal{F}_0\text{ contains all the }P\text{ null sets of }\mathcal{F}
\]

For a stopping/optional time $\tau$, we denote by $[\tau]=\{(\omega,t) \in \Omega \times \mathbf{T}: \tau(\omega)=t\}$ its graph.

!!! proposition
    Let $X$ be a càdlàg, adapted process on a filtration satisfying the usual conditions.
    Then there exists a sequence of stopping times $(\tau^n)$ which exhausts the jumps\footnote{For $X$ càdlàg, the jump process $\Delta X$ is the difference of $X$ with the càglàd version $X_{-}$ of $X$} $\Delta X=X-X_{-}$ of $X$, that is

    
    \[
    \left\{\Delta X\neq 0\right\}\subseteq\bigcup_{n}\left[ \tau^n \right].
    \]

This proposition is also particularly difficult to prove buy it basically shows that the jumps can be described by stopping times.

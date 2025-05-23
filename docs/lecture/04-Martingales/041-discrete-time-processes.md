# Discrete Time Stochastic Processes


## Stochastic Process, Filtration, Adaptiveness

!!! definition

    A **stochastic process* is a family $X=(X_t)$ of random variables $X_t:\Omega \to \mathbb{R}$ indexed by $t$ in $\mathbb{N}_0$.

    For a given state $\omega$, the mapping $t \mapsto X_t(\omega)$ describing the evolution in state $\omega$ of the process is called a **sample path** or **trajectory**.


A stochastic process $X=(X_t)_{t=0,\ldots, T}$ may also be viewed as:

- A **single random variable**
  
    \[
    \begin{aligned}
      X\colon\Omega \times \mathbb{N}_0 &\longrightarrow \mathbb{R}\\
      (\omega,t)&\longmapsto X(t, \omega)  X_t(\omega)
    \end{aligned}
    \]

    where the $\sigma$-algebra on $\Omega \times \{0,1, \ldots \}$ is given by the product $\sigma$-algebra $\mathcal{F}\otimes 2^{N_0}$.

- A **measurable function with values in the sample space**

    \[
    \begin{aligned}
        X\colon\Omega &\longrightarrow \mathbb{R}^{\mathbb{N}_0}\\
        \omega &\longmapsto X(\omega) = (X_0(\omega), X_1(\omega), \ldots)
    \end{aligned}
    \]

  where the $\sigma$-algebra on the sample space is the product Borel $\sigma$-algebra on $\mathbb{R}^{\mathbb{N}_0}$.

!!! exercice
    Show that the three definitions of a stochastic process in finite discrete time are equivalent.

!!! example "Example: Random Walk"

    Consider now our example of coin tossing but infinitely many times.
    To do so consider a sequence $(Y_t)_{t=1, 2, \ldots}$ of iid random variables with

    \[
      P[Y_t = 1] = P[Y_1 = 1] = p\quad \text{and}\quad P[Y_t = -1] = P[Y_1 = -1] = 1-p
    \]
    
    for $0\leq p\leq 1$, in other terms the sequence are iid binary random variables.

    We define the random walk $S=(S_t)$

    \[
    S_0=s_0 \quad \text{ and }\quad S_t= S_{t-1} + Y_t = s_0+\sum_{s=1}^t Y_s, \quad t =1, \ldots
    \]

    where $s_0$ in $\mathbb{R}$ is the start value of the random walk.

    
    ![Random Walk](./../../images/rw_dark.svg#only-dark){align = right}
    ![Random Walk](./../../images/rw_white.svg#only-light){ align = right}


As such, a process is nothing else than an arbitrary family of random variables indexed by time.
However, our intuitive understanding of a process rather corresponds to observing the outcome of which as times goes by.
In other terms $X_s$ "is providing less information" than $X_t$ whenever $s\leq t$.
To model this intuition, we use an increasing set of information.

!!! definition "Definition: Filtration, Adapted Processes"

    A **filtration** $\mathbb{F}=(\mathcal{F}_t)$ is a family of $\sigma$-algebras on $\Omega$

    \[
      \mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \ldots \subseteq \mathcal{F}_t \subseteq \ldots \subseteq \mathcal{F}
    \]

    A measurable space together with a filtration is called a **filtered** space and denoted by the tuple $(\Omega, \mathcal{F}, \mathbb{F},P)$.

    We call a stochastic process $X$ **adapted** if $X_t$ is $\mathcal{F}_t$-measurable for every $t$.

The $\sigma$-algebras in a filtration become finer and finer due to the inclusion.
It means that the considered events at time $t$ provide more information than those at previous times.

Filtrations can be given, but also generated by stochastic processes.
Indeed, given a stochastic process $X$, we can define the filtration generated by the information revealed by $X$ over time, that is

\[
\mathcal{F}_t^X=\sigma(X_0, X_1, \ldots, X_t)
\]

for every time $t$.
It is clearly a filtration called **filtration generated by** $X$ and denoted by $\mathbb{F}^X$.
Note that $X$ by definition $X$ is adapted to $\mathbb{F}^X$.
It is in fact the smallest filtration to which $X$ is adapted to.
That is, if $X$ is adapted to any other filtration $\mathbb{F}$ then it holds that $\mathbb{F}^X \subseteq \mathbb{F}$.

!!! example
    In our random walk example, we did not specify a filtration, but we can consider the following sequences of $\sigma$-algebras

    - $\mathcal{F}^X_t$;
    - $\mathcal{F}^S_t$;
    - $\mathcal{G}_t:=\sigma(S_t)$;
    - $\mathcal{H}_t:=\sigma(X_t)$.

    As an exercise, try to figure out which sequence of $\sigma$-algebras is a filtration.


## Stopping Time

A further important notion in the theory of stochastic processes is the so-called **stopping time**.
Before diving into the definition and properties, let us consider the following game.

!!! example "Example: Strategic Betting?"

    You have $100$ renminbi and you are offered a choice between the following games:

    * **Game 1:** toss a coin 100 times and every time you get $1$ you increase by 1 renminbi while if you get $-1$ you loose $1$ renminbi. (all in strategy)

    * **Game 2:** toss a coin 100 times and every time you get $1$ you increase by 1 renminbi while if you get $-1$ you loose $1$ renminbi.
        However, as soon as your total amount of money drops to $70$ renminbi you are allowed to quit playing. (stop loss strategy)

    * **Game 3:** toss a coin 100 times and every time you get $1$ you increase by 1 renminbi while if you get $-1$ you loose $1$ renminbi.
        However, as soon as your total amount of money reaches a value of $120$ renminbi you are allowed to stop playing. (stop gain strategy)

    * **Game 4:** toss a coin 100 times and every time you get $1$ you increase by 1 renminbi while if you get $-1$ you loose $1$ renminbi.
        However, as soon as your total amount of money reaches a value of $120$ or drop to $70$ renminbi you are allowed to stop playing. (stop loss-gain strategy)

    * **Game 5:** don't play and keep your 100 renminbi. (coward strategy)

    The coin is fair, now which game would you choose?
    After your decision, suppose that I scale the game by $10000$ (start value and $100% rmb per coin toss), would you choose the same game?
    Why?


    The random walk $S= (S_t)$ starting at $100$ is clearly well suited to model it.
    In the case of the first game your outcome is given by $S_{100}(\omega)$ where $\omega = (\omega_t)_{t=1,\ldots, 100}$ represents the outcomes of the coin toss $\pm 1$.
    In the case of the last game the outcome is $S_0 = 100$.
    We are stilll facing the following questions
    
    * What about the other games? The time at which you quit the game is random depending on the evolution of the stochastic process.
    * Which game delivers in expectation the largest outcome?


We therefore introduce the notion of a *random time* which intuitively provides information about when a random event occurs.

!!! definition "Definition: Stopping Time"

    A **random time** is a measurable mapping $\tau :\Omega \to \mathbb{N}_0 \cup \{\infty\}$.

    A random time is a **stopping time** if $\{\tau \leq t\}$ is an event in $\mathcal{F}_t$ for every $t=0, 1, \ldots$.

!!! remark
  
    Since we are working in discrete time, for a random time $\tau$ to be a stopping time, it is equivalent to require $\{\tau = t\}$ being an event in $\mathcal{F}_t$ for all $t$.
    Indeed, it follows from $\mathbb{F}$ being a filtration and

    \[
      \{\tau \leq t\} = \cup_{s=0}^t \{\tau = s\} \quad \text{and}\quad \{\tau = t\} = \{\tau \leq t\} \cap \{\tau \leq t-1\}^c
    \]


The notion of stopping time just precises that the event to stop before a given time only depends on the information up to time $t$.
Stopping times are truly complex object conceptually as they are inherently depending on the whole past history.
However, it is relatively easy to construct stopping times:
Let $X=(X_t)$ be a stochastic process and $B \subseteq \mathbb{R}$.
We define the function

\[
\tau_B(\omega) = \inf\{t \colon X_t(\omega) \in B\}
\]

This function is called a **hitting time** or **entry time** and is well defined.
However, it requires further assumption so as to be a random time let alone a stopping time.

!!! proposition
    If $B$ is a Borel set, then $\tau_B$ is a random time.
    If additionally $X$ is adapted then $\tau_B$ is a stopping time.


!!! proof

    For any $t$ it holds that $\{\tau \leq t\} = \cup_{s=0}^t\{X_s \in B\}$ showing that if $B$ is borel, the right hand side is a finite union of events.
    If additionally $X$ is adapted, each event in the finite union belongs to some $\mathcal{F}_s \subseteq \mathcal{F}_t$ for $s\leq t$.


Let us collect some standard properties of stopping times.

!!! proposition
    The following assertions hold:

    1. Every deterministic time $\tau \equiv t$ is a stopping time;
    2. $\tau+\sigma$, $\tau \vee \sigma$ and $\tau\wedge \sigma$ are stopping times as soon as $\tau,\sigma$ are stopping times;

    3. $\lim \tau^n$ is a stopping time as soon as $(\tau^n)$ is an increasing sequence of stopping times.

    4. If $\tau$ is a stopping time, then the collection $\mathcal{F}_\tau=\{A \in \mathcal{F}: A\cap \{\tau\leq t\}\in \mathcal{F}_t\}$ is a $\sigma$-algebra and $\tau$ is $\mathcal{F}_{\tau}$-measurable.

    5. For any two stopping times, it holds $\mathcal{F}_{\sigma}\cap \{\sigma\leq \tau\}\subseteq \mathcal{F}_{\sigma \wedge \tau}=\mathcal{F}_{\sigma}\cap \mathcal{F}_{\tau}$.
        For every integrable random variable $X$ with respect to some probability on $\mathcal{F}$, it holds

        \[
        E[E[X\,|\,\mathcal{F}_{\sigma}]\,|\, \mathcal{F}_{\tau}]=E[X\,|\, \mathcal{F}_{\sigma \wedge \tau}]
        \]

!!! proof

    1. Define $\tau \equiv t_0$ for some given time.
        From $\{\tau \leq t\} = \emptyset$ if $t<t_0$ or $\Omega$ otherwize, it follows that $\tau$ is a stopping time.

    2. Follows from

        \[
          \begin{align}
            \left\{\tau+\sigma \leq t\right\} &= \cup_{q=0}^t\left\{\sigma\leq t-q\right\}\cap \left\{\tau \leq q\right\}\\
            \left\{\tau\vee \sigma \leq t\right\} &= \left\{\tau \leq t\right\}\cap \left\{\sigma \leq t\right\}\\
            \left\{\tau\wedge \sigma \leq t\right\} &= \left\{\tau \leq t\right\}\cup \left\{\sigma \leq t\right\}.
          \end{align}
        \]
        
        all right-hand sides being finite union of events contained in $\mathcal{F}_t$.

    2. Follows from

        \[
        \left\{\lim \tau^n\leq t\right\}=\left\{\tau^n\leq t:\text{ for all }n\right\}=\cap\left\{\tau^n \leq t\right\}
        \]

    3. Clearly, $\emptyset$ and $\Omega$ belong to $\mathcal{F}_\tau$.
        For $A \in \mathcal{F}_\tau$ it holds

        \[
          A^c \cap \left\{\tau\leq t\right\}=(A \cup \left\{\tau >t\right\})^c=[(A\cap \left\{\tau \leq t\right\})\cup \left\{\tau\leq t\right\}^c]^c \in \mathcal{F}_t.
        \]

        Finally, for $(A_n)\subseteq \mathcal{F}_{\tau}$ it holds

        \[
          (\cup A_n)\cap \left\{\tau \leq t\right\}=\cup (A_n \cap \{\tau \leq t\}) \in \mathcal{F}_t.
        \]

    4. Let $A \in \mathcal{F}_{\sigma}$.
        For every $t$, it holds

        \[
          A\cap \left\{ \sigma \leq \tau \right\}\cap \left\{ \tau \leq t \right\} =\left( A\cap \left\{\sigma \leq t \right\} \right)\cap \left\{ \tau \leq t \right\}\cap \left\{ \sigma \wedge t\leq \tau \wedge t \right\},
        \]

        \[
          A\cap \left\{ \sigma \leq \tau \right\}\cap \left\{ \sigma \leq t \right\} =\left( A\cap \left\{\sigma \leq t \right\} \right)\cap \left\{ \sigma \wedge t\leq \tau \wedge t \right\}.
        \]

        Both of these are in $\mathcal{F}_t$ since $\sigma \wedge t$ and $\tau\wedge t$ are $\mathcal{F}_t$-measurable.
        Hence, $\mathcal{F}_{\sigma}\cap \{\sigma\leq \tau\}\subseteq \mathcal{F}_{\sigma}\cap \mathcal{F}_\tau$.

        We now show that $\mathcal{F}_{\sigma}\cap \mathcal{F}_{\tau}=\mathcal{F}_{\sigma \wedge \tau}$.
        Let $A \in \mathcal{F}_\sigma\cap \mathcal{F}_{\tau}$.
        It follows that $A\cap \{\sigma\leq t\} \in \mathcal{F}_t$ and $A\cap \{\tau \leq t\} \in \mathcal{F}_t$ for every $t$.
        Hence,

        \[
          (A\cap \{\sigma \leq t\})\cup(A\cap \{\tau \leq t\})=A\cap(\{\sigma \leq t\}\cup\{\tau\leq t\})=A\cap \{\sigma\wedge \tau \leq t\}
        \]

        showing that $A \in \mathcal{F}_{\sigma\wedge \tau}$ and therefore $\mathcal{F}_{\sigma}\cap \mathcal{F}_{\tau}\subseteq \mathcal{F}_{\sigma\wedge \tau}$.

        Conversely, let $A \in \mathcal{F}_{\sigma\wedge \tau}$.
        It follows that

        \[
          A\cap (\{\sigma\leq t\}\cup \{\tau \leq t\})= (A\cap \{\sigma \leq t\})\cup(A\cap \{\tau \leq t\})\in \mathcal{F}_t
        \]

        for every $t$.  
        Since $\{\sigma \leq t\}$ is in $\mathcal{F}_t$, it follows that

        \[
          (A\cap \{\sigma \leq t\})\cup(A\cap \{\tau \leq t\})\cap \{\sigma \leq t\}=A\cap \{\sigma \leq t\}
        \]

        is also in $\mathcal{F}_t$ for every $t$.
        Hence, $A$ is in $\mathcal{F}_\sigma$.
        Similarly, $A$ is in $\mathcal{F}_\tau$, and therefore $A$ is in $\mathcal{F}_{\sigma}\cap \mathcal{F}_{\tau}$, showing that $\mathcal{F}_{\sigma\wedge \tau}=\mathcal{F}_{\sigma}\cap \mathcal{F}_{\tau}$.
        Note that $\{\sigma \leq \tau\}$ and $\{\tau \leq \sigma\}$ are both in $\mathcal{F}_{\sigma\wedge \tau}$.
        Hence, for $X$ integrable, it follows that

        \[
          E[E[X|\mathcal{F}_{\sigma}]|\mathcal{F}_\tau]=E[E[X|\mathcal{F}_\sigma]1_{\{\sigma \leq \tau\}}|\mathcal{F}_{\tau}]+E[E[X|\mathcal{F}_\sigma]|\mathcal{F}_{\tau}]1_{\{\tau<\sigma\}}.
        \]

        From $\mathcal{F}_{\sigma}\cap \{\sigma \leq \tau\}\subseteq \mathcal{F}_{\sigma \wedge \tau}$, it follows that $E[X|\mathcal{F}_\sigma]1_{\{\sigma \leq \tau\}}$ is $\mathcal{F}_{\sigma \wedge \tau}$-measurable, and so is $E[E[X|\mathcal{F}_\sigma]1_{\{\sigma \leq \tau\}}|\mathcal{F}_{\tau}]$.
        A similar argument applies to $E[E[X|\mathcal{F}_\sigma]|\mathcal{F}_{\tau}]1_{\{\tau <\sigma\}}$, proving the assertion.

!!! proposition "Proposition/Definition: Stopped Process"
    Let $X$ be an adapted process and $\tau$ a stopping time.

    * If $\tau$ is finite, that is $\tau<\infty$, then $X_\tau(\omega):=X_{\tau(\omega)}(\omega)$ is an $\mathcal{F}_{\tau}$-measurable random variable.

    * The process $X^\tau:=(X_{t\wedge \tau})$ is an adapted process called the **stopped process**.

!!! proof
    Let $B$ be a Borel subset of $\mathbb{R}$ and $\tau$ be a finite stopping time.
    It holds

    \[
      \left\{ X_{\tau}\in B \right\}=\cup_t (\left\{ X_t\in B \right\}\cap \{\tau=t\})
    \]

    the right hand side being a countable union of events in $\mathcal{F}$ showing that $X_{\tau}$ is a random variable.
    Let us show that this random variable is $\mathcal{F}_\tau$-measurable.
    Let $A=\{ X_{\tau}\in B\}$ and fix $t$.
    It holds

    \[
      A\cap \{\tau \leq t\}=\cup_{s\leq t}\left(\left\{ X_s\in B \right\}\cap \{\tau=s\}\right).
    \]

    However, $\{X_s\in B\}\cap \{\tau=s\}=\{X_s\in B\}\cap \{\tau\leq s\}\cap \{\tau\leq s-1\}^c$ is an event in $\mathcal{F}_s\subseteq \mathcal{F}_t$ for every $s\leq t$.
    Hence, $A\cap \{\tau \leq t\}$ is in $\mathcal{F}_t$ for every $t$, showing that $A$ is an event in $\mathcal{F}_{\tau}$ by definition.
    Thus, $X_{\tau}$ is $\mathcal{F}_{\tau}$-measurable.

    Let now $\tau$ be any stopping time.
    It follows that $t\wedge \tau$ is a finite stopping time smaller than $t$, and therefore $\mathcal{F}_{t\wedge \tau}\subseteq \mathcal{F}_t$.
    Since $X^\tau_t=X_{t\wedge \tau}$ is $\mathcal{F}_{t\wedge \tau}$-measurable, it is in particular $\mathcal{F}_t$-measurable so that $X^\tau$ is an adapted process too.


## Stochastic Integral


Let us now define one of the most important objects in stochastic analysis, namely, the **stochastic integral**.

!!! definition "Definition: Stochastic Integral"

    Let $X = (X_t)$ and $H=(H_t)$ be two stochastic process whereby 

    * $X$ is adapted;
    * $H$ is **predictable**, that is $H_0$ is in $\mathbb{R}$ and $H_t$ is $\mathcal{F}_{t-1}$-measurable for every $t=1, \ldots$;

    The **stochastic integral** $H\bullet X$ of $H$ with respect to $X$ is defined as the process

    \[
      H\bullet X_t=H_0X_0+\sum_{s=1}^t H_s \left( X_s-X_{s-1} \right)=H_0X_0+\sum_{s=1}^t H_s \Delta X_s.
    \]

In other terms the stochastic integral is the integration of $H$ against the increments $\Delta X$ of $X$.
In continuous terms it would formally look like this

\[
H\bullet X_t = H_0 X_0 + \int_0^t H_s dX_s
\]


!!! lemma
    Clearly the collection of adapted and predictable processes are vector spaces.

    * The operator $\bullet$ is bilinear;
    * $H\bullet X$ is an adapted process itself;
    * For every stopping time $\tau$, the stochastic process $1_{\{\cdot \leq \tau\}} = (1_{\{t\leq \tau\}})$, is predictable

    * **Stopping the stochastic integral:** For any stopping time $\tau$ it holds that

        \[
          \left( H1_{\{\cdot \leq \tau\}}\right) \bullet X = \left(H\bullet X\right)^\tau = H\bullet X^\tau
        \]

        In particular $1_{\{\cdot \leq \tau\}}\bullet X = X^\tau$ since $1\bullet X = X$.

The last equality might be better understood in classical integral terms (ignoring the first constant term):

\[
\int_0^t H_s 1_{\{s\leq \tau\}} dX_s = \int_0^{t\wedge \tau} H_s dX_s = \int_0^t H_s dX^\tau_s
\]

since $H1_{\{\cdot \leq \tau\}}$ is equal to $0$ after $\tau$ and $X^\tau$ is constant after $\tau$ (hence null increments after $\tau$).


!!! proof

    The proof is mechanical and left as an exercise.
    Only for $1_{\{\cdot \leq \tau\}}$ being predictable it comes from the fact that $\{t\leq \tau\} = \{\tau < t\}^c = \{\tau \leq t-1\}^c$ which is an event in $\mathcal{F}_{t-1}$.



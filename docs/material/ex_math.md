# Exercises: Probability and Stochastic Processes


## Probability

!!! remark

    For the Radon Nykodym theorem, the notion of absolute continuity and equivalence between probability measure is central.

    !!! definition

        Given two probability measure $P$ and $Q$ we say that

        1. $Q$ is absolutely continuous with respect to $P$ and denote $Q\ll P$ if 

            \[ P[A] = 0 \quad \text{implies} \quad Q[A] = 0\]

        2. $Q$ is equivalent to $P$ and denote $Q\sim P$ if both $Q\ll P$ and $P\ll Q$.
            That is

            \[ P[A] = 0 \quad \text{if and only if} \quad Q[A] = 0\]
      
    By definition it clearly holds that

    \[
        Q \ll P \quad \text{if and only if} \quad P[A] = 1 \, \text{implies}\, Q[A] = 1
    \]

    or

    \[
        Q \ll P \quad \text{if and only if} \quad Q[A] > 0 \, \text{implies}\, P[A] > 0
    \]

    and in the equivalent case


    \[
        Q \sim P \quad \text{if and only if} \quad P[A] = 1 \, \text{if and only if}\, Q[A] = 1
    \]

    or

    \[
        Q \sim P \quad \text{if and only if} \quad P[A] > 0 \, \text{if and only if}\, Q[A] > 0
    \]




!!! exercise

    The Radon-Nykodym theorem states that if a probability measure \( Q \ll P \), then there exists a (\( P \)-almost surely) unique random variable $Z$ such that


    \[
      \begin{equation*}
        \begin{cases}
          Z & \geq 0 \\
          E^P[Z] & = 1 \\
          E^Q[X] & = E^P[Z X] \quad \text{ for any positive bounded random variable }X
        \end{cases}
      \end{equation*}
    \]

    This unique random variable is called the density of $Q$ with respect to $P$ and denoted by $dQ/dP$.

    This density allows to compute expectation of random variable under $Q$ in terms of expectation under $P$.
    If $Q\sim P$ then $dQ/dP$ is strictly positive and $dP/dQ = (dQ/dP)^{-1}$.
    
    This fundamental theorem is complex to prove in the general case, relying on other fundamental theorems of functional analysis.
    However, you can prove it easily in the finite state setting.

    Let \( \Omega=\{\omega_1,\ldots,\omega_n\} \) be a finite state space with \( \sigma \)-algebra \( \mathcal{F}=2^\Omega \) and probability measure \( P \) given by the vector \( \boldsymbol{p}=(p_1,\ldots,p_n) \) where \( P[\{\omega_i\}]=p_i>0 \) for every \( i \) and \( \sum p_i=1 \).
    
    Let now \( Q \) be another probability measure on \( (\Omega,\mathcal{F}) \) given by the vector \( \boldsymbol{q}=(q_1,\ldots,q_n) \) where \( Q[\{\omega_i\}]=q_i\geq 0 \) and \( \sum q_i=1 \).
    Since \( P[A]=0 \) implies \( A=\emptyset \), it follows that \( Q[A]=Q[\emptyset]=0 \).
    Hence, \( Q \) is absolutely continuous with respect to \( P \).
    
    Find a random variable \( \frac{dQ}{dP}:\Omega \to \mathbb{R} \) such that \( \frac{dQ}{dP}\geq 0 \), \( E_P[\frac{dQ}{dP}]=1 \), and 
    
    \[
    E_Q[X]=E_P\left[ \frac{dQ}{dP}X \right]
    \]
    
    for every random variable \( X:\Omega\to \mathbb{R} \).
    Show that \( \frac{dQ}{dP} \) is also unique.

    Note that since it is a finite setting, the random variable $dQ/dP$ can be represented by an \( n \)-dimensional vector $\boldsymbol{z} = (z_1, \ldots, z_n)$ with $z_i = dQ/dP(\omega_i)$.
    The conditions therefore translate into finding such a vector $\boldsymbol{z}$ with $z_i \geq 0$, $\sum z_i p_i = 1$ and such that for every vector $\boldsymbol{x}=(x_1, \ldots, x_n)$ it holds

    \[
      \sum x_i q_i =E^Q[X] = E\left[ \frac{dQ}{dP}X \right] = \sum x_i z_i p_i
    \]


!!! exercise

    Let \( (\Omega, \mathcal{F}, P) \) be a probability space. Given a positive random variable \( X \), we define 
    
    \[
    A = \left\{ X > 0 \right\} := \left\{ \omega \colon X(\omega) > 0 \right\} \quad \text{and} \quad A_n = \left\{ X > \frac{1}{n} \right\}, \quad n \in \mathbb{N}.
    \]
    
    Show that:
    
    1. \( A_n \subseteq A_{n+1} \) and \( \cup_{k \leq n} A_k = A_n \nearrow A \).
    2. \( P[A_n] \nearrow P[A] \).
    
        **Hint:** Show that the sequence of events \( B_1 = A_1 \), \( B_2 = A_2 \setminus A_1 \), \( B_3 = A_3 \setminus A_2 \), \( \ldots \) is such that:
    
        \[
        B_k \cap B_j = \emptyset \text{ for } k \neq j, \quad \cup_{k=1}^n B_k = A_n, \quad \text{and} \quad \cup_{k=1}^\infty B_k = A,
        \]
    
        and conclude with the property of a probability measure which implies:
    
        \[
        P\left[ \cup_{k=1}^n B_k \right] = \sum_{k=1}^{n} P\left[ B_k \right] \nearrow \sum_{k=1}^\infty P[B_k] = P\left[\cup_{k=1}^\infty B_k \right].
        \]
    
    3. Show that \( X \leq Y \) implies \( E[X] \leq E[Y] \), and deduce:
    
        \[
        \frac{1}{n} P\left[ A_n \right] \leq E\left[ X 1_{A_n} \right] \leq E\left[ X \right].
        \]
    
    4. Deduce that if \( X \geq 0 \) and \( E[X] = 0 \), then \( P[X > 0] = 0 \).
    5. Deduce that if \( X \geq 0 \) and \( P\left[ X > 0 \right] > 0 \), then \( E\left[ X \right] > 0 \).



!!! exercise

    Let \( (\Omega, \mathcal{F}, P) \) be a probability space.
    Let further \( (A_n) \) be a sequence of pairwise disjoint elements\footnote{That is \( A_n \cap A_m = \emptyset \) for every \( n \neq m \).} of \( \mathcal{F} \) such that \( P[A_n] > 0 \) for every \( n \).
    Define \( \mathcal{G} = \sigma(A_n \colon n) \), the \( \sigma \)-algebra generated by the sequence \( (A_n) \).
    That is,
    
    \[
    A \in \mathcal{G} \quad \text{if and only if} \quad A = \cup_{i \in I} A_i, \quad I \subseteq \mathbb{N}.
    \]
    
    Show that:
    
    1. For every \( B \in \mathcal{F} \), it holds
    
        \[
        P\left[ B|\mathcal{G} \right] := E\left[ 1_B |\mathcal{G} \right] = \sum P\left[ B | A_n \right] 1_{A_n}
        \]
    
        where \( P[B|A_n] := \frac{P[B \cap A_n]}{P[A_n]} \).
    
    2. For every \( X \), a bounded random variable, it holds
    
        \[
        E\left[ X|\mathcal{G} \right] = \sum \frac{E\left[ 1_{A_n} X \right]}{P[A_n]} 1_{A_n}.
        \]



## Stochastic Processes

!!! exercise

    1. Let \( X \) and \( Y \) be two identically distributed random variables. Show that
    
        \[
        E\left[ X \big| \sigma(X+Y) \right] = \frac{X+Y}{2}.
        \]
    
        **Hint:** Note that \( E[X+Y | \sigma(X+Y)] = X+Y \).
    
    2. Let \( X = (X_t)_{0 \leq t \leq T} \) be a martingale on a probability space \( (\Omega, \mathcal{F}, P) \) with a filtration \( \mathbb{F} = (\mathcal{F}_t)_{0 \leq t \leq T} \). Show that \( E[X_s|\mathcal{F}_t]=X_t \) for every \( 0 \leq t \leq s \leq T \).
    
    3. Let \( Y_1, \ldots, Y_T \) be independent random variables on a probability space \( (\Omega, \mathcal{F}, P) \) with \( Y_t > 0 \) \( P \)-almost surely and \( E[Y_t]=1 \) for every \( t \). Show that
    
        \[
        X_0 = 1, \quad X_t = \prod_{s=1}^t Y_s, \quad t = 1, \ldots, T
        \]
    
        is a martingale with respect to the filtration \( \mathcal{F}_0 = \{\emptyset, \Omega\} \) and \( \mathcal{F}_t = \sigma(Y_1, \ldots, Y_t) \).
    
    4. Let \( Y_1, \ldots, Y_t \) be independent random variables such that \( Y_t \sim \mathcal{N}(0,1) \) on some probability space \( (\Omega, \mathcal{F}, P) \). Consider the filtration \( \mathcal{F}_0 = \{\emptyset, \Omega\} \) and \( \mathcal{F}_t = \sigma(Y_1, \ldots, Y_t) \). We consider the price process
    
        \[
        S_0 > 0, \quad S_t = S_0 \exp\left( \sum_{s=1}^t \left(\sigma Y_s + \mu\right) \right)
        \]
    
        where \( \sigma, \mu \) are constants such that \( \sigma > 0 \). Let further the bank account be
    
        \[
        B_t = (1 + r)^t.
        \]
    
        For which values of \( \mu \) is the discounted price process
    
        \[
        X_t = \frac{S_t}{B_t}
        \]
    
        a martingale?
    
        **Hint:** Note that if \( Z \sim \mathcal{N}(0, \sigma^2) \), then it holds that \( E[e^Z] = e^{\sigma^2 / 2} \).




!!! exercise "Exercise: Measure Change"

    Consider a probability space \( (\Omega, \mathcal{F}, P) \) and a filtration \( \{\emptyset, \Omega\} = \mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \cdots \subseteq \mathcal{F}_T \).
    
    Let \( Q \) be a probability measure equivalent to \( P \), and we denote by \( Z = dQ / dP \) its density, that is, the unique positive integrable random variable with expectation \( 1 \) such that for any \( Q \)-integrable random variable \( H \) it holds
    
    \[
    E^Q\left[ H \right] = E\left[ Z H \right]
    \]
    
    We further denote by
    
    \[
    Z_t = E\left[ Z \, | \, \mathcal{F}_t \right], \quad t = T, T-1, \ldots, 0
    \]
    
    the conditional density.
    
    Show that:
    
    - \( Z_t \) is a positive random variable with expectation \( 1 \). It defines therefore a probability measure \( Q_t \sim P \) on \( \mathcal{F}_t \).
    - Show that the stochastic process \( Z = Z_0, Z_1, \ldots \) is a \( P \)-martingale.
    - Show that for any \( Q \)-integrable random variable \( H \) it holds
    
        \[
        E^Q\left[ H \big| \mathcal{F}_t \right] = \frac{1}{Z_t} E^P\left[ Z H \big| \mathcal{F}_t \right]
        \]
    
    - Let \( M = M_0, M_1, \ldots \) be an adapted and \( Q \)-integrable stochastic process. Show that \( M \) is a \( Q \)-martingale if and only if \( Z M \) is a \( P \)-martingale.
 

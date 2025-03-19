# Measures On Polish Spaces

In this section we address how topological assumptions on the underlying state space interplay with the probability measure.

!!! warning 
    Throughout, $S$ is a metric space[^1] with distance $d$ with corresponding Borel $\sigma$-algebra $\mathcal{S}=\mathcal{B}(S)$.

    With $B_\delta(x) = \{y \in S\colon d(x,y)<\delta\}$ we denote the open ball of size $\delta$ centered at $x$.

    For a set $A$ we define $d(x,A) = \inf \{d(x,y)\colon y \in A\}$ wich is the distance of $x$ to $a$.
    By triangular inequality it holds that $d(x, A)\leq d(x, z) + d(z, A)$ for any $z$ showing that $|d(x, A)- d(z,A)|\leq d(x,z)|$, that is $x \mapsto d(x, A)$ is Lipshitz continuous.


!!! definition "Definition: Tightness and Regularity"

    A probability measure $P$ on $(S, \mathcal{S})$ is called

    * **tight** if for any $\varepsilon>0$, there exists a compact $K$ such that 
        
        \[
          P[S\setminus K] \leq \varepsilon
        \]

    * **regular:** if for every borel set $A$ it holds

        \[
          P[A] = \sup \left\{ P[K]\colon K\subseteq A\text{ and } K \text{ compact} \right\}
        \]


Tightness shows that the metric space can be modulo $\varepsilon$ reduced in probability to a compact subset, while regularity shows that the measure of any complex Borel set can be approximated from inside by compacts.


!!! theorem

    For a probability measure $P$ on $(S, \mathcal{S})$ the following are equivalent

    * $P$ is tight;
    * $P$ is regular;

??? proof

    Clearly, regularity implies tightness.
    Reciprocally, suppose that $P$ is tight.

    * **Step 1:** We show that for any Borel set $A$ it holds
        
        \[
            P[A] = \sup\{P[F]\colon F\subseteq A \text{ where }F \text{ is closed.}\} 
        \]


        * If $A$ is an open set, define $F_n = \{x \colon d(x, A^c)\geq 1/n\}\subseteq A$ which is a closed set.
            Indeed, $x \mapsto d(x, A^c)$ is Lipschitz continuous and $F_n = d(\cdot , A^c)^{-1}([1/n, \infty))$ is the reciprocal image of a closed set, hence closed.
            Furthermore $A = \cup F_n$ since $A^c$ is closed.
            Indeed, if there exists $x$ in $A\setminus \cup F_n$, it follows that $d(x, y_n)<2/n$ for some sequence $(y_n)$ in $A^c$ showing that $y_n \to x$.
            Since $A^c$ is closed it follows that $x$ is in $A^c$ which is a contradiction.

            Since the sequence of sets $F_n$ is increasing, by lower continuity of the probability measure it follows that

            \[
              \begin{align*}
                \sup\left\{ P[F]\colon F\subseteq A, F \text{ closed} \right\} 
                    & \leq P[A]\\
                    & = P[\cup F_n ]\\
                    & = \sup P[F_n]\\
                    & \leq \sup\left\{ P[F]\colon F\subseteq A, F \text{ closed} \right\}
              \end{align*}
            \]

        * Define the collection $\mathcal{C}$ of those borel sets $A$ such that $P[A]$ and $P[A^c]$ can be approximated from inside by closed sets.
            Clearly any open set is member of $\mathcal{C}$, in particular $S$ itself.
            It is by definition closed under complementation.
            Finally, it is closed under countable unions.
            Indeed, let $(A_n)$ be a sequence in $\mathcal{C}$ and define $A = \cup A_n$.
            Choose closed sets $F_n$ and $G_n$ such that $P[A_n\setminus F_n]\leq \varepsilon/2^{n+1}$ and $P[A_n^c \setminus G_n]\leq \varepsilon/2^{n+1}$.
            Fix $m$ such that $P[A\setminus \cup_{n \leq m}A_n] \leq \varepsilon/2$ and define $F = \cup_{n\leq m}F_n \subseteq \cup_{n\leq m} A_n \subseteq A$.
            It follows that

            \[
              \begin{align*}
                P[A\setminus F] 
                  & = P[A \setminus \cup_{n\leq m} A_n] + P[\cup_{n\leq m}A_n \setminus F]\\
                  & \leq \frac{\varepsilon}{2} + P\left[ \cup_{n \leq m} A_n \setminus F_n \right]\\
                  & \leq \frac{\varepsilon}{2} + \sum_{n \leq m} \frac{\varepsilon}{2^{n+1}}
                   \leq \varepsilon
              \end{align*}
            \]

            Since $G = \cap G_n$ is closed, it follows that

            \[
              \begin{align*}
                P\left[ A\setminus G \right] 
                  & = P[\cap A_n^c \setminus \cap G_n]\\
                  & \leq P\left[ \cup A_n^c \setminus G_n \right]\\
                  & \leq \sum P[A_n^c \setminus G_n] \leq \varepsilon
              \end{align*}
            \]

            showing that $\mathcal{C}$ is a $\sigma$-algebra henceforth equal to $\mathcal{S}$ finishing the proof of the first step.

    * **Step 2:** We show the inner approximation with compacts.

        For a Borel set $A$ choose a closed set $F$ such that $P[A\setminus F] \leq \varepsilon/2$.
        By tightness, choose a compact $K$ such that $P[S\setminus K]\leq \varepsilon/2$.
        The set $F\cap K$ is itself compact, and it holds

        \[
          P[A \setminus (F\cap K)] \leq P\left[ A\setminus F \right] + P[A \setminus K] \leq \frac{\varepsilon}{2} + P[S\setminus K] \leq \varepsilon
        \]


A metric space is automatically first countable, that is, each point has a countable basis of neighborhoods namely $B_{1/n}(x)$.
Most of the metric space we will encounter later have further properties that are useful from a measure viewpoint.
Such metric spaces are called **Polish**.


!!! definition "Definition: Polish Space"

    A metric space $S$ is called **Polish** if it is 

    * separable: there exists a countable dense subset $(x_n)$;
    * complete: any Cauchy sequence is converging.


!!! theorem "Ulam's Theorem"

    Any probability measure $P$ on a Polish space $(S, \mathcal{S})$ is tight, in particular, regular.

!!! proof

    Recall that in a metric space a set $K$ is compact if and only if it is closed, complete and totally bounded.
    Clearly if $K$ is compact it is closed.
    Furthermore, as any sequence has a converging subsequence, if this sequence is Cauchy, it has a limit in $K$, hence $K$ is complete.
    Finally, for any $\varepsilon>0$, $B_{\varepsilon}(x)$ for $x$ in $K$ is an open covering which can be reduce to a finite one because of compactness.
    Reciprocally, let $(x_n)$ be a sequence in the closed, complete and totally bounded set $K$.
    For any integer $m$ there exists a finite open covering of $K$ by open balls of radius $1/m$.
    Infinitely many elements of the sequence must belong to one of such ball.
    We can therefore construct a subsequence which is Cauchy which by completness will converge showing that $K$ is compact.


    Let $(x_n)$ be a countable dense subset of $S$.
    For any $m$, since $S = \cup_n \bar{B}_{1/m}(x_n)$ where $\bar{B}_{1/m}(x_n)$ is the closed ball of radius $1/m$ centered in $x_n$, choose $N_m$ be such that $P[S \setminus K_m]\leq \varepsilon/2^m$ where $K_m = \cup_{n\leq N_m}\bar{B}_{1/m}(x_n)$.
    Clearly $K_m$ is closed as finite union of closed sets and also complete as closed subset of a complete space.
    So is $K := \cap_m K_m$.
    Let us show that $K$ is totally bounded.
    For $\delta>0$ choose $m$ such that $1/m<\delta$.
    It follows that $K \subseteq K_m =\cup_{n\leq N_m} \bar{B}_{1/m}(x_n) \subseteq \cup_{n\leq N_m}B_{\delta}(x_n)$ showing that $K$ can be covered by finitely many balls of size $\delta$, hence is totally bounded.
    We deduce that $K$ is compact.
    Finally it holds that

    \[
      P[S \setminus K] \leq \sum P[S\setminus K_m] \leq \sum \frac{\varepsilon}{2^m} = \varepsilon
    \]




[^1]: The definition of tightness and regularity only requires a topological space but most of the interesting results we will address are for Polish spaces. 

# Independence

Unlike the previous section that do hold in large part for measures without considering the special case of probability, independence is a concept that is genuinly cored into probability.

Throughout we fix a probability space $(\Omega, \mathcal{F}, P)$.

!!! definition "Definition: Independence"

    * **Independence of families:**
        A family $(\mathcal{C}^i)$ of collections of events is called **independent** if for every finite collection $(A_{i_k})_{k\leq n}$ with $A_{i_k}$ event in $\mathcal{C}^{i_k}$ for every $k=1,\ldots, n$, it holds

        \[
        P\left[ A_{i_1}\cap \cdots\cap A_{i_n} \right]=\prod_{k\leq n} P\left[ A_{i_k} \right].
        \]

    * **Independence of events:**
        A family of events $(A_i)$ is called independent if the family $(\{A_i\})$ is independent.

    * **Independence of random variables:**
        A family of random variables $(X_i)$ is called independent if $(\sigma(X_i))$ are independent.

!!! remark

    A family $(\mathcal{C}^i)$ is called *pairwise independent* if

    \[
    P[A_{i_1}\cap A_{i_2}]=P[A_{i_1}]P[A_{i_2}]
    \]

    for every $A_{i_1}\in \mathcal{C}^{i_1}$, $A_{i_2}\in \mathcal{C}^{i_2}$, which is a weaker version of independence.
    As an exercise, find three sets $A,B$ and $C$ on some probability space which are pairwise independent but not independent.

!!! proposition

    The following assertions hold:

    1. Let $\mathcal{P}_1, \ldots, \mathcal{P}_n$ be a finite family of independent $\pi$-systems.
       Then $\sigma(\mathcal{P}_1), \ldots,\sigma(\mathcal{P}_n)$ are also independent.
    2. Let $X,Y$ be two independent random variables, either positive or such that $X,Y, XY \in L^1$, then it follows that

        \[
        E[XY]=E[X]E[Y]
        \]

    3. Let $X$ be a random variable independent of a sigma-algebra $\mathcal{G}$.
        Then it holds

        \[
          E\left[ X|\mathcal{G} \right]=E\left[ X \right]
        \]

!!! proof

    1. We show the case $n=2$, the general one is done by induction.
        Let $\mathcal{C}_1$ be the collection of elements $A_1$ in $\sigma(\mathcal{P}_1)$ for which it holds

        \[
        P\left[ A_1\cap A_2 \right]=P[A_1]P[A_2] \quad \text{for every }A_2 \in \mathcal{P}_2.
        \]

        Let us show that $\mathcal{C}_1$ is a $\lambda$-system.
        Clearly, $\Omega \in \mathcal{C}_1$.
        Let $A_1 \in \mathcal{C}_1$ and $A_2\in \mathcal{P}_2$.
       
        It follows that

        \[
        P[A_1^c\cap A_2]=P\left[ A_2\right]-P[A_1\cap A_2]=P[A_2]-P[A_1]P[A_2]=(1-P[A_1])P[A_2]=P[A_1^c]P[A_2],
        \]

        showing that $A_1^c\in \mathcal{C}_1$.
        Finally, let $(A_1^n)$ be a sequence of pairwise disjoint elements in $\mathcal{C}_1$ and $A_2$ in $\mathcal{P}_2$.
        By $\sigma$-additivity of probability measures, it holds

        \[
          P\left[ \left( \cup A_1^n \right)\cap A_2 \right]=\sum P\left[ A_1^n\cap A_2 \right]=\sum P[A_1^n]P[A_2]=\left(\sum P[A_1^n]\right)P[A_2]=P\left[ \cup A_1^n \right]P[A_2],
        \]

        showing that $\cup A_1^n\in \mathcal{C}_1$.
        We deduce that $\mathcal{C}_1$ is a $\lambda$-system containing the $\pi$-system $\mathcal{P}_1$.
        Since $\sigma(\mathcal{P}_1)\subseteq \sigma(\mathcal{C}_1)=\mathcal{C}_1\subseteq \sigma(\mathcal{P}_1)$, it follows that $\mathcal{C}_1=\sigma(\mathcal{P}_1)$.
        Now let $\mathcal{C}_2$ be the set of those $A_2$ in $\sigma(\mathcal{P}_2)$ such that

        \[
          P\left[ A_1\cap A_2 \right]=P[A_1]P[A_2] \quad \text{for every }A_1 \in \sigma(\mathcal{P}_1).
        \]

        Since $\sigma(\mathcal{P}_1)$ is independent of $\mathcal{P}_2$, the same argumentation as above shows that $\mathcal{C}_2$ is a $\lambda$-system.
       
        Therefore, $\mathcal{C}_2=\sigma(\mathcal{P}_2)$ showing that $\sigma(\mathcal{P}_1)$ is independent of $\sigma(\mathcal{P}_2)$.

    2. By assumption, $\sigma(X)$ is independent of $\sigma(Y)$.
        Assume that $X$ and $Y$ are positive.
        Let $\tilde{X}=\sum_{k\leq n} \alpha_k 1_{A_k}$ and $\tilde{Y}=\sum_{l\leq m}\beta_l 1_{B_l}$ for $\alpha_k,\beta_l$ positives and $A_k\in \sigma(X)$ and $B_l\in \sigma(Y)$.
        It follows that

        \[
          E\left[ \tilde{X}\tilde{Y} \right]=\sum_{k\leq n,l\leq m}\alpha_k \beta_l P[A_k\cap B_l]=\sum_{k\leq n,l\leq m}\alpha_k\beta_l P[A_k]P[B_l].
        \]

        Since there exist sequences $\tilde{X}_n,\tilde{Y}_n$ such that $\tilde{X}_n\nearrow X$ and $\tilde{Y}_n\nearrow Y$, it follows from Lebesgue's monotone convergence that

        \[
          E\left[ XY \right]=\lim E\left[ \tilde{X}_n\tilde{Y}_n \right]=\lim E\left[ \tilde{X}_n \right]E\left[ \tilde{Y}_n \right]=E[X]E[Y].
        \]

        The case where $X,Y,XY$ are in $L^1$ follows by separating positive and negative parts.

    3. Let $X$ be an integrable random variable independent of the $\sigma$-algebra $\mathcal{G}$.
        For every $A\in \mathcal{G}$, it follows that $1_A$ and $X$ are independent, and therefore, from the previous point, it holds

        \[
          E\left[ X1_{A} \right] = E\left[ X \right]E\left[ 1_A \right].
        \]

        But on the other hand,

        \[
        E\left[ E\left[ X \right]1_{A} \right]=E\left[ X \right]E\left[ 1_A \right].
        \]

        Since $E[X]$ is a constant and $\mathcal{G}$-measurable, it follows from the uniqueness of the conditional expectation that

        \[
          E[X|\mathcal{G}]=E[X].
        \]


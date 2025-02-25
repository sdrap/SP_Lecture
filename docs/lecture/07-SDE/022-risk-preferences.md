# Risk Preferences and Measures

So far, we have introduced potential examples of risk measures and discussed their shortcomings regarding properties deemed sound for risk assessment.
Additionally, the selection of these measures might appear arbitrary.
In the following, we aim to formalize the concepts of *risk* and *uncertainty*.

On the one hand, *uncertainty* refers to the possibility of multiple outcomes.
In other words, it considers the set \( \Omega \) within a probability space.
This concept is inherently an *objective* matter, tied to the nature of the world.

On the other hand, *risk* represents a *subjective* or personal perception of uncertainty.
It depends on an individual's viewpoint and can be understood as a cautious response to uncertainty.
To model this consistently within a mathematical framework, we rely on *decision theory*, which captures preferences among various choices.
The set of possible choices is denoted by \( \mathcal{X} \).
In this context, uncertain outcomes are modeled as random variables, meaning we work with a vector space \( \mathcal{X} \) of random variables (primarily bounded for mathematical convenience).

!!! definition "Definition: Preference Order and Numerical Representation"

    A *preference order* \( \preccurlyeq \) on \( \mathcal{X} \) is a binary relation \( x \preccurlyeq y \) indicating that choice \( y \) is preferred to choice \( x \).  
    We assume this relation satisfies the following *normative* properties:

    - **Transitivity**: \( x \preccurlyeq y \) and \( y \preccurlyeq z \) imply \( x \preccurlyeq z \);
    - **Completeness**: For any two possible choices \( x \) and \( y \), either \( x \preccurlyeq y \) or \( y \preccurlyeq x \).

    A function \( U\colon \mathcal{X} \to \mathbb{R} \) is called a *numerical representation* (or utility) of a preference order \( \preccurlyeq \) if:

    \[
        x \preccurlyeq y \quad \text{if and only if} \quad U(x) \leq U(y)
    \]

Preference orders are a generic way to represent subjective views on outcomes.
The first property, **transitivity**, ensures consistency: if \( y \) is preferred to \( x \), and \( z \) is preferred to \( y \), then \( z \) must also be preferred to \( x \).
This property appears quite intuitive.
The second property, **completeness**, requires that, for any two elements, one must always express a preference between them.
This is a strong assumption, as it mandates the ability to decide between any two elements in a potentially infinite set \( \mathcal{X} \).  

These two rational (or *normative*, as decision theorists would say) assumptions often fail in empirical decision-making.
However, they are intended to model fully rational behavior in decision-making processes involving prospective outcomes.  

A *numerical representation* maps the preference ranking into \( \mathbb{R} \), providing a quantitative measure of preferences.


??? note

    Note first that if we have a numerical representation \( U \) for a preference order \( \preccurlyeq \), it is not unique.
    Any strictly increasing function \( \phi \colon \mathbb{R} \to \mathbb{R} \) defines another numerical representation \( \tilde{U} = \phi \circ U \).
    Indeed, \( x \preccurlyeq y \) is equivalent to \( U(x) \leq U(y) \), which is equivalent to \( \phi(U(x)) = \tilde{U}(x) \leq \tilde{U}(y) = \phi(U(y)) \).

    Second, starting directly with a function \( U \colon \mathcal{X} \to \mathbb{R} \), it defines a preference order \( \preccurlyeq \) by:

    \[
        x \preccurlyeq y \Leftrightarrow U(x) \leq U(y)
    \]

    As an exercise, show that \( \preccurlyeq \), so defined through a function \( U \), is a preference order, satisfying transitivity and completeness.

    Third, even if a numerical function defines a preference order, the reciprocal is not necessarily true.
    Additional assumptions are required to ensure that, for a given preference order, a numerical representation \( U \) exists.
    However, under reasonable assumptions, this is often the case.

    !!! proposition
        If the set \( \mathcal{X} \) is countable (1), then any preference order \( \preccurlyeq \) on \( \mathcal{X} \) admits a numerical representation.  
        {.annotate}

        1. Meaning that \( \mathcal{X} \) can be enumerated as a subset of \( \mathbb{N} \).

    !!! proof
        Without loss of generality, assume \( \mathcal{X} = \{x_1, x_2, \ldots\} \).
        On \( \mathbb{N} \), define a probability measure \( P[\{n\}] = p_n = 1 / 2^n \), since \( \sum p_n = 1 \).
        For each \( x_n \), define \( A_n = \{k \colon x_k \preccurlyeq x_n\} \), the set of indices \( k \) for elements in \( \mathcal{X} \) that are less preferred than \( x_n \).
        By definition, \( x_n \preccurlyeq x_m \) if and only if \( A_n \subseteq A_m \).
        The function:

        \[
            \begin{equation*}
                \begin{split}
                    U \colon \mathcal{X} &\longrightarrow \mathbb{R}\\
                        x_n & \longmapsto U(x_n) = P[A_n] = \sum_{\{k \colon x_k \preccurlyeq x_n\}} p_k
                \end{split}
            \end{equation*}
        \]
        
        defines a numerical representation of \( \preccurlyeq \).
        Indeed, \( x_n \preccurlyeq x_m \) if and only if \( A_n \subseteq A_m \).
        Since \( P \) assigns a unique probability to each element of \( \mathbb{N} \), it follows that \( A_n \subseteq A_m \) if and only if \( U(x_n) = P[A_n] \leq P[A_m] = U(x_m) \). This completes the proof.

    This proposition uses probability measures to define a numerical representation.
    The argument extends to more general sets, provided you can relate sublevel sets \( \{\tilde{x} \colon \tilde{x} \preccurlyeq x\} \) using topological arguments like smoothness.
    If such smoothness is absent, preference orders may exist without a numerical representation.

    !!! example "The Lexicographical Order Does Not Admit a Numerical Representation"
        Consider \( \mathcal{X} = [0, 1] \times [0, 1] \) and define the lexicographical order as:

        \[
            x = (x_1, x_2) \preccurlyeq y = (y_1, y_2) \quad \text{if and only if} \quad 
            \begin{cases}
              \text{either } & x_1 < y_1, \\
              \text{or } & x_1 = y_1 \text{ and } x_2 \leq y_2.
            \end{cases}
        \]

        This is a preference order (similar to library book ordering). However, since \( \mathcal{X} \) is uncountable and the preference order lacks smoothness, it can be shown that no numerical representation exists.
        Try this as an exercise: assume a numerical representation exists and derive a contradiction.

Decision theory typically frames preferences and utilities (where higher values are better). However, when discussing risk, we consider possible loss profiles \( \mathcal{L} \)—random variables representing losses.
For simplicity, we consider complete binary relations \( \preccurlyeq \), where \( L_1 \preccurlyeq L_2 \) means "\( L_1 \) is less risky than \( L_2 \)."
Thus, loss profiles are ranked by \( \preccurlyeq \) based on perceived risk.
However, the basic properties of a preference order \( \preccurlyeq \) on \( \mathcal{L} \) do not inherently convey insights about risk perception.

!!! definition "Definition: Risk Order and Risk Measures"

    A preference order \( \succcurlyeq \) on \( \mathcal{L} \) is called a *risk order* if the following two additional assumptions are satisfied:

    - **Diversification**: If \( L_1 \) is more risky than \( L_2 \), then any diversified position between the two is less risky than the worse one:

        \[
            \text{if } L_1 \succcurlyeq L_2, \quad \text{then}\quad L_1 \succcurlyeq \lambda L_1 + (1-\lambda) L_2, \quad \text{for every } 0 \leq \lambda \leq 1.
        \]

    - **Monotonicity (worse for sure is more risky)**: If the losses of \( L_1 \) are worse than those of \( L_2 \) in every state of the world, then \( L_1 \) is more risky than \( L_2 \):

        \[
            \text{if } L_1(\omega) \geq L_2(\omega) \text{ for every } \omega, \quad \text{then } L_1 \succcurlyeq L_2.
        \]

    A numerical representation \( R \colon \mathcal{L} \to \mathbb{R} \) of a risk order is called a *risk measure*.

These two additional properties express reasonable and intuitive features of risk perception. They also have implications for the properties of risk measures.

!!! proposition
    Let \( R \) be a numerical representation of a preference order \( \succcurlyeq \) on \( \mathcal{L} \).
    Then the following assertions are equivalent:
    
    - \( \succcurlyeq \) is a risk order;
    - \( R \) satisfies:
        - *Quasi-convexity*: \( \max\{R(L_1), R(L_2)\} \geq R(\lambda L_1 + (1-\lambda) L_2) \) for every \( 0 \leq \lambda \leq 1 \);
        - *Monotonicity*: If \( L_1(\omega) \geq L_2(\omega) \) for every \( \omega \), then \( R(L_1) \geq R(L_2) \).

??? proof
    Let \( L_1 \) and \( L_2 \) be two loss profiles. Assume that \( \succcurlyeq \) is a risk order.  

    For quasi-convexity, due to the completeness of the relation, assume without loss of generality that \( L_1 \succcurlyeq L_2 \), which is equivalent to \( R(L_1) = \max\{R(L_1), R(L_2)\} \).  
    For any \( 0 \leq \lambda \leq 1 \), the diversification property implies \( L_1 \succcurlyeq \lambda L_1 + (1-\lambda) L_2 \), which gives:

    \[
        \max\{R(L_1), R(L_2)\} = R(L_1) \geq R(\lambda L_1 + (1-\lambda) L_2),
    \]

    showing quasi-convexity of \( R \).

    For monotonicity, assume \( L_1(\omega) \geq L_2(\omega) \) for every \( \omega \).
    By the monotonicity assumption, \( L_1 \succcurlyeq L_2 \), which implies \( R(L_1) \geq R(L_2) \).  

    The reverse implication—that a numerical representation being quasi-convex and monotone implies \( \succcurlyeq \) is a risk order—is straightforward to verify.

This proposition shows that neither the mean-variance risk measure nor the Value at Risk represents a risk order.
Additional properties may be required of a risk measure, but they might not always align with the underlying risk order.

!!! definition

    A risk measure \( R \) is called:

    - **Cash-Invariant**: if \( R(L-m) = R(L) - m \) for every \( m \in \mathbb{R} \);
    - **Positive-Homogeneous**: if \( R(\lambda L) = \lambda R(L) \) for every \( \lambda > 0 \);
    - **Law-Invariant**: if \( R(L) = R(\tilde{L}) \) whenever the CDFs of \( L \) and \( \tilde{L} \) coincide.

Aside from law invariance, the other two properties do not hold if the risk measure is transformed by a strictly increasing function. Nevertheless, they are commonly used and practical.

!!! remark "Cash-Invariance"

    Cash-invariance is typically required from regulatory or financial perspectives. For instance, consider a financial institution with a risky position \( X \).
    The question is how much liquidity \( m \) is needed in the bank account to ensure the overall position (cash plus risky assets) has acceptable risk.  
    The threshold is that the total risk must be below zero. The total loss profile is \( L - m \), where \( L = -X \).
    By cash-invariance:

    \[
        0 \geq R(L - m) = R(L) - m \implies m \geq R(L).
    \]

    Thus, the minimal liquidity required to make the risky position acceptable is \( m = R(L) \).
    This interpretation ties the risk measure to capital requirements.

    Moreover, cash-invariance, combined with quasi-convexity, implies convexity.

    !!! lemma
        If \( R \) is a cash-invariant risk measure, then \( R \) is convex.

    ??? proof
        Let \( R \) be a cash-invariant risk measure, \( 0 \leq \lambda \leq 1 \), and \( L_1, L_2 \) be loss profiles.
        To prove \( R(\lambda L_1 + (1-\lambda) L_2) \leq \lambda R(L_1) + (1-\lambda) R(L_2) \), define \( m_1 = R(L_1) \) and \( m_2 = R(L_2) \).
        By cash-invariance and quasi-convexity:

        \[
            \begin{align*}
                R(\lambda L_1 + (1-\lambda) L_2) - \lambda m_1 - (1-\lambda)m_2 & = R\left( \lambda L_1 + (1-\lambda) L_2 - \lambda m_1 - (1-\lambda)m_2 \right) \\
                & = R\left( \lambda (L_1 - m_1) + (1-\lambda)(L_2 - m_2) \right) \\
                & \leq \max\{R(L_1 - m_1), R(L_2 - m_2)\} \\
                & = \max\{0, 0\} = 0.
            \end{align*}
        \]

!!! remark "Positive Homogeneity"

    Positive homogeneity has a financial interpretation: if \( L \) represents the loss exposure of an investment with risk \( R(L) \), scaling the investment by \( \lambda > 0 \) scales the corresponding risk by \( \lambda \).
    While desirable for mathematical reasons, super-linear scaling might be expected in some contexts.
    Positive homogeneity also implies sub-additivity, ensuring that risk is not exacerbated by combining positions.

    !!! lemma
        Let \( R \) be a cash-invariant risk measure. If \( R \) is positive homogeneous, then:

        \[
            R(L_1 + L_2) \leq R(L_1) + R(L_2).
        \]

    ??? proof
        Let \( R \) be a cash-invariant and positive-homogeneous risk measure.
        By convexity:

        \[
            \begin{align*}
                R(L_1 + L_2) & = R\left( 2 \cdot \frac{1}{2}(L_1 + L_2) \right) \\
                & = 2 R\left(\frac{1}{2}L_1 + \frac{1}{2}L_2 \right) \quad \text{(Positive Homogeneity)} \\
                & \leq 2 \left( \frac{1}{2}R(L_1) + \frac{1}{2}R(L_2) \right) \quad \text{(Convexity)} \\
                & = R(L_1) + R(L_2).
            \end{align*}
        \]


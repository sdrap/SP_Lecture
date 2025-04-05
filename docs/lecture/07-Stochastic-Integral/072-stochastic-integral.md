# Stochastic Integral

Let us fix some notations.

- By $\mathcal{M}^2_c$ we denote the space of square integrable continuous martingales $M$ such that $M_0=0$.

- For $M$ in $\mathcal{M}_c^2$, we denote by $\langle M\rangle$ the continuous natural process of bounded variation in the Doob-Meyer decomposition of the sub-martingale $M^2$. 
    That is, $M^2=\text{martingale}+\langle M\rangle$.
    We call $\langle M\rangle$ the **quadratic variations** of $M$.

- Such a continuous quadratic variation process $\langle M\rangle$ defines a product measure $P\otimes d\langle M\rangle$ on $\Omega\otimes [0,\infty)$ with $\sigma$-algebra $\mathcal{G}\otimes \mathcal{B}([0, \infty))$.

- For every locally bounded and progressive measurable process $H$ we can define the continuous and adapted process $\int H d\langle M\rangle$, and we denote by $\mathcal{L}^2(M)$ the space of progressively measurable processes $H$ such that
  
    \[
    E\left[ \int_{0}^{t}H^2 d\langle M\rangle  \right]<\infty
    \]
  
    for every $t$.
    If there is no risk of confusion, we often drop the reference to $M$ and use the notation $\mathcal{L}^2:=\mathcal{L}^2(M)$.

- We generically denote by $\Pi=\{0=\tau_0<\tau_1<\ldots<\tau_n<T\}$ a stochastic partition where $\tau_k$ are stopping times and $T>0$.
    We call it a deterministic partition if each $\tau_k=t_k \in [0,\infty)$.
    Further, we adopt the handy notation $\Delta_k Y=Y^{\tau_k}-Y^{\tau_{k-1}}$ for an increment of a progressive stochastic process $Y$.
    That is, $\Delta_kY_t=Y_t^{\tau_k}-Y_{t}^{\tau_{k-1}}=Y_{t\wedge \tau_k}-Y_{t\wedge \tau_{k-1}}$ for every $t$.

- We denote by $\mathcal{S}$ the set of simple predictable integrands
  
      \[
        H=H_0+\sum_{k=1}^n H_k 1_{(\tau_{k-1},\tau_k]}
      \]
  
      where along a stochastic partition $\Pi$, $H_k$ is $\mathcal{F}_{\tau_{k-1}}$-measurable and $|H_k|\leq C$ for every $k$ and some constant $C$.

- Finally for $H$ in $\mathcal{S}$ and $M$ in $\mathcal{M}_c^2$, we define the discrete stochastic integral
  
    \[
    \int H dM:=M_0H_0+\sum_{k=1}^nH_k(M^{\tau_k}-M^{\tau_{k-1}})=\sum_{k=1}^nH_k\Delta_k M
    \]

According to what has been done so far, we have from Doob's optional sampling theorem and the fact that $M$ is a square integrable the following proposition easily follows

!!! proposition
    Let $M$ in $\mathcal{M}_c^2$.
    It follows that $\int \cdot\, dM$ is an operator from $\mathcal{S}$ to $\mathcal{M}_c^2$.
    It satisfies the following properties:
    
    1. **Linearity:** $\int (\alpha H+\beta G) dM=\alpha\int HdM+\beta \int GdM$ for $\alpha$ and $\beta$ constants.
    
    2. **Stopping property:** $\int 1_{\{\cdot \leq \tau\}} H dM=\int H dM^\tau=\int_0^{\cdot \wedge\tau} H dM$.
    
    3. **Ito-Isometry:** for every $t$
    
        \[
          E\left[ \left( \int_{0}^{t}H dM  \right)^2 \right]= E\left[ \int_{0}^{t} H^2 d\langle M \rangle   \right]
        \]

!!! proof
    Since $H$ is uniformly bounded, we know from Doob's optional sampling theorem that $\int HdM$ is a martingale which is continuous since $M$ is continuous.
    Linearity is immediate and the stopping property is a simple adaptation of the discrete time version.

    We show the Ito-Isometry which as a consequence will show that $\int HdM$ is square integrable since $H$ is bounded and $\langle M\rangle$ is integrable, hence an element of $\mathcal{M}_c^2$.
    We denote by $N$ the martingale in the Doob-Meyer decomposition $M^2=N+\langle M\rangle$.
    Since $H$ is uniformly bounded and $M$ is square integrable, the following expectations and conditional expectations are well defined.
    
    \[
    E\left[ \left( \int_{0}^{t}H dM  \right)^2 \right]=\sum_{k=1}^n E\left[H_k^2\left(\Delta_kM_t\right)^2  \right]
    +2\sum_{k<j} E\left[ H_kH_j\Delta_k M_t \Delta_j M_t \right]
    \]
    
    Note that for every martingale, $E[M_{t\wedge \tau_j}|\mathcal{F}_{\tau_{j-1}}]=M_{t\wedge \tau_{j-1}}$, and therefore $E[\Delta_kM_t|\mathcal{F}_{\tau_{k-1}}]=0$.
    Since $j>k$ and $H$ is predictable, for the second term it holds
    
    \[
    E\left[ H_kH_j\Delta_kM_t \Delta_j M_t \right] =E\left[ H_kH_j\Delta_k M_tE\left[\Delta_j M_t|\mathcal{F}_{\tau_{j-1}}\right]\right]=0
    \]
    
    As for the first term, for the same reasons, one has
    
    \[
    \begin{align*}
      E\left[ H_k^2\left(\Delta_k M_{t} \right)^2\right]
        & = E\left[ H_k^2\left(\left(M_{t\wedge \tau_k}^2 - M_{t\wedge \tau_{k-1}}^2\right) -2 M_{t\wedge \tau_{k-1}}\left(M_{t\wedge \tau_k} - M_{t\wedge \tau_{k-1}}\right)\right) \right]\\
        & = E\left[ H_k^2 \Delta_k M^2_t \right] -2 E\left[ H_k^2 M_{t\wedge \tau_{k-1}}\underbrace{E\left[\Delta_k M_t | \mathcal{F}_{\tau_{k-1}}\right]}_{=0} \right]\\
        & = E\left[ H_k^2 \left( \Delta_k N_t + \Delta_k \langle M\rangle_t \right) \right]\\
        & = E\left[ H_k^2 \underbrace{E\left[ \Delta_k N_t|\mathcal{F}_{\tau_{k-1}} \right]}_{=0}\right] + E\left[H_k^2\Delta_k \langle M\rangle_{t} \right]\\
        & =E\left[H_k^2\Delta_k \langle M\rangle_{t} \right] 
    \end{align*}
    \]
   
    Summing up yields
    
    \[
    E\left[ \left(\int_{0}^{t}H dM\right)^2  \right]=E\left[\sum_{k=1}^n H_k^2 \Delta_k\langle M\rangle_t\right] =E\left[ \int_{0}^{t}H^2 d\langle M\rangle  \right]
    \]
    
    Showing the Ito-Isometry and finishes the proof.

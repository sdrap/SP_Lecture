# Stochastic Integral


!!! remark

    Note that if $X$ is a càdlàg sub-martingale such that $\sup_{s\leq t} X_s$ is integrable for each $t$, then $X$ is of class (DL).
    Indeed, for any stopping time it holds

    \[
        |X_{\tau \wedge t}|\leq \sup_{s \leq t}|X_s|
    \]

    showing that the family is uniformly bounded by an integrable random variable, hence, is uniformly integrable.

    In particular, if $M$ is a càdlàg martingale which is $p$-integrable for $p>1$, then $|M|^p$ is a positive sub-martingale and from from Doob's maximal inequality it follows that

    \[
        E\left[ \sup_{s\leq t} |M_s|^p \right]^{1/p} \leq \frac{p}{p-1}\left\| M_t \right\|_{p} <\infty
    \]

    For $p=2$, it follows that $M^2$ is a sub-martingale of class (DL), hence, admits a Doob-Meyer decomposition.
    In particular, if $M$ is continuous, it follows that the natural process in the decomposition is continuous too.

Let us fix some notations.

- By $\mathcal{M}^2_c$ we denote the space of square integrable continuous martingales $M$ such that $M_0=0$.

- For $M$ in $\mathcal{M}_c^2$, we denote by $\langle M\rangle$ the continuous natural process of bounded variation in the Doob-Meyer decomposition of the sub-martingale $M^2$. 
    That is, $M^2=\text{martingale}+\langle M\rangle$.
    We call $\langle M\rangle$ the **quadratic variations** of $M$.

- Such a continuous quadratic variation process $\langle M\rangle$ defines a product measure $P\otimes d\langle M\rangle$ on $\Omega\otimes [0,\infty)$ with $\sigma$-algebra $\mathcal{F}\otimes \mathcal{B}([0, \infty))$.

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

!!! remark

    The stochastic integral $\int H dM$ for simple $H$ follows the same definition as for the integral in the Lebesgue-Stieljes integral if we replace $M$ by some BV process $A$.
    Both are clearly linear operators, however, a fundamental difference between both, is the lack of monotonicity for the $\int \cdot dM$, which is a corner stone of the definition of the Lebesgue-Stieljes integral that yields monotone convergence and then dominated convergence.

    In other terms, defining the stochastic integral $\int \cdot dM$ beyond the class of simple processes can not involve the same arguments as the classical Lebesgue-Stieljes approach.
    The key answer to this problem is the so called Ito-Isometry.


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

So far we constructed a stochastic integral operator from $\mathcal{S}$ to $\mathcal{M}_{c}^2$.  
The question is whether we can extend it to some closure to $\mathcal{S}\subseteq \mathcal{L}^2(M)$ and in which form.

Let us state first a classical topological result.

!!! definition
    A metric vector space $(E,d)$ is called a Fréchet space if

    - Addition and multiplication by a scalar are continuous operations with respect to $d$.
    - $d$ is translation invariant, that is, $d(x,y)=d(x+z,y+z)$.
    - $(E,d)$ is complete.

!!! proposition
    Let $(E,d)$ and $(E^\prime,d^\prime)$ be two Fréchet spaces and $F\subseteq E$ a linear subspace.
    Any linear function $f:F\to E^\prime$ which is an isometry, that is, $d\left( f(x),f(y) \right)=d(x,y)$, can be extended uniquely to a linear function $f:\bar{F}\to E^\prime$ which is also an isometry where $\bar{F}$ is the closure of $F$ in $E$.
    In particular, the extension is continuous.

!!! proof
    For $x \in \bar{F}$, let $(x_n)$ be a sequence of elements in $F$ converging to $x$.
    It follows that $(x_n)$ is in particular Cauchy.
    By the isometric property, so is the sequence $(f(x_n))$, which, by completeness of $E^\prime$, converges to some $y \in E^\prime$.
    For another sequence $(\tilde{x}_n)$ converging to $x$, it also follows that $(f(\tilde{x}_n))$ converges to some $\tilde{y} \in E^\prime$.
    By isometry and triangular inequality

    \[
    \begin{align*}
    d^\prime(y,\tilde{y}) 
        & \leq d^\prime(y,f(x_n))+d^\prime(f(x_n),f(\tilde{x}_n))+d^\prime(f(\tilde{x}_n),\tilde{y})
        \\
        & = d^\prime(y,f(x_n))+d(x_n,\tilde{x}_n)+d^\prime(f(\tilde{x}_n),\tilde{y})
        \\
        & \leq d^\prime(y,f(x_n))+d^\prime(f(\tilde{x}_n),\tilde{y})+d(x_n,x)+d(x,\tilde{x}_n) \xrightarrow[n\to \infty]{} 0
    \end{align*}
    \]

    showing that $y = \tilde{y}$.
    Hence, the limit does not depend on the choice of the sequence $(x_n)$ converging to $x$, so that we can extend $f$ to $\bar{F}$.
    It is straightforward to check that the extension is once again an isometry and also linear since both metrics are translation invariant distances and addition as well as multiplication are continuous.
    As for the uniqueness of this isometric extension, it is also straightforward.

Since $\int \cdot \, dM$ is a linear operator which is an isometry, we will apply this classical result of functional analysis to define the stochastic integral on the closure of $\mathcal{S}$.
Two main questions now:

* **Question 1:** What are the metrics $d$ and $d^\prime$ we consider on $\mathcal{L}^2(M)$ and $\mathcal{M}_c^2$ making them into Fréchet spaces?

* **Question 2:** What is the closure of $\mathcal{S}$?

As for the first question, the answer comes from a general fact that Fréchet distances are generated by countable families of semi-norms.
For every $n$, with some abuse of notations, let

\[
  \begin{align*}
    \left\Vert H1_{[0,n]}\right\Vert_{2}
      & : =E\left[ \int H^21_{[0,n]} d\langle M\rangle \right]^{1/2}\\
      & =E\left[ \int_{0}^{n}H^2 d\langle M\rangle \right]^{1/2} \\
    \left\Vert N_n\right\Vert_{2}
      & :=E\left[ N_n^2 \right]^{1/2}
  \end{align*}
\]

for $H$ in $\mathcal{L}^2(M)$ and $N \in \mathcal{M}_c^2$.
On the one hand $\left\Vert\cdot 1_{[0,n]}\right\Vert_{2}$ is the standard $L^2$ norm on the product space of $\Omega\times [0,n]$ with the measure $P\otimes d\langle M\rangle$, and therefore a semi-norm on $\mathcal{L}^2(M)$.
On the other hand, by Doob's maximal inequality $E[\sup_{s\leq n}N_s^2]\leq C E[N_n^2]$, and therefore $\left\Vert\cdot_n\right\Vert_{2}$ is a norm on the space of continuous square integrable martingales restricted to $[0,n]$, hence a semi-norm on $\mathcal{M}^2_c$.

We can define

\[
\begin{align*}
d(H,H^\prime) &= \sum \frac{1}{2^n}\frac{\left\Vert(H-H^\prime)1_{[0,n]}\right\Vert_{2}}{1+\left\Vert(H-H^\prime)1_{[0,n]}\right\Vert_{2}}, \\
d^\prime(N,N^\prime) &= \sum \frac{1}{2^n}\frac{\left\Vert N_n-N^\prime_n\right\Vert_{2}}{1+\left\Vert N^\prime_n-N^\prime_n\right\Vert_{2}}
\end{align*}
\]

for $H,H^\prime$ in $\mathcal{L}^2(M)$ and $N,N^\prime$ in $\mathcal{M}^2_c$.

!!! lemma
    Both $(\mathcal{L}^2(M),d)$ and $(\mathcal{M}_c^2,d^\prime)$ are Fréchet spaces.

!!! proof
    It is quite standard to check that both functions define distances which are translation invariant and for which addition and multiplication by scalar in both vector spaces are continuous.
    Furthermore, it is also clear that $\mathcal{L}^2(M)$ is complete since the $\left\Vert\cdot\right\Vert_2$ norm on any compact $[0,n]$ makes $L^2(P\otimes d\langle M\rangle)$ into a complete normed space.
    We just check that $\mathcal{M}_c^2$ is complete for the distance $d^\prime$.

    Let $(M^n)$ be a Cauchy sequence in $\mathcal{M}^2_c$.
    It follows that $(M_t^n)$ is Cauchy in $L^2_t$ for any $t$, hence converges in $L^2$ to $M_t$.
    Let further $A$ be an event in $\mathcal{F}_s$.
    It follows from the martingale property of $M^n$ that $E[M_t1_{A}]=\lim_n E[M_t^n1_{A}]=\lim_n E[M_s^n 1_{A}]=E[M_s1_{A}]$.
    Choosing the càdlàg version of $M$ shows that $M$ is a càdlàg martingale with $M_t$ in $L^2_t$ for every $t$.
    Let us prove that $M$ is actually continuous.
    By Doob's maximal inequality one has

    \[
    P\left[ \sup_{s\leq t} \left\vert M_s^n-M_s\right\vert>\lambda \right]\leq \frac{1}{\lambda} \left\Vert M_t^n-M_t\right\Vert_2^2 \xrightarrow[n\to \infty]{} 0.
    \]

    Hence $P[\sup_{s\leq t}\left\vert M_s^{n_k}-M_s\right\vert>\lambda]\leq 1/2^{k}$ for some $n_k$ and every $k$.
    Applying Borel-Cantelli, it follows that $P[\liminf \{\sup_{s\leq t}\left\vert M_s^n-M_s\right\vert\leq \lambda\}]=1$ for every $\lambda$, showing that for $P$-almost all $\omega\in \Omega$ the continuous path $M^n(\omega)$ converges uniformly on $[0,t]$ to $M(\omega)$, that is $M$ is continuous.



As for the second question about the closure of $\mathcal{S}$, we have

!!! lemma
    The space $\mathcal{S}$ is dense in $\mathcal{L}^2(M)$.
    In particular, for each $H\in\mathcal{L}^2(M)$ there exists a sequence $(H^n)\subseteq\mathcal{S}$ satisfying $\left\Vert(H-H^n)1_{[0,t]}\right\Vert_{2}\to 0$ for all $t$.

!!! remark
    The “size” of the closure of $\mathcal{S}$ depends on the “regularity” of $\langle M\rangle$, allowing for more or fewer integrands for the stochastic integral with respect to $M$.
    On the one hand, if $\langle M\rangle$ is absolutely continuous — for instance in the case of the Brownian motion — then it is even possible to define a stochastic integral with respect to integrands in $L^2(P\otimes d\langle M\rangle)$ which are “only” measurable and adapted and not necessarily progressive.
    On the other hand, if $M$ were an element of $\mathcal{M}^2$ — those càdlàg martingales such that $E[M_t^2]<\infty$ for all $t$, such as some class of Lévy Processes — then it is also possible to define a stochastic integral but with respect to a smaller set of integrands, namely those predictable processes in $\mathcal{L}^2(M)$.

!!! proof
    **Step 1:** Assume first that the paths of $\langle M\rangle$ are absolutely continuous almost surely.
    In particular, $P\otimes d\langle M\rangle \ll P\otimes dt$.
    Fix $t$.

    * If $H$ is continuous, adapted and bounded, hence, by a proposition in the previous chapter, progressive, it holds that $H^n$ were

        \[
          H^n_s = H_{\frac{kt}{2^n}},
        \]

        for $kt/2^n < s \leq (k+1)t/2^n$ converges $P\otimes dt$ to $H$ on $\Omega \times [0,t]$, and by Lebesgue's dominated convergence, it follows that $\left\Vert(H^n-H)1_{[0,t]}\right\Vert_{2}\to 0$, showing that continuous adapted and bounded processes are included in $\bar{\mathcal{S}}$.

    * If $H$ is progressively measurable and bounded.
        For every $n$, define
  
        \[
        G_s^n(\omega) = n \int_{(s - 1/n) \vee 0}^s H_u(\omega) \, du.
        \]
  
        It follows that $G^n$ is a bounded, adapted and continuous process on $[0,t]$.
        By the fundamental theorem of calculus, it follows that for almost all $\omega \in \Omega$, $G_s^n(\omega) \to H_s(\omega)$ for $dt$-almost all $s \in [0,t]$.
        Hence, by Fubini, $\{\lim G^n \neq H\}$ is a $P \otimes dt$-null measure set.
        Indeed,
  
        \[
        P\otimes dt\left[ \lim G_n \neq H \right] = \int_{\Omega}\left( \int_{0}^{t} 1_{\left\{ (\omega,u): \lim G_u^n(\omega) \neq H_u(\omega) \right\}}(s) \, ds \right) P(d\omega) = 0.
        \]
  
        And since $P \otimes d\langle M\rangle \ll P \otimes dt$, it follows that $\{\lim G^n \neq H\}$ is a $P \otimes d\langle M\rangle$-null set.
        In other terms, $G^n \to H$ $P \otimes d\langle M\rangle$-almost surely.
        By Lebesgue's dominated convergence, it follows that $\left\Vert(G^n - H)1_{[0,t]}\right\Vert_{2} \to 0$.
      
        Hence, bounded progressively measurable processes are included in the closure of continuous adapted and bounded processes, themselves included in $\bar{\mathcal{S}}$.

    * If $H$ is a progressive process, define $G^n_t = H_t 1_{\{|H_t| \leq n\}}$, which is progressive and bounded.
        It follows that $G^n \to H$ $P \otimes d\langle M\rangle$-almost surely and is dominated by $H$, which is integrable.
        Hence, by dominated convergence we have $\left\Vert(H^n - H)1_{[0,t]}\right\Vert_{2} \to 0$, showing that $\mathcal{L}^2(M)$ is included in the closure of bounded progressively measurable processes, themselves included in $\bar{\mathcal{S}}$.

    **Step 2:** Let us now address the case where $d\langle M\rangle$ is not absolutely continuous with respect to $dt$.
    Just as previously, it is enough to show that every $H$ progressive, uniformly bounded by a constant $C$, and nonzero only on $[0,m]$ can be approximated by elements of $\mathcal{S}$ in the $\left\Vert\cdot\right\Vert_{2}$-norm.
    The idea is to “tweak” $d\langle M\rangle$ into a measure absolutely continuous with respect to $dt$ by means of a time change.
    Since $\langle M \rangle_s + s$ is strictly increasing and continuous, there exists a strictly increasing and continuous inverse $T:\Omega \times \mathbf{T} \to \mathbf{T}$ such that $\langle M\rangle_{T_s(\omega)}(\omega) + T_s(\omega) = s$ for all $s \in \mathbf{T}$.
    In particular,(1) $T_s \leq s$ since $A_t + t \geq t$ and $\{T_s \leq t\} = \{A_t + t \geq s\} \in \mathcal{F}_t$ for all $t$.
    It follows that $T_s$ is a bounded stopping time for every $s$.
    {.annotate}

    1.  Recall that the general right-continuous inverse of an increasing function $f$ is given by $f^{-1}(s)=\sup\{t: f(t)\leq s\}$. However, if $f$ is strictly increasing and continuous, it follows that $f^{-1}(s)=\inf\{t: s\leq f(t)\}$. Furthermore, if $f(t)\geq t$, then $f^{-1}(s)\leq s$.


    We then define the new filtration $\mathcal{G}_s := \mathcal{F}_{T_s}$ for $s \in \mathbf{T}$ and the process $G_s = H_{T_s}$, which is $\mathbb{G}$-adapted and measurable since $H$ is $\mathbb{F}$-progressive.
    However, we do not know whether $G$ is progressive.
    We can however modify it and assume that it is progressive and adapted.
    From the previous argumentation, there exists a simple process $G^\varepsilon$ of the form

    \[
    H^n_s = H_{\frac{kt}{2^n}}, \quad \text{for } \frac{kt}{2^n} < s \leq \frac{(k+1)t}{2^n}
    \]

    such that $E[\int_0^\lambda |G - G^\varepsilon|^2 ds] \leq \varepsilon/2$ for a given $\lambda$.
    However, since

    \[
    E\left[\int G_s^2 \, ds\right] \leq E\left[\int 1_{\{T_s \leq m\}} H_{T_s}^2 \, ds\right] \leq C E[\langle M\rangle_m + m] < \infty,
    \]

    we may choose $\lambda$ large enough and $G^\varepsilon$ zero outside $[0,\lambda]$ to get

    \[
    E\left[\int |G^\varepsilon_s - G_s|^2 \, ds\right] < \varepsilon.
    \]

    Reversing the time clock, it follows that

    \[
    H^\varepsilon_t = H_0 1_{\{0\}}(t) + \sum G^\varepsilon_{s_k} 1_{]T_{s_k}, T_{s_{k+1}}]}(t)
    \]

    which is a simple process since $T_{s_k}$ is a bounded stopping time and $G^\varepsilon_{s_k}$ is $\mathcal{F}_{T_{s_k}}$-measurable.
    Hence, by definition

    \[
    E\left[ \int_0^m |H_t^\varepsilon - H_t|^2 d\langle M\rangle_t \right] \leq E\left[ \int_0^m |H_t^\varepsilon - H_t|^2 (d\langle M\rangle_t + dt) \right] \leq E\left[ \int |G^\varepsilon_s - G_s|^2 ds \right] \leq \varepsilon,
    \]

    which ends the proof.


We have now all the ingredients to define the stochastic integral.

!!! theorem
    Let $M \in \mathcal{M}_c^2$.
    There exists a unique continuous linear functional 

    \[
    \begin{equation*}
      \begin{split}
        \int \cdot \, dM  \colon \mathcal{L}^2(M) & \longrightarrow \mathcal{M}_2^c\\
                                  H & \longmapsto \int H dM
      \end{split}
    \end{equation*}
    \]
    
    coinciding with the elementary stochastic integral on $\mathcal{S}$.
    Furthermore, the following properties hold:

    1. **Linearity:** $\int (\alpha H + \beta G) \, dM = \alpha \int H \, dM + \beta \int G \, dM$ for constants $\alpha$ and $\beta$.

    2. **Stopping property:** $\int 1_{\{\cdot \leq \tau\}} H \, dM = \int H \, dM^\tau = \int_0^{\cdot \wedge \tau} H \, dM$.

    3. **Itô-Isometry:** For every $t$
        
        \[
        E\left[ \left( \int_{0}^{t}H \, dM  \right)^2 \right] = E\left[ \int_{0}^{t} H^2 \, d\langle M \rangle \right]
        \]

    
    And the quadratic variations of the square integrable continuous martingale $\int H \, dM$ are given by

    \[
          \left\langle \int H \, dM \right\rangle = \int H^2 \, d\langle M \rangle
    \]

!!! proof
    We already handled here all the elements of the proof which are consequences of the previous results, up to the stopping property and the quadratic variations of $\int H \, dM$.
    As for the stopping property, it follows directly by approximating $H \in \mathcal{L}^2$ by elements in $\mathcal{S}$.

    As for the quadratic variations of $\int H \, dM$, note that $\int H_s^2 \, d\langle M\rangle$ is a continuous process of bounded variation, hence normal.
    From the uniqueness of the Doob-Meyer decomposition, we just have to show that

    \[
    \left( \int H \, dM \right)^2 - \int H^2 \, d\langle M\rangle
    \]

    is a martingale.
    Clearly it is integrable and adapted.
    For $s \leq t$ and any event $A$ in %\mathcal{F}_s$, by Itô-isometry and $\int H \, dM$ being a square integrable martingale, it holds

    \[
    \begin{multline*}
    E\left[ 1_A \left( \left( \int_{0}^{t} H \, dM \right)^2 - \int_{0}^{t} H^2 \, d\langle M\rangle - \left( \int_{0}^{s} H \, dM \right)^2 + \int_{0}^{s} H^2 \, d\langle M\rangle \right) \right] \\
    = E\left[ 1_A \left( \int_{s}^{t} H \, dM \right)^2 \right] - E\left[ 1_A \int_{s}^{t} H^2 \, d\langle M\rangle \right] + E\left[ 1_A \left( \int_{0}^{s} H \, dM \right) \left( \int_{s}^{t} H \, dM \right) \right] \\
    = E\left[ 1_A E\left[ \left( \int_{s}^{t} H \, dM \right)^2 \big| \mathcal{F}_s \right] \right] - E\left[ 1_A \int_{s}^{t} H^2 \, d\langle M\rangle \right] + E\left[ 1_A \left( \int_{0}^{s} H \, dM \right) E\left[ \int_{s}^{t} H \, dM \big| \mathcal{F}_s \right] \right] \\
    = E\left[ 1_A \int_{s}^{t} H^2 \, d\langle M\rangle \right] - E\left[ 1_A \int_{s}^{t} H^2 \, d\langle M\rangle \right] = 0
    \end{multline*}
    \]

    finishing the proof.

We call this operator the **stochastic integral** of $H$ with respect to $M$.
For square integrable continuous martingales $M$ and $N$, the covariation of $M,N$ is given by the polar formula

\[
  \langle M, N\rangle = \frac{1}{4} \left( \langle M + N \rangle - \langle M - N \rangle \right)
\]

The following relation holds

!!! proposition
    Let $M, N \in \mathcal{M}_c^2$ and $G \in \mathcal{L}^2(M)$, $H \in \mathcal{L}^2(N)$.
    Then it holds

    \[
    \langle \int G \, dM, \int H \, dN \rangle = \int G \, d\langle M, \int H \, dN \rangle = \int GH \, d\langle M, N \rangle
    \]

    In particular, for $G \in \mathcal{L}^2(M)$ and $H \in \mathcal{L}^2\left( \int G \, dM \right)$, it holds that $GH \in \mathcal{L}^2(M)$ and the chain rule

    \[
    \int H \, d \int G \, dM = \int GH \, dM
    \]

This relation is straightforward for $G, H \in \mathcal{S}$.
The passage to the limit is left as an exercise by using the following proposition known as the Kunita-Watanabe inequality, a stochastic version of Hölder.


!!! proposition
    Let $M, N \in \mathcal{M}_{c}^2$ and $G \in \mathcal{L}^2(M)$, $H \in \mathcal{L}^2(N)$.
    Then it holds

    \[
      \begin{align*}
         \left\vert\int GH \, d\langle M,N\rangle \right\vert 
            & \leq \int \left\vert GH \right\vert \, d\left\vert \langle M,N \rangle \right\vert
            \\
            & \leq \left( \int \left\vert G \right\vert^2 \, d\langle M \rangle \right)^{1/2} \left( \int \left\vert H \right\vert^2 \, d\langle N \rangle \right)^{1/2}
      \end{align*}
    \]


!!! proof
    Recall that

    \[
    \langle M, N \rangle = \frac{1}{4}(\langle M + N \rangle - \langle M - N \rangle)
    \]

    and therefore

    \[
    |\langle M, N \rangle| = \frac{1}{4}(\langle M + N \rangle + \langle M - N \rangle).
    \]

    Furthermore, for two simple processes $G, H \in \mathcal{S}$, a painful but easy inspection shows that $GH \in \mathcal{S}$.
    Hence,

    \[
    \begin{align*}
      \left\vert \int GH \, d\langle M,N\rangle \right\vert 
        & = \left\vert \sum G_k H_k \Delta_k \langle M, N \rangle \right\vert
        \\
        & \leq \sum \left\vert G_k H_k \right\vert \left\vert \Delta_k \langle M, N \rangle \right\vert\\
        & = \int \left\vert GH \right\vert \, d|\langle M, N \rangle|
    \end{align*}
    \]

    showing, by passing to the limit on the simple processes, the first inequality.
    Furthermore, by the Cauchy-Schwarz inequality, it holds

    \[
    |\Delta_k \langle M, N \rangle| \leq (\Delta_k \langle M \rangle)^{1/2} (\Delta_k \langle N \rangle)^{1/2}.
    \]

    Hence, for simple integrands, using Hölder's inequality, it holds

    \[
    \begin{align*}
      \int \left\vert GH \right\vert \, d|\langle M,N \rangle|
        & = \sum \left\vert G_k H_k \right\vert \left\vert \Delta_k \langle M, N \rangle \right\vert
        \\
        & \leq \sum \left\vert G_k \right\vert \left\vert H_k \right\vert (\Delta_k \langle M \rangle )^{1/2} (\Delta_k \langle N \rangle )^{1/2}
        \\
        & \leq \left( \sum \left\vert H_k \right\vert^2 \Delta_k \langle M \rangle \right)^{1/2} \left( \sum \left\vert G_k \right\vert^2 \Delta_k \langle N \rangle \right)^{1/2}
        \\
        & = \left( \int \left\vert G \right\vert^2 \, d\langle M \rangle \right)^{1/2} \left( \int \left\vert H \right\vert^2 \, d\langle N \rangle \right)^{1/2}
    \end{align*}
    \]

    The case of general integrands follows by passing to the limit with simple integrands in this inequality.


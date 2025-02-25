#%%

from lib.standard_lib import *
from IPython.display import display, HTML


import plotly
plotly.offline.init_notebook_mode()
display(HTML(
    '<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_SVG"></script>'
))
import numpy as np
from scipy.stats import norm
#%%


# Generate data for the normal distribution
x = np.linspace(-4, 4, 500)
cdf = norm.cdf(x)

# Calculate 90% quantile
quantile_90 = norm.ppf(0.90)

# Create the figure
fig = go.Figure()

# Add the CDF line
fig.add_trace(go.Scatter(x=x, y=cdf, mode='lines', name='CDF', line=dict(color=plt_colors[0])))

# Add the vertical line at the origin

fig.add_shape(
    type="line",
    x0=-4,
    y0=0.9,
    x1=4,
    y1=0.9,
    line=dict(color=plt_colors[2], width=2, dash="dash"),
    )

fig.add_annotation(
    x= -3,
    y=0.95,
    text=r'$\text{Confidence Level }1-\alpha\\$',
    showarrow=False,
    font=dict(size=24, color=plt_colors[2])
)



fig.add_shape(type="line", x0=quantile_90, y0=0, x1=quantile_90, y1=0.9,
              line=dict(color=plt_colors[1], width=2, dash="dash"))

# Annotate the quantile with '$V@R_{\\alpha}$'
fig.add_annotation(
    x=quantile_90, 
    y=0, 
    text=r'$V@R_{\alpha}(L)$',
    showarrow=True,
    arrowhead=2,
    ax=80,
    ay=-50,
    font=dict(size=24, color=plt_colors[1]),  # Bigger text size and color
    arrowcolor=plt_colors[1],  # Arrow color
    arrowsize=2 
    )

fig.add_annotation(
    x=-1, 
    y=norm.cdf(-1), 
    text=r'$m \mapsto F_L(m) = P[L\leq m]$',
    showarrow=True,
    arrowhead=2,
    ax=-120,
    ay=-50,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    arrowcolor=plt_colors[0],  # Arrow color
    arrowsize=2 
    )


fig.add_trace(go.Scatter(x=x, y=cdf, mode='lines', name='CDF', line=dict(color=plt_colors[0])))


# Remove the grid and update layout
fig.update_layout(showlegend=False,
                  xaxis=dict(visible = False),
                  yaxis=dict(visible = False, range = [-0.1, 1.1]),
                  margin=dict(l=20, r=20, t=20, b=20))

fig.add_hline(y=0, line_color='black', line_width=2)
fig.add_hline(y=1, line_color='black', line_width=2)
fig.add_vline(x=0, line_color='black', line_width=1)
fig.update_layout(template = "plotly_white+draft")

fig.show()

#%%
# Show the plot

fig_white = fig
fig_black = fig
fig_white.add_hline(y=0, line_color='black', line_width=2)
fig_white.add_hline(y=1, line_color='black', line_width=2)
fig_white.add_vline(x=0, line_color='black', line_width=1)
fig_white.update_layout(template = "plotly_white+draft")
fig_white.write_image("./../docs/images/var_white.svg")
fig_black.add_hline(y=0, line_color='grey', line_width=2)
fig_black.add_hline(y=1, line_color='grey', line_width=2)
fig_black.add_vline(x=0, line_color='grey', line_width=1)
fig_black.update_layout(template = "plotly_dark+draft")
fig_black.write_image("./../docs/images/var_dark.svg")


#%%

# Generate data for the normal distribution
x = np.linspace(-4, 10, 500)
cdf = norm.cdf(x)

mask = x>q

# Calculate 90% quantile
q = norm.ppf(0.90)

c = 0.4

epsilon = np.where(x<q, 0, ((x + q)/10)**c)

modify_cdf = epsilon* (0.1*norm.cdf(x - 7) + 0.9) + (1-epsilon) * norm.cdf(x)

# Create the figure
fig = go.Figure()

# Add the CDF line
fig.add_trace(go.Scatter(x=x, y=cdf, mode='lines', name='CDF', line=dict(color=plt_colors[0])))
fig.add_trace(go.Scatter(x=x+0.05, y=modify_cdf, mode='lines', name='CDF', line=dict(color=plt_colors[3])))

# Add the vertical line at the origin

fig.add_shape(
    type="line",
    x0=-4,
    y0=0.9,
    x1=10,
    y1=0.9,
    line=dict(color=plt_colors[2], width=2, dash="dash"),
    )

fig.add_annotation(
    x= -3,
    y=0.95,
    text=r'$\text{Confidence Level }1-\alpha\\$',
    showarrow=False,
    font=dict(size=24, color=plt_colors[2])
)



fig.add_shape(type="line", x0=q, y0=0, x1=q, y1=0.9,
              line=dict(color=plt_colors[1], width=2, dash="dash"))

# Annotate the quantile with '$V@R_{\\alpha}$'
fig.add_annotation(
    x=q, 
    y=0, 
    text=r'$V@R_{\alpha}(L) = V@R_{\alpha}(\tilde{L})$',
    showarrow=True,
    arrowhead=2,
    ax=100,
    ay=-50,
    font=dict(size=24, color=plt_colors[1]),  # Bigger text size and color
    arrowcolor=plt_colors[1],  # Arrow color
    arrowsize=2 
    )

fig.add_annotation(
    x=q+0.25, 
    y=0.97, 
    text=r'$ES_{\alpha}(L)$',
    showarrow=True,
    arrowhead=2,
    ax=60,
    ay=80,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    arrowcolor=plt_colors[0],  # Arrow color
    arrowsize=2 
    )


fig.add_annotation(
    x=q+4, 
    y=0.97, 
    text=r'$ES_{\alpha}(\tilde{L})> ES_{\alpha}(L)$',
    showarrow=True,
    arrowhead=2,
    ax=60,
    ay=80,
    font=dict(size=24, color=plt_colors[3]),  # Bigger text size and color
    arrowcolor=plt_colors[3],  # Arrow color
    arrowsize=2 
    )




fig.add_annotation(
    x=-1, 
    y=norm.cdf(-1), 
    text=r'$m \mapsto F_L(m) = P[L\leq m]$',
    showarrow=True,
    arrowhead=2,
    ax=-120,
    ay=-50,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    arrowcolor=plt_colors[0],  # Arrow color
    arrowsize=2 
    )

fig.add_annotation(
    x=0.5, 
    y=norm.cdf(0.5), 
    text=r'$m \mapsto F_{\tilde{L}}(m) = P[\tilde{L}\leq m]$',
    showarrow=True,
    arrowhead=2,
    ax=-200,
    ay=-40,
    font=dict(size=24, color=plt_colors[3]),  # Bigger text size and color
    arrowcolor=plt_colors[3],  # Arrow color
    arrowsize=2 
    )






fig.add_trace(go.Scatter(x=x, y=cdf, mode='lines', name='CDF', line=dict(color=plt_colors[0])))

fig.add_trace(go.Scatter(
    x=np.concatenate((x[mask], x[mask][::-1])),  # X values forward and backward
    y=np.concatenate((cdf[mask], [1] * len(cdf[mask]))),  # f(X) and 1
    fill='toself',
    fillcolor='rgba(51,102,204,0.3)',
    line=dict(color='rgba(255,255,255,0)'),
    name='Region between f(X) and y=1'
))

fig.add_trace(go.Scatter(
    x=np.concatenate((x[mask], x[mask][::-1])),  # X values forward and backward
    y=np.concatenate((modify_cdf[mask], [1] * len(modify_cdf[mask]))),  # f(X) and 1
    fill='toself',
    fillcolor='rgba(16,150,24,0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    name='Region between f(X) and y=1'
))

# Remove the grid and update layout
fig.update_layout(showlegend=False,
                  xaxis=dict(visible = False),
                  yaxis=dict(visible = False, range = [-0.1, 1.1]),
                  margin=dict(l=20, r=20, t=20, b=20))


#%%
fig_white = fig
fig_black = fig
fig_white.add_hline(y=0, line_color='black', line_width=2)
fig_white.add_hline(y=1, line_color='black', line_width=2)
fig_white.add_vline(x=0, line_color='black', line_width=1)
fig_white.update_layout(template = "plotly_white+draft")
fig_white.write_image("./../docs/images/ES_white.svg")
fig_black.add_hline(y=0, line_color='grey', line_width=2)
fig_black.add_hline(y=1, line_color='grey', line_width=2)
fig_black.add_vline(x=0, line_color='grey', line_width=1)
fig_black.update_layout(template = "plotly_dark+draft")
fig_black.write_image("./../docs/images/ES_dark.svg")



#%% Optimized certaintyequivalent


# Generate data for the normal distribution
x = np.linspace(-4, 4, 500)

y0 = x
y1 = 2 * np.maximum(x,0)+0.01
y2 = np.maximum(x,0) + np.maximum(x, 0) ** 2 /2 - 0.01
y3 = np.exp(x) -1

# Create the figure
fig = go.Figure()

# Add the identity line

fig.add_trace(
    go.Scatter(
        x=x,
        y=x,
        mode='lines',
        name='Identity',
        showlegend=False, 
        line=dict(color='grey', dash = 'dash')
    )
)

fig.add_trace(
    go.Scatter(
        x=x,
        y=y1,
        mode='lines',
        name='Piecewise Linear',
        showlegend=True, 
        line=dict(color=plt_colors[0], width=2),
        line_width=4
    )
)
fig.add_trace(
    go.Scatter(
        x=x,
        y=y2,
        mode='lines',
        name='Right quadratic',
        showlegend=True, 
        line=dict(color=plt_colors[2], width=2),
        line_width=4
    )
)
fig.add_trace(
    go.Scatter(
        x=x,
        y=y3,
        mode='lines',
        name='Exponential',
        showlegend=True, 
        line=dict(color=plt_colors[3]),
        line_width=4
    )
)

fig.update_layout(
    xaxis=dict(visible=False, range = [-2, 3]),
    yaxis=dict(visible=False, range = [-2,6]),
    margin=dict(l=0, r=0, t=0, b=0),
    width=600,
    height=600
)


fig.show()

#%%
# Show the plot

fig_white = fig
fig_black = fig

fig_white.add_hline(y=0, line_color='black', line_width=1)
fig_white.add_vline(x=0, line_color='black', line_width=1)
fig_white.update_layout(template = "plotly_white+draft")
fig_white.write_image("./../docs/images/loss_white.svg")
fig_black.add_hline(y=0, line_color='grey', line_width=1)
fig_black.add_vline(x=0, line_color='grey', line_width=1)
fig_black.update_layout(template = "plotly_dark+draft")
fig_black.write_image("./../docs/images/loss_dark.svg")


#%% Optimized certaintyequivalent


# Generate data for the normal distribution
x = np.linspace(-10, 10, 500)

y0 = x
y3 = x + np.exp(-x-1) -1

x0 = -1
y0 = -1 + np.exp(-x0-1) -1


# Create the figure
fig = go.Figure()

# Add the identity line


fig.add_trace(
    go.Scatter(
        x=x,
        y=y3,
        mode='lines',
        showlegend=False, 
        line=dict(color=plt_colors[0], width=2),
        line_width=4
    )
)

fig.add_annotation(
    x=x0, 
    y=y0, 
    text=r'$m^\ast = \mathrm{argmin} \{g(m) \}$',
    showarrow=True,
    arrowhead=2,
    ax=150,
    ay=0,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    arrowcolor=plt_colors[0],  # Arrow color
    arrowsize=2 
    )

fig.add_annotation(
    x=1, 
    y=1+np.exp(-2) -1, 
    text=r'$m \mapsto g(m)$',
    showarrow=True,
    arrowhead=2,
    ax=-150,
    ay=-50,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    arrowcolor=plt_colors[0],  # Arrow color
    arrowsize=2 
    )



fig.update_layout(
    xaxis=dict(visible = False, range = [-3, 3]),
    yaxis=dict(visible = False, range = [-2,3]),
    margin=dict(l=0, r=0, t=0, b=0),
    width=400,
    height=400
)


fig.show()

#%%
# Show the plot

fig_white = fig
fig_black = fig

fig_white.add_hline(y=0, line_color='black', line_width=1)
fig_white.add_vline(x=0, line_color='black', line_width=1)
fig_white.update_layout(template = "plotly_white+draft")
fig_white.write_image("./../docs/images/ocefun_white.svg")
fig_black.add_hline(y=0, line_color='grey', line_width=1)
fig_black.add_vline(x=0, line_color='grey', line_width=1)
fig_black.update_layout(template = "plotly_dark+draft")
fig_black.write_image("./../docs/images/ocefun_dark.svg")


#%%

from scipy.stats import norm

N = 10000
u = np.random.rand(N)
x0 = norm.ppf(u)
x1 = norm.rvs(size=N)

fig = go.Figure()
fig.add_histogram(
    x=x0,
    histnorm='probability',
    name='Quantile of Uniform Sample',
    marker=dict(color=plt_colors[0])
    )
fig.add_histogram(
    x=x1,
    histnorm='probability',
    name='Standard Normal Sample',
    marker=dict(color=plt_colors[1])
    )

fig.show()
#%%

from lib.standard_lib import *
from IPython.display import display, HTML


import plotly
plotly.offline.init_notebook_mode()
display(HTML(
    '<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_SVG"></script>'
))

#%%

X = np.linspace(0, 10, 200)
FORWARD = X-5
CALL = np.maximum(0, X - 5)
PUT = np.maximum(0, 5 - X)
STRADDLE = CALL + PUT
# butterfly option where K1 = 3, K2 = 5 and K3 = 7
BUTTERFLY = np.maximum(0, X - 3) - 2*np.maximum(0, X - 5) + np.maximum(0, X - 7)


#%%

# Forward

fig = go.Figure()
fig.add_scatter(x = X, y = FORWARD, name="Forward")

# Add vertical line at K=5
fig.add_shape(
    type="line",
    x0=5, x1=5,
    y0=0, y1=max(CALL),  # Line from y=0 to the max CALL value
    line=dict(color=plt_colors[3], dash="dash"),
)

# Add annotation at the top-right of the vertical line
fig.add_annotation(
    x=5, y=max(CALL),  # Position annotation at the top of the vertical line
    text=r'Strike $K=5$',  # Annotation text
    showarrow=False,
    font=dict(size=24),
    xanchor="right",  # Position text to the right of the line
    yanchor="bottom"  # Position text above the line
)

fig.show()
fig.update_layout(template = "plotly_white+draft")
fig.write_image("./../docs/images/forward_payoff_white.svg")
fig.update_layout(template = "plotly_dark+draft")
fig.write_image("./../docs/images/forward_payoff_dark.svg")




#%%
# Payoff of Call/Put Option
fig = go.Figure()
fig.add_scatter(x = X, y = CALL, name="Call")
fig.add_scatter(x = X, y = PUT, name="Put")

# Add vertical line at K=5
fig.add_shape(
    type="line",
    x0=5, x1=5,
    y0=0, y1=max(CALL),  # Line from y=0 to the max CALL value
    line=dict(color=plt_colors[3], dash="dash"),
)

# Add annotation at the top-right of the vertical line
fig.add_annotation(
    x=5, y=max(CALL),  # Position annotation at the top of the vertical line
    text=r'Strike $K=5$',  # Annotation text
    showarrow=False,
    font=dict(size=24),
    xanchor="right",  # Position text to the right of the line
    yanchor="bottom"  # Position text above the line
)

fig.show()
fig.update_layout(template = "plotly_white+draft")
fig.write_image("./../docs/images/call_put_payoff_white.svg")
fig.update_layout(template = "plotly_dark+draft")
fig.write_image("./../docs/images/call_put_payoff_dark.svg")


#%%

# Straddle

fig = go.Figure()
fig.add_scatter(x = X, y = STRADDLE, name="Straddle")

# Add vertical line at K=5
fig.add_shape(
    type="line",
    x0=5, x1=5,
    y0=0, y1=max(CALL),  # Line from y=0 to the max CALL value
    line=dict(color=plt_colors[3], dash="dash"),
)

# Add annotation at the top-right of the vertical line
fig.add_annotation(
    x=5, y=max(CALL),  # Position annotation at the top of the vertical line
    text=r'Strike $K=5$',  # Annotation text
    showarrow=False,
    font=dict(size=24),
    xanchor="right",  # Position text to the right of the line
    yanchor="bottom"  # Position text above the line
)

fig.show()
fig.update_layout(template = "plotly_white+draft")
fig.write_image("./../docs/images/straddle_payoff_white.svg")
fig.update_layout(template = "plotly_dark+draft")
fig.write_image("./../docs/images/straddle_payoff_dark.svg")


#%%

# Butterfly

fig = go.Figure()
fig.add_scatter(x = X, y = BUTTERFLY, name="Butterfly")

# Add vertical line at K=5


# Add annotation at the top-right of the vertical line

fig.add_shape(
    type="line",
    x0=3, x1=3,
    y0=0, y1=max(BUTTERFLY),  # Line from y=0 to the max CALL value
    line=dict(color=plt_colors[2], dash="dash"),
)

fig.add_shape(
    type="line",
    x0=7, x1=7,
    y0=0, y1=max(BUTTERFLY),  # Line from y=0 to the max CALL value
    line=dict(color=plt_colors[2], dash="dash"),
)

fig.add_shape(
    type="line",
    x0=5, x1=5,
    y0=0, y1=max(BUTTERFLY),  # Line from y=0 to the max CALL value
    line=dict(color=plt_colors[3], dash="dash"),
)

# Add annotation at the top-right of the vertical line

fig.add_annotation(
    x=3, y=max(BUTTERFLY),  # Position annotation at the top of the vertical line
    text=r'$\underline{K} = 3$',  # Annotation text
    showarrow=False,
    font=dict(size=24),
    xanchor="right",  # Position text to the right of the line
    yanchor="bottom"  # Position text above the line
)

fig.add_annotation(
    x=7, y=max(BUTTERFLY),  # Position annotation at the top of the vertical line
    text=r'$\overline{K}=7$',  # Annotation text
    showarrow=False,
    font=dict(size=24),
    xanchor="right",  # Position text to the right of the line
    yanchor="bottom"  # Position text above the line
)


fig.add_annotation(
    x=5, y=max(BUTTERFLY),  # Position annotation at the top of the vertical line
    text="$K=5$",  # Annotation text
    showarrow=False,
    font=dict(size=24),
    xanchor="right",  # Position text to the right of the line
    yanchor="bottom"  # Position text above the line
)

fig.show()
fig.update_layout(template = "plotly_white+draft")
fig.write_image("./../docs/images/butterfly_payoff_white.svg")
fig.update_layout(template = "plotly_dark+draft")
fig.write_image("./../docs/images/butterfly_payoff_dark.svg")

#%% super subhedging

import plotly.graph_objects as go

# Create the figure
fig = go.Figure()

# Add the horizontal black line
fig.add_trace(go.Scatter(
    x=[0, 12],
    y=[0, 0],
    mode="lines",
    line=dict(color="black", width=2),
    showlegend=False
))

# Add the shaded green area (left side)
fig.add_vrect(
    x0 = 0,
    x1 = 4,
    line_width = 0,
    fillcolor = plt_colors[1],
    opacity = 0.2
)
fig.add_vline(x=4, line_dash="dot", line_color=plt_colors[1],
              annotation_text='Sub-hedging prices', 
              annotation_position="top left",
              annotation_font_color=plt_colors[1],
              )
fig.add_vrect(
    x0 = 4,
    x1 = 8,
    line_width = 0,
    fillcolor = plt_colors[0],
    opacity = 0.2
)
fig.add_vline(x=8, line_dash="dot", line_color=plt_colors[3],
              annotation_text='Super-hedging prices', 
              annotation_position="top right",
              annotation_font_color=plt_colors[3],
              )

fig.add_vrect(
    x0 = 8,
    x1 = 12,
    line_width = 0,
    fillcolor = plt_colors[3],
    opacity = 0.2
)



fig.add_annotation(
    x=1.8, y=2.5,
    text='Risk free bids',
    showarrow=False,
    font=dict(size=24, color=plt_colors[1])
)

fig.add_annotation(
    x=1.8, y=1,
    text=r'$\{y \colon y + \boldsymbol{\nu}\cdot \Delta \boldsymbol{X}_1 \leq \frac{C}{1+r} \text{ for some }\boldsymbol{\nu}\}$',
    showarrow=False,
    font=dict(size=48, color=plt_colors[1])
)

fig.add_annotation(
    x=9.8, y=2.5,
    text='Risk free asks',
    showarrow=False,
    font=dict(size=24, color=plt_colors[3])
)

fig.add_annotation(
    x=9.8, y=1,
    text=r'$\{x \colon x + \boldsymbol{\eta}\cdot \Delta \boldsymbol{X}_1 \geq \frac{C}{1+r} \text{ for some }\boldsymbol{\eta}\}$',
    showarrow=False,
    font=dict(size=48, color=plt_colors[3])
)


fig.add_annotation(
    x=5.8, y=2.5,
    text='Fair Prices',
    showarrow=False,
    font=dict(size=24, color=plt_colors[0])
)

fig.add_annotation(
    x=5.8, y=1,
    text=r'$\left\{E^{P^\ast}\left[\frac{C}{1+r}\right]\colon P^\ast \sim P \text{ pricing measure}\right\}$',
    showarrow=False,
    font=dict(size=48, color=plt_colors[0])
)

fig.add_annotation(
    x=4,
    y=-0.25,
    text=r'$\underline{\pi}(C)$',
    showarrow=False,
    font=dict(size=14, color = plt_colors[1]),
    xanchor="center",
    yanchor="top"
)

fig.add_annotation(
    x=8,
    y=-0.25,
    text=r'$\overline{\pi}(C)$',
    showarrow=False,
    font=dict(size=14, color = plt_colors[3]),
    xanchor="center",
    yanchor="top"
)


fig.update_layout(
    xaxis=dict(visible=False),
    yaxis=dict(visible=False, range = [-1,4]),
    margin=dict(l=0, r=0, t=0, b=0),
    width=1000,
    height=200
)
# Show the figure
fig.show()

fig.update_layout(template = "plotly_white+draft")
fig.write_image("./../docs/images/superhedging_white.svg")
fig.update_layout(template = "plotly_dark+draft")
fig.write_image("./../docs/images/superhedging_dark.svg")

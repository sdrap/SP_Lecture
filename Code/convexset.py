#%%

from lib.standard_lib import *
from IPython.display import display, HTML


import plotly
plotly.offline.init_notebook_mode()
display(HTML(
    '<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_SVG"></script>'
))



#%%

import numpy as np

# Define the convex set as the epigraph of e^(-x) - 1/2
x = np.linspace(-2, 2, 500)
y = np.exp(-x) -0.9

# Generate a filled region for the epigraph
x_fill = np.concatenate([x, x[::-1]])
y_fill = np.concatenate([y, np.full_like(x, 2)])  # Fill up to y = 2

# Define a tangent line
tangent_x = np.linspace(-2, 2, 500)
tangent_y = -tangent_x +0.1  # Tangent line equation: y = -x + 0.2

# Define the normal vector
normal_x = [0.05, 0.5]
normal_y = [0.05, 0.5]

# Create the figure
fig = go.Figure()

# Plot the convex set as a filled region
fig.add_trace(go.Scatter(
    x=x_fill, y=y_fill,
    fill='toself',
    mode='none',
    name='Convex Set C',
    fillcolor='rgba(51, 102, 204, 0.5)'
))

# Plot the boundary of the convex set
fig.add_trace(go.Scatter(
    x=x, y=y,
    mode='lines',
    name='Boundary of C',
    line=dict(color=plt_colors[0])
))

# Plot the tangent line
fig.add_trace(go.Scatter(
    x=tangent_x, y=tangent_y,
    mode='lines',
    name='Tangent Line',
    line=dict(dash='dash', color=plt_colors[1])
))


# Add a marker at the origin
fig.add_trace(go.Scatter(
    x=[0], y=[0],
    mode='markers',
    name='Origin (0)',
    marker=dict(size=10, color='black', symbol='circle')
))

# Add the normal vector
# Add the normal vector as an arrow


fig.add_annotation(
    x=normal_x[1], y=normal_y[1],
    ax=normal_x[0], ay=normal_y[0],
    axref='x', ayref='y',
    text="",
    showarrow=True,
    arrowhead=3,
    arrowsize=2,
    arrowwidth=2,
    arrowcolor=plt_colors[3]
)

# Add annotations
fig.add_annotation(
    x=1.2, y=1.2,
    text=r'$\Large{\text{Convex Set}\quad \mathcal{C}}$',
    showarrow=False,
    font=dict(size=48, color=plt_colors[0])
)

fig.add_annotation(
    x=0.6, y=0.6,
    text=r'$\Large{\text{Normal Vector }\boldsymbol{\eta}}$',
    showarrow=False,
    arrowhead=2,
    ax=20, ay=-30,
    font=dict(size=24, color=plt_colors[3])
)
fig.add_annotation(
    x=1.4, y=-0.8,
    text="Separation",
    showarrow=False,
    font=dict(size=24, color=plt_colors[1])
)

# Update layout for better visualization
fig.update_layout(
    showlegend=False,
    xaxis=dict(
        range=[-1, 2],
        zeroline=True,  # Show only 0 line
        zerolinecolor="black",
        showgrid=False,
        tickvals=[0],  # Only show tick at 0
        ticks="outside"
    ),
    yaxis=dict(
        range=[-1, 2],
        zeroline=True,  # Show only 0 line
        zerolinecolor="black",
        showgrid=False,
        tickvals=[0],  # Only show tick at 0
        ticks="outside"
    ),
    width=600,
    height=600
)

# Show the figure
fig.show()

fig.update_layout(template = "plotly_white+draft")
fig.write_image("./../docs/images/separation_white.svg")
fig.update_layout(template = "plotly_dark+draft")
fig.write_image("./../docs/images/separation_dark.svg")

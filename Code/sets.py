#%%

from lib.standard_lib import *
from IPython.display import display, HTML


import plotly
plotly.offline.init_notebook_mode()
display(HTML(
    '<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_SVG"></script>'
))

#%%

fig = go.Figure()
fig.add_shape(
    type="circle",
    xref="x", yref="y",
    x0=-1, y0=-1, x1=1, y1=1,
    line_color=plt_colors[0],
    fillcolor=plt_colors[0],
    opacity=0.3
)

# Circle for set B
fig.add_shape(
    type="circle",
    xref="x", yref="y",
    x0=0, y0=-1, x1=2, y1=1,
    line_color=plt_colors[1],
    fillcolor=plt_colors[1],
    opacity=0.3
)

# Annotations for the sets
fig.add_annotation(
    x=-0.5, y=0.1, text=r"$A$", showarrow=False, font=dict(size = 48, color = plt_colors[0])
)
fig.add_annotation(
    x=1.5, y=0.1, text=r"$B$", showarrow=False, font=dict(size = 48, color=plt_colors[1])
)

fig.add_annotation(
    x=0.5, y=0.1, text=r"$A\cap B$", showarrow=False, font=dict(size = 48)
)

fig.update_layout(
    xaxis=dict(range=[-2, 3], showgrid=False, zeroline=False, visible=False),
    yaxis=dict(range=[-2, 2], showgrid=False, zeroline=False, visible=False),
    width=500, height=500
)

fig.show()

#%%

import plotly.graph_objects as go

plt_colors = ['blue', 'red']

fig = go.Figure()
# Circle for set A
fig.add_shape(
    type="circle",
    xref="x", yref="y",
    x0=-1, y0=-1, x1=1, y1=1,
    line_color=plt_colors[0],
    fillcolor=plt_colors[0],
    opacity=0.3
)
# Circle for set B
fig.add_shape(
    type="circle",
    xref="x", yref="y",
    x0=0, y0=-1, x1=2, y1=1,
    line_color=plt_colors[1],
    fillcolor=plt_colors[1],
    opacity=0.3
)

# Annotations for the sets
fig.add_annotation(
    x=-0.5, y=0.1, text=r"$A$", showarrow=False, font=dict(size=48, color=plt_colors[0])
)
fig.add_annotation(
    x=1.5, y=0.1, text=r"$B$", showarrow=False, font=dict(size=48, color=plt_colors[1])
)
fig.add_annotation(
    x=0.5, y=1.3, text=r"$A\cup B$", showarrow=False, font=dict(size=48)
)

fig.update_layout(
    xaxis=dict(range=[-2, 3], showgrid=False, zeroline=False, visible=False),
    yaxis=dict(range=[-2, 2], showgrid=False, zeroline=False, visible=False),
    width=500, height=500
)

fig.show()

#%%


def circle_arc(center, radius, start_deg, end_deg, num=50):
    angles = np.linspace(np.deg2rad(start_deg), np.deg2rad(end_deg), num)
    return center[0] + radius * np.cos(angles), center[1] + radius * np.sin(angles)

# Define circle parameters:
# Circle A: center (0,0), radius 1  (drawn from x0=-1,y0=-1 to x1=1,y1=1)
# Circle B: center (1,0), radius 1  (drawn from x0=0,y0=-1 to x1=2,y1=1)

# Intersection points for these circles are (0.5, 0.8660) and (0.5, -0.8660).

# Compute arc for circle A from 60° down to -60°.
xA, yA = circle_arc(center=(0,0), radius=1, start_deg=60, end_deg=-60, num=50)
# Compute arc for circle B from -120° up to 120°.
xB, yB = circle_arc(center=(1,0), radius=1, start_deg=-120, end_deg=120, num=50)

# Combine the arcs to form a closed polygon.
x_int = np.concatenate([xA, xB])
y_int = np.concatenate([yA, yB])

fig = go.Figure()

# Outlines for circles (no fill)
fig.add_shape(
    type="circle",
    xref="x", yref="y",
    x0=-1, y0=-1, x1=1, y1=1,
    line_color=plt_colors[0],
    fillcolor="rgba(0,0,0,0)"
)
fig.add_shape(
    type="circle",
    xref="x", yref="y",
    x0=0, y0=-1, x1=2, y1=1,
    line_color=plt_colors[1],
    fillcolor="rgba(0,0,0,0)"
)

# Filled intersection region (using a scatter polygon)
fig.add_trace(go.Scatter(
    x=x_int, y=y_int,
    fill="toself",
    fillcolor="rgba(128,0,128,0.3)",  # purple with opacity
    line=dict(color="rgba(0,0,0,0)"),
    mode="lines",
    showlegend=False
))

# Annotations for sets and result
fig.add_annotation(
    x=-0.5, y=0.1, text=r"$A$", showarrow=False,
    font=dict(size=48, color=plt_colors[0])
)
fig.add_annotation(
    x=1.5, y=0.1, text=r"$B$", showarrow=False,
    font=dict(size=48, color=plt_colors[1])
)
fig.add_annotation(
    x=0.5, y=0.1, text=r"$A\cap B$", showarrow=False,
    font=dict(size=48)
)

fig.update_layout(
    xaxis=dict(range=[-2, 3], showgrid=False, zeroline=False, visible=False),
    yaxis=dict(range=[-2, 2], showgrid=False, zeroline=False, visible=False),
    width=500, height=500
)

fig.show()


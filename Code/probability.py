#%%

from lib.standard_lib import *
from IPython.display import display, HTML


import plotly
plotly.offline.init_notebook_mode()
display(HTML(
    '<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_SVG"></script>'
))
#%%

A = np.linspace(1, 3, 100)


# Create the figure
fig = go.Figure()

# Add the CDF line
fig.add_trace(
    go.Scatter(
        x=A, 
        y=np.ones(len(A)), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[0], width=2),
        fill='tozeroy',
        fillcolor='rgba(51,102,204,0.05)',
        )
    )


fig.add_annotation(
    x=4.6, 
    y=-.1, 
    text=r'$\Omega$',
    showarrow=False,
    font=dict(size=24, color="black"),  # Bigger text size and color
    )

fig.add_annotation(
    x=2, 
    y=-.1, 
    text=r'$A$',
    showarrow=False,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    )



# Remove the grid and update layout
fig.update_layout(
    showlegend=False,
    xaxis=dict(
        linewidth = 2,
        showline = False,
        zeroline = True,
        showgrid = False,
        showticklabels = False,
        range = [-1, 5]
        ),
    yaxis=dict(
        linewidth = 2,
        showline = False,
        zeroline = True,
        showgrid = False,
        tickmode = 'linear',
        dtick = 1,
        showticklabels = True,
        range = [-1, 1.5]
    )
)

fig.update_layout(template = "plotly_white+draft")

fig.show()

#%%
# Show the plot

fig_white = fig
fig_black = fig
fig_white.update_layout(template = "plotly_white+draft")
fig_white.write_image("./../docs/images/indicator_white.svg")
fig_black.update_layout(template = "plotly_dark+draft")
fig_black.write_image("./../docs/images/indicator_dark.svg")




#%%


#%%

A0 = np.linspace(-.5, 0.2, 100)
A1 = np.linspace(0.5, 2, 100)
A3 = np.linspace(2.01, 3, 100)
A4 = np.linspace(3.5, 4.5)



# Create the figure
fig = go.Figure()


fig.add_trace(
    go.Scatter(
        x=A0, 
        y=2*np.ones(len(A0)), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[0], width=2),
        fill='tozeroy',
        fillcolor='rgba(51,102,204,0.1)',
        )
    )

fig.add_trace(
    go.Scatter(
        x=A1, 
        y=np.ones(len(A1)), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[0], width=2),
        fill='tozeroy',
        fillcolor='rgba(51,102,204,0.1)',
        )
    )

fig.add_trace(
    go.Scatter(
        x=A3, 
        y=4*np.ones(len(A4)), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[0], width=2),
        fill='tozeroy',
        fillcolor='rgba(51,102,204,0.1)',
        )
    )


fig.add_trace(
    go.Scatter(
        x=A4, 
        y=1.5*np.ones(len(A4)), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[0], width=2),
        fill='tozeroy',
        fillcolor='rgba(51,102,204,0.1)',
        )
    )



fig.add_annotation(
    x=4.7, 
    y=-.1, 
    text=r'$\Omega$',
    showarrow=False,
    font=dict(size=24, color="black"),  # Bigger text size and color
    )

fig.add_annotation(
    x=-.15, 
    y=-.1, 
    text=r'$A1$',
    showarrow=False,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    )

fig.add_annotation(
    x=1.25, 
    y=-.1, 
    text=r'$A2$',
    showarrow=False,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    )

fig.add_annotation(
    x=2.25, 
    y=-.1, 
    text=r'$A3$',
    showarrow=False,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    )

fig.add_annotation(
    x=4, 
    y=-.1, 
    text=r'$A4$',
    showarrow=False,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    )





# Remove the grid and update layout
fig.update_layout(
    showlegend=False,
    xaxis=dict(
        linewidth = 2,
        showline = False,
        zeroline = True,
        showgrid = False,
        showticklabels = False,
        range = [-1, 5]
        ),
    yaxis=dict(
        linewidth = 2,
        showline = False,
        zeroline = True,
        showgrid = True,
        tickmode = 'array',
        tickvals = [2, 1, 4, 1.5],
        ticktext = [r'$\alpha_1$',r'$\alpha_2$', r'$\alpha_3$', r'$\alpha_4$' ],        
        range = [-1, 5]
    )
)

fig.update_layout(template = "plotly_white+draft")

fig.show()

#%%
# Show the plot

fig_white = fig
fig_black = fig
fig_white.update_layout(template = "plotly_white+draft")
fig_white.write_image("./../docs/images/simple_rv_white.svg")
fig_black.update_layout(template = "plotly_dark+draft")
fig_black.write_image("./../docs/images/simple_rv_dark.svg")



#%%

A0 = np.linspace(-.5, 0.2, 100)
A1 = np.linspace(0.5, 2, 100)
A3 = np.linspace(2, 3, 100)
A4 = np.linspace(3.5, 4.5)



# Create the figure
fig = go.Figure()


fig.add_trace(
    go.Scatter(
        x=A0, 
        y=2*np.ones(len(A0)), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[0], width=2),
        fill='tozeroy',
        fillcolor='rgba(51,102,204,1)',
        )
    )

fig.add_trace(
    go.Scatter(
        x=A1, 
        y=np.ones(len(A1)), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[0], width=2),
        fill='tozeroy',
        fillcolor='rgba(51,102,204,1)',
        )
    )

fig.add_trace(
    go.Scatter(
        x=A3, 
        y=4*np.ones(len(A4)), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[0], width=2),
        fill='tozeroy',
        fillcolor='rgba(51,102,204,1)',
        )
    )


fig.add_trace(
    go.Scatter(
        x=A4, 
        y=1.5*np.ones(len(A4)), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[0], width=2),
        fill='tozeroy',
        fillcolor='rgba(51,102,204,1)',
        )
    )



fig.add_annotation(
    x=4.7, 
    y=-.1, 
    text=r'$\Omega$',
    showarrow=False,
    font=dict(size=24, color="black"),  # Bigger text size and color
    )

fig.add_annotation(
    x=-.15, 
    y=-.1, 
    text=r'$A1$',
    showarrow=False,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    )

fig.add_annotation(
    x=1.25, 
    y=-.1, 
    text=r'$A2$',
    showarrow=False,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    )

fig.add_annotation(
    x=2.25, 
    y=-.1, 
    text=r'$A3$',
    showarrow=False,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    )

fig.add_annotation(
    x=4, 
    y=-.1, 
    text=r'$A4$',
    showarrow=False,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    )





# Remove the grid and update layout
fig.update_layout(
    showlegend=False,
    xaxis=dict(
        linewidth = 2,
        showline = False,
        zeroline = True,
        showgrid = False,
        showticklabels = False,
        range = [-1, 5]
        ),
    yaxis=dict(
        linewidth = 2,
        showline = False,
        zeroline = True,
        showgrid = True,
        tickmode = 'array',
        tickvals = [2, 1, 4, 1.5],
        ticktext = [r'$\alpha_1$',r'$\alpha_2$', r'$\alpha_3$', r'$\alpha_4$' ],        
        range = [-1, 5]
    )
)

fig.update_layout(template = "plotly_white+draft")

fig.show()

#%%
# Show the plot

fig_white = fig
fig_black = fig
fig_white.update_layout(template = "plotly_white+draft")
fig_white.write_image("./../docs/images/expectation_white.svg")
fig_black.update_layout(template = "plotly_dark+draft")
fig_black.write_image("./../docs/images/expectation_dark.svg")

#%%

#%%

X = np.linspace(0, 5, 100)
def fun(x):
    return 2 * np.sin(x) + x + 1

Y = fun(X)

# Create the figure
fig = go.Figure()

fig.add_scatter(
    x=X,
    y=Y,
    mode='lines',
    line=dict(color=plt_colors[0], width=2),
)

fig.add_trace(
    go.Scatter(
        x=np.linspace(0, 0.34, 100), 
        y=np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )

fig.add_trace(
    go.Scatter(
        x=np.linspace(0.34,0.7, 100), 
        y=2*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )

fig.add_trace(
    go.Scatter(
        x=np.linspace(0.7,1.16, 100), 
        y=3*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )
fig.add_trace(
    go.Scatter(
        x=np.linspace(3.30,5, 100), 
        y=3*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )



fig.add_trace(
    go.Scatter(
        x=np.linspace(1.16, 3.30, 100), 
        y=4*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )



# Remove the grid and update layout
fig.update_layout(
    showlegend=False,
    xaxis=dict(
        linewidth = 2,
        showline = False,
        zeroline = True,
        showgrid = False,
        showticklabels = False,
        range = [0, 5]
        ),
    yaxis=dict(
        linewidth = 2,
        showline = False,
        zeroline = True,
        showgrid = True,
        #tickmode = 'array',
        #tickvals = [2, 1, 4, 1.5],
        #ticktext = [r'$\alpha_1$',r'$\alpha_2$', r'$\alpha_3$', r'$\alpha_4$' ],        
        range = [0, 5]
    )
)

fig.update_layout(template = "plotly_white+draft")

fig.show()

#%%
fig_white = fig
fig_black = fig
fig_white.update_layout(template = "plotly_white+draft")
fig_white.write_image("./../docs/images/expectation1_white.svg")
fig_black.update_layout(template = "plotly_dark+draft")
fig_black.write_image("./../docs/images/expectation1_dark.svg")


#%%

X = np.linspace(0, 5, 100)
def fun(x):
    return 2 * np.sin(x) + x + 1

Y = fun(X)

# Create the figure
fig = go.Figure()

fig.add_scatter(
    x=X,
    y=Y,
    mode='lines',
    line=dict(color=plt_colors[0], width=2),
)

fig.add_trace(
    go.Scatter(
        x=np.linspace(0, 0.17, 100), 
        y=np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )

fig.add_trace(
    go.Scatter(
        x=np.linspace(0.17, 0.34, 100), 
        y=1.5*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )


fig.add_trace(
    go.Scatter(
        x=np.linspace(0.34,0.51, 100), 
        y=2*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )

fig.add_trace(
    go.Scatter(
        x=np.linspace(0.51,0.7, 100), 
        y=2.5*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )

fig.add_trace(
    go.Scatter(
        x=np.linspace(0.7,0.91, 100), 
        y=3*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )

fig.add_trace(
    go.Scatter(
        x=np.linspace(0.91,1.16, 100), 
        y=3.5*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )

fig.add_trace(
    go.Scatter(
        x=np.linspace(1.16, 1.51, 100), 
        y=4*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )
fig.add_trace(
    go.Scatter(
        x=np.linspace(1.51, 2.75, 100), 
        y=4.5*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )
fig.add_trace(
    go.Scatter(
        x=np.linspace(2.75, 3.30, 100), 
        y=4*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )

fig.add_trace(
    go.Scatter(
        x=np.linspace(3.30,3.93, 100), 
        y=3.5*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )


fig.add_trace(
    go.Scatter(
        x=np.linspace(3.93,4.42, 100), 
        y=3*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )

fig.add_trace(
    go.Scatter(
        x=np.linspace(4.42,5, 100), 
        y=3.5*np.ones(100), 
        mode='lines', 
        showlegend = False, 
        line=dict(color=plt_colors[1], width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 57, 18, 0.1)',
        )
    )

# Remove the grid and update layout
fig.update_layout(
    showlegend=False,
    xaxis=dict(
        linewidth = 2,
        showline = False,
        zeroline = True,
        showgrid = False,
        showticklabels = False,
        range = [0, 5]
        ),
    yaxis=dict(
        linewidth = 2,
        showline = False,
        zeroline = True,
        showgrid = True,
        tickmode = 'linear',
        dtick = 0.5,
        showticklabels = True,
        #tickmode = 'array',
        #tickvals = [2, 1, 4, 1.5],
        #ticktext = [r'$\alpha_1$',r'$\alpha_2$', r'$\alpha_3$', r'$\alpha_4$' ],        
        range = [0, 5]
    )
)

fig.update_layout(template = "plotly_white+draft")

fig.show()

#%%
fig_white = fig
fig_black = fig
fig_white.update_layout(template = "plotly_white+draft")
fig_white.write_image("./../docs/images/expectation2_white.svg")
fig_black.update_layout(template = "plotly_dark+draft")
fig_black.write_image("./../docs/images/expectation2_dark.svg")

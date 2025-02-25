import numpy as np
# pandas is a framework for manipulating complex set of data on top of numpy
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objs as go
import plotly.io as pio
from plotly.subplots import make_subplots
# numpy is an efficient array library for python
from tqdm import tqdm

pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.max_rows", 100)
tqdm.pandas(desc="my bar!")

pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.max_rows", 100)
tqdm.pandas(desc="my bar!")

pd.options.plotting.backend = "plotly"

pio.templates["draft"] = go.layout.Template()
pio.templates["draft"].layout.legend = {"orientation": "h", "yanchor": "bottom", "y": 1.02, "xanchor": "right", "x": 1}
pio.templates["draft"].layout.autosize = False
pio.templates["draft"].layout.width = 800
pio.templates["draft"].layout.height = 500
pio.templates["draft"].layout.margin = dict(l=50, r=50, b=50, t=50, pad=4)
pio.templates["draft"].layout.title.xanchor = "center"
pio.templates["draft"].layout.title.x = 0.5

# we set transparenccy for the background

pio.templates["draft"].layout.paper_bgcolor = "rgba(0,0,0,0)"
#
pio.templates["draft"].layout.plot_bgcolor = "rgba(0,0,0,0)"
#

plt_colors = px.colors.qualitative.G10
plt_dark_color = "rgb(102, 102, 102)"
pio.templates["draft"].layout.colorway = plt_colors
pio.templates.default = "plotly_white+draft"




__all__ = [
    "pd",
    "np",
    "px",
    "ff",
    "go",
    "make_subplots",
    "tqdm",
    "plt_colors",
    "plt_dark_color",
    "pio",
]

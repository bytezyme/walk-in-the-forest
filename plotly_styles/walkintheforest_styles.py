import plotly.graph_objects as go
import plotly.io as pio

pio.templates["walkintheforest-dark"] = go.layout.Template(
    layout = go.Layout(
        font = {
            "family" : "'Open Sans', verdana, arial, sans-serif",
            "color"  : "white"
        },
        showlegend = True,
        paper_bgcolor = "#1e1e1e",
        plot_bgcolor = "#1e1e1e",
        
        title_font = {"size" : 20},
        margin = {"l": 100,
                  "r": 50,
                  "b": 90,
                  "t": 90,
                  },

        xaxis = {
            "color" : "white",
            "showgrid" : False,
            "zerolinewidth" : 2,
            "title_font" :  {"size": 16}
        },
        yaxis = {
            "color" : "white",
            "showgrid" : False,
            "zerolinewidth" : 2,
            "title_font" :  {"size": 16}
        },
        hovermode = "closest"
    )
)
#!/usr/bin/python
import json
import numpy as np

from bokeh.io import export_png_and_data    # Custom function
from bokeh.models import ColumnDataSource, LabelSet, Legend
from bokeh.plotting import figure

if __name__ == "__main__":

    # define starts/ends for wedges from percentages of a circle
    percents = [0, 0.3, 0.4, 0.6, 0.9, 1]
    starts = [p*2*np.pi for p in percents[:-1]]
    ends = [p*2*np.pi for p in percents[1:]]

    thetas = [starts[i] + (ends[i] - starts[i])/2 for i in range(len(starts))]
    rad = 0.75
    x = [rad*np.cos(theta) for theta in thetas]
    y = [rad*np.sin(theta) for theta in thetas]

    # a color for each pie piece
    colors = ["red", "green", "blue", "orange", "yellow"]
    pie_label_data = ColumnDataSource(dict(colors=colors, x=x, y=y))

    p = figure(plot_width=400, plot_height=400, x_range=(-1.25,1.25), y_range=(-1.25,1.25), title="the_title", toolbar_location=None)

    wedge1 = p.wedge(x=0, y=0, radius=1, start_angle=starts[0], end_angle=ends[0], color=colors[0], name="the_pie1")
    wedge2 = p.wedge(x=0, y=0, radius=1, start_angle=starts[1], end_angle=ends[1], color=colors[1], name="the_pie2")
    wedge3 = p.wedge(x=0, y=0, radius=1, start_angle=starts[2], end_angle=ends[2], color=colors[2], name="the_pie3")
    wedge4 = p.wedge(x=0, y=0, radius=1, start_angle=starts[3], end_angle=ends[3], color=colors[3], name="the_pie4")
    wedge5 = p.wedge(x=0, y=0, radius=1, start_angle=starts[4], end_angle=ends[4], color=colors[4], name="the_pie5")
    legend = Legend(
        items=[
            (colors[0], [wedge1]),
            (colors[1], [wedge2]),
            (colors[2], [wedge3]),
            (colors[3], [wedge4]),
            (colors[4], [wedge5])
        ],
        location="bottom_right",
        name="the_legend"
    )
    
    p.add_layout(legend, 'right')

    labels = LabelSet(x='x', y='y', text='colors', level='glyph', source=pie_label_data, render_mode='canvas', text_color='black', name="the_pie_labels")
    p.add_layout(labels)

    p.xaxis.visible = False
    p.yaxis.visible = False
    p.grid[0].visible = False
    p.grid[1].visible = False
    p.outline_line_color = None

    # Export to HTML, PNG, and get bbox data
    data = export_png_and_data(p, "pie_glyphs_legend.png", "pie_glyphs_legend.html")

    with open("pie_glyphs_legend.json", "w") as f:
        json.dump(data, f)

#!/usr/bin/python
import json
import numpy as np

from bokeh.io import export_png_and_data    # Custom function
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, LabelSet

if __name__ == "__main__":
    output_file("pie.html")

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

    p.wedge(x=0, y=0, radius=1, start_angle=starts, end_angle=ends, color=colors, name="the_pie")

    labels = LabelSet(x='x', y='y', text='colors', level='glyph', source=pie_label_data, render_mode='canvas', text_color='black')
    p.add_layout(labels)

    p.xaxis.visible = False
    p.yaxis.visible = False
    p.grid[0].visible = False
    p.grid[1].visible = False
    p.outline_line_color = None

    # Export to HTML, PNG, and get bbox data
    data = export_png_and_data(p, "pie.png", "pie.html")
    #print data

    with open("pie.json", "w") as f:
        json.dump(data, f)

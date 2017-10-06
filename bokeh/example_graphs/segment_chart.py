#!/usr/bin/python
import numpy as np
import json

from bokeh.io import export_png_and_data    # Custom function
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, DataRange1d, Plot, LinearAxis, Grid
from bokeh.models.glyphs import Segment
from bokeh.io import curdoc, show

if __name__ == "__main__":
    N = 9
    x = np.linspace(-2, 2, N)
    y = x**2

    segment_data = ColumnDataSource(dict(
            x_start=x,
            y_start=y,
            x_end=x-x**3/10 + 0.3,
            y_end=y-x**2/10 + 0.5,
        )
    )

    output_file("segments.html")

    p = figure(plot_width=400, plot_height=400, title="title_title", toolbar_location=None)

    p.add_glyph(segment_data, Segment(x0="x_start", y0="y_start", x1="x_end", y1="y_end", line_color="#f4a582", line_width=3, name="the_segments"))

    p.xaxis.name = "the_xaxis"
    p.xaxis.axis_label = "xaxis_label"
    p.yaxis.name = "the_yaxis"
    p.yaxis.axis_label = "yaxis_label"
    p.title.name = "the_title"

    if p.grid[0].dimension == 0:
        p.grid[0].name = "the_x_gridlines"
        p.grid[1].name = "the_y_gridlines"
    else:
        p.grid[0].name = "the_y_gridlines"
        p.grid[1].name = "the_x_gridlines"

    # Export to HTML, PNG, and get bbox data
    data = export_png_and_data(p, "segments.png", "segments.html")
    #print data

    with open("segments.json", "w") as f:
        json.dump(data, f)
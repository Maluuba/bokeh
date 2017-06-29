#!/usr/bin/python
import json

from bokeh.io import export_png_and_data    # Custom function
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource
from bokeh.models.glyphs import Line

if __name__ == "__main__":
    output_file("line.html")

    p = figure(plot_width=400, plot_height=400, title="title_title", toolbar_location=None)

    # add a line renderer
    p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2, name="the_line")
    #xs = [1, 2, 3, 4, 5]
    #ys = [6, 7, 2, 4, 5]
    #line_data = ColumnDataSource(dict(x=xs, y=ys))

    #p.add_glyph(line_data, Line(x="x", y="y", line_width=2, line_color="#F46D43", name="the_line"))

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
    data = export_png_and_data(p, "line.png", "line.html")
    #print data

    with open("line.json", "w") as f:
        json.dump(data, f)

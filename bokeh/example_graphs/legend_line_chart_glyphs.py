#!/usr/bin/python
import json

from bokeh.io import export_png_and_data    # Custom function
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, Legend
from bokeh.models.glyphs import Line

if __name__ == "__main__":

    p = figure(plot_width=400, plot_height=400, title="title_title", toolbar_location=None)

    # add a line renderer
    xs = [1, 2, 3, 4, 5]
    ys = [6, 7, 2, 4, 5]
    line_data = ColumnDataSource(dict(x=xs, y=ys))
    line1 = p.add_glyph(line_data, Line(x="x", y="y", line_width=2, line_color="#F46D43", name="the_line1"))

    xs = [1, 2, 3, 4, 5]
    ys = [1, 2, 3, 4, 5]
    line_data = ColumnDataSource(dict(x=xs, y=ys))
    line2 = p.add_glyph(line_data, Line(x="x", y="y", line_width=2, line_color="#000000", name="the_line2"))

    legend = Legend(items=[
        ("thing1"   , [line1]),
        ("thing2"   , [line2])
    ], location=(0, -30), name="the_legend")

    p.add_layout(legend, 'right')

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
    data = export_png_and_data(p, "legend_line_glyph.png", "legend_line_glyph.html")
    #print data

    with open("legend_line_glyph.json", "w") as f:
        json.dump(data, f)

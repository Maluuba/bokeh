#!/usr/bin/python
import json

from bokeh.io import export_png_and_data    # Custom function
from bokeh.plotting import figure, output_file, save, show
from bokeh.models import ColumnDataSource, Legend
from bokeh.models.glyphs import Line

if __name__ == "__main__":

    p = figure(plot_width=500, plot_height=500, title="title_title", toolbar_location=None)

    # add a line renderer
    xs = [1, 2, 3, 4, 5]
    ys = [6, 7, 2, 4, 5]
    line_data = ColumnDataSource(dict(x=xs, y=ys))
    line1 = p.add_glyph(line_data, Line(x="x", y="y", line_width=2, line_color="#F46D43", name="the_line1"))
    line1.name = "the_line1"
    xs = [1, 2, 3, 5, 7]
    ys = [1, 2, 3, 4, 5]
    line_data = ColumnDataSource(dict(x=xs, y=ys))
    line2 = p.add_glyph(line_data, Line(x="x", y="y", line_width=2, line_color="#000000", name="the_line2"))
    line2.name = "the_line2"


    legend = Legend(items=[
        ("thing1"   , [line1]),
        ("thing2"   , [line2])
    ], name="the_legend", label_text_font_size='5pt', glyph_width=20, glyph_height=10, location="top_right", padding=5, margin=0,
    background_fill_color=None, border_line_color=None, background_fill_alpha=0
    )

    p.add_layout(legend)

    p.xaxis.name = "the_xaxis"
    p.xaxis.axis_label = "yxaxisy_ylabely"
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
    data = export_png_and_data(p, "legend_line_glyph_inside.png", "legend_line_glyph_inside.html")
    #print data

    #with open("legend_line_glyph.json", "w") as f:
    #    json.dump(data, f)

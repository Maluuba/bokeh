#!/usr/bin/python
import json

from bokeh.io import export_png_and_data    # Custom function
from bokeh.models import ColumnDataSource, Legend
from bokeh.models.glyphs import Line
from bokeh.plotting import figure

LEGEND_INSIDE = True

if __name__ == "__main__":

    p = figure(plot_width=400, plot_height=400, title="title_title", toolbar_location=None)

    # add a line renderer
    xs = [1, 2, 3, 4, 5]
    ys = [6, 7, 2, 4, 5]
    line_data = ColumnDataSource(dict(x=xs, y=ys))
    line1 = p.add_glyph(line_data, Line(x="x", y="y", line_width=2, line_color="#F46D43", name="the_line1"))
    line1.name = "the_line1"

    xs = [1, 2, 3, 4, 5]
    ys = [1, 2, 3, 4, 5]
    line_data = ColumnDataSource(dict(x=xs, y=ys))
    line2 = p.add_glyph(line_data, Line(x="x", y="y", line_width=2, line_color="#000000", name="the_line2"))
    line2.name = "the_line2"

    legend = Legend(
        items=[
            ("thing1"   , [line1]),
            ("thing2"   , [line2])
        ],
        name="the_legend",
        label_text_font_size='5pt',
        glyph_width=20,
        glyph_height=10,
        location="top_right",
        padding=5,
        margin=0,
        background_fill_color=None,
        border_line_color=None,
        background_fill_alpha=0
    )

    # Control where the legend appears
    # Inside
    if LEGEND_INSIDE:
        p.add_layout(legend)
    # Outside
    else:
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
    data = export_png_and_data(p, "line_glyphs_legend.png", "line_glyphs_legend.html")

    with open("line_glyphs_legend.json", "w") as f:
        json.dump(data, f)

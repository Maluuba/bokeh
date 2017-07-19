#!/usr/bin/python
import json

from bokeh.io import export_png_and_data    # Custom function
from bokeh.plotting import figure, save, show, output_file
from bokeh.models import ColumnDataSource, Legend
from bokeh.models.markers import Asterisk, Circle, Cross, Diamond, Square, Triangle, X

if __name__ == "__main__":

    p = figure(plot_width=400, plot_height=400, title="title_title", toolbar_location=None)
    x = [1,2,3,4,5]
    sizes = [10]*len(x)
    circles = [1]*len(x)
    crosses = [2]*len(x)
    triangles = [3]*len(x)
    exes = [4]*len(x)
    asterisks = [5]*len(x)
    diamonds = [6]*len(x)
    squares = [7]*len(x)

    scatter_data = ColumnDataSource(dict(x=x, circles=circles, crosses=crosses, triangles=triangles, exes=exes, asterisks=asterisks, diamonds=diamonds, squares=squares, sizes=sizes))

    #circle_glyphs = Triangle(x="x", y="y", size="sizes", line_color="#de2d26", line_width=2, fill_color=None)
    glyphs = []
    glyphs.append(Circle(x="x", y="circles", size="sizes", fill_color="red", name="the_circles"))
    glyphs.append(Cross(x="x", y="crosses", size="sizes", fill_color="blue", name="the_crosses"))
    glyphs.append(Triangle(x="x", y="triangles", size="sizes", fill_color="green", name="the_triangles"))
    glyphs.append(X(x="x", y="exes", size="sizes", fill_color="purple", name="the_xs"))
    glyphs.append(Asterisk(x="x", y="asterisks", size="sizes", fill_color="orange", name="the_asterisks"))
    glyphs.append(Diamond(x="x", y="diamonds", size="sizes", fill_color="yellow", name="the_diamonds"))
    glyphs.append(Square(x="x", y="squares", size="sizes", fill_color="gray", name="the_squares"))

    legend_items = []
    for glyph in glyphs:
        renderer = p.add_glyph(scatter_data, glyph)
        renderer.name = glyph.name
        legend_items.append((renderer.name, [renderer]))
    
    legend = Legend(items=legend_items, location=(0, -30), name="the_legend")
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
    data = export_png_and_data(p, "legend_scatter.png", "legend_scatter.html")
    #print data

    with open("legend_scatter_data.json", "w") as f:
        json.dump(data, f)

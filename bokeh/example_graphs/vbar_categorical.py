#!/usr/bin/python

import io
import json
import os

from bokeh.io import export_png_and_data    # Custom function
from bokeh.plotting import figure

if __name__ == "__main__":

    # Set up the plot
    categories = ['cat_a','cat_b','cat_c']
    p = figure(plot_width=400, plot_height=400, title="title_title", toolbar_location=None, x_range=categories)
    p.vbar(x=categories, width=0.5, bottom=0,
        top=[1.2, 2.5, 3.7], color="firebrick", name="the_bars")
    
    # Set identifiers for the figure elements
    p.xaxis.name = "the_xaxis"
    p.xaxis.axis_label = "xaxis_label"
    p.yaxis.name = "the_yaxis"
    p.yaxis.axis_label = "yaxis_label"
    p.title.name = "the_title"
    p.xaxis.major_label_orientation = "vertical"
    if p.grid[0].dimension == 0:
        p.grid[0].name = "the_x_gridlines"
        p.grid[1].name = "the_y_gridlines"
    else:
        p.grid[0].name = "the_y_gridlines"
        p.grid[1].name = "the_x_gridlines"

    # Export to HTML, PNG, and get bbox data
    data = export_png_and_data(p, "vbar_categorical.png", "vbar_categorical.html")

    with open("vbar_categorical.json", "w") as f:
        json.dump(data, f)

#!/usr/bin/python

from bokeh.plotting import figure, save, show, output_file, curdoc
from bokeh.io import curstate
output_file('vbar.html')

p = figure(plot_width=400, plot_height=400, title="title_title", toolbar_location=None)
p.vbar(x=[1, 2, 3], width=0.5, bottom=0,
       top=[1.2, 2.5, 3.7], color="firebrick", name="the_bars")
p.xaxis.name = "the_xaxis"
p.xaxis.axis_label = "xaxis_label"
p.yaxis.name = "the_yaxis"
p.yaxis.axis_label = "yaxis_label"
p.title.name = "the_title"
save(p)
#show(p)
print dir(curdoc())
with open("vbar.json", "w") as f:
    f.write(curdoc().to_json_string())

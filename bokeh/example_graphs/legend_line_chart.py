#!/usr/bin/python
import json

from bokeh.io import export_png_and_data    # Custom function
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, Legend
from bokeh.models.glyphs import Line

if __name__ == "__main__":

    p = figure(plot_width=400, plot_height=400, title="title_title", toolbar_location=None)
    data = [{"y": [79.01551158109253, 78.83660697319964, 79.91674176459345, 78.51556035342148, 78.40814508675398, 80.28948609154212, 78.02871480223638, 80.46881344067468, 80.17178687969299, 79.05146940057337, 80.88162605179498, 79.46533464195267, 78.13796886556054, 78.97334393700966, 80.45708599043624, 80.68451006326531, 78.88781620349147, 79.9381945564395, 79.03576861862459, 79.23174949858311], "x": [48.0, 50.31578947368421, 52.631578947368425, 54.94736842105263, 57.26315789473684, 59.578947368421055, 61.89473684210526, 64.21052631578948, 66.52631578947368, 68.84210526315789, 71.15789473684211, 73.47368421052632, 75.78947368421052, 78.10526315789474, 80.42105263157895, 82.73684210526315, 85.05263157894737, 87.36842105263159, 89.6842105263158, 92.0], "colour": "#E0FFFF", "class": 0, "label": "Light Cyan"}, {"y": [51.134117882839924, 53.18975878851897, 56.21888912245981, 56.322360816219664, 56.617724056381135, 56.66706670914428, 60.64525366389036, 61.618134027182904, 62.24540728790753, 62.398406247697636, 64.20274430107541, 65.19608097305469, 65.76167051778573, 66.27517975188853, 67.24549399385221, 69.04659593968347, 69.07094954643308, 70.75629713682993, 71.29753042568292, 73.78776679197698], "x": [51.134117882839924, 53.18975878851897, 56.21888912245981, 56.322360816219664, 56.617724056381135, 56.66706670914428, 60.64525366389036, 61.618134027182904, 62.24540728790753, 62.398406247697636, 64.20274430107541, 65.19608097305469, 65.76167051778573, 66.27517975188853, 67.24549399385221, 69.04659593968347, 69.07094954643308, 70.75629713682993, 71.29753042568292, 73.78776679197698], "colour": "#F5FFFA", "class": 1, "label": "Mint Cream"}, {"y": [80.37848206832736, 80.21258327703755, 80.7168824205484, 80.44041116714372, 80.45423310898542, 80.48209341306129, 79.85783361259665, 80.57678523042196, 80.57515616781697, 80.51748367719064, 80.67185527202119, 80.86603456822802, 80.41203542814894, 80.5997044226832, 80.81516898453822, 80.93724040603513, 80.33263172852868, 80.48206696191195, 80.5521074054051, 80.72963054774394], "x": [50.22959147952605, 51.09046889847078, 52.59016258405952, 53.832838452733725, 54.259731800470014, 60.632717538043636, 61.634695443229205, 63.889790900309535, 63.979303525157135, 63.98222614610634, 68.10977633302598, 68.8018863984151, 70.86554743284582, 75.4169894756208, 77.60839091007502, 78.51399838914487, 80.51542579087402, 88.12262947831502, 89.00867269339508, 90.2495930927613], "colour": "#90EE90", "class": 2, "label": "Light Green"}, {"y": [92.0, 89.6842105263158, 87.36842105263159, 85.05263157894737, 82.73684210526315, 80.42105263157895, 78.10526315789474, 75.78947368421052, 73.47368421052632, 71.15789473684211, 68.84210526315789, 66.52631578947368, 64.21052631578948, 61.89473684210526, 59.578947368421055, 57.26315789473684, 54.94736842105263, 52.631578947368425, 50.31578947368421, 48.0], "x": [48.0, 50.31578947368421, 52.631578947368425, 54.94736842105263, 57.26315789473684, 59.578947368421055, 61.89473684210526, 64.21052631578948, 66.52631578947368, 68.84210526315789, 71.15789473684211, 73.47368421052632, 75.78947368421052, 78.10526315789474, 80.42105263157895, 82.73684210526315, 85.05263157894737, 87.36842105263159, 89.6842105263158, 92.0], "colour": "#7FFF00", "class": 3, "label": "Chartreuse"}]

    # Create the column data source and glyphs scatter data
    glyph_renderers = []
    for i, point_set in enumerate(data):
        col_data = ColumnDataSource({ 'x': point_set['x'], 'y': point_set['y'], 's': [10]*len(point_set['x'])})
        glyph = Line(x='x', y='y', line_width=2, line_color=point_set['colour'], name=point_set['label'])
        glyph_renderer = p.add_glyph(col_data, glyph)
        glyph_renderers.append(glyph_renderer)

    legend = Legend(items=[("model " + gr.glyph.name, [gr]) for i, gr in enumerate(glyph_renderers)], location=(0, -30))
    
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
    data = export_png_and_data(p, "legend_line.png", "legend_line.html")
    #print data

    with open("line.json", "w") as f:
        json.dump(data, f)

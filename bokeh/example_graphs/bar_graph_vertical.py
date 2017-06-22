#!/usr/bin/python

import io
import os

from bokeh.io import _wait_until_render_complete, _crop_image, _detect_filename
from bokeh.plotting import figure, save, show, output_file, curdoc
from bokeh.resources import INLINE
from bokeh.util.dependencies import import_required, detect_phantomjs

def export_png_and_data(obj, filename, html_path, driver=None):
    webdriver = import_required('selenium.webdriver',
                                'To use bokeh.io.export_png you need selenium ' +
                                '("conda install -c bokeh selenium" or "pip install selenium")')

    Image = import_required('PIL.Image',
                            'To use bokeh.io.export_png you need pillow ' +
                            '("conda install pillow" or "pip install pillow")')
    # assert that phantomjs is in path for webdriver
    detect_phantomjs()

    fwd_slash_html_path = save(obj, filename=html_path, resources=INLINE, title="").replace('\\', '/')

    if driver is None:
        web_driver = webdriver.PhantomJS(service_log_path="webdriver.log")
    else:
        web_driver = driver

    web_driver.get("file:///" + fwd_slash_html_path)

    ## resize for PhantomJS compat
    web_driver.execute_script("document.body.style.width = '100%';")
    _wait_until_render_complete(web_driver)
    png = web_driver.get_screenshot_as_png()
    bounding_rect_script = "return document.getElementsByClassName('bk-root')[0].children[0].getBoundingClientRect()"
    b_rect = web_driver.execute_script(bounding_rect_script)

    get_localstorage_script = "return window.localStorage.getItem(Object.keys(window.localStorage)[0])"
    localstorage = web_driver.execute_script(get_localstorage_script)
    print "localstorage", localstorage

    get_localstorage_keys_script = "return Object.keys(window.localStorage)"
    localstorage_keys = web_driver.execute_script(get_localstorage_keys_script)
    print "localstorage keys", localstorage_keys

    if driver is None: # only quit webdriver if not passed in as arg
        web_driver.quit()

    image = Image.open(io.BytesIO(png))
    cropped_image = _crop_image(image, **b_rect)

    if filename is None:
        filename = _detect_filename("png")

    cropped_image.save(filename)

    return localstorage

if __name__ == "__main__":
    output_file('vbar.html')

    p = figure(plot_width=400, plot_height=400, title="title_title", toolbar_location=None)
    p.vbar(x=[1, 2, 3], width=0.5, bottom=0,
        top=[1.2, 2.5, 3.7], color="firebrick", name="the_bars")
    p.xaxis.name = "the_xaxis"
    p.xaxis.axis_label = "xaxis_label"
    p.yaxis.name = "the_yaxis"
    p.yaxis.axis_label = "yaxis_label"
    p.title.name = "the_title"
    #fname = "vbar.png"
    #abs_fname = save(p, filename="vbar.html")
    #print abs_fname
    #show(p)
    #with open("vbar.json", "w") as f:
    #    f.write(curdoc().to_json_string())
    export_png_and_data(p, "vbar.png", "vbar.html")

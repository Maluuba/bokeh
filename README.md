# Bokeh

## Introduction

This fork of Bokeh gets the coordinates of drawn primitives for bounding boxes.

Bokeh has no dependency on matplotlib (thank goodness).

At a high-level, here's how the library works:

- The figure is defined in Python. Source code lives in the Bokeh Python library: bokeh/bokeh
--- Make sure you add `name` attributes to the different parts of your figure
--- Use the `export_png_and_data` function from bokeh.io to get the PNG and a Python dict of the bounding box data

- The Bokeh Python library calls the Bokeh JavaScript library (bokeh/bokehjs) which renders to a canvas and exports this to a PNG
--- Python lib generates an HTML file with JSON defining the figure
--- JS lib takes the HTML file and renders it in a headless browser (PhantomJS)
--- JS lib renders the figure (model-view coffeescript, like Backbone.js) and intercepts draws to the canvas
--- JS lib takes canvas draws, figures out bounding boxes, associates with names defined in Python lib, and saves to localStorage in PhantomJS
--- Python lib grabs the data from the PhantomJS webdriver's localStorage

## Prerequisites

- Install the following Python packages: NumPy, Jinja2, Six, Requests, Tornado >= 4.0, PyYaml, DateUtil, Selenium, PhantomJS, Pillow
- Install NodeJS
- Install PhantomJS globally with `npm install -g phantomjs-prebuilt`
- Make sure the PhantomJS executable is on your PATH. I found mine at: `C:\Users\adatkins\AppData\Roaming\npm\node_modules\phantomjs-prebuilt\lib\phantom\bin`
- cd to bokeh/bokehjs and do `npm install`

## Development

### Installation

#### Python + JS

- cd to the root directory, bokeh
- run `python setup.py develop --build-js` to build the JS bundle and include it in the Python library
- This needs to be done everytime you want to use new JS changes with the Python Bokeh library!

#### JS Only

- cd to bokeh/bokehjs
- if you want to recompile on new changes, run `gulp watch`
- if you want to build an un-minified bundle, run `gulp dev-build`

#### Python Only

- Can do Python + JS step above, or add symlink in site-packages to the current project with `python setup.py develop`. This uses the last added JS lib in the Python + JS step.

### Workflows

#### Python + JS

#### JS Only

#### Python Only

## Usage and Examples

See `bokeh/bokeh/example_graphs/bar_graph_vertical.py`

# Stuff from original Bokeh README

<table>
<tr>
  <td>Latest Release</td>
  <td><img src="https://badge.fury.io/gh/bokeh%2Fbokeh.svg" alt="latest release" /></td>
</tr>
<tr>
  <td>License</td>
  <td>
    <a href="https://github.com/bokeh/bokeh/blob/master/LICENSE.txt">
    <img src="https://img.shields.io/github/license/bokeh/bokeh.svg" alt="Bokeh license" />
    </a>
  </td>
</tr>
<tr>
  <td>Build Status</td>
  <td>
    <a href="https://travis-ci.org/bokeh/bokeh">
    <img src="https://travis-ci.org/bokeh/bokeh.svg?branch=master" alt="build status" />
    </a>
  </td>
</tr>
<tr>
  <td>Conda</td>
  <td>
    <a href="http://bokeh.pydata.org/en/latest/docs/installation.html">
    <img src="http://pubbadges.s3-website-us-east-1.amazonaws.com/pkgs-downloads-bokeh.png" alt="conda downloads" />
    </a>
  </td>
</tr>
<tr>
  <td>PyPI</td>
  <td>
    <img src="http://bokeh.pydata.org/pip-bokeh-badge.png" />
  </td>
</tr>
<tr>
  <td>Gitter</td>
  <td>
    <a href="https://gitter.im/bokeh/bokeh?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge">
    <img src="https://badges.gitter.im/bokeh/bokeh.svg" />
    </a>
  </td>
</tr>
<tr>
  <td>Twitter</td>
  <td>
    <a href="https://https://twitter.com/BokehPlots">
    <img src="https://img.shields.io/twitter/follow/bokehplots.svg?style=social&label=Follow" />
    </a>
  </td>
</tr>
</table>

Bokeh, a Python interactive visualization library, enables beautiful and
meaningful visual presentation of data in modern web browsers. With Bokeh,
you can quickly and easily create interactive plots, dashboards, and data
applications.

Bokeh helps provide elegant, concise construction of novel graphics in the
style of D3.js, while also delivering **high-performance** interactivity over
very large or streaming datasets.

[Interactive gallery](http://bokeh.pydata.org/en/latest/docs/gallery.html)
---------------------------------------------------------------------------

<p>
<table cellspacing="20">
<tr>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/image.html">
  <img alt="image" src="http://bokeh.pydata.org/en/latest/_images/image_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/anscombe.html">
  <img alt="anscombe" src="http://bokeh.pydata.org/en/latest/_images/anscombe_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/stocks.html">
  <img alt="stocks" src="http://bokeh.pydata.org/en/latest/_images/stocks_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/lorenz.html">
  <img alt="lorenz" src="http://bokeh.pydata.org/en/latest/_images/lorenz_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/candlestick.html">
  <img alt="candlestick" src="http://bokeh.pydata.org/en/latest/_images/candlestick_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/color_scatter.html">
  <img alt="scatter" src="http://bokeh.pydata.org/en/latest/_images/scatter_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/iris_splom.html">
  <img alt="splom" src="http://bokeh.pydata.org/en/latest/_images/splom_t.png" />
  </a>
  </td>

</tr>
<tr>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/iris.html">
  <img alt="iris" src="http://bokeh.pydata.org/en/latest/_images/iris_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/histogram.html">
  <img alt="histogram" src="http://bokeh.pydata.org/en/latest/_images/histogram_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/periodic.html">
  <img alt="periodic" src="http://bokeh.pydata.org/en/latest/_images/periodic_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/texas.html">
  <img alt="choropleth" src="http://bokeh.pydata.org/en/latest/_images/choropleth_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/burtin.html">
  <img alt="burtin" src="http://bokeh.pydata.org/en/latest/_images/burtin_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/streamline.html">
  <img alt="streamline" src="http://bokeh.pydata.org/en/latest/_images/streamline_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/image_rgba.html">
  <img alt="image_rgba" src="http://bokeh.pydata.org/en/latest/_images/image_rgba_t.png" />
  </a>
  </td>

</tr>
<tr>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/brewer.html">
  <img alt="stacked" src="http://bokeh.pydata.org/en/latest/_images/stacked_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/quiver.html">
  <img alt="quiver" src="http://bokeh.pydata.org/en/latest/_images/quiver_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/elements.html">
  <img alt="elements" src="http://bokeh.pydata.org/en/latest/_images/elements_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/boxplot.html">
  <img alt="boxplot" src="http://bokeh.pydata.org/en/latest/_images/boxplot_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/categorical.html">
  <img alt="categorical" src="http://bokeh.pydata.org/en/latest/_images/categorical_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/unemployment.html">
  <img alt="unemployment" src="http://bokeh.pydata.org/en/latest/_images/unemployment_t.png" />
  </a>
  </td>

  <td>
  <a href="http://bokeh.pydata.org/en/latest/docs/gallery/les_mis.html">
  <img alt="les_mis" src="http://bokeh.pydata.org/en/latest/_images/les_mis_t.png" />
  </a>
  </td>

</tr>
</table>
</p>

Documentation
-------------
Visit the [Bokeh web page](http://bokeh.pydata.org/en/latest) for information and full documentation.

Contribute to Bokeh
-------------------
To contribute to Bokeh, please review the [Developer Guide](http://bokeh.pydata.org/en/latest/docs/dev_guide.html).

Follow us
---------
Follow us on Twitter [@bokehplots](https://twitter.com/BokehPlots) and on [YouTube](https://www.youtube.com/channel/UCK0rSk29mmg4UT4bIOvPYhw).

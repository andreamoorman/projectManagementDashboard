from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend

# prepare some data
x = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
y = [.90, .91, .92, .93, .94, .95, .96, .97, .98, .99, 1.00]

menRetention = [1, .938, 1, 1, .909, 1, .917, 1, 1, .95, .933]
womenRetention = [.944, .944, .933, .929, .824, .963, 1, 1, 1, .95, .96]

# output to static HTML file
output_file("ipfwCCRetention.html")

# create a new plot with a title and axis labels
scores = figure(title="IPFW Cross Country Retention/Year", plot_height=300, plot_width=435, x_axis_label='year', y_axis_label='retention', toolbar_location=None, tools="")

# add a line renderer with legend and line thickness

menReten = scores.line(x, menRetention, line_width=4, color='#6460AA')
womenReten = scores.line(x, womenRetention, line_width=4, color='#0DB14B')

legend = Legend(items=[
    ("Men's Cross Country", [menReten]),
    ("Women's Cross Country", [womenReten])], location=(0, 0))

scores.add_layout(legend, 'right')

# show the results
show(scores)
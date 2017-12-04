from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend

# prepare some data
x = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
y = [.90, .91, .92, .93, .94, .95, .96, .97, .98, .99, 1.00]

menRetention = [.923, 1, .938, 1, .882, .941, .941, 1, .929, 1, .941]
womenRetention = [1, 1, .857, 1, 1, .938, 1, 1, .857, 1, 1]

# output to static HTML file
output_file("ipfwTennisRetention.html")

# create a new plot with a title and axis labels
scores = figure(title="IPFW Tennis Retention/Year", plot_height=300, plot_width=435, x_axis_label='year', y_axis_label='retention', toolbar_location=None, tools="")

# add a line renderer with legend and line thickness

menReten = scores.line(x, menRetention, line_width=4, color='#6460AA')
womenReten = scores.line(x, womenRetention, line_width=4, color='#0DB14B')

legend = Legend(items=[
    ("Men's Tennis", [menReten]),
    ("Women's Tennis", [womenReten])], location=(0, 0))

scores.add_layout(legend, 'right')

# show the results
show(scores)
from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend

# prepare some data
x = [ 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
y = [940, 950, 960, 970, 980, 990, 1000]

menScores = [1000, 941, 967, 1000, 958, 1000, 1000, 969, 844, 1000]
womenScores = [944, 1000, 1000, 1000, 1000, 957, 1000, 1000, 1000, 1000]

# output to static HTML file
output_file("ipfwGolfScores.html")

# create a new plot with a title and axis labels
scores = figure(title="IPFW Golf Score/Year", plot_height=300, plot_width=435, x_axis_label='year', y_axis_label='score', toolbar_location=None, tools="")

# add a line renderer with legend and line thickness

menSco = scores.line(x, menScores, line_width=4, color='#6460AA')
womenSco = scores.line(x, womenScores, line_width=4, color='#0DB14B')

legend = Legend(items=[
    ("Men's Golf", [menSco]),
    ("Women's Golf", [womenSco])], location=(0, 0))

scores.add_layout(legend, 'right')

# show the results
show(scores)
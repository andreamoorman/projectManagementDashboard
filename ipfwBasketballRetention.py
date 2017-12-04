from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend

# prepare some data
x = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
y = [.90, .91, .92, .93, .94, .95, .96, .97, .98, .99, 1.00]

menRetention = [.84, .864, .885, .958, .962, .96, .84, .92, .958, 1, .963]
womenRetention = [.893, .893, .966, .897, 1, 1, .964, .926, .958, 1, .963]

# output to static HTML file
output_file("ipfwBasketballRetention.html")

# create a new plot with a title and axis labels
scores = figure(title="IPFW Basketball Retention/Year", plot_height=300, plot_width=435, x_axis_label='year', y_axis_label='retention', toolbar_location=None, tools="")

# add a line renderer with legend and line thickness

menReten = scores.line(x, menRetention, line_width=4, color='#6460AA')
womenReten = scores.line(x, womenRetention, line_width=4, color='#0DB14B')

legend = Legend(items=[
    ("Men's Basketball", [menReten]),
    ("Women's Basketball", [womenReten])], location=(0, 0))

scores.add_layout(legend, 'right')

# show the results
show(scores)
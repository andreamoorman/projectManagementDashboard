from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend

# prepare some data
x = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
y = [.90, .91, .92, .93, .94, .95, .96, .97, .98, .99, 1.00]

menRetention = [.932, .935, .951, .929, .914, .923, .935, .925, .864, .980, .959]
womenRetention = [.958, .933, .962, 1, .929, .936, 1, 1, .929, 1, .926]

# output to static HTML file
output_file("ipfwBaseballSoftballRetention.html")

# create a new plot with a title and axis labels
scores = figure(title="IPFW Baseball/Softball Retention/Year", plot_height=300, plot_width=435, x_axis_label='year', y_axis_label='retention', toolbar_location=None, tools="")

# add a line renderer with legend and line thickness

menReten = scores.line(x, menRetention, line_width=4, color='#6460AA')
womenReten = scores.line(x, womenRetention, line_width=4, color='#0DB14B')

legend = Legend(items=[
    ("Men's Baseball", [menReten]),
    ("Women's Softball", [womenReten])], location=(0, 0))

scores.add_layout(legend, 'right')

# show the results
show(scores)
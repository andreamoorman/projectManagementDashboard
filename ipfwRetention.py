from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend

# prepare some data
x = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
y = [.90, .91, .92, .93, .94, .95, .96, .97, .98, .99, 1.00]

ipfwRetention = [.935, .954, .953, .962, .929, .958, .958, .977, .945, .973, .961]
menRetention = [.914, .954, .951, .968, .927, .950, .942, .968, .926, .965, .963]
womenRetention = [.950, .954, .956, .956, .931, .964, .972, .984, .960, .979, .958]

# output to static HTML file
output_file("ipfwRetention.html")

# create a new plot with a title and axis labels
scores = figure(title="IPFW Average Retention/Year", plot_height=300, plot_width=435, x_axis_label='year', y_axis_label='retention', toolbar_location=None, tools="")

# add a line renderer with legend and line thickness

totalRetention = scores.line(x, ipfwRetention, line_width=4, color='#CC004C')
menReten = scores.line(x, menRetention, line_width=4, color='#6460AA')
womenReten = scores.line(x, womenRetention, line_width=4, color='#0DB14B')

legend = Legend(items=[
    ("All Sports", [totalRetention]),
    ("Men Sports", [menReten]),
    ("Women Sports", [womenReten])], location=(0, 0))

scores.add_layout(legend, 'right')

# show the results
show(scores)
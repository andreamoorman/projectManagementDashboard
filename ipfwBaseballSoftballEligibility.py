from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend

# prepare some data
x = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
y = [.90, .91, .92, .93, .94, .95, .96, .97, .98, .99, 1.00]

menEligibility = [1, .913, .976, .976, .972, .976, .915, .963, .841, .981, .959]
womenEligibility = [1, .903, .962, .938, .929, .903, .96, .972, 1, 1, .968]

# output to static HTML file
output_file("ipfwBaseballSoftballEligibility.html")

# create a new plot with a title and axis labels
scores = figure(title="IPFW Baseball/Softball Eligibility/Year", plot_height=300, plot_width=435, x_axis_label='year', y_axis_label='eligibility', toolbar_location=None, tools="")

# add a line renderer with legend and line thickness)
menElig = scores.line(x, menEligibility, line_width=4, color='#6460AA')
womenElig = scores.line(x, womenEligibility, line_width=4, color='#0DB14B')

legend = Legend(items=[
    ("Men's Baseball", [menElig]),
    ("Women's Softball", [womenElig])], location=(0, 0))

scores.add_layout(legend, 'right')

# show the results
show(scores)
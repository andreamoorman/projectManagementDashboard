from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend

# prepare some data
x = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
y = [.90, .91, .92, .93, .94, .95, .96, .97, .98, .99, 1.00]

menEligibility = [1, .941, .933, 1, 1, 1, 1, 1, .75, 1]
womenEligibility = [.889, 1, 1, 1, .917, 1, 1, 1, 1, 1]

# output to static HTML file
output_file("ipfwGolfEligibility.html")

# create a new plot with a title and axis labels
scores = figure(title="IPFW Golf Eligibility/Year", plot_height=300, plot_width=435, x_axis_label='year', y_axis_label='eligibility', toolbar_location=None, tools="")

# add a line renderer with legend and line thickness)
menElig = scores.line(x, menEligibility, line_width=4, color='#6460AA')
womenElig = scores.line(x, womenEligibility, line_width=4, color='#0DB14B')

legend = Legend(items=[
    ("Men's Golf", [menElig]),
    ("Women's Golf", [womenElig])], location=(0, 0))

scores.add_layout(legend, 'right')

# show the results
show(scores)
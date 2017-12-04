from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend

# prepare some data
x = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
y = [.90, .91, .92, .93, .94, .95, .96, .97, .98, .99, 1.00]

menEligibility = [.929, .936, .957, 1, .84, .971, .966, 1, 1, .907, 1]
womenEligibility = [.929, .936, .955, 1, .813, .972, .97, 1, 1, .907, 1]

# output to static HTML file
output_file("ipfwTrackEligibility.html")

# create a new plot with a title and axis labels
scores = figure(title="IPFW Track Eligibility/Year", plot_height=300, plot_width=435, x_axis_label='year', y_axis_label='eligibility', toolbar_location=None, tools="")

# add a line renderer with legend and line thickness)
menElig = scores.line(x, menEligibility, line_width=4, color='#6460AA')
womenElig = scores.line(x, womenEligibility, line_width=4, color='#0DB14B')

legend = Legend(items=[
    ("Women's Indoor Track", [menElig]),
    ("Women's Outdoor Track", [womenElig])], location=(0, 0))

scores.add_layout(legend, 'right')

# show the results
show(scores)
from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend

# prepare some data
x = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
y = [.90, .91, .92, .93, .94, .95, .96, .97, .98, .99, 1.00]

ipfwEligibility = [.979, .959, .970, .980, .934, .966, .964, .965, .968, .949, .972]
menEligibility = [.985, .966, .979, .964, .950, .968, .938, .938, .942, .927, .968]
womenEligibility = [.974, .953, .962, .993, .921, .965, .985, .985, .989, .966, .976]

# output to static HTML file
output_file("ipfwEligibility.html")

# create a new plot with a title and axis labels
scores = figure(title="IPFW Average Eligibility/Year", plot_height=300, plot_width=435, x_axis_label='year', y_axis_label='eligibility', toolbar_location=None, tools="")

# add a line renderer with legend and line thickness)
totalEligibility = scores.line(x, ipfwEligibility, line_width=4, color='#CC004C')
menElig = scores.line(x, menEligibility, line_width=4, color='#6460AA')
womenElig = scores.line(x, womenEligibility, line_width=4, color='#0DB14B')

legend = Legend(items=[
    ("All Sports", [totalEligibility]),
    ("Men Sports", [menElig]),
    ("Women Sports", [womenElig])], location=(0, 0))

scores.add_layout(legend, 'right')

# show the results
show(scores)
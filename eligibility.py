from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend

# prepare some data
x = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
y = [.90, .91, .92, .93, .94, .95, .96, .97, .98, .99, 1.00]

d1men = [.952, .950, .949, .953, .958, .961, .963, .964, .970, .973, .976]
d1women = [.977, .975, .975, .976, .977, .979, .980, .982, .984, .985, .988]
d2men = [.971, .956, .950, .958, .971, .972, .968, .964, .966, .966, .958]
d2women = [.981, .939, .955, .986, .968, .982, .989, .991, .981, .995, .974]
d3men = [.980, .983, .984, .989, .986, .988, .994, 1.000, .995, .985, .983]
d3women = [1.000, 1.000, .996, .995, .997, .994, .995, .987, .996, 1.000, 1.000]

# output to static HTML file
output_file("eligibility.html")

# create a new plot with a title and axis labels
scores = figure(title="Average Eligibility/Year", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
d1m = scores.line(x, d1men, line_width=4, color='#F9C7A8')
d1w = scores.line(x, d1women, line_width=4, color='#F39A9B')
d2m = scores.line(x, d2men, line_width=4, color='#EC6E8D')
d2w = scores.line(x, d2women, line_width=4, color='#D74A88')
d3m = scores.line(x, d3men, line_width=4, color='#A93790')
d3w = scores.line(x, d3women, line_width=4, color='#7B2397')

legend = Legend(items=[
    ("D1 Men",   [d1m]),
    ("D1 Women", [d1w]),
    ("D2 Men", [d2m]),
    ("D2 Women", [d2w]),
    ("D3 Men", [d3m]),
    ("D3 Women", [d3w])], location=(0, 0))

scores.add_layout(legend, 'right')

# show the results
show(scores)
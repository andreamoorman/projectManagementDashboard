from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend

# prepare some data
x = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
y = [.90, .91, .92, .93, .94, .95, .96, .97, .98, .99, 1.00]

d1men = [.944, .944, .945, .948, .959, .961, .961, .961, .964, .966, .968]
d1women = [.962, .962, .963, .963, .973, .975, .975, .977, .978, .978, .981]
d2men = [.939, .937, .918, .941, .961, .967, .957, .945, .952, .969, .954]
d2women = [.973, .945, .915, .953, .965, .980, .980, .965, .971, .979, .967]
d3men = [.965, .973, .958, .962, .976, .976, .982, .995, .976, .981, .982]
d3women = [.96, .965, .960, .973, .981, .988, .979, .974, .994, .997, .988]

# output to static HTML file
output_file("retention.html")

# create a new plot with a title and axis labels
scores = figure(title="Average Retention/Year", plot_height=300, plot_width=435, x_axis_label='year', y_axis_label='retention', toolbar_location=None, tools="")

# add a line renderer with legend and line thickness
d1m = scores.line(x, d1men, line_width=4, color='#FCB711')
d1w = scores.line(x, d1women, line_width=4, color='#F37021')
d2m = scores.line(x, d2men, line_width=4, color='#CC004C')
d2w = scores.line(x, d2women, line_width=4, color='#6460AA')
d3m = scores.line(x, d3men, line_width=4, color='#0089D0')
d3w = scores.line(x, d3women, line_width=4, color='#0DB14B')

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
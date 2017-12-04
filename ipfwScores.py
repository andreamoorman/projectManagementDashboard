from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend

# prepare some data
x = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
y = [940, 950, 960, 970, 980, 990, 1000]

ipfwScores = [960.71, 962.94, 965.38, 981.44, 937.94, 971.5, 965.31, 974.81, 967.94, 964.75, 969.5]
menScores = [956.00, 973.00, 969.00, 978.86, 953.71, 969.14, 948.57, 960.4, 951.43, 955.29, 970.57]
womenScores = [964.25, 955.11, 962.56, 982.67, 925.67, 973.33, 978.33, 986.22, 980.78, 972.11, 968.67]

# output to static HTML file
output_file("ipfwScores.html")

# create a new plot with a title and axis labels
scores = figure(title="IPFW Average Score/Year", plot_height=300, plot_width=435, x_axis_label='year', y_axis_label='score', toolbar_location=None, tools="")

# add a line renderer with legend and line thickness

totalScores = scores.line(x, ipfwScores, line_width=4, color='#CC004C')
menSco = scores.line(x, menScores, line_width=4, color='#6460AA')
womenSco = scores.line(x, womenScores, line_width=4, color='#0DB14B')

legend = Legend(items=[
    ("All Sports", [totalScores]),
    ("Men Sports", [menSco]),
    ("Women Sports", [womenSco])], location=(0, 0))

scores.add_layout(legend, 'right')

# show the results
show(scores)
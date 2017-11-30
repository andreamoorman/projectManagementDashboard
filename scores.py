from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend

# prepare some data
x = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
y = [940, 950, 960, 970, 980, 990, 1000]

d1men = [949.52, 950.09, 950.03, 954.12, 962.22, 964.11, 965.29, 965.69, 970.05, 972.53, 973.93]
d1women = [969.72, 969.24, 970.06, 971.17, 976.59, 978.61, 979.08, 980.95, 982.44, 983.10, 985.38]
d2men = [955.43, 948.00, 935.27, 950.92, 967.85, 970.38, 963.31, 957.23, 959.06, 968.85, 957.15]
d2women = [977.00, 942.17, 936.22, 970.78, 967.78, 981.22, 985.56, 979.22, 976.11, 987.32, 971.44]
d3men = [972.44, 978.22, 972.3, 975.2, 981.00, 982.2, 989.2, 997.5, 985.6, 984.8, 982.8]
d3women = [980.00, 982.5, 977.71, 983.88, 988.88, 990.75, 986.75, 980.5, 997.25, 998.67, 994.11]

# output to static HTML file
output_file("scores.html")

# create a new plot with a title and axis labels
scores = figure(title="Average Score/Year", plot_height=300, plot_width=435, x_axis_label='year', y_axis_label='score', toolbar_location=None, tools="")

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
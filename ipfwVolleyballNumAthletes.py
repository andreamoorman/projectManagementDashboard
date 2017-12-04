from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

output_file("ipfwVolleyballNumAthletes.html")

years = ['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014']
divisions = ['Men Athletes', 'Women Athletes']

data = {'years' : years,
        'Men Athletes'   : [10, 13, 14, 13, 12, 12, 11, 10, 11, 10, 9],
        'Women Athletes'   : [12, 11, 12, 12, 12, 12, 14, 12, 13, 11, 12]
        }

palette = ["#6460AA", "#0DB14B"]

# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
x = [ (year, division) for year in years for division in divisions ]
counts = sum(zip(data['Men Athletes'], data['Women Athletes']), ()) # like an hstack

source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), plot_height=250, plot_width=1300, title="IPFW Number of Volleyball Athletes Per Year",
           toolbar_location=None, tools="")

p.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",
       fill_color=factor_cmap('x', palette=palette, factors=divisions, start=1, end=2))

p.y_range.start = 0
p.x_range.range_padding = 0.025
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

show(p)
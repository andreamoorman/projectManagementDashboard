from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

output_file("numAthletes.html")

years = ['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014']
divisions = ['D1 Mens', 'D1 Womens', 'D2 Mens', 'D2 Womens', 'D3 Mens', 'D3 Womens']

data = {'years' : years,
        'D1 Mens'   : [21.91, 22.25, 22.34, 22.15, 22.48, 22.30, 22.31, 22.35, 22.65, 22.89, 23.01 ],
        'D1 Womens'   : [15.60, 15.80, 16.03, 16.17, 16.28, 16.41, 16.68, 16.87, 17.01, 17.23, 17.41],
        'D2 Mens'   : [21.83, 21.96, 22.35, 21.23, 21.58, 21.5, 21.04, 21.69, 19.97, 19.28, 19.51],
        'D2 Womens': [19.00, 21.17, 18.56, 18.33, 18.00, 17.56, 17.78, 17.89, 16.00, 15.64, 16.22 ],
        'D3 Mens': [23.67, 22.89, 22.90, 22.90, 23.60, 24.50, 24.00, 24.60, 24.40, 24.10, 25.70 ],
        'D3 Womens': [16.60, 16.50, 16.00, 15.88, 16.63, 19.13, 19.25, 19.75, 20.75, 18.44, 18.89]
        }

palette = ["#F9C7A8", "#F39A9B", "#EC6E8D", "#D74A88", "#A93790", "#7B2397"]

# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
x = [ (year, division) for year in years for division in divisions ]
counts = sum(zip(data['D1 Mens'], data['D1 Womens'], data['D2 Mens'], data['D2 Womens'], data['D3 Mens'], data['D3 Womens']), ()) # like an hstack

source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), plot_height=350, plot_width=800, title="Average Number of Athletes Per Year",
           toolbar_location=None, tools="")

p.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",
       fill_color=factor_cmap('x', palette=palette, factors=divisions, start=1, end=2))

p.y_range.start = 10
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

show(p)
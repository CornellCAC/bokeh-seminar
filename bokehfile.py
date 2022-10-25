
"""
bokehfile.py: file input in bokeh
"""

# run in server mode via: bokeh serve --show bokehfile.py
# then click FileInput widget and choose file Scan4.csv

from bokeh.io import curdoc
from bokeh.models.widgets import FileInput
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from base64 import b64decode
import pandas as pd
import io

def upload_data(attr, old, new):
    global datasource, plot
    decoded = b64decode(new)
    data = io.BytesIO(decoded)
    print(data)
    df = pd.read_csv(data, header=None)
    df.columns = ('x', 'y')
    datasource = ColumnDataSource(df)
    plot.line('x', 'y', source=datasource)

datasource = ColumnDataSource({'x': [], 'y': []})
plot = figure(width=500, height=400)

file_input = FileInput(accept=".csv")
file_input.on_change('value', upload_data)

doc=curdoc()
doc.add_root(file_input)
doc.add_root(plot)


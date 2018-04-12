
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('Happy_Das', 'gqFHrnV4u2yQkUdckBtD')
trace1 = {
  "x": [1, 5, 10, 15, 20, 25, 30],
  "y": [0.7452054794520547, 0.35753424657534244, 0.1191780821917808, 0.05890410958904109, 0.024657534246575342, 0.00821917808219178, 0.005479452054794521,],

  "name": "Training Accuracy",
  "type": "scatter"
}


data = Data([trace1])
layout = {
  "title": "Accuracy against training data set.",
  "xaxis": {"title": "Number of training data."},
  "yaxis": {"title": "Accuracy"}
}

fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)


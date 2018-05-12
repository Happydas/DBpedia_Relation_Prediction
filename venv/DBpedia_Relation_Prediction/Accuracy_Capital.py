
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('Happy_Das', 'gqFHrnV4u2yQkUdckBtD')
X, Y = [], []
for line in open('../Results/Main_Capital_Counter_Average.txt', 'r'):
  values = [str(s) for s in line.split()]
  X.append(values[0])
  Y.append(values[1])

data1 = {
  "x": X,
  "y": Y,

  "name": "Accuracy for Country-Capital",
  "type": "scatter"
}


data = Data([data1])
#data = Data([trace1])
layout = {
  "title": "Accuracy against testing data set.",
  "xaxis": {"title": "Number of Vectors."},
  "yaxis": {"title": "Accuracy"}
}

fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)




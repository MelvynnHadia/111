import statistics
from numpy import show_config
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random

data = pd.read_csv("medium_data.csv")
date = data["date"].to_list()
datemean = statistics.mean(date)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_displot([df], ["temp"], show_hist =False)
    fig.show()

random_set_of_mean();
setup();
show_fig();

datedev = statistics.stdev(date)
date_firstdeviation_start, date_firstdeviation_end = datemean - datedev, datemean + datedev
date_seconddeviation_start, date_seconddeviation_end = datemean - (2*datedev), datemean + (2*datedev)
date_thirddeviation_start, date_thirddeviation_end = datemean - (3*datedev), datemean + (3*datedev)
print("std1", date_firstdeviation_start, date_firstdeviation_end)
print("std2", date_seconddeviation_start, date_seconddeviation_end)
print("std3", date_thirddeviation_start, date_thirddeviation_end)

fig = ff.create_displot([mean_list], ["date"], show_hist=False)
fig.add_trace(go.Scatter(x=[datemean, datemean], y =[0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[date_firstdeviation_start, date_firstdeviation_start], y=[0, 0.17], mode="lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[date_firstdeviation_end, date_firstdeviation_end], y=[0, 0.17], mode="lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[date_seconddeviation_start, date_seconddeviation_start], y=[0, 0.17], mode="lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[date_seconddeviation_start, date_seconddeviation_start], y=[0, 0.17], mode="lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[date_thirddeviation_start, date_thirddeviation_start], y=[0, 0.17], mode="lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[date_thirddeviation_start, date_thirddeviation_start], y=[0, 0.17], mode="lines", name = "MEAN"))
fig.show()

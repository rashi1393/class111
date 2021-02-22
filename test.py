import plotly.figure_factory as ff
import plotly.graph_objects as go 
import statistics
import random
import pandas as pd 
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

#plot the graph
#fig = ff.create_distplot([data], ["Math Scores"], show_hist = False)
#fig.show()

#calculating population mean and sd
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("Mean of population: ", mean)
print("Standard deviation of population: ", std_deviation)

#Sampling
#Code to find the mean of 100 data points 1000 times
#func to get the mean of given data samples
#pass the counter of data pints you want as counteer
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean 

#pass the no of times u want the mean of the data points as a parameter in range func in for loop
mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

#calculating mean and sd of sampling dist
sam_sd = statistics.stdev(mean_list)
sam_mean = statistics.mean(mean_list)
print("Mean of sampling dist: ", sam_mean)
print("Standard deviation of sampling dist: ", sam_sd)

#plotting the mean of sampling data
fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[sam_mean, sam_mean], y=[0, 0.20], mode="lines", name="MEAN"))
fig.show()

    
import pandas, statistics as stats, plotly.figure_factory as ff

dataset = pandas.read_csv("data.csv")

data = dataset["math score"].tolist()

mean = stats.mean(data)
median = stats.median(data)
mode = stats.mode(data)
sd = stats.stdev(data)

sd1start, sd1end = mean - sd, mean + sd

sd2start, sd2end = mean - (2*sd), mean + (2*sd)

sd3start, sd3end = mean - (3*sd), mean + (3*sd)

# Calculating how much data is in between STD1, STD2, STD3
list1 = [result for result in data if result > sd1start and result < sd1end]

list2 = [result for result in data if result > sd2start and result < sd2end]

list3 = [result for result in data if result > sd3start and result < sd3end]

print("Mean of dataset is", mean)
print("Median of dataset is", median)
print("Mode of dataset is", mode)
print("Standard Deviation of dataset is", sd)

print("{}% of data lies with in SD1".format(len(list1)*100.0/len(data)))
print("{}% of data lies with in SD2".format(len(list2)*100.0/len(data)))
print("{}% of data lies with in SD3".format(len(list3)*100.0/len(data)))
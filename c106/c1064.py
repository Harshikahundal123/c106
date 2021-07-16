from numpy.lib.stride_tricks import DummyArray
import plotly.express as px
import csv
import numpy as np 

def getDataSource(data_path):
    tv_size = []
    time_spent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tv_size.append(float(row["Tv-Size"]))
            time_spent.append(float(row["Time-Spent"]))
    return{ "x" : tv_size, "y" : time_spent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between the TV size and the Time Spent on the TV", correlation[0,1])
def setup():
    data_path = "timeSpentOnTv.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
setup()
    
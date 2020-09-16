import plotly.figure_factory as ff
import csv
import statistics
import random
import pandas as pd 
import plotly.graph_objects as go

df = pd.read_csv('data10.csv')
data = df['claps'].tolist()
dataSet = []

def randomSetOfMean(counter):
    dataSet2 = []
    for i in range(0 , counter):
      randomIndex = random.randint(0 , len(data) -1)
      value = data[randomIndex]
      dataSet2.append(value)
    mean = statistics.mean(dataSet2)
    return mean

def showFig(meanList):
    df = meanList
    fig = ff.create_distplot([df] , ['claps'] , show_hist = False)
    fig.show()

def setup():
    meanList = []
    for i in range(0 , 100):
        SetOfMean = randomSetOfMean(30)
        meanList.append(SetOfMean)

    showFig(meanList)

setup()

import matplotlib.pyplot as plt
import numpy as np
import random
y_int = 2
slope = 5
points = []

class point:
    def __init__ (self, x, y, classification):
        self.x = x
        self.y = y
        self.classification = classification

#Black - Under, Red - Over
def plot():
    xpoints = np.array([0,100])
    ypoints = np.array([y_int,y_int+(slope * 100)])
    plt.plot(xpoints, ypoints)
    for x in points:
        xpoints = np.array([x.x])
        ypoints = np.array([x.y])
        plt.plot(xpoints,ypoints, "o", color = "red" if x.classification else "black")
    plt.show()
plot()

#Set up network
neuronCount = 2
weights = []
for i in range(20):
    weights.append(random.random(-1.0,1.0))
bias = random.random(-1.0,1.0)

while True:
    inputx=random.random(0,100)
    inputy=random.random(0,100)
    neuronvalues = [inputx, inputy]
    value = 0
    for x in range(neuronCount):
        value += weights[x] * neuronvalues[x] + bias
    above = False
    if(value > 0):
        above = True
    points.append(point(inputx, inputy, above))
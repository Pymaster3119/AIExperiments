import matplotlib.pyplot as plt
import numpy as np
import random
y_int = 2
slope = 5
points = []
batch = 0

class point:
    def __init__ (self, x, y, classification):
        self.x = x
        self.y = y
        self.classification = classification

#Black - Under, Red - Over
def plot():
    global points
    plt.clf()
    for x in points:
        xpoints = np.array([x.x])
        ypoints = np.array([x.y])
        plt.plot(xpoints,ypoints, "o", color = "red" if x.classification else "black")
    xpoints = np.array([0,100])
    ypoints = np.array([y_int,y_int+(slope * 100)])
    points = []
    plt.plot(xpoints, ypoints)
    plt.savefig("FirstPerceptron/ImageOutput/" + str(batch) +'.png')

def save_model():
    global weights, bias
    with (open("FirstPerceptron/ModelSaves/" + str(batch) +'.txt', "w") as txt):
        txt.write(str(bias) + "\n")
        for x in range(len(weights)):
            txt.write(str(weights[x]) + "\n")
#Set up network
neuronCount = 2
weights = []
for i in range(neuronCount):
    weights.append(random.random() * 2 - 1)
bias = random.random() * 2 - 1
learning_rate = 1


for batch in range(100):
    for i in range(1000):
        inputx=random.random() * 100
        inputy=random.random() * 100 * slope
        neuronvalues = [inputx, inputy]
        value = 0
        for x in range(neuronCount):
            value += weights[x] * neuronvalues[x] + bias
        value = min(max(0,round(value)), 1)
        above = False
        if(value > 0.5):
            above = True
        points.append(point(inputx, inputy, above))
        truth = 1 if inputy > (slope * inputx) + y_int else 0
        error = truth - value
        for x in range(neuronCount):
            weights[x] = weights[x] + learning_rate * error * neuronvalues[x]
        bias = bias + learning_rate * error
    plot()
    save_model()
    points = []
    learning_rate = pow(0.9,batch)
    print("Batch " + str(batch) + " Learning Rate " + str(learning_rate))
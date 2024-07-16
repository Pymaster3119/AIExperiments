import matplotlib.pyplot as plt
import numpy as np
import random
y_int = 0
slope = 5
points = []
batch = 0
bestlayer = 0
accuracytobeat = 0

class point:
    def __init__ (self, x, y, classification, truth):
        self.x = x
        self.y = y
        self.classification = classification
        self.truth = truth


def plot():
    global points, accuracytobeat, bestlayer
    truenegatives = 0
    falsenegatives = 0
    truepositives = 0
    falsepositives = 0
    for x in points:
        if (x.classification == True and x.truth == True):
            truepositives += 1
        if (x.classification == False and x.truth == True):
            falsenegatives += 1
        if (x.classification == True and x.truth == False):
            falsepositives += 1
        if (x.classification == False and x.truth == False):
            truenegatives += 1
    accuracy =(truenegatives + truepositives)/len(points)
    if (accuracy > accuracytobeat):
        bestlayer = batch
        accuracytobeat = accuracy
    with (open("LineDetector/ModelStats/" + str(batch) +'.txt', "w") as txt):
        txt.write("True Negatives: " + str(truenegatives) + "\n")
        txt.write("False Negatives: " + str(falsenegatives) + "\n")
        txt.write("True Positives: " + str(truepositives) + "\n")
        txt.write("False Positives: " + str(falsepositives) + "\n")
        txt.write("Accuracy: " + str(accuracy))


def save_model():
    global weights, bias
    with (open("LineDetector/ModelSaves/" + str(batch) +'.txt', "w") as txt):
        txt.write(str(bias) + "\n")
        for x in range(len(weights)):
            txt.write(str(weights[x]) + "\n")
#Set up network
neuronCount = 3
weights = []
for i in range(neuronCount):
    weights.append(random.random() * 2 - 1)
bias = random.random() * 2 - 1
learning_rate = 0.5


for batch in range(100):
    for i in range(1000):
        y_int = random.random() * 20 - 10
        inputx=random.random() * 100
        inputy=random.random() * 100 * slope
        neuronvalues = [inputx, inputy, y_int]
        value = 0
        for x in range(neuronCount):
            value += weights[x] * neuronvalues[x] + bias
        value = min(max(0,round(value)), 1)
        above = False
        if(value > 0.5):
            above = True
        
        truth = 1 if inputy > (slope * inputx) + y_int else 0
        points.append(point(inputx, inputy, above, truth==1))
        error = truth - value
        for x in range(neuronCount):
            weights[x] = weights[x] + learning_rate * error * neuronvalues[x]
        bias = bias + learning_rate * error
    plot()
    save_model()
    points = []
    learning_rate = pow(0.99,batch + 5)
    print("Batch " + str(batch) + " Learning Rate " + str(learning_rate))
print(bestlayer)
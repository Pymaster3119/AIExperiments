import numpy
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
    averageaccuracy = 0
    for x in points:

        if (x.classification[0] > 0.5 and x.truth == True):
            truepositives += 1
        if (x.classification[0] < 0.5 and x.truth == True):
            falsenegatives += 1
        if (x.classification[0] > 0.5 and x.truth == False):
            falsepositives += 1
        if (x.classification[0] < 0.5 and x.truth == False):
            truenegatives += 1
        averageaccuracy += 0.5 * (x.classification - x.truth) ** 2
    accuracy =(truenegatives + truepositives)/len(points)
    averageaccuracy /= len(points)
    if (accuracy > accuracytobeat):
        bestlayer = batch
        accuracytobeat = accuracy

    with (open("FFNNLineDetector/ModelStats/" + str(batch) +'.txt', "w") as txt):
        txt.write("True Negatives: " + str(truenegatives) + "\n")
        txt.write("False Negatives: " + str(falsenegatives) + "\n")
        txt.write("True Positives: " + str(truepositives) + "\n")
        txt.write("False Positives: " + str(falsepositives) + "\n")
        txt.write("Accuracy: " + str(accuracy) + "\n")
        txt.write("Average Accuracy: " + str(averageaccuracy[0]))


def ReLu(val):
    output = numpy.zeros(val.shape[0])
    for x in range(val.shape[0]):
        output[x] = max(min(val[x], 1), 0)
    return output

def relu_derivative(x):
    return numpy.where((x > 0) & (x < 1), 1, 0)
#Set up layers
inputLayerNeuronCount = 4
z1LayerNeuronCount = 10
z2LayerNeuronCount = 10
outputLayerNeuronCount = 1

#Initialize weights
inputLayerToZ1Weights = numpy.random.rand(z1LayerNeuronCount, inputLayerNeuronCount)
z1ToZ2Weights = numpy.random.rand(z2LayerNeuronCount, z1LayerNeuronCount)
z2ToOutputWeights = numpy.random.rand(outputLayerNeuronCount, z2LayerNeuronCount)

#Initialize biases
inputLayerToZ1Biases = numpy.random.rand(z1LayerNeuronCount)
z1ToZ2Biases = numpy.random.rand(z2LayerNeuronCount)
z2ToOutputBiases = numpy.random.rand(outputLayerNeuronCount)

#Training parameters
learning_rate = 0.01
#Mainloop
for batch in range(100):
    points = []
    for d in range(100):
        #Set parameters for current iteration & formulate input layer
        y_int = random.random() * 400 - 200
        slope = random.random() * 20 - 10
        inputx=random.random() * 100
        inputy=random.random() * 100
        inputlayer = numpy.array([y_int, slope, inputx, inputy])

        
        #Run the model - input -> z1
        preactivationZ1 = numpy.dot(inputLayerToZ1Weights, inputlayer)
        preactivationZ1 = numpy.add(preactivationZ1, inputLayerToZ1Biases)
        x1 = ReLu(preactivationZ1)

        #Run the model - z1 -> z2
        preactivationZ2 = numpy.dot(z1ToZ2Weights, x1)
        preactivationZ2 = numpy.add(preactivationZ2, z1ToZ2Biases)
        x2 = ReLu(preactivationZ2)

        #Run the model - z2 -> output
        output = numpy.dot(z2ToOutputWeights, x2)
        output = numpy.add(output, z2ToOutputBiases)

        #Evaluate and save results
        truth = 1 if inputy > (slope * inputx) + y_int else 0
        points.append(point(inputx, inputy, output, truth))
        error = 0.5 * (output[0] - truth) ** 2

        #Storing updated weights as temp vars to make sure that there is no conflict
        #Backwards pass - output -> z2
        lossgradient = (output[0] - truth)
        z2ToOutputWeightsTemp = numpy.subtract(z2ToOutputWeights, learning_rate * lossgradient * ReLu(preactivationZ2))
        z2ToOutputBiasesTemp = numpy.subtract(z2ToOutputBiases, learning_rate * lossgradient)

        #Backwards pass - z2 -> z1
        gradientz2 = numpy.dot(lossgradient, z2ToOutputWeights) * relu_derivative(preactivationZ2)
        z2delta = numpy.dot(lossgradient, z2ToOutputWeights.T) * relu_derivative(preactivationZ2)
        z1ToZ2WeightsChange = numpy.dot(z2delta,x1)
        z1ToZ2BiasChange = numpy.dot(lossgradient, z2ToOutputWeights.T) * relu_derivative(preactivationZ2)
        z1ToZ2WeightsTemp = numpy.subtract(z1ToZ2Weights, learning_rate * z1ToZ2WeightsChange)
        z1ToZ2BiasesTemp = numpy.subtract(z1ToZ2Biases, learning_rate * z1ToZ2BiasChange)

        #Backwards pass - input -> z1
        
        inputLayerToZ1WeightsChange = numpy.dot(z1ToZ2Weights.T, numpy.dot(lossgradient, z2ToOutputWeights.T) * relu_derivative(preactivationZ2)) * relu_derivative(preactivationZ1)
        inputLayerToZ1WeightsDelta = numpy.dot(inputLayerToZ1WeightsChange, inputlayer.T)
        inputLayerToZ1BiasesDelta = numpy.sum(inputlayer, axis=1, keepdims=True)
        inputLayerToZ1WeightsTemp = numpy.subtract(inputLayerToZ1Weights, learning_rate * inputLayerToZ1WeightsDelta)
        inputLayerToZ1BiasesTemp = numpy.subtract(inputLayerToZ1Biases, learning_rate * inputLayerToZ1BiasesDelta)

        #Update weights - replace the weights + biases with the temporary ones calculated
        inputLayerToZ1Weights = inputLayerToZ1WeightsTemp
        inputLayerToZ1Biases = inputLayerToZ1BiasesTemp
        z1ToZ2Weights = z1ToZ2WeightsTemp
        z1ToZ2Biases = z1ToZ2BiasesTemp
        z2ToOutputWeights = z2ToOutputWeightsTemp
        z2ToOutputBiases = z2ToOutputBiasesTemp

        
    print("Batch " + str(batch) + " done!")
    plot()
print(bestlayer)
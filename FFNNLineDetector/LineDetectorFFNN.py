import numpy
import random
y_int = 0
slope = 5
points = []
batch = 0
bestlayer = 0
accuracytobeat = 10000000000000000000

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

        if (x.classification[0,0] > 0.5 and x.truth == True):
            truepositives += 1
        if (x.classification[0,0] < 0.5 and x.truth == True):
            falsenegatives += 1
        if (x.classification[0,0] > 0.5 and x.truth == False):
            falsepositives += 1
        if (x.classification[0,0] < 0.5 and x.truth == False):
            truenegatives += 1
        averageaccuracy += (x.classification[0,0] - x.truth) ** 2
    accuracy =(truenegatives + truepositives)/len(points)
    averageaccuracy /= len(points)
    if (averageaccuracy < accuracytobeat):
        bestlayer = batch
        accuracytobeat = averageaccuracy

    with (open("FFNNLineDetector/ModelStats/" + str(batch) +'.txt', "w") as txt):
        txt.write("True Negatives: " + str(truenegatives) + "\n")
        txt.write("False Negatives: " + str(falsenegatives) + "\n")
        txt.write("True Positives: " + str(truepositives) + "\n")
        txt.write("False Positives: " + str(falsepositives) + "\n")
        txt.write("Accuracy: " + str(accuracy) + "\n")
        txt.write("Average Accuracy: " + str(averageaccuracy))


def ReLu(val):
    return 1 / (1 + numpy.exp(-val))

def relu_derivative(x):
    sig = ReLu(x)
    return sig * (1 - sig)

def save_model():
    global inputLayerToZ1Weights, z1ToZ2Weights, z2ToOutputWeights, inputLayerToZ1Biases, z1ToZ2Biases, z2ToOutputBiases, batch
    numpy.save("FFNNLineDetector/ModelSaves/" + str(batch) + " inputToZ1Weights.npy", inputLayerToZ1Weights)
    numpy.save("FFNNLineDetector/ModelSaves/" + str(batch) + " z1ToZ2Weights.npy", z1ToZ2Weights)
    numpy.save("FFNNLineDetector/ModelSaves/" + str(batch) + " z2ToOutputWeights.npy", z2ToOutputWeights)
    numpy.save("FFNNLineDetector/ModelSaves/" + str(batch) + " inputToZ1Biases.npy", inputLayerToZ1Biases)
    numpy.save("FFNNLineDetector/ModelSaves/" + str(batch) + " z1ToZ2Biases.npy", z1ToZ2Biases)
    numpy.save("FFNNLineDetector/ModelSaves/" + str(batch) + " z2ToOutputBiases.npy", z2ToOutputBiases)
#Set up layers
inputLayerNeuronCount = 4
z1LayerNeuronCount = 5
z2LayerNeuronCount = 3
outputLayerNeuronCount = 1

#Initialize weights
inputLayerToZ1Weights = numpy.random.rand(z1LayerNeuronCount, inputLayerNeuronCount)
z1ToZ2Weights = numpy.random.rand(z2LayerNeuronCount, z1LayerNeuronCount)
z2ToOutputWeights = numpy.random.rand(outputLayerNeuronCount, z2LayerNeuronCount)

#Initialize biases
inputLayerToZ1Biases = numpy.random.rand(z1LayerNeuronCount,1)
z1ToZ2Biases = numpy.random.rand(z2LayerNeuronCount,1)
z2ToOutputBiases = numpy.random.rand(outputLayerNeuronCount,1)

#Training parameters
learning_rate = 0.001
#Mainloop
for batch in range(5000):
    points = []
    for d in range(100000):
        #Set parameters for current iteration & formulate input layer
        y_int = random.random() * 400 - 200
        slope = random.randint(0,20)
        inputx=random.random() * 100
        inputy=random.random() * 100
        inputlayer = numpy.array([[y_int], [slope], [inputx], [inputy]])

        
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
        error = (output[0, 0] - truth)

        #Storing updated weights as temp vars to make sure that there is no conflict
        #Backwards pass - output -> z2
        lossgradient = 2 * (output[0, 0] - truth)
        z2ToOutputWeightsTemp = z2ToOutputWeights - learning_rate * lossgradient * x2.T
        z2ToOutputBiasesTemp = z2ToOutputBiases - learning_rate * lossgradient

        #Backwards pass - z2 -> z1
        gradientz2 = lossgradient * z2ToOutputWeights.T * relu_derivative(preactivationZ2)
        z1ToZ2WeightsTemp = z1ToZ2Weights - learning_rate * numpy.dot(gradientz2, x1.T) 
        z1ToZ2BiasesTemp = z1ToZ2Biases - learning_rate * gradientz2
        

        #Backwards pass - input -> z1
        gradientz1 = numpy.dot(z1ToZ2Weights.T, gradientz2) * relu_derivative(preactivationZ1)
        inputLayerToZ1WeightsTemp = inputLayerToZ1Weights - learning_rate * numpy.dot(gradientz1, inputlayer.T)
        inputLayerToZ1BiasesTemp = inputLayerToZ1Biases - learning_rate * gradientz1

        #Update weights - replace the weights + biases with the temporary ones calculated
        inputLayerToZ1Weights = inputLayerToZ1WeightsTemp
        inputLayerToZ1Biases = inputLayerToZ1BiasesTemp
        z1ToZ2Weights = z1ToZ2WeightsTemp
        z1ToZ2Biases = z1ToZ2BiasesTemp
        z2ToOutputWeights = z2ToOutputWeightsTemp
        z2ToOutputBiases = z2ToOutputBiasesTemp

        
    print("Batch " + str(batch) + " done!")
    save_model()
    plot()
print(bestlayer)
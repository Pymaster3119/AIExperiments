import tkinter
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
main = tkinter.Tk()
frame = tkinter.Frame(main)
frame.pack()
yint = tkinter.IntVar(frame)
slope = tkinter.IntVar(frame)
slider = tkinter.Scale(frame, variable=yint, from_=-200, to=200, orient="horizontal", label="y-intercept")
slider.grid(row=1, column=0)
tkinter.Scale(frame, variable=slope, from_=-10, to=10, orient="horizontal", label= "slope").grid(row=2, column=0)
selected = tkinter.StringVar(frame)
options = [x for x in range(1000)]
dropdown = tkinter.OptionMenu(frame, selected, *options)
dropdown.grid(row=1, column=1)
canvas = tkinter.Canvas(frame, width=1000, height=1000)
canvas.grid(row=0, column=0, columnspan=2)
button = tkinter.Button(frame, text="Make a large batch", command= lambda :create_points(1000,runDraw=True))
button.grid(row=1, column=2)
points = []
class point:
    def __init__ (self, x, y, classification):
        self.x = x
        self.y = y
        self.classification = classification

def ReLu(val):
    return np.maximum(0, np.minimum(1, val))

def create_points(numPoints, runDraw = False):
    #Import the model
    inputLayerToZ1Weights = np.loadtxt("FFNNLineDetector/ModelSaves/" + selected.get() + " inputToZ1Weights.txt")
    z1ToZ2Weights = np.loadtxt("FFNNLineDetector/ModelSaves/" + selected.get() + " z1ToZ2Weights.txt")
    z2ToOutputWeights = np.loadtxt("FFNNLineDetector/ModelSaves/" + selected.get() + " z2ToOutputWeights.txt")
    inputLayerToZ1Biases = np.loadtxt("FFNNLineDetector/ModelSaves/" + selected.get() + " inputToZ1Biases.txt")
    z1ToZ2Biases = np.loadtxt("FFNNLineDetector/ModelSaves/" + selected.get() + " z1ToZ2Biases.txt")
    z2ToOutputBiases = np.loadtxt("FFNNLineDetector/ModelSaves/" + selected.get() + " z2ToOutputBiases.txt")

    #Create the points & run FFNN on all of them
    for x in range(numPoints):
        inputx=random.random() * 100
        inputy=random.random() * 100
        inputLayer = np.array([[yint.get()], [slope.get()], [inputx], [inputy]])

        #Run the model - input -> z1
        preactivationZ1 = np.dot(inputLayerToZ1Weights, inputLayer)
        preactivationZ1 = np.add(preactivationZ1, inputLayerToZ1Biases)
        x1 = ReLu(preactivationZ1)

        #Run the model - z1 -> z2
        preactivationZ2 = np.dot(z1ToZ2Weights, x1)
        preactivationZ2 = np.add(preactivationZ2, z1ToZ2Biases)
        x2 = ReLu(preactivationZ2)

        #Run the model - z2 -> output
        output = np.dot(z2ToOutputWeights, x2)
        output = np.add(output, z2ToOutputBiases)
        
        #Save point
        points.append(point(inputx, inputy, (output-0.5) * 2))

    if runDraw:
        draw(0, 0, "FLAG")

def draw(a,b,c):
    global draw, selected, yint,points, canvas
    fig = Figure(figsize = (5, 5), dpi = 100)
    axes1 = fig.add_axes([0.1,0.1,0.9,0.9])
    axes1.set_ylim(0, 100)
    axes1.set_xlim(0, 100)
    if (c != "FLAG"):
        create_points(100, False)
    plt.clf()
    for x in points:
        if(x.classification[0] > 0):
            axes1.plot(x.x, x.y, "o",color="Blue")
        if(x.classification[0] <= 0):
            axes1.plot(x.x, x.y, "o",color="Green")
    xpoints = np.array([0,100])
    ypoints = np.array([yint.get(),yint.get()+(slope.get() * 100)])
    points = []
    axes1.plot(xpoints, ypoints)
    canvas = FigureCanvasTkAgg(fig,  master = frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)
selected.trace_add("write", draw)
yint.trace_add("write", draw)
slope.trace_add("write", draw)
selected.set("0")
main.mainloop()
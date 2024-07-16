import tkinter
import matplotlib.pyplot as plt
import numpy as np
import random
main = tkinter.Tk()
frame = tkinter.Frame(main)
frame.pack()
yint = tkinter.IntVar(frame)
slider = tkinter.Scale(frame, variable=yint, from_=-10, to=10, orient="horizontal")
slider.grid(row=1, column=0)
selected = tkinter.StringVar(frame)
options = [x for x in range(100)]
dropdown = tkinter.OptionMenu(frame, selected, *options)
dropdown.grid(row=1, column=1)
canvas = tkinter.Canvas(frame, width=1000, height=1000)
canvas.grid(row=0, column=0)
points = []
class point:
    def __init__ (self, x, y, classification):
        self.x = x
        self.y = y
        self.classification = classification
def create_points(numPoints):
    for x in range(numPoints):
        inputx=random.random() * 100
        inputy=random.random() * 500
        neuronvalues = [inputx, inputy, yint.get()]
        weights = []
        bias = 0
        with (open("LineDetector/ModelSaves/" + selected.get() +'.txt', "r") as txt):
            bias = float(txt.readline())
            for i in range(3):
                weights.append(float(txt.readline()))
        value = 0
        for x in range(3):
            value += weights[x] * neuronvalues[x] + bias
        value = min(max(0,round(value)), 1)
        above = False
        if(value > 0.5):
            above = True
        truth = 1 if inputy > (5 * inputx) + yint.get() else 0
        points.append(point(inputx, inputy, above))
def draw(a,b,c):
    global draw, selected, yint,points
    create_points(1000)
    plt.clf()
    for x in points:
        xpoints = np.array([x.x])
        ypoints = np.array([x.y])
        plt.plot(xpoints,ypoints, "o", color = "red" if x.classification else "black")
    xpoints = np.array([0,100])
    ypoints = np.array([yint.get(),yint.get()+(5 * 100)])
    points = []
    plt.plot(xpoints, ypoints)
    plt.show()
selected.trace_add("write", draw)
selected.set("0")
main.mainloop()
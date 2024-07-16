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
slider = tkinter.Scale(frame, variable=yint, from_=-200, to=200, orient="horizontal")
slider.grid(row=1, column=0)
selected = tkinter.StringVar(frame)
options = [x for x in range(100)]
dropdown = tkinter.OptionMenu(frame, selected, *options)
dropdown.grid(row=1, column=1)
canvas = tkinter.Canvas(frame, width=1000, height=1000)
canvas.grid(row=0, column=0, columnspan=2)
button = tkinter.Button(frame, text="Make a large batch", command= lambda :create_points(1000))
button.grid(row=1, column=2)
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
        value = min(max(0,value), 1)
        points.append(point(inputx, inputy, (value-0.5) * 2))
def lerp(c2, time):
    r = int(c2[0] * (time))
    g = int(c2[1] * (time))
    b = int(c2[2] * (time))
    return '#{:02x}{:02x}{:02x}'.format(r, g, b).capitalize()
def draw(a,b,c):
    global draw, selected, yint,points, canvas
    fig = Figure(figsize = (5, 5), dpi = 100)
    axes1 = fig.add_axes([0.1,0.1,0.9,0.9])
    axes1.set_ylim(0, 500)
    axes1.set_xlim(0, 100)
    create_points(100)
    plt.clf()
    for x in points:
        if(x.classification > 0):
            color = lerp((0,255,0), x.classification)
            axes1.plot(x.x, x.y, "o",color=color)
        if(x.classification <= 0):
            color = lerp((0,0,255), -x.classification)
            axes1.plot(x.x, x.y, "o",color=color)
    xpoints = np.array([0,100])
    ypoints = np.array([yint.get(),yint.get()+(5 * 100)])
    points = []
    axes1.plot(xpoints, ypoints)
    canvas = FigureCanvasTkAgg(fig,  master = frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)
selected.trace_add("write", draw)
yint.trace_add("write", draw)
selected.set("0")
main.mainloop()
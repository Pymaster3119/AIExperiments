import tkinter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

main = tkinter.Tk()
frame = tkinter.Frame(main)
frame.pack()
canvas = tkinter.Canvas(frame)
canvas.grid(row=0, column=0)
function = tkinter.StringVar(main)
function.set("f(x,y): ")
tkinter.Entry(frame, textvariable=function).grid(row=1, column=0)
tkinter.Button(frame, command= lambda: plot_function(function.get()), text="Plot function!").grid(row=2, column=0)
def plot_function(functionstr):
    global canvas
    functionstr = functionstr.replace("^", "**").replace("f(x,y):","")
    x = np.linspace(-100, 100, 200)
    y = np.linspace(-100, 100, 200)
    x, y = np.meshgrid(x, y)
    z = eval(functionstr)

    fig = plt.figure(figsize=(10, 8))
    axes1 = fig.add_axes([0.1,0.1,0.9,0.9])
    axes1.set_ylim(-100,100)
    axes1.set_xlim(-100,100)

    maxheight = z.max().item()
    minheight = z.min().item()
    contourHeights = np.linspace(minheight,maxheight, 40)
    print(contourHeights)
    for i in range(-100, 101):
        for j in range(-100, 101):
            x = i
            y = j
            height = eval(functionstr)
            plot = False
            for k in contourHeights:
                if abs(height-k) <= 1:
                    plot = True
            if plot:
                color = round((height-minheight)*(255)/(maxheight-minheight))
                color = '#%02x%02x%02x' % (color, color, color)
                axes1.plot(i, j, "o", color = color)
    canvas = FigureCanvasTkAgg(fig,  master = frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)

main.mainloop()
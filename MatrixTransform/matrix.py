import tkinter
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 
import numpy
root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()
canvas = tkinter.Canvas(frame,width=1000, height=1000)
canvas.grid(row=0, column=0)
points = []
def generate_square_points():
    global points

    # Generate points for the bottom side of the square
    for x in range(20,31):
        points.append((x, 20))

    # Generate points for the right side of the square
    for y in range(20,31):
        points.append((30, y))

    # Generate points for the top side of the square
    for x in range(30, 19, -1):
        points.append((x, 30))

    # Generate points for the left side of the square
    for y in range(30,19, -1):
        points.append((20, y))

def create_visualizer():
    global canvas, points, matrixa, matrixb, matrixc, matrixd, graphFrom, graphTo
    print(len(points))
    fig = Figure(figsize = (5, 5), dpi = 100)
    axes1 = fig.add_axes([0.1,0.1,0.9,0.9])
    axes1.set_ylim(int(graphFrom.get()), int(graphTo.get()))
    axes1.set_xlim(int(graphFrom.get()), int(graphTo.get()))
    #Draw axes
    for x in range(-100 + round(axes1.get_ylim()[0]), 100 +round(axes1.get_ylim()[1])):
        start = [x,-100]
        start = [start[0] * float(matrixa.get()) + start[1] * float(matrixb.get()), start[0] * float(matrixc.get()) + start[1] * float(matrixd.get())]
        end = [x, 100]
        end = [end[0] * float(matrixa.get()) + end[1] * float(matrixb.get()), end[0] * float(matrixc.get()) + end[1] * float(matrixd.get())]
        xpoints = numpy.array([start[0],end[0]])
        ypoints = numpy.array([start[1],end[1]])
        axes1.plot(xpoints, ypoints, color = "gray")
    for y in range(-100, 100):
        start = [-100,y]
        start = [start[0] * float(matrixa.get()) + start[1] * float(matrixb.get()), start[0] * float(matrixc.get()) + start[1] * float(matrixd.get())]
        end = [100,y]
        end = [end[0] * float(matrixa.get()) + end[1] * float(matrixb.get()), end[0] * float(matrixc.get()) + end[1] * float(matrixd.get())]
        xpoints = numpy.array([start[0],end[0]])
        ypoints = numpy.array([start[1],end[1]])
        axes1.plot(xpoints, ypoints, color = "blue")
    #Draw each point
    for p in points:
        point = [p[0],p[1]]
        point = [point[0] * float(matrixa.get()) + point[1] * float(matrixb.get()), point[0] * float(matrixc.get()) + point[1] * float(matrixd.get())]
        xpoints = numpy.array([point[0]])
        ypoints = numpy.array([point[1]])
        axes1.plot(xpoints, ypoints, "o", color = "red")
    canvas = FigureCanvasTkAgg(fig,  master = frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)
def create_point():
    global points, pointx, pointy
    points.append((float(pointx.get()),float(pointy.get())))

matrixa = tkinter.StringVar(frame, "1")
matrixb = tkinter.StringVar(frame, "0")
matrixc = tkinter.StringVar(frame, "0")
matrixd = tkinter.StringVar(frame, "1")
tkinter.Entry(frame, textvariable=matrixa).grid(row=1,column=0)
tkinter.Entry(frame, textvariable=matrixb).grid(row=1,column=1)
tkinter.Entry(frame, textvariable=matrixc).grid(row=2,column=0)
tkinter.Entry(frame, textvariable=matrixd).grid(row=2,column=1)
tkinter.Button(frame, text="Create plot", command=create_visualizer).grid(row=3, column=0)
tkinter.Button(frame, text="Create square", command=generate_square_points).grid(row = 3, column=1)
pointx = tkinter.StringVar(frame)
pointy = tkinter.StringVar(frame)
tkinter.Entry(frame, textvariable=pointx).grid(row=4, column=0)
tkinter.Entry(frame, textvariable=pointy).grid(row=4, column=1)
tkinter.Button(frame, text="create point", command=create_point).grid(row=5, column=0)
graphFrom = tkinter.StringVar(frame, "0")
graphTo = tkinter.StringVar(frame, "50")
tkinter.Label(frame, text = "Graph from").grid(row=6, column=0)
tkinter.Label(frame, text = "Graph to").grid(row=6, column=1)
tkinter.Entry(frame, textvariable=graphFrom).grid(row=7, column=0)
tkinter.Entry(frame, textvariable=graphTo).grid(row=7, column=1)
create_visualizer()
root.mainloop()
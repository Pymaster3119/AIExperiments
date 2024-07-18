import tkinter
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 
from matplotlib.image import imread
import numpy
from tkinter.filedialog import askopenfilename
root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()
canvas = tkinter.Canvas(frame,width=300, height=300)
canvas.grid(row=0, column=0)
points = []
def generate_square_points():
    global points, status
    status.set("Status: creating square...")
    for x in range(20,31):
        points.append((x, 20))
    for y in range(20,31):
        points.append((30, y))
    for x in range(30, 19, -1):
        points.append((x, 30))
    for y in range(30,19, -1):
        points.append((20, y))
    status.set("Status: idle")
def generate_triangle_points():
    global points, status
    status.set("Status: creating square...")
    for x in range(20,31):
        points.append((x, 20))
    for y in range(20,31):
        points.append((30 - ((y-20)/2), y))
    for y in range(30,19, -1):
        points.append((20 + ((y-20)/2), y))
    status.set("Status: idle")

def generate_plus_points():
    global points, status
    status.set("Status: creating square...")
    for x in range(20,31):
        points.append((x, 25))
    for y in range(20,31):
        points.append((25, y))
    status.set("Status: idle")

def create_visualizer():
    global canvas, points, matrixa, matrixb, matrixc, matrixd, graphFrom, graphTo, status
    status.set("Status: drawing plots...")
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
        if(len(p) != 2):
            axes1.plot(xpoints, ypoints, "o", color = p[2])
        else:
            axes1.plot(xpoints, ypoints, "o", color = "red")
    canvas = FigureCanvasTkAgg(fig,  master = frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)
    status.set("Status: idle")
def create_point():
    global points, pointx, pointy, status
    points.append((float(pointx.get()),float(pointy.get())))
def import_image():
    global points, imageFromX, imageToX, imageFromY, imageToY, status
    status.set("Status: importing image...")
    filename = askopenfilename(filetypes=[("JPG", "*.jpg")])
    image = imread(filename)
    deltaX = float(imageToX.get()) - float(imageFromX.get())
    deltaY = float(imageToY.get()) - float(imageFromY.get())

    prevx = float('inf')
    prevy = float('-inf')
    xcount = 0
    ycount = 0
    for i in range(image.shape[0]):
        x = float(imageToX.get())-(i / image.shape[0]) * deltaX 
        if (abs(prevx-x) > 0.1):
            prevx = x
            xcount+= 1
            prevy = float('-inf')
            ycount = 0
            for j in range(image.shape[1]):
                y = (j / image.shape[1]) * deltaY + float(imageFromY.get())
                if (y - prevy > 0.1):
                    prevy = y
                    ycount += 1
                    r, g, b = image[i][j][:3] / 255.0
                    points.append((y, x, (r, g, b)))
    status.set("Status: idle")
            
    
def delete_points():
    points = []
matrixa = tkinter.StringVar(frame, "1")
matrixb = tkinter.StringVar(frame, "0")
matrixc = tkinter.StringVar(frame, "0")
matrixd = tkinter.StringVar(frame, "1")
status = tkinter.StringVar(root, "Status: idle")
tkinter.Entry(frame, textvariable=matrixa).grid(row=1,column=0)
tkinter.Entry(frame, textvariable=matrixb).grid(row=1,column=1)
tkinter.Entry(frame, textvariable=matrixc).grid(row=2,column=0)
tkinter.Entry(frame, textvariable=matrixd).grid(row=2,column=1)
tkinter.Button(frame, text="Create plot", command=lambda:root.after(1, create_visualizer)).grid(row=3, column=0)
tkinter.Button(frame, text="Create square", command=lambda:root.after(1, generate_square_points)).grid(row = 3, column=1)
tkinter.Button(frame, text="Create triangle", command=lambda:root.after(1, generate_triangle_points)).grid(row = 4, column=0)
tkinter.Button(frame, text="Create plus", command=lambda:root.after(1, generate_plus_points)).grid(row = 4, column=1)
pointx = tkinter.StringVar(frame)
pointy = tkinter.StringVar(frame)
tkinter.Label(frame, text = "Point X").grid(row=5, column=0)
tkinter.Label(frame, text = "Point Y").grid(row=5, column=1)
tkinter.Entry(frame, textvariable=pointx).grid(row=6, column=0)
tkinter.Entry(frame, textvariable=pointy).grid(row=6, column=1)
tkinter.Button(frame, text="create point", command=lambda:root.after(1, create_point)).grid(row=7, column=0)
graphFrom = tkinter.StringVar(frame, "0")
graphTo = tkinter.StringVar(frame, "50")
tkinter.Label(frame, text = "Graph from").grid(row=8, column=0)
tkinter.Label(frame, text = "Graph to").grid(row=8, column=1)
tkinter.Entry(frame, textvariable=graphFrom).grid(row=9, column=0)
tkinter.Entry(frame, textvariable=graphTo).grid(row=9, column=1)
imageFromX = tkinter.StringVar(frame, "0")
imageToX = tkinter.StringVar(frame, "50")
imageFromY = tkinter.StringVar(frame, "0")
imageToY = tkinter.StringVar(frame, "50")
tkinter.Label(frame, text = "Image from (x,y)").grid(row=10, column=0)
tkinter.Label(frame, text = "Image to (x,y)").grid(row=10, column=1)
tkinter.Entry(frame, textvariable=imageFromY).grid(row=11, column=0)
tkinter.Entry(frame, textvariable=imageToY).grid(row=11, column=1)
tkinter.Entry(frame, textvariable=imageFromX).grid(row=12, column=0)
tkinter.Entry(frame, textvariable=imageToX).grid(row=12, column=1)
tkinter.Button(frame, text= "import image", command=lambda:root.after(1, import_image)).grid(row=13, column=0)
tkinter.Button(frame, text= "delete all points", command=lambda:root.after(1, delete_points)).grid(row=13, column=1)
#tkinter.Label(frame, textvariable=status).grid(row=0, column=1)
create_visualizer()
root.mainloop()
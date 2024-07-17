import tkinter as tk
import random
points = []
def draw_point(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill='red')
    points.append((x,y))

def generate_points():
    global points
    delete_points()
    for i in range(500):
        x = random.randint(0,500)
        y = random.randint(0,500)
        canvas.create_oval(x-2, y-2, x+2, y+2, fill='red')
        points.append((x,y))
def delete_points():
    points = []
    canvas.delete("all")
def run_kmeans_clustering():
    print("TODO: Write code here")
root = tk.Tk()
root.title("Point Drawer")

canvas = tk.Canvas(root, width=500, height=500, bg='white')
canvas.pack()

canvas.bind("<Button-1>", draw_point)
generatePoints = tk.Button(root, text="Generate 100 points", command= generate_points)
generatePoints.pack()
deletePoints = tk.Button(root, text="Delete Points", command= delete_points)
deletePoints.pack()
kvalue = tk.StringVar(root, "Set K-Value (integers only)")
kinput = tk.Entry(root, textvariable=kvalue)
kinput.pack()
algorithmstart = tk.Button(root, text="Run K-Means Clustering", command=run_kmeans_clustering)
algorithmstart.pack()
root.mainloop()

import tkinter as tk
import random
#Pulled from Stack Overflow - Thank you!
colors  =[]
with(open("K-MeansClustering/colors.txt", "r") as txt):
    colors = txt.readlines()
random.shuffle(colors)
points = []
def draw_point(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill='black')
    points.append((x,y))

def generate_points():
    global points
    delete_points()
    for i in range(500):
        x = random.randint(0,500)
        y = random.randint(0,500)
        canvas.create_oval(x-2, y-2, x+2, y+2, fill='black')
        points.append((x,y))
def delete_points():
    global points
    points = []
    canvas.delete("all")
def run_kmeans_clustering():
    global kvalue
    clusterPoints = []
    nearpoints = []
    for i in range(int(kvalue.get())):
        x = random.randint(0,500)
        y = random.randint(0,500)
        clusterPoints.append((x,y))

    num_iterations = 100
    for i in range(num_iterations):
        #Find the nearest points
        nearpoints = []
        for j in range(len(clusterPoints)):
            nearpoints.append([])
        for j in points:
            nearestclusterpoint = -1
            nearestsquaredistance = 10000000
            for k in clusterPoints:
                squaredistance = (k[0] - j[0]) ** 2 + (k[1] - j[1]) ** 2
                if (squaredistance < nearestsquaredistance):
                    nearestsquaredistance = squaredistance
                    nearestclusterpoint = clusterPoints.index(k)
            nearpoints[nearestclusterpoint].append(points.index(j))
        
        #Calculating averages
        for i in clusterPoints:
            averageX = 0
            averageY = 0
            for j in nearpoints[clusterPoints.index(i)]:
                averageX += points[j][0]
                averageY += points[j][1]
            if(len(nearpoints[clusterPoints.index(i)]) != 0):
                averageX /= len(nearpoints[clusterPoints.index(i)])
                averageY /= len(nearpoints[clusterPoints.index(i)])
            else:
                #Try again randomly because there is nothing here
                averageX = random.randint(0,500)
                averageY = random.randint(0,500)
            clusterPoints[clusterPoints.index(i)]=(averageX, averageY)

        #Plot the centroids and points
        canvas.delete("all")
        for i in clusterPoints:
            x, y = i
            canvas.create_oval(x-10, y-10, x+10, y+10, fill=colors[clusterPoints.index(i)].strip())
        for i in points:
            x, y = i
            for j in nearpoints:
                if points.index(i) in j:
                    canvas.create_oval(x-2, y-2, x+2, y+2, fill=colors[nearpoints.index(j)].strip())



root = tk.Tk()
root.title("K-Means Clustering - Lloyd's Algorythm")

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
shufflecolors = tk.Button(root, text= "Shuffle colors", command=lambda: random.shuffle(colors))
shufflecolors.pack()
root.mainloop()

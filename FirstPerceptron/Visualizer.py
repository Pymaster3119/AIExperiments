import tkinter
from PIL import Image, ImageTk
root = tkinter.Tk()
root.title("Perceptron Visualizer")
frame = tkinter.Frame(root)
frame.pack()

canvas = tkinter.Canvas(frame,width=500, height=200)
canvas.grid(row = 0, column=0)
canvas2 = tkinter.Canvas(frame, width=900, height=500)
canvas2.grid(row = 1, column=0)

selected = tkinter.StringVar()

def draw(x,y,z):
    global canvas, canvas2
    canvas.delete("all")
    #Make the connections to the output
    canvas.create_line(50,66,150,100)
    canvas.create_line(50,132,150,100)
    canvas.create_line(150,100, 350,100)

    #Draw the inputs/outputs
    canvas.create_oval(25,41,75,91, fill = "blue")
    canvas.create_oval(25,107,75,157, fill = "blue")
    canvas.create_oval(125,75,175,125, fill= "blue")
    canvas.create_oval(325,75,375,125, fill= "blue")

    #Draw the annotation
    with (open("FirstPerceptron/ModelSaves/" + selected.get() + ".txt", "r") as txt):
        bias = str(round(float(txt.readline()) * 100)/100)
        weight1 = str(round(float(txt.readline()) * 100)/100)
        weight2 = str(round(float(txt.readline()) * 100)/100)
        equation = f"Z = ({weight1})(x-coordinate)\n + ({weight2})(y-coordinate)\n + {bias}"
        canvas.create_text(200,150, text=equation)
    canvas.create_text(350, 65, text="ŷ = min(max(round(Z),0),1)")
    #Draw the appropriate image
    img = ImageTk.PhotoImage(Image.open("FirstPerceptron/ImageOutput/" + selected.get() +'.png'))
    root.img = img
    canvas2.create_image(10,10,image = img, anchor = "nw")

options = [x for x in range(100)]
dropdown = tkinter.OptionMenu(frame, selected, *options)
dropdown.grid(row=0, column=1)
selected.trace_add("write", draw)
selected.set("0")
root.mainloop()
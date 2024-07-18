import tkinter
root = tkinter.Tk()

frame = tkinter.Frame(root)
frame.pack()
h = tkinter.Scrollbar(frame, orient = 'horizontal')
h.pack(side = tkinter.BOTTOM, fill = "y")
matrix1 = []
matrix2 = []
outputmatrix = []
#First window - asking for matrix size
def draw_first_window():
    global frame, matrix1width, matrix1height, matrix2width, matrix2height
    for child in frame.winfo_children():
        child.destroy()
    tkinter.Label(frame, text= "What should matrix 1 be?").grid(row = 0, column=0)
    tkinter.Entry(frame, textvariable=matrix1width).grid(row=1, column=0)
    tkinter.Entry(frame, textvariable=matrix1height).grid(row=1, column=2)
    tkinter.Label(frame, text= "What should matrix 2 be?").grid(row = 2, column=0)
    tkinter.Entry(frame, textvariable=matrix2width).grid(row=3, column=0)
    tkinter.Entry(frame, textvariable=matrix2height).grid(row=3, column=2)
    tkinter.Button(frame, command=draw_second_window,text="Create matrices and assign values").grid(row=4, column=0)

def draw_second_window(regenVars = True):
    global matrix1, matrix2
    for child in frame.winfo_children():
        child.destroy()
   

    tkinter.Label(frame, text="Matrix 1:").grid(row=0, column=0)
    for j in range(int(matrix1height.get())):
        if regenVars:
            matrix1.append([])
        for i in range(int(matrix1width.get())):
            if regenVars:
                matrix1[j].append(tkinter.StringVar())
            tkinter.Entry(frame, textvariable=matrix1[j][i]).grid(row = i + 1, column= j)
    tkinter.Label(frame, text="Matrix 2:").grid(row=int(matrix1width.get()) + 1, column=0)
    for j in range(int(matrix2height.get())):
        if regenVars:
            matrix2.append([])
        for i in range(int(matrix2width.get())):
            if regenVars:
                matrix2[j].append(tkinter.StringVar())
            tkinter.Entry(frame, textvariable=matrix2[j][i]).grid(row = i + int(matrix1width.get()) + 2, column= j)
    tkinter.Button(frame, text="Add Matrices", command=add).grid(row =  int(matrix2width.get()) + int(matrix1width.get()) + 3, column=0)
    tkinter.Button(frame, text="Subtract Matrices", command=subtract).grid(row =  int(matrix2width.get()) + int(matrix1width.get()) + 3, column=1)
    tkinter.Button(frame, text="Multiply Matrices", command=multiply).grid(row =  int(matrix2width.get()) + int(matrix1width.get()) + 3, column=2)
    tkinter.Button(frame, text="Transpose of Matrix 1", command=transpose).grid(row =  int(matrix2width.get()) + int(matrix1width.get()) + 3, column=3)
    tkinter.Button(frame, text="Reset Matreces", command=draw_first_window).grid(row =  int(matrix2width.get()) + int(matrix1width.get()) + 3, column=4)
    tkinter.Label(frame, text="Output:").grid(row =  int(matrix2width.get()) + int(matrix1width.get()) + 4, column=0)
    for j in range(len(outputmatrix)):
        for i in range(len(outputmatrix[j])):
            tkinter.Label(frame, textvariable=outputmatrix[j][i]).grid(row = i + int(matrix2width.get()) + int(matrix1width.get()) + 6, column= j)
def add():
    global outputmatrix
    outputmatrix = []
    if (int(matrix1width.get())==int(matrix2width.get())) and (int(matrix1height.get())==int(matrix2height.get())):
        for i in matrix1:
            outputmatrix.append([])
            for j in i:
                outputmatrix[matrix1.index(i)].append(tkinter.StringVar())
                outputmatrix[matrix1.index(i)][i.index(j)].set(str(int(j.get()) + int(matrix2[matrix1.index(i)][i.index(j)].get())))
    else:
        outputmatrix = [[tkinter.StringVar()]]
        outputmatrix[0][0].set("Dimention Mismatch")
    draw_second_window(regenVars=False)

def subtract():
    global outputmatrix
    outputmatrix = []
    if (int(matrix1width.get())==int(matrix2width.get())) and (int(matrix1height.get())==int(matrix2height.get())):
        for i in matrix1:
            outputmatrix.append([])
            for j in i:
                outputmatrix[matrix1.index(i)].append(tkinter.StringVar())
                outputmatrix[matrix1.index(i)][i.index(j)].set(str(int(j.get()) - int(matrix2[matrix1.index(i)][i.index(j)].get())))
    else:
        outputmatrix = [[tkinter.StringVar()]]
        outputmatrix[0][0].set("Dimention Mismatch")
    draw_second_window(regenVars=False)

def multiply():
    global outputmatrix
    outputmatrix = []
    if(matrix1height.get()==matrix2width.get()):
        for j in range(int(matrix2height.get())):
            outputmatrix.append([])
            for i in range(int(matrix1width.get())):
                value = 0
                for k in range(int(matrix1height.get())):
                    value+= int(matrix1[k][i].get()) * int(matrix2[j][k].get())
                    print(value)
                outputmatrix[j].append(tkinter.StringVar())
                outputmatrix[j][i].set(str(value))

    else:
        outputmatrix = [[tkinter.StringVar()]]
        outputmatrix[0][0].set("Dimention Mismatch")
    draw_second_window(regenVars=False)

def transpose():
    global outputmatrix
    outputmatrix = []
    for j in range(len(matrix1[0])):
        outputmatrix.append([])
        for i in range(len(matrix1)):
            outputmatrix[j].append(tkinter.StringVar())
            outputmatrix[j][i].set(matrix1[i][j].get())
    draw_second_window(regenVars=False)

matrix1width = tkinter.StringVar()
matrix1height = tkinter.StringVar()
matrix2width = tkinter.StringVar()
matrix2height = tkinter.StringVar()

draw_first_window()
root.mainloop()
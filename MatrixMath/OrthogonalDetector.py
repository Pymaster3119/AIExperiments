import tkinter

root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()
matrixvars = []
#First window - asking for matrix size
def draw_first_window():
    global frame, matrixsize
    for child in frame.winfo_children():
        child.destroy()
    tkinter.Label(frame, text= "What should the size of your matrix be (all orthogonal matrices must be square so there is only one input)").grid(row = 0, column=0)
    tkinter.Entry(frame, textvariable=matrixsize).grid(row=1, column=0)
    tkinter.Button(frame, command=draw_second_window,text="Create matrix and assign values").grid(row=2, column=0)

#Second window - asking for matrix contents and giving the orthogonality
def draw_second_window():
    global matrixvars
    for child in frame.winfo_children():
        child.destroy()
    tkinter.Label(frame, text="Enter your " + matrixsize.get() + " x " + matrixsize.get() + " matrix here:").grid(row=0, column=0, columnspan=int(matrixsize.get()))
    matrixvars = []
    for i in range(int(matrixsize.get())):
        matrixvars.append([])
        for j in range(int(matrixsize.get())):
            matrixvars[i].append(tkinter.StringVar(frame))
            tkinter.Entry(frame, textvariable=matrixvars[i][j]).grid(row=j + 1, column=i)
    tkinter.Button(frame, text="Calculate whether it is orthagonal", command= checkIfOrthagonal).grid(row=int(matrixsize.get())+1, column=0)
    tkinter.Label(frame, textvariable=output).grid(row=int(matrixsize.get())+1, column=1)

def checkIfOrthagonal():
    for i in matrixvars:
        #Check length
        squarelen = 0
        for j in i:
            squarelen += int(j.get()) ** 2
        if (squarelen != 1):
            output.set("Your matrix is not orthagonal")
            return
    for i in matrixvars:
        for j in matrixvars:
            if i != j:
                #Dot product must equal 1
                dot = 0
                for k in range(len(i)):
                    dot += int(i[k].get()) * int(j[k].get())
                if (dot != 0):
                    output.set("Your matrix is not orthagonal")
                    return
    output.set("Your matrix is orthagonal")
    

output = tkinter.StringVar()
matrixsize = tkinter.StringVar()
draw_first_window()
root.mainloop()
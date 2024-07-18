import tkinter
import math
root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()
matrixvars = []
Q = []
R = []
#First window - asking for matrix size
def draw_first_window():
    global frame, matrixWidth, matrixHeight
    for child in frame.winfo_children():
        child.destroy()
    tkinter.Label(frame, text= "What should the size of your matrix be").grid(row = 0, column=0)
    tkinter.Entry(frame, textvariable=matrixWidth).grid(row=1, column=0)
    tkinter.Entry(frame, textvariable=matrixHeight).grid(row=1, column=1)
    tkinter.Button(frame, command=draw_second_window,text="Create matrix and assign values").grid(row=2, column=0)

#Second window - asking for matrix contents and giving the orthogonality
def draw_second_window(reassignVars = True):
    global matrixvars, matrixWidth, matrixHeight
    for child in frame.winfo_children():
        child.destroy()
    tkinter.Label(frame, text="Enter your matrix here:").grid(row=0, column=0)
    if (reassignVars):
        matrixvars = []
    for i in range(int(matrixHeight.get())):
        if (reassignVars):
            matrixvars.append([])
        for j in range(int(matrixWidth.get())):
            if(reassignVars):
                matrixvars[i].append(tkinter.StringVar(frame))
            tkinter.Entry(frame, textvariable=matrixvars[i][j]).grid(row=j + 1, column=i)
    tkinter.Button(frame, text="Calculate QR Factorization", command= getQR).grid(row=int(matrixHeight.get())+2, column=0)
    for j in range(len(Q)):
        for i in range(len(Q[j])):
            tkinter.Label(frame, textvariable=Q[j][i]).grid(row = i + int(matrixHeight.get())+ 3, column= j)

def getQR():
    global Q, R
    #Calculate Q
    for i in matrixvars:
        a = i
        for j in Q:
            currterm = dot(i, j)
        length = findlength(a, True)
        Q.append([])
        for j in i:
            Q[len(Q)-1].append(tkinter.StringVar())
            Q[len(Q)-1][len(Q[len(Q)-1])-1].set(str(float(j.get())/length))
    draw_second_window(reassignVars=False)
    
def findlength(i, get):
    length = 0
    for j in i:
        if get:
            length += float(j.get()) * float(j.get())
        else:
            length += j * j
    length = math.sqrt(length)
    return length

def dot(i, j):
    out = 0
    for x in range(len(i)):
        out +=float(i[x].get()) * float(j[x].get())
    return out

def subtract(v1, v2, gets = True):
    output = []
    for i in range(len(v1)):
        if gets:
            output.append(float(v1[i].get())-float(v2[i].get()))
        else:
            output.append(v1[i]-v2[i])
    return output

matrixWidth = tkinter.StringVar()
matrixHeight = tkinter.StringVar()
draw_first_window()
root.mainloop()
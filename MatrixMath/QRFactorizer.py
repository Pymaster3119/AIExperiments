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
    tkinter.Label(frame, text="Q: ").grid(row=int(matrixHeight.get())+3, column=0)
    for j in range(len(Q)):
        for i in range(len(Q[j])):
            tkinter.Label(frame, textvariable=Q[j][i]).grid(row = i + int(matrixHeight.get())+ 4, column= j)

    tkinter.Label(frame, text="R: ").grid(row=len(Q) + int(matrixHeight.get())+ 5, column=0)
    for j in range(len(R)):
        for i in range(len(R[j])):
            tkinter.Label(frame, textvariable=R[j][i]).grid(row = i + len(Q) + int(matrixHeight.get())+ 6, column= j)

def getQR():
    global Q, R
    #Calculate Q
    for i in matrixvars:
        a = i
        for j in Q:
            currterm = dot(i, j)
            currterm = multiply(currterm, j)
            print(currterm)
            a = subtract(i, currterm,gets=False)
        if (len(Q) == 0):
            out = []
            for j in a:
                out.append(float(j.get()))
            a=out
        length = findlength(a, False)
        Q.append([])
        for j in a:
            Q[len(Q)-1].append(tkinter.StringVar())
            Q[len(Q)-1][len(Q[len(Q)-1])-1].set(str(j/length))
    
    #Calculating P
    for i in range(len(matrixvars)):
        R.append([])
        for j in range(len(matrixvars[i])):
            if j <= i:
                a = matrixvars[i]
                e = Q[j]
                result = dot(a,e)
                R[i].append(tkinter.StringVar())
                R[i][j].set(str(result))
            else:
                R[i].append(tkinter.StringVar())
                R[i][j].set("0")
    draw_second_window(reassignVars=False)
    
def findlength(i, get):
    length = 0
    if get:
        length = math.sqrt(sum(float(x.get())**2 for x in i))
    else:
        length = math.sqrt(sum(x**2 for x in i))
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
            output.append(float(v1[i].get())-v2[i])
    return output

def multiply(const, v2):
    output = []
    for i in range(len(v2)):
        output.append(const * float(v2[i].get()))

    return output
matrixWidth = tkinter.StringVar()
matrixHeight = tkinter.StringVar()
draw_first_window()
root.mainloop()
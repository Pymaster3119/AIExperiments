import numpy as np
import matplotlib.pyplot as plt

def plot_3d_function(functionstr):
    x = np.linspace(-10, 10, 20)
    y = np.linspace(-10, 10, 20)
    
    z = eval(functionstr)

    fig = plt.figure(figsize=(10, 8))
    axes1 = fig.add_axes([0.1,0.1,0.9,0.9])
    axes1.set_ylim(-10,10)
    axes1.set_xlim(-10,10)

    print(z.shape)
    print(z)
    for i in x:
        for j in y:
            pass
            

    
    plt.show()

if __name__ == "__main__":
    func_str = input("Enter a 3-D function of x and y (e.g., 'np.sin(np.sqrt(x**2 + y**2))', 'x**2 - y**2', 'np.exp(-x**2 - y**2)'): ")
    plot_3d_function(func_str)
import numpy as np
import matplotlib.pyplot as plt

def gr_python():
    
    np.random.seed(19680801)

    dt = 1.0
    t = np.arange(0, 100000000, dt)
    nse1 = np.random.randn(len(t))
        
    fig, axs = plt.subplots()
    axs.plot(t, nse1)
        
    fig.tight_layout()
    plt.show()
    
    
if __name__ == "__main__":    
    gr_python()

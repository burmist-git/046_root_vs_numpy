import numpy as np
import matplotlib.pyplot as plt

def h1_python():
    
    np.random.seed(19680801)

    nse1 = np.random.randn(100000000)

    bins = 100000
    
    fig, axs = plt.subplots()
    axs.hist(nse1, bins)
        
    fig.tight_layout()
    plt.show()
    
    
if __name__ == "__main__":    
    h1_python()

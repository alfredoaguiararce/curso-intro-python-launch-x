import numpy as np
import matplotlib.pyplot as plt

def print_graph():
    data = np.random.default_rng(12345)
    oxy_nums = data.integers(low=0, high=10, size=10)

    plt.bar(range(len(oxy_nums)), oxy_nums)
    plt.show()

if __name__ == "__main__":
    # Mostramos la grafica
    print_graph()
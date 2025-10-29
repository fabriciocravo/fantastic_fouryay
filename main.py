import matplotlib.pyplot as plt

from supporting_scripts import *
from supporting_scripts.fourrier_computation import sliding_window_fourier
from supporting_scripts.synthetic_data_generation import create_synthetic_data

if __name__ == '__main__':

    f = 30
    ts_a, _ = create_synthetic_data(frequency=f, percentage_missing=0)
    power_spec = sliding_window_fourier(ts_a, sampling_frequency=f, window_percentage=0.5)

    plt.plot(power_spec)
    plt.show()




    pass


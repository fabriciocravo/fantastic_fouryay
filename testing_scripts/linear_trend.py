import matplotlib.pyplot as plt

from supporting_scripts.fourrier_computation import sliding_window_fourier
from supporting_scripts.import_manager import *


def linear_trend_test(data_amp=1, noise_amp=0, data_points=1000):

    data = data_amp*np.linspace(0, 10, data_points)





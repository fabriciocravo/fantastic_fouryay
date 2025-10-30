
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 14:28:42 2025

@author: tripl
"""
import matplotlib.pyplot as plt
import numpy as np
from supporting_scripts.power_input import generate_power_input
from supporting_scripts.synthetic_data_generation import create_synthetic_data
from supporting_scripts.data_and_permutation_structure import permute_data
from supporting_scripts.permutation_test import statistical_test
from supporting_scripts.fourrier_computation import sliding_window_fourier
from supporting_scripts.data_and_permutation_structure import permute_data

def null_test(noise_amp=1, n_time_pts=10000):
    n_check = 100

    curr_noise_std = noise_amp
    passed = 0
    for j in range(n_check):
        ts = np.random.normal(0 ,curr_noise_std ,n_time_pts)
        permuted_ts = permute_data(ts)


        #y = sliding_window_fourier(ts)
        #ts_p = permute_data(ts)[0]
        #y_perm = sliding_window_fourier(ts_p)

        #plt.plot(y)
        #plt.plot(y_perm)
        #plt.show()

        #exit()

        ft_data, ft_permute = generate_power_input(ts ,permuted_ts)

        if statistical_test(ft_data ,ft_permute):
            passed += 1

    power = passed /n_check

    return power
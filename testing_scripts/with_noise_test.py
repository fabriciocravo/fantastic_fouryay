# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 14:59:02 2025

@author: tripl
"""

import numpy as np
from supporting_scripts.power_input import generate_power_input
from supporting_scripts.synthetic_data_generation import create_synthetic_data
from supporting_scripts.data_and_permutation_structure import permute_data
from supporting_scripts.permutation_test import statistical_test


def noise_test(noise_std, time_duration=1, n_time_pts=1000, frequency=20):
    n_check = 100
    power = np.array(len(noise_std), 1)

    ts, _ = create_synthetic_data(percentage_missing=0, max_time=time_duration, frequency=frequency,
                                  n_points=n_time_pts)
    for i in range(len(noise_std)):
        curr_noise_std = noise_std[i]
        passed = 0
        for j in range(n_check):
            noise = np.random.normal(0, curr_noise_std, n_time_pts)
            ts_noise = ts + noise
            permuted_ts = permute_data(ts_noise)
            ft_data, ft_permute = generate_power_input(ts_noise, permuted_ts)

            if statistical_test(ft_data, ft_permute):
                passed += 1

        power[i] = passed / n_check

    return power
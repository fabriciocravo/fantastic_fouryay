import numpy as np

from supporting_scripts.fourrier_computation import sliding_window_fourier

def generate_power_input(data, permutations, window_percentage=0.05, sampling_frequency=1):

    ft_data = sliding_window_fourier(data)

    ft_perms = np.zeros((permutations.shape[0], len(ft_data)))
    for i in range(permutations.shape[0]):
        p = permutations[i]
        ft_p = sliding_window_fourier(p)
        ft_perms[i] = ft_p

    return ft_data, ft_perms





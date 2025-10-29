from supporting_scripts.import_manager import *

# This is the actual data you'll be wanting to use since fourier transform doesn't work without
def sliding_window_fourier(data, window_percentage=0.05, sampling_frequency=1):
    window_size = int(window_percentage*len(data))

    if window_size is not None:
        _, _, Zxx = stft(data, fs=sampling_frequency, nperseg=window_size)
    else:
        _, _, Zxx = stft(data, fs=sampling_frequency)

    average_power = np.mean(np.abs(Zxx), axis=1)

    return average_power

def permute_data(data):

    randomized_data = np.random.permutation(data)
    return randomized_data


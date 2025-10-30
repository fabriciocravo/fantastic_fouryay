from supporting_scripts.import_manager import *


# This is the actual data you'll be wanting to use since fourier transform doesn't work without
def sliding_window_fourier(data, window_percentage=0.05, sampling_frequency=1):
    window_size = int(window_percentage * len(data))

    if window_size != len(data):
        _, _, Zxx = stft(data, fs=sampling_frequency, nperseg=window_size)
    else:
        _, _, Zxx = stft(data, fs=sampling_frequency, window='boxcar', nperseg=window_size)

    # Remove DC component
    average_power = np.mean(np.abs(Zxx), axis=1)[1:]

    # Normalize it
    average_power = average_power / np.sum(average_power)


    return average_power


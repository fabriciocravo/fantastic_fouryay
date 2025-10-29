import matplotlib.pyplot as plt

from supporting_scripts.import_manager import *
# Make some fake periodic function


def create_synthetic_data(percentage_missing=0.1, max_time=1, frequency=20, n_points=1000):

    time_points = np.linspace(0, max_time, n_points)
    periodic_function = np.sin(2 * np.pi * frequency * time_points)
    periodic_data = pd.DataFrame({'t': time_points, 'amplitude': periodic_function})

    # Set the percentage of missingness

    number_missing = int(percentage_missing * len(periodic_data))
    index_to_replace = np.random.randint(0, len(periodic_data)-1, number_missing)
    periodic_data.loc[index_to_replace, 'amplitude'] = np.nan

    # This is the actual data you'll be wanting to use since fourier transform doesn't work without

    final_data = periodic_data.dropna()

    time_ts = final_data['t'].to_numpy()
    amplitude_ts = final_data['amplitude'].to_numpy()

    return amplitude_ts, time_ts


if __name__ =='__main__':

    A, _ = create_synthetic_data()
    plt.plot(A)
    plt.show()
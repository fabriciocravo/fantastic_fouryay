from supporting_scripts.power_input import generate_power_input
from supporting_scripts.synthetic_data_generation import create_synthetic_data
from supporting_scripts.data_and_permutation_structure import permute_data
from supporting_scripts.permutation_test import statistical_test


if __name__ == '__main__':

    # for loop - to calcule tpr, fpr
    n_checks = 100

    passed = 0
    for i in range(n_checks):
        f = 30
        ts_a, _ = create_synthetic_data(frequency=f, percentage_missing=0)

        permuted_ts = permute_data(ts_a)

        ft_data, ft_permute = generate_power_input(ts_a, permuted_ts)

        if statistical_test(ft_data, ft_permute):
            passed += 1

    print(passed/n_checks)



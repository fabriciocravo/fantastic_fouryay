from supporting_scripts.power_input import generate_power_input
from supporting_scripts.synthetic_data_generation import create_synthetic_data
from supporting_scripts.data_and_permutation_structure import permute_data
from supporting_scripts.permutation_test import statistical_test
from testing_scripts.linear_trend import linear_trend_test


def missing_percentage_test():

    missingness_percentages = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    n_checks = 10
    for percentage in missingness_percentages:
        passed_missingness_test = 0

        for i in range(n_checks):
            ts_a, _ = create_synthetic_data(percentage_missing=percentage)

            permuted_ts = permute_data(ts_a)

            ft_data, ft_permute = generate_power_input(ts_a, permuted_ts)

            if statistical_test(ft_data, ft_permute):
                passed_missingness_test += 1

        print(f"For {percentage} missingness: ")
        print("Fraction of checks passed: ", (passed_missingness_test/n_checks))
        print()
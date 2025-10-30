import numpy as np

def statistical_test(ft_data, ft_perms, alpha=0.05, method='shannon'):

    if method == 'shannon':
        p_val = shannon_entropy_pvalue(ft_data, ft_perms)
    elif method == 'kl_uni':
        p_val = kl_uniform_pvalue(ft_data, ft_perms)
    else:
        raise TypeError('Method name not supported')

    if p_val < alpha:
        return True
    else:
        return False

def shannon_entropy_pvalue(empirical_spectrum, perm_spectra, base=100):
    """
    Calculate Shannon entropy and p-value from permutation test.

    Parameters:
    -----------
    empirical_spectrum : ndarray
        Empirical power spectrum (normalized), shape (n_frequencies, 1)
    perm_spectra : ndarray
        Permutation power spectra (normalized), shape (n_frequencies, n_permutations)
    base : int
        Base for logarithm (default: 100)

    Returns:
    --------
    p_value : float
        P-value from permutation test
    empirical_ent : float
        Empirical Shannon entropy
    perm_ent : ndarray
        Permutation entropies, shape (1, n_permutations)
    """
    # Calculate Shannon entropy: -sum(p * log_base(p))
    empirical_ent = -np.sum(np.lib.scimath.logn(base, empirical_spectrum) * empirical_spectrum)
    perm_ent = -np.sum(np.lib.scimath.logn(base, perm_spectra) * perm_spectra, axis=0, keepdims=True)

    # P-value: proportion of permutations with entropy >= empirical
    p_value = 1 - np.mean(empirical_ent < perm_ent)

    return p_value


def kl_uniform_pvalue(empirical_spectrum, perm_spectra, base=100):
    """
    Calculate KL divergence from uniform distribution and p-value from permutation test.

    Parameters:
    -----------
    empirical_spectrum : ndarray
        Empirical power spectrum (normalized), shape (n_frequencies, 1)
    perm_spectra : ndarray
        Permutation power spectra (normalized), shape (n_frequencies, n_permutations)
    base : int
        Base for logarithm (default: 100)

    Returns:
    --------
    p_value : float
        P-value from permutation test
    empirical_KL : float
        Empirical KL divergence
    perm_KL : ndarray
        Permutation KL divergences, shape (1, n_permutations)
    """
    n_freq = empirical_spectrum.shape[0]
    expected_distribution = np.ones((n_freq, 1)) / n_freq

    # Calculate KL divergence: sum(p * log(p/q))
    empirical_KL = np.sum(expected_distribution * np.lib.scimath.logn(base, expected_distribution / empirical_spectrum))
    perm_KL = np.sum(expected_distribution * np.lib.scimath.logn(base, expected_distribution / perm_spectra), axis=0,
                     keepdims=True)

    # P-value: proportion of permutations with KL <= empirical
    p_value = 1 - np.mean(empirical_KL > perm_KL)

    return p_value

# Example usage:
# p_shannon, emp_ent, perm_ent = shannon_entropy_pvalue(empirical_s, perm_s)
# p_kl, emp_kl, perm_kl = kl_divergence_pvalue(empirical_s, perm_s)
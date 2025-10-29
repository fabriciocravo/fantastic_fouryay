
def sliding_window_fourier(sliding=True, data):
    data = data.dropna()
    if sliding:
        window_size = 50
        sampling_frequency = 0.001
        frequency_array, _, _ = stft(data,fs=sampling_frequency,nperseg=window_size)
    else:
        frequency_array, _, _ = stft(data,fs=sampling_frequency,nperseg=window_size)
    return frequency_array

def permute_data(data):
    randomized_data = random.permutation(data)
    return randomized_data


# In[45]:


# start with real data power spectrum and permutations power spectra
empirical_s = np.random.randn(100,1)
empirical_s = empirical_s-np.min(empirical_s)
empirical_s = empirical_s/np.sum(empirical_s)
empirical_s = empirical_s+0.001
perm_s = np.random.randn(100,1000)
perm_s = perm_s-np.min(perm_s,axis=0,keepdims=True)
perm_s = perm_s/np.sum(perm_s,axis=0,keepdims=True)
perm_s = perm_s + 0.001


# In[ ]:


# method 1 (correlation distance; try with triangle inequality)
# also plot the empirical and mean


# In[ ]:


# method 2 (sum of abs difference)


# In[61]:


# method 3 (shannon entropy, though might not work if random spectrum is a decay function and not flat)
empirical_ent = -np.sum(np.lib.scimath.logn(100,empirical_s)*empirical_s)
perm_ent = -np.sum(np.lib.scimath.logn(100,perm_s)*perm_s,axis=0,keepdims=True)

p3 = 1 - np.mean((empirical_ent<perm_ent).astype(int))


# In[73]:


# method 4 (KL divergence)
expected_distribution = np.transpose(np.array([[1/100]*100]))
empirical_KL = np.sum(expected_distribution*np.lib.scimath.logn(100,expected_distribution/empirical_s))
perm_KL = np.sum(expected_distribution*np.lib.scimath.logn(100,expected_distribution/perm_s),axis=0,keepdims=True)

p4 = 1 - np.mean((empirical_KL>perm_KL).astype(int))


# In[ ]:


# method 5 (KS test against uniform)


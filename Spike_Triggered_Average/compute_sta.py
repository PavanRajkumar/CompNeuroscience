# Author : Paavan Rajkumar Magesh

# Code to compute spike-triggered average from a stimulus and spike-train.

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

"""Compute the spike-triggered average from a stimulus and spike-train.
    Args:
        stim: stimulus time-series
        rho: spike-train time-series
        num_timesteps: how many timesteps to use in STA
    Returns:
        spike-triggered average for num_timesteps timesteps before spike
"""

def compute_sta(stim, rho, num_timesteps):
    sta = np.zeros((num_timesteps,))

    # This command finds the indices of all of the spikes that occur
    # after 300 ms into the recording.
    spike_times = rho[num_timesteps:].nonzero()[0] + num_timesteps

    num_spikes = len(spike_times)
    print(num_spikes)

    for i in range(num_spikes):
        windows = stim[(spike_times[i] - num_timesteps):spike_times[i]]
        sta = sta+windows
    sta = sta/num_spikes
    return sta

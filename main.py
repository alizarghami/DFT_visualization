# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 12:42:37 2020

@author: Ali
"""

from periodic_signal import Signal


# Some parameters here

sampling_frequency = 1000        # In Hz
sample_length = 1                # In seconds


# Add a signal
sig = Signal(sampling_frequency, sample_length)



# Add a cos components
amp1 = 1
omega1 = 5
phase1 = 0

sig.add('cos', omega1, amp1, phase1, name='cos5Hz')


# Add a sin component
omega2 = 10
amp2 = 1
phase2 = 1

sig.add('sin', omega2, amp2, phase2, name='sin10Hz')


# Plot the result
sig.plot()

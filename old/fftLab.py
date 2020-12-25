# THIS IS WHAT THE CODE INITIALLY WAS

# Welcome To FFT Lab

import numpy as np
import matplotlib.pyplot as plt



# ------------------- Sample Properties ------------------

sample_rate = 1.0/128
sample_duration = 1     # In seconds
samp = np.arange(0, sample_duration, sample_rate)


# ---------- Signal construction and properties ----------

omega1 = 5
mag1 = 2
signal1 = mag1 * np.cos(2 * np.pi * omega1 * samp )
omega2 = 10
mag2 = 1
signal2 = mag2 * np.cos(2 * np.pi * omega2 * samp )

signal = signal1 + signal2


# ------------------ Fourier Transform -------------------
freq = np.fft.rfftfreq(samp.size, sample_rate)
fourier = np.abs(np.fft.rfft(signal))


# ------------------------Plotting-----------------------

plt.subplot(4,1,1)
plt.plot(samp, signal1)

plt.subplot(4,1,2)
plt.plot(samp, signal2)

plt.subplot(4,1,3)
plt.plot(samp, signal)

plt.subplot(4,1,4)
plt.plot(freq, fourier)
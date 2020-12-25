
# DFT visualization for periodic signals

### Introduction

This is a simple code that lets you experiment with the DFT (Discrete Fourier Transform) of a periodic signal. In this code the periodic signal is constructed by mixture of Sine and Cosine components with different amplitudes, frequencies and phases. One can see the effect of each parameter by changing them and looking at the resulting graphs.
The following parameters are shared between all components and can be changed:
* Sampling Frequency: Frequency by which you sample your signal (in Hz)
* Signal Length: The length which you took sample from your signal (in seconds)

The following parameters should be set for each component individually:
* Frequency: Frequency of the periodic component (in cycles per second)
* Amplitude: Amplitude of the periodic component
* Phase: Phase by which your periodic component is shifted (in radians)

### Getting Started

In order to use this code you just need to have the following requirements installed:
* Python 2.7 or Python 3.6 or above
* Numpy
* Matplotlib

You can install each of the requirements separately or use Anaconda distribution [click here](https://www.anaconda.com/) to get all of them at once.

Then you need to clone this repository and run ```main.py```. Make sure to change the parameters as you wish.

### Instructions

In order to use the code you need create a `Signal` and add as many components as you like.
To create a `Signal` you need to instantiate the `Signal` class from `periodic_signal` module.

```python
from periodic_signal import Signal
sig = Signal(sampling_frequency, sample_length)
```
	
Make sure to set `sampling_frequency` and `sample_length` parameters.
Then you can add a component like this:

```python
sig.add(sig_type, omega, amp, phase)
```
	
Make sure to set `sig_type`, `omega`, `amp`, `phase` parameters.

Finally you can see the result:

```python
sig.plot()
```
	
Use the `reset` method to start over.

```python
sig.reset()
```

Look at ```main.py``` as an example.
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:11:25 2020

@author: Ali
"""

import numpy as np
from matplotlib import pyplot as plt

        
class Signal(object):
    def __init__(self, sampling_frequency, sampling_length):
        '''
        Create a periodic signal

        Parameters
        ----------
        sampling_frequency : int
            The frequency which the signal should be sampled (Hz).
        sampling_length : int
            The length of signal in time to sample from (Seconds).
        '''
        self.sampling_frequency = sampling_frequency
        self.length = sampling_length
        self.sample_rate = 1./self.sampling_frequency
        self.size = sampling_frequency * sampling_length
        
        self.components_size = 0
        self.collection = {}
        self.x = None
        self.y = None
        self.fx = None
        self.fy = None
        
        self.set_domain()
        
    def add(self, signal_type, frequency, amplitude, phase, **kwargs):
        '''
        Add a component to the signal

        Parameters
        ----------
        signal_type : str
            Component type. Should be either 'sin' or 'cos'.
        frequency : float
            Components frequency in cycles per second.
        amplitude : float
            The components peak value.
        phase : float
            The components phase.
            
        Keyword Args
        ------------
        name: str
            Name of the component.
        '''
        c_id = self.components_size
        if 'name' in kwargs:
            name = kwargs['name']
        else:
            name = '{}_{}'.format(signal_type, c_id)
        if name not in self.collection.keys():
            sig = BasicSignal(signal_type, frequency, amplitude, phase, self.sampling_frequency, self.length)
            self.collection[name] = sig
            self.update()
            self.components_size += 1
        else:
            print("A component with the name {} already exist".format(name))
        
    def remove(self, name):
        if name in self.collection.keys():
            del self.collection[name]
            self.update()
        else:
            print("Component doesn't exist")
        
    def update(self):
        self.y = np.sum([signal.y for signal in self.collection.values()], axis=0)
        self.fy = np.abs(np.fft.rfft(self.y))

    def set_domain(self):
        self.x = np.arange(0, self.length, self.sample_rate)
        self.fx = np.fft.rfftfreq(self.size, self.sample_rate)
        
    def reset(self):
        '''Resets the signal'''
        self.collection.clear()
        self.y = None
        
    def plot(self):
        '''Plots each component, theperiodic signal and it's DFT'''
        c_size = len(self.collection)
        
        plt.figure()
        for i, k in enumerate(self.collection.keys()):
            c = self.collection[k]
            plt.subplot(c_size+2, 1, i+1)
            plt.plot(c.x, c.y)
            
        plt.subplot(c_size+2, 1, c_size+1)
        plt.plot(self.x, self.y)
        plt.subplot(c_size+2, 1, c_size+2)
        plt.plot(self.fx, self.fy)
        
        
class BasicSignal(object):
    def __init__(self, signal_type, frequency, amplitude, phase, sampling_frequency, length):
        '''
        Creates a basic sin or cos signal

        Parameters
        ----------
        signal_type : str
            Signal type. Should be either 'sin' or 'cos'.
        frequency : float
            Signals frequency in cycles per second.
        magnitude : float
            The signals peak value.
        phase : float
            The signals phase.
        sampling_frequency : int
            The frequency which the signal should be sampled (Hz).
        length : int
            The length of signal in time to sample from (Seconds).
        '''
        self.sampling_frequency = sampling_frequency
        self.length = length
        self.type = signal_type
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = phase
        self.sample_rate = 1./self.sampling_frequency
        self.size = sampling_frequency * length
        
        self.x = None
        self.y = None
        self.create_signal()
        
    def create_signal(self):
        function = self.set_function()
        self.x = np.arange(0, self.length, self.sample_rate)
        self.y = self.amplitude * function(2 * np.pi * self.frequency * self.x + self.phase)
        
    def set_function(self):
        if self.type == 'sin':
            return np.sin
        elif self.type == 'cos':
            return np.cos
        else:
            raise Exception('Invalid signal type')
            
    def get_signal(self):
        '''Returns the sampled values'''
        return self.x, self.y
        
    def __str__(self):
        text = 'Signal type: {}\nFrequency: {}\nMagnitude: {}'.format(self.type, self.frequency, self.magnitude)
        return text

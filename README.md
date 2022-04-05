# Grover's Algorithm simulation

Contributors: Anthony Chang, Oustan Ding, Michael Pu, Tony Zhao

University of Waterloo - ECE 405, Winter 2022

This is a simulation of Grover's algorithm using matrices to represent the Oracle function and diffusion operator. It takes two inputs: `N`, the number of items in the data set to search, and `w`, the index of the winning item.

The simulation animates the probability amplitudes of the states and outputs the number of iterations (`r`) required for the winning item to have the maximal probability amplitude.

## Usage

Install all dependencies listed below, and run `python grovers.py`.

## Dependencies

- `numpy`
- `matplotlib`

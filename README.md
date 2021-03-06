# neuron-simulator
Simulates firing rates of Hodgkin-Huxley, Leaky Integrate and Fire (LIF), and Izhikevich models of neurons based on 
simulated input current.

## How to Use
This project requires Python to run, and was developed using Python 3.6.1.
1. Clone this repository, and navigate to the correct directory: `neuron-simulator`. 
1. Run the following command: `pip install -r requirements.txt`
1. Run the following command: `python simulator.py`
1. Follow instructions as prompted

## Leaky Integrate and Fire Model
The code to simulate the LIF model can be found in `lif.py`. All of the simulators make use of `plotter.py` to plot the 
results.

### Algorithm
The algorithm used for this model follows the formulas provided in the project description. Arbitrary values were used 
for the following: 

| Variable | Value Used |
|----------|--------------------------------|
| `Cm` | Used arbitrary capacitor value of 30 |
| `Rm` | Used arbitrary resistor value of 7 |
| `Vt` | Used arbitrary voltage threshold of 10 |
| `Vr` | Used arbitrary voltage reset value of 0 |

Since a neuron is essentially an RC circuit, `I` decays over time following an RC circuit's pattern

## Izhikevich Model
The code to simulate the Izhikevich model can be found in `izhikevich.py`. All of the simulators make use of 
`plotter.py` to plot the results.

### Algorithm
The algorithm used for this model follows the formulas provided in the project description. No arbitrary values were 
used, except for initial values of `u` and `v`. Initially, `u = 0.0` and `v = -65.0`. 

The user is able to control values of `a`, `b`, `c`, `d`, and `I`.
However, suggested values are: 

| Variable | Value Suggested |
|----------|--------------------------------|
| `a` | 0.02 to 0.04 |
| `b` | 0.2 to 0.4 |
| `c` | -55.0 to -80.0 |
| `d` | 2 to 4 |
| `I` | Any amount, however depending on the above values the neuron should spike at approximately 4 |

## Hodgkin-Huxley Model
The code to simulate the Hodgkin-Huxley model can be found in `hodgkin_huxley.py`. All of the simulators make use of 
`plotter.py` to plot the results.

### Algorithm
The formulas provided in the original project description were used to simulate the neuron. The only arbitrary value is
that of the injected current, which was found via research and testing different numbers. For `0.0ms < t < 1.0ms`, 
`I = 150`, and for `10.0ms < t < 11.0ms`, `I = 50`. For all other values of `t`, `I = 0`.  

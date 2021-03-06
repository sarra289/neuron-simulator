# LIF Simulator
# Completed for Rutgers University Brain-Inspired Computing (198:525)
# Priya Pamnani (pp572@rutgers.edu)

import plotter
from numpy import exp


# Helper function: shows decay of I over time
def I_t(I, t, tau):
    return I * exp(-t/tau)


def simulate():
    # Create list of times to run simulation
    times = [0]
    dt = 0.1

    # Set vars to be used in calculation
    # Variable names equivalent to those used in assignment description
    Vm = [0.0]  # voltage
    Cm = 30  # capacitance
    Rm = 7  # resistance
    tau_m = Rm*Cm  # time constant
    Vt = 10  # threshold of V, neuron fires when exceeding threshold
    Vr = 0.0  # reset to Vr after firing

    # User selects current to be injected
    print("Enter desired current")
    I = float(input())

    # Integrate V from 0.0ms to 200.0ms
    while times[-1] < 200:
        times.append(round(times[-1] + dt, 1))
        old_V = Vm[-1]
        Vm.append(old_V + (((-old_V + I_t(I, times[-1], tau_m) * Rm) / tau_m) * dt))

        # Test for spike, if exceeded threshold return to Vr
        if Vm[-1] >= Vt:
            Vm[-1] = Vr

    # Display plot
    plotter.plot(times, Vm, 'LIF Simulation with I='+str(I))

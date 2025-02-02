import pandas as pd
import os
import numpy as np

# Constants
k_B = 1.38 * 10**(-23) # Joules/Kelvin (Boltzmann Constant)
N_a = 6.022e23 # (Avogadro's Number)

# Parameters (Default Values)
temp = 273.15 # Kelvin (water freezing temp)
molar_mass = 1.00794 # grams (Hydrogen)
m = (molar_mass / N_a) * 10 ** (-3)  # convert to kg

# DataFrame of Periodic Table of Elements.
df_periodic_table = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data/Periodic Table of Elements.csv"), encoding="ISO-8859-1")
# DEBUG: test DataFrame
# print(df.head())

def f(v):
    return (m/(2*np.pi*k_B*temp))**(3/2) * 4 * np.pi * v**2 * np.exp(-(m*v**2)/(2*k_B*temp))
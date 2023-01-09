import numpy as np

# Density of UO2 as a function of temperature in the interval 273K - 923K [g\cm³]:

def UO2_density(T):
    theoretical = 10.960 # g/cm³
    K1 = 0.99734 + 9.802e-6*T - 2.705e-10*(T**2) + 4.291e-13*(T**3)
    return theoretical/(K1**3)

# Thermal expansion of U02 in the interval 273K - 923K:

def UO2_expansion(L0, T1, T2):
    #alpha = 9.828*(10**(-6)) - 6.39*(10**(-10))*T + 1.38*(10**(-12))*(T**2) - 1.757*(10**(-17))*(T**3)
    I1 = 9.828*(10**(-6))*T1 - (6.39/2)*(10**(-10))*(T1**2) + (1.38/3)*(10**(-12))*(T1**3) - (1.757/4)*(10**(-17))*(T1**4)
    I2 = 9.828*(10**(-6))*T2 - (6.39/2)*(10**(-10))*(T2**2) + (1.38/3)*(10**(-12))*(T2**3) - (1.757/4)*(10**(-17))*(T2**4)
    I = I2 - I1
    return L0*np.exp(I)

# Density of helium as a function of temperature and pressure [g/cm³]:

def helium_density(T, p):
    M = 4.002602e-3   # kg/mol
    R = 8.314472      # J/K*mol
    rho = (p*M)/(R*T) # kg/m³
    return rho/1000

# Density of zirconium as a function of temperature [g/cm³]:

def zirconium_density(T):
    return (6550 - 0.1685*T)/1000

# Thermal expansion of zirconium in the interval 300K - 1100K:

def zirconium_expansion(L0, T1, T2):
    #alpha = (5.22 + 1.82*(10**(-3))*T)*(10**(-6))
    I1 = (5.22*T1 + (1.82/2)*(10**(-3))*(T1**2))*(10**(-6))
    I2 = (5.22*T2 + (1.82/2)*(10**(-3))*(T2**2))*(10**(-6))
    I = I2 - I1
    return L0*np.exp(I)

# Density of UN as a function of temperature in the interval 298K - 2523K [g\cm³]:

def UN_density(T):
    rho = 14420 - 0.2779*T - 4.897*(10**(-5))*(T**2)
    return rho/1000
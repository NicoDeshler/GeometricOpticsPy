# Homework 6
# Author: Nico Deshler

##############################################
################# Problem 2 ##################
##############################################
# Provided System Parameters:
R1 = 127
R2 = -77
t = 17

# Part a
n1 = 1
n2 = 1.472
n3 = 1

# Part b
n1 = 1
n2 = 1.8573
n3 = 1


# Part c
n1 = 1.333
n2 = 1.472
n3 = 1.333

# object and image space refractive indices
n = n1
n_prime = n3


# Gaussian Reduction Parameters
tau = t/n2                      # reduced lens thickness
phi1 = (n2-n1)/R1               # power of first surface
phi2 = (n3-n2)/R2               # power of second surface
phi_sys = phi1 + phi2 - phi1*phi2*tau   # power of reduced system
F = 1/phi_sys                           # focal length of reduced system
delta = -phi2/phi_sys * tau1            # reduced distance from front vertex V to front principle plane P
delta_prime = -phi1/phi_sys * tau       # reduced distance from rear vertex V' to rear principle plane P'
d = n*delta                             # physical distance from V to P
d_prime = n3*delta_prime                # physical distance from V' to P'
fF = -F*n0                              # front focal length
fR = F*n3                               # rear focal length
BFL = fR+d_prime                        # back focal length



##############################################
################# Problem 3 ##################
##############################################

# Initial parameters for 3-surface system
n0 = 1.33
n1 = 1.5
n2 = 1.6
n3 = 1.33

# Object and image space refractive index
n = n0
n_prime = n3

# Radius of curvature for each surface
R1 = 25
R2 = -40
R3 = -60

# Physical and reduced thicknesses
t1 = 5
t2 = 5
tau1 = t1/n1
tau2 = t2/n2

# Surface Powers
phi1 = (n1-n0)/R1
phi2 = (n2-n1)/R2
phi3 = (n3-n2)/R3

# First Gaussian Reduction
phi12 = phi1 + phi2 - phi1*phi2*tau1
delta_prime12 = -phi1 / phi12 * tau1
tau = tau2-delta_prime12

# Second Gaussian Reduction
phi = phi12 + phi3 - phi12*phi3*tau # system power
F = 1/phi                           # system focal length
fR = n_prime*F                      # system rear focal length
delta = phi3/phi_sys * tau         # reduced distance from front vertex V to front principle plane P
delta_prime = -phi12/phi*tau        # reduced distance from V' to P'
d_prime = n_prime * delta_prime     # physical distance from V' to P'
BFL = fR + d_prime                  # physical distance from V' to F'

# Print parameters
print('Power:', phi)
print('Focal Length:', F)
print('d\':', d_prime)
print('BFL:', BFL)

"""
# Terminal Output
Power: 0.008693401041666661
Focal Length: 115.02977893313482
d': -5.550654142000668
BFL: 147.43895183906866
"""

##############################################
################# Problem 5 ##################
##############################################

# Initial parameters for 3-surface system (The HumanEye)
n0 = 1
n1 = 1.336
n2 = 1.413
n3 = 1.336
n = n0
n_prime = n3

# Radius of curvature for each surface
R1 = 7.8
R2 = 10
R3 = -6

# Physical and reduced thicknesses
t1 = 3.6
t2 = 3.6
tau1 = t1/n1
tau2 = t2/n2

# Surface Powers
phi1 = (n1-n0)/R1
phi2 = (n2-n1)/R2
phi3 = (n3-n2)/R3

# First Gaussian Reduction
phi12 = phi1 + phi2 - phi1*phi2*tau1
delta_prime12 = -phi1 / phi12 * tau1
tau = tau2-delta_prime12

# Second Gaussian Reduction
phi = phi12 + phi3 - phi12*phi3*tau # system power
F = 1/phi                           # system focal length
fR = n_prime*F                      # system rear focal length
delta_prime = -phi12/phi*tau        # reduced distance from V' to P'
d_prime = n_prime * delta_prime     # physical distance from V' to P'
BFL = fR + d_prime                  # physical distance from V' to F'

# print parameters
print('Power:', phi)
print('Focal Length:', F)
print('d\':', d_prime)
print('BFL:', BFL)

"""
# Terminal Output
Power: 0.05959583995164986
Focal Length: 16.77969470371255
d': -5.451223446837235
BFL: 16.96644867732273
"""

##############################################
################# Extra ######################
##############################################

# A general implementation for Gaussian Reduction
def GaussianReduction(n_list, R_list, t_list):

    # Quick input check
    assert(len(n_list)-2 == len(R_list)-1 == len(t_list))

    # Preprocess
    phis = [(n_list[i+1]-n_list[i])/R_list[i] for i in range(len(n_list)-1)] # A list of surface powers
    taus = [t_list[i]/n_list[i+1] for i in range(len(t_list))]               # A list of reduced thicknesses

    # initialization
    n1_idx,n2_idx,n3_idx = 0,1,2

    # Output parameters (these get updated after each iteration of reduction)
    phi = phi_surfs
    F = 0
    BFL = 0

    while len(phi) > 1:
        n1,n2,n3 = n_list[n1_idx],n_list[n2_idx],n_list[n3_idx]
        phi1 = phi[0]
        phi2 = phi[1]

        # Pairwise gaussian reduction
        def GaussianReductionPairwise(n1,n2,n3,tau,phi1,phi2):
            phi_sys = phi1 + phi2 - phi1*phi2*tau   # power of reduced system
            F = 1/phi_sys                           # focal length of reduced system
            delta_prime = -phi1/phi_sys * tau       # reduced distance from rear vertex V' to rear principle plane P'
            d_prime = n3*delta_prime                # physical distance from V' to P'
            fR = F*n3                               # rear focal length
            BFL = fR+d_prime                        # back focal length

            return phi_sys, F,  BFL

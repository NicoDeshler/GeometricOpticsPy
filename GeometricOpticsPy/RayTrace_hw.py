# OPTI 502 Fall 2021
# Homework 7: Ray Tracing
# Author: Nico Deshler

# Notes:
# Open a terminal and run 'python RayTrace.py'

def main():

    #########################
    ###### PROBLEM 3 ########
    #########################
    print('-----------------')
    print('----PROBLEM 3A---')
    print('-----------------\n')

    # Initialize ray...
    y0 = 1
    u0 = 0
    ti = 0
    tf = 0

    # Lens system parameters
    n = [1,1.4,1.8,1.33]
    R = [20,-10,-15]
    t = [20,20]

    # calculate surface powers
    Phi = [(n[i + 1] - n[i]) / R[i] for i in range(len(R))]

    # Flag if desired propagation distance is to z-axis (is true by default)
    PropToAxis = True

    # Send the Ray through the optical system
    TraceSystem(y0, u0, ti, tf, n, Phi, t, PropToAxis)


    print('-----------------')
    print('----PROBLEM 3B---')
    print('-----------------\n')

    # Initialize ray...
    y0 = 1
    u0 = 0
    ti = 0
    tf = 0

    # Lens system parameters
    # flip param order (prop backwards)
    n.reverse()
    t.reverse()
    Phi.reverse()

    # Flag if desired propagation distance is to z-axis (is true by default)
    PropToAxis = True

    # Send the Ray through the optical system
    TraceSystem(y0, u0, ti, tf, n, Phi, t, PropToAxis)


    #########################
    ###### PROBLEM 4 ########
    #########################
    print('-----------------')
    print('----PROBLEM 4----')
    print('-----------------\n')

    # Initialize ray...
    y0 = 1
    u0 = 0
    ti = 0
    tf = 0

    # Lens system parameters
    n = [1, 1.5, 1]
    R = [25, -25]
    t = [50]
    # calculate surface powers
    Phi = [(n[i + 1] - n[i]) / R[i] for i in range(len(R))]
    
    # Flag if desired propagation distance is to z-axis (is true by default)
    PropToAxis = True

    # Send the Ray through the optical system
    TraceSystem(y0, u0, ti, tf, n, Phi, t, PropToAxis)


    #########################
    ###### PROBLEM 5 ########
    #########################
    print('-----------------')
    print('----PROBLEM 5----')
    print('-----------------\n')

    # Initialize ray...
    y0 = 1
    u0 = 0
    ti = 0
    tf = 0

    # Lens system parameters
    n = [1, 1.336, 1.413, 1.336]
    R = [7.8, 10, -6]
    t = [3.6,3.6]
    # calculate surface powers
    Phi = [(n[i + 1] - n[i]) / R[i] for i in range(len(R))]

    # Flag if desired propagation distance is to z-axis (is true by default)
    PropToAxis = True

    # Send the Ray through the optical system
    TraceSystem(y0, u0, ti, tf, n, Phi, t, PropToAxis)

    #########################
    ###### PROBLEM 6 ########
    #########################
    print('-----------------')
    print('----PROBLEM 6A---')
    print('-----------------\n')

    # Initialize ray...
    y0 = 1
    u0 = 0
    ti = 0
    tf = 0

    # Lens system parameters
    n = [1, 1.5, 1]
    R = [1/-.01, 1/.01]
    t = [5]
    # calculate surface powers
    Phi = [(n[i + 1] - n[i]) / R[i] for i in range(len(R))]

    # Flag if desired propagation distance is to z-axis (is true by default)
    PropToAxis = True

    # Send the Ray through the optical system
    TraceSystem(y0, u0, ti, tf, n, Phi, t, PropToAxis)


    print('-----------------')
    print('----PROBLEM 6B---')
    print('-----------------\n')


    print('-----Ray 1-----')
    # Initialize Ray 1...
    y0 = 0
    u0 = 0.1
    ti = 100
    tf = 0
    # Send Ray 1 through the optical system
    TraceSystem(y0, u0, ti, tf, n, Phi, t, True)

    print('-----Ray 2-----')
    # Initialize Ray 2...
    y0 = 10
    u0 = 0
    ti = 100
    tf = -51.85185185185185

    # Send Ray 2 through the optical system
    TraceSystem(y0, u0, ti, tf, n, Phi, t, False)


    print('-----------------')
    print('----PROBLEM 6C---')
    print('-----------------\n')

    print('-----Ray 1-----')
    # Initialize Ray 1...
    y0 = 0
    u0 = 10/150
    ti = 150
    tf = 0
    # Send Ray 1 through the optical system
    TraceSystem(y0, u0, ti, tf, n, Phi, t, True)

    print('-----Ray 2-----')
    # Initialize Ray 2...
    y0 = 10
    u0 = 0
    ti = 150
    tf = -61.61449752883032

    # Send Ray 2 through the optical system
    TraceSystem(y0, u0, ti, tf, n, Phi, t, False)


    print('-----------------')
    print('----PROBLEM 7A---')
    print('-----------------\n')

    # Initialize ray...
    y0 = 1
    u0 = 0
    ti = 0
    tf = 0

    # Lens system parameters
    n = [1, 1.5, -1.5, -1]
    R = [-100, -150, -100]
    t = [10, -10]
    # calculate surface powers
    Phi = [(n[i + 1] - n[i]) / R[i] for i in range(len(R))]

    # Flag if desired propagation distance is to z-axis (is true by default)
    PropToAxis = True

    # Send the Ray through the optical system
    TraceSystem(y0, u0, ti, tf, n, Phi, t, PropToAxis)

    print('-----------------')
    print('----PROBLEM 7B---')
    print('-----------------\n')

    # Initialize ray...
    y0 = 1
    u0 = 0
    ti = 0
    tf = 0

    # Lens system parameters
    n.reverse()
    t.reverse()
    Phi.reverse()

    # Flag if desired propagation distance is to z-axis (is true by default)
    PropToAxis = True

    # Send the Ray through the optical system
    TraceSystem(y0, u0, ti, tf, n, Phi, t, PropToAxis)




    ##############################
    ##############################

def TraceSystem(y0, u0, ti, tf, n, Phi, tt, PropToAxis = 1):

    # some preprocessing for pass-by-reference python
    t = tt.copy()
    t.append(tf)

    # initialize containers for ray height and ray angle at each surface
    y = [0 for i in range(len(Phi) + 1)]
    u = [0 for i in range(len(Phi) + 1)]
    u[0] = u0
    y[0] = propagate(y0, u0, ti)

    # RayTrace through surfaces
    for i in range(len(Phi)):
        n_in = n[i]
        n_out = n[i + 1]
        u_in = u[i]
        phi = Phi[i]
        t_prop = t[i]
        y_in = y[i]

        u[i + 1], y[i + 1] = RayTrace(n_in, n_out, u_in, y_in, phi, t_prop)

    # Gaussian parameters
    phi_sys = -n[-1] * u[-1] / y[0]
    fE = 1 / phi_sys
    fR = n[-1] * fE
    fF = -n[0] * fE

    if PropToAxis:
        assert (u[-1] * y[-1] >= 0, 'Outgoing ray does not intersect optical axis!')
        y[-1] = 0
        t2Axis = -y[-2] / u[-1]
        t[-1] = t2Axis

    print('y: ', y)
    print('u: ', u)
    print('t: ', t)
    print('fE: ', fE)
    print('fR: ', fR)
    print('fF: ', fF)
    if PropToAxis: print('t2z_axis', t2Axis)
    print('\n\n')

def RayTrace(n, nn, u, y, phi, t):
    uu = refract(n,nn,u,y,phi)
    yy = propagate(y, uu, t)
    return uu,yy

def propagate(y,uu,t):
    yy = y + uu*t
    return yy

def refract(n, nn, u, y, phi):
    uu = (n*u - y*phi)/nn
    return uu


main()

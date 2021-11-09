################
GEOMETRIC OPTICS PY
################
Details:
################
This package uses the sign conventions for angles, axis vectors, and refractive indices
defined in the Geometric Optics SPIE Field Guide by John Grievenkamp.

This package is designed to handle the following optical surface types:
   - Thin Lenses
   - Spherical surfaces [refractive (thick lens) and reflective] (no conic sections)

The systems are assumed to be rotationally symmetric about the optical axis and have no higher-order aberrations.
That is, the package operates under the paraxial regime:
    - no large ray bending angles

###############
Outputs:
###############
After setting up an system, a user may choose to do one of the following:
    - trace rays through the system (identify the marginal ray and chief ray automatically)
    - position and object with a given height and determine the location and magnification of its image.
    - perform gaussian reduction of the system to identify the system focal length, BFD, FFD, Front and Rear Principal
      Planes, and Nodal Points (all cardinal points).

##############
GUI:
##############
***I might build this one day***



# Author: Nicolas Deshler (ndeshler@email.arizona.edu)
# University of Arizona, James C. Wyant College of Optical Sciences

################

GEOMETRIC OPTICS PY

Author(s): Nicolas Deshler (ndeshler@email.arizona.edu)
University of Arizona, James C. Wyant College of Optical Sciences

################

Details:

################

This package uses the sign conventions for angles, axis vectors, and refractive indices
defined in the Geometric Optics SPIE Field Guide by John Grievenkamp.

Currently the package is designed to handle the following optical surface types:
   - Thin Lenses
   - Spherical Surfaces (no other conic sections)

All optical systems are assumed to be rotationally symmetric about the optical axis.
Ray tracing and gaussian imaging functions make paraxial approximations and thus describe systems up to first-order only.

###############

Outputs:

###############

After setting up an optical system, the following analysis techniques are at the user's disposal:
    - trace rays through the system (marginal ray and chief rays can be identified automatically)
    - object and image locations with axial and lateral magnification details.
    - perform gaussian reduction of an optical system to identify the system focal length, BFD, FFD, Front and Rear Principal
      Planes, and Nodal Points (all cardinal points).

##############

GUI:

##############
***This might be built one day***


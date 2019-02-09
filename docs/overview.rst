Overview
########

pyJac creates the C or OpenCL source code files necessary to evaluate the
analytical Jacobian matrix for a constant-pressure (CONP) or constant-volume (CONV) reacting system.

.. _state_vec:

============
State Vector
============

Briefly, a CONP thermochemical state is described using a state vector:

.. math::
    \Phi = \left \lbrace T, V, n_1, n_2, \dotsc,
    n_{N_{\text{sp}} - 1} \right \rbrace^{\text{T}}

where *T* is the temperature, *V* the volume, :math:`n_i` the moles of each species,
and :math:`N_{\text{sp}}` is the number of species in the model.
The moles of the final species is determined through the ideal gas law:

.. math::
    n_{N_{\text{sp}}} = \frac{P V}{\mathcal{R} T} - \sum_{k=1}^{N_{\text{sp}} - 1} n_k

where the *P* is the pressure of the system, and :math:`\mathcal{R}` the ideal gas constant.
In a constant-volume system (CONV), the pressure takes the place of the volume in
the state vector.

.. _jacobian_formulation:

====================
Jacobian Formulation
====================

The governing equations of chemical kinetics include ordinary differential
equations for the (CONP) rate of change of temperature, pressure and species moles':

.. math::
    f &= \frac{\text{d} \Phi}{\text{d} t} \\
      &= \left \lbrace \frac{\text{d} T}{\text{d} t},
      \frac{\text{d} V}{\text{d} t}
      \frac{\text{d} n_1}{\text{d} t}, \frac{\text{d} n_2}{\text{d} t},
      \dotsc, \frac{\text{d} n_{N_{\text{sp}} - 1}}{\text{d} t}
      \right \rbrace^{\text{T}}

where

.. math::
    \frac{\text{d} T}{\text{d} t} &= -
    \frac{\sum_{k=1}^{N_{\text{sp}}} H_k \dot{\omega}_k}{\sum_{k=1}^{N_{\text{sp}}} [C]_k C_{p,k}} \\
    \frac{\text{d}V}{\text{d}t} &= V\left(\frac{T\mathcal{R}}{P} \sum_{k=1}^{N_{\text{sp} -1}} \left( 1 - \frac{W_k}{W_{N_{\text{sp}}}}\right) \dot{\omega}_k + \frac{1}{T} \frac{\text{d} T}{\text{d} t} \right) \\
    \frac{\text{d} n_k}{\text{d} t} &= V \dot{\omega}_k \quad k = 1, \dotsc, N_{\text{sp}} - 1

where :math:`C_{p, k}` is the molar constant-pressure specific heat of species *k*,
:math:`H_k` is the molar enthalpy of species *k*, :math:`\dot{\omega}_k`
is the overall production rate of species *k*, :math:`W_k` the molecular weight of
species *k* and :math:`[C]_k` the concentration of species *k*.

The Jacobian matrix is then filled by the partial derivaties
:math:`\partial f / \partial \Phi`, such that

.. math::
    \mathcal{J}_{i,j} = \frac{\partial f_i}{\partial \Phi_j}

The full set of equations solved by pyJac are available in the supplimental derivations_, while more details on version 2 of pyJac can be found in the published paper_

.. _derivations: https://arxiv.org/src/1809.01029v1/anc/derivations.pdf
.. _paper: https://arxiv.org/abs/1809.01029

.. _units:

=====
Units
=====

pyJac utilizes SI units, namely Pascals for pressure, :math:`m^3` for Volume, Joules for energy, Kelvin for temperature, and kmoles for species moles.

Since the user is free to specify two extensive properties, i.e., Volume and moles for CONP systems, the choice of moles is somewhat arbitrary, as long as the supplied state satistifies the ideal gas relation:

.. math::
    P V = n \mathcal{R} T

One typical choice is to simply pick :math:`V=1 \left[m^3\right]`, :math:`n_k` = :math:`X_k` (the mole fraction of species *k*) and let the total number of moles in the system (*n*) adjust accordingly.  Alternatively, if you
are working on a CFD-problem, a convienient choice is select the volume of each cell in the domain.

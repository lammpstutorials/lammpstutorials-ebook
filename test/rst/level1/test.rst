.. _test-label:

Test RST file
*************

.. container:: hatnote

   Small RST file for testing conversion

.. figure:: ../figures/water-adsorption-dark.png
    :alt: testing figure
    :height: 250
    :align: right
    :class: only-dark

.. figure:: ../figures/water-adsorption-light.png
    :alt: testing figure
    :height: 250
    :align: right
    :class: only-light

..  container:: abstract

    In summatione, *investigatio* in scientia de materia molli et
    simulatione moleculari praebet non solum intellectum profundiorem
    de *structuris* et :math:`x = 2` proprietatibus materiae, :math:`y = 3` sed etiam viam ad
    applicandam technologiam et innovationem in variis campis scientificis
    et industrialibus.

..  container:: abstract

    Simulationes Monte Carlo et Dynamics Molecularis, in mundo soft
    matter, repraesentationem materiae submolecularem exhibent, :cite:`lammps1994`
    delineantes thermodynamicas et kineticas proprietates systematum.
    Moleculae surfactantes in solutionibus amphiphilicis et
    structurae micellarum sunt objecta principalia, scrutantes
    adsorptionem et aggregationem molecularem.

Figure
======

.. figure:: ../figures/example-1-light.png
    :alt: Test figure
    :class: only-light
    :name: fig-lennard-jones

.. figure:: ../figures/example-1-dark.png
    :alt: Test figure
    :class: only-dark

..  container:: figurelegend

    Figure: Just a test figure.

Random text
===========

..  container:: justify

    Some text that is supposed to the justified.

..  container:: justify

    Simulationes Monte Carlo et Dynamics Molecularis, in mundo soft
    matter, repraesentationem materiae submolecularem exhibent,
    delineantes thermodynamicas et kineticas proprietates systematum.
    Moleculae surfactantes in solutionibus amphiphilicis et
    structurae micellarum sunt objecta principalia, scrutantes
    adsorptionem et aggregationem molecularem.

Some sub title
--------------

..  container:: justify

    Some sub content with an equation:

.. math::

    y = x^2

Random LAMMPS code
==================

.. code-block:: lammps

    units lj
    dimension 3
    boundary p p p
    atom_style atomic

    pair_style hybrid/overlay lj/cut 2.5 &
        morse 5.0 1.8 2.5 1.5

    velocity all create 1.0 87287

    timestep 0.005
    fix 1 all nve

    thermo 100
    thermo_style custom step temp etotal
    run 1000

Admonition
==========

.. admonition:: About admonition
    :class: info

    ..  container:: justify

        This is a class info with an equation.

    .. math::
        
        y = a x + b

    ..  container:: justify
        
        And some more text.

        - list item 1
        - list item 2

    .. math::
        
        y = x^2

    ..  container:: justify

        Simulationes Monte Carlo et Dynamics Molecularis, in mundo soft
        matter, repraesentationem materiae submolecularem exhibent.

    .. code-block:: lammps

        fix npt1 all npt temp 300 300 0.1 y 1 1 1 z 1 1 1

    ..  container:: justify

        instead of:

    .. code-block:: lammps

        fix nvt1 all nvt temp 300 300 0.1

    ..  container:: justify

        Simulationes Monte Carlo et Dynamics Molecularis, in mundo soft
        matter, repraesentationem materiae submolecularem exhibent.

..  container:: justify

    Simulationes Monte Carlo et Dynamics Molecularis, in mundo soft
    matter, repraesentationem materiae submolecularem exhibent,
    delineantes thermodynamicas et kineticas proprietates systematum.
    Moleculae surfactantes in solutionibus amphiphilicis et
    structurae micellarum sunt objecta principalia, scrutantes
    adsorptionem et aggregationem molecularem.

    - list item 1
    - list item 2

Include-sub-text
================

.. include:: ../sub-content/subcontent.rst

.. container:: justify

    Final text
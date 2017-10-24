# Welcome to openrocketengine
[![Build status](https://travis-ci.org/cmflannery/openrocketengine.svg?branch=master)](https://travis-ci.org/cmflannery/openrocketengine)

[openrocketengine](https://github.com/cmflannery/openrocketengine) is an open source project designed to help with the design and development of liquid rocket engines.

## Release Notes
__Pre-release - Version 0.0.2__

## Contribution guidlines
Community support is welcome.

For __problems__ with calculations and equations, open an __issue__ and I'll correct it.

For __improvements__ to algorithms, create a __pull request__ that details what has been changed.

For all other contributions, use issues and pull requests at your discretion.

## Verification and Validation
openrocketengine undergoes verification and validation testing in accordance to IEEE 1012-2012.

## Functionality
Currently, the program supports liquid engine design with propellant combinations seen in [propellant.json](https://github.com/cmflannery/openrocketengine/enginebuilder/propellant.json).
Vacuum engine design is not yet fully supported. Namely, there is currently no method used to optimize the exit area of the nozzle. This will likely require more user input as it will be the optimization of nozzle weight, material selection, and expansion area ratio.

#### Current Challenges
What parameters need to be optimized, and what is an optimized engine design?
</br>
__Parameters to Optimize__
* thrust/weight ratio
* material cost
* manufacturing difficulty (this will be hard)
Using the DEAP library, a genetic algorithm will be used to optimize the liquid engine design across these parameters.

#### 3D Modeling
Eventually, I want <code>openrocketengine</code> to output a generic IGES file given the chamber dimensions and design
#### Design Iteration and Testing
openrocketengine should have the ability to take test data inputs and use that information to improve the engine model.

#### Latex output
Generate latex calculations output using template.

## Licensing
openrocketengine is released under the MIT license.

<!-- References -->
[1]: http://soliton.ae.gatech.edu/people/jseitzma/classes/ae6450/bell_nozzle.pdf "GATech: Bell Nozzles"
[2]: https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19710019929.pdf "Design of Liquid Propellant Rocket Engines"
[3]: https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19720026079.pdf "Liquid Propellant Rocket Combustion Instability, NASA SP-194"

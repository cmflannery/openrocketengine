# Welcome to openrocketengine

[openrocketengine](https://github.com/cmflannery/openrocketengine) is an open source project designed to help with the design and development of liquid rocket engines
The equations used in this program were taken from [_Design of Liquid Propellant Rocket Engines_](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19710019929.pdf) by Huzel and Huang.

### Running openrocketengine
To run openrocketengine, execute [engine_builder.py](https://github.com/cmflannery/openrocketengine/engine_builder.py) with a python 2.7 interpreter from the [enginebuilder](https://github.com/cmflannery/openrocketengine/) directory.

### Release Notes
__Alpha Release - Version 0.1__

Currently, the program does not compute propellant curves. Consequently, chamber pressure can not be optimized, and a value of 75 atm is chosen. This is a dangerous assumption. Until [curves.py](https://github.com/cmflannery/openrocketengine/enginebuilder/performance/curves.py) is complete, the results obtained with openrocketengine should not be consulted in the design of any liquid rocket engine.

All analysis is done at steady-state.

### Contribution guidlines
Community support is welcome. Pull requests are encouraged for meaningful changes.

### Verification and Validation
openrocketengine undergoes verification and validation testing in accordance to IEEE 1012-2012.

### Functionality
Currently, the program supports liquid engine design with propellant combinations seen in [propellant.json](https://github.com/cmflannery/openrocketengine/enginebuilder/propellant.json).
Vacuum engine design is not yet fully supported. Namely, there is currently no method used to optimize the exit area of the nozzle. This will likely require more user input as it will be the optimization of nozzle weight, material selection, and expansion area ratio.

##### Current Challenges
What parameters need to be optimized, and what is an optimized engine design?
__Parameters to Optimize__
* thrust/weight ratio
* material cost
* manufacturing difficulty (this will be hard)

##### 3D Modeling
Currently, openrocketengine creates an excel file with some design parameters that can be used to design an engine. Future support for generating '.IGES' files would be great.

Looking at using/improving [this](https://pypi.python.org/pypi/pyIGES/0.0.27) library to generate .IGES files.

##### Design Iteration and Testing
openrocketengine should have the ability to take test data inputs and use that information to improve the engine model.

### References
[GATech: Bell Nozzles](http://soliton.ae.gatech.edu/people/jseitzma/classes/ae6450/bell_nozzle.pdf)
</br>
[_Design of Liquid Propellant Rocket Engines_](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19710019929.pdf)

### Licensing
openrocketengine is released under the MIT license.

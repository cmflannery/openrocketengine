# Welcome to openrocketengine

[openrocketengine](https://github.com/cmflannery/openrocketengine) is an open source project designed to help with the design and development of liquid rocket engines
The equations used in this program were taken from [_Design of Liquid Propellant Rocket Engines_](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19710019929.pdf) by Huzel and Huang.

## Release Notes
__Beta Release__

Currently, the program does not compute propellant curves. Consequently, chamber pressure can not be optimized, and a value of 75 atm is chosen. This is a dangerous assumption. Until [curves.py](https://github.com/cmflannery/openrocketengine/enginebuilder/performance/curves.py) is complete, the results obtained with openrocketengine should not be consulted in the design of any liquid rocket engine.

## Contributing
Community support is welcome. Pull requests are encouraged for meaningful changes.

## Verification and Validation
openrocketengine undergoes verification and validation testing in accordance to IEEE 1012-2012

## Support
Currently, the program supports liquid engine design with propellant combinataions seen in [propellant.json](https://github.com/cmflannery/openrocketengine/enginebuilder/propellant.json).
Vacuum engine design is not yet fully supported.

## Licensing
openrocketengine is released under the MIT license.

Welcome to Open Rocket Engine
=============================

OpenRocketEngine performs the calculations for simple analysis and design of rocket engines.

Basic Usage
-----------

Currently, only SI units are supported.

    import openrocketengine as ore


    ore.Engine(thrust=1000,Tc=3000,pc=3000000,pa=10000,MR=2.77,MW=20,gamma=1.201)
    # once you do this, you can call the properties of Engine to see the
    # design values of your engine.
    # i.e. ore.Isp will return the specific impulse of the engine

Note: checkout "Nomenclature" below if you are unsure about any of the variable used above

These input parameters are typical of what is used in industry design of rocket engines. If you are unfamiliar with this process, I recommend reading "Rocket Propulsion Elements" for basics, and "Mechanics and Thermodynamics of Propulsion" for a more rigorous mathematical overview.

To get these input parameters, you have essentially three options: (I've listed them in order of my preference)
1. NASA CEA
 1. free, but difficult to use
 1. generally trust worthy data
1. Braeuing (http://www.braeunig.us/space/comb.htm)
 1. super simple and fast
 1. data is based on STANJAN (older version of CEA)
 1. no access to actual data files, so plot interpretation can result in signifant errors
1. Testing
 1. challenging, but fun
 1. expensive and not really necessary given the resources above

Nomenclature:
------------
Tc : chamber temperature
thrust : Thrust
pc : chamber pressure
pa : ambient pressure
MR : propellant mixture ratio
MW : propellant gas molecular weight
gamma : ratio of coefficient of heats

# Equations used to define engine parameters and performance
# Distribution approved under MIT License


# import test
def import_test():
    print "equations imported"


# gravitational constant
#   Generally,
#     g0(option):
#   option == 0
#     English Engineering (ft/s/s)
#   option == 1
#     Metric (m/s/s)
def get_g0(option):
    if option == 0:
        return 32.174
    elif option == 1:
        return 9.8066
    else:
        return False


# exit pressure
#   Generally,
#     Pexit(option):
#   option == 0
#     Sea-level, N/m**2
#   option == 1
#     Sea-level, psi
#   option == 2
#     Vacuum
def get_Pexit(option):
    if option == 0:
        return 101325.00   # exit pressure in atmospheres
    elif option == 1:
        return 14.6959
    elif option == 2:
        print "NOTE: NOT ALL FEATURES CURRENTLY SUPPORTED FOR VACUUM ENGINES"
        return 0.00


# total impulse
#   Generally,
#     It(var, option):
#   option == 0:
#     var[] = force, time
#     It = force * time
def get_It(var, option):
    if option == 0:
        force = float(var[0])  # force float to preserve accuracy
        time = float(var[1])   #
        return force * time
    else:
        return False


# specific impulse
#   Generally,
#     Isp(var, option)
def get_Isp(var, option):
    if option == 0:
        force = float(var[0])
        mdot = float(var[1])
        return force/(mdot*g0)
    elif option == 1:
        force = float(vat[0])
        wdot = float(var[1])
        return force/wdot

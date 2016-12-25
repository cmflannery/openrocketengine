import os
import json


with open('propellant.json') as propellant_raw:
    propellant_data = json.load(propellant_raw)
    propellant_raw.close()


# prompt_for_propellants():
#   prompt user for propellants
def prompt_for_propellants():
    confirmed = False
    propellants = []
    while not(confirmed):
        propellants = []
        propellants.append(raw_input("Enter oxidizer in atomic forumula, i.e. O2: "))
        propellants.append(raw_input("Enter fuel in atomic formula/shorthand, i.e. RP1: "))
        print "Oxidizer: ",
        print propellants[0]
        print "Fuel: ",
        print propellants[1]
        while True:
            response = raw_input("Correct? [Y/n]: ")
            if response.upper() == 'Y':
                confirmed = True
                break
            elif response.upper() == 'N':
                confirmed = False
                break
            else:
                print "Please enter Y or n"
    return propellants


# pull_Isp(propellants[], propellant_data[])
#   propellants[0] : Oxidizer
#   propellants[1] : Fuel
def pull_Isp(propellants, propellant_data):
    return propellant_data["Propellants_Dict"]


# main()
#   used for testing and debugging
#   only executes when main script
def main():
    propellants = prompt_for_propellants()
    Isp = pull_Isp(propellants, propellant_data)
    print Isp


if __name__ == "__main__":
    main()

import os
import json


with open('propellant.json') as propellant_combinations:
    d = json.load(propellant_combinations)
    propellant_combinations.close()
    print d


def prompt_for_propellants():
    confirmed = False
    while not(confirmed):
        Oxidizer = raw_input("Enter oxidizer in atomic forumula, i.e. O2: ")
        Fuel = raw_input("Enter fuel in atomic formula/shorthand, i.e. RP1: ")
        print "Oxidizer: ",
        print Oxidizer
        print "Fuel: ",
        print Fuel
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
    return 0


if __name__ == "__main__":
    prompt_for_propellants()

# Parameters and Arguments example
def check_driver_age(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off 😟")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride! 🏎️")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride! 🚀")


check_driver_age()

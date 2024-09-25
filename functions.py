# To create a function, you use the def keyword followed by a name, parentheses, and then the body with the function code:
def rocket_parts():
    return "payload, propellant, structure"


output = rocket_parts()

print(output)


# def distance_from_earth(destination):
#     if destination == "Moon":
#         return "238,855"
#     else:
#         return f"""Unable to compute the distance to {destination}"""


# user_input = input("Enter planet name :")

# print(f"{distance_from_earth(user_input)}")


def days_to_complete(distance, speed):
    hours = distance / speed
    return hours / 24


days = days_to_complete(238855, 75)
print(f"{round(days)} days")


def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank {main_tank}
    External tank {external_tank}
    Hydrogen tank {hydrogen_tank}
    """
    print(output)


generate_report(125, 650, 99)


from datetime import timedelta, datetime


def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")


print(arrival_time("orbit", 0.13))


def variable_length(*args):
    print(args)


variable_length()
variable_length("one", 2, "three", 4)
variable_length(None)


def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"


print(sequence_time(45, 5, 9))

print(sequence_time(180, 240, 56))


def variable_length1(**kwargs):
    print(kwargs)


variable_length1(tanks=1, day="Wednesday", pilots=3)


def crew_members(**kwargs):
    print(f"{len(kwargs)} spacemen assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")


crew_members(captain="Jack Sparrow", pilot="Red Baron", command_pilot="Major Tom")


def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f"{name}, {value}")


fuel_report(George="$400", Ringo="$699", Paul="$999", Bonzo="$.99")

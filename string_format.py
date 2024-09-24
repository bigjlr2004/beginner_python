# Percent sign (%) formatting The placeholder for the variable in the string is %s.
# After the string, use another % character followed by the variable name.
# The following example shows how to format by using the % character:

mass_percentage = "1/6"
print(
    "On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage
)


print(
    """Both sides of the %s get the same amount of sunlight, but only one side is seen from %s
     because the %s rotates around its own axis when it orbits %s."""
    % ("Moon", "Earth", "Moon", "Earth")
)

# The format() method
# The .format() method uses braces ({}) as placeholders within a string,
# and it uses variable assignment for replacing text.

mass_percentage = "1/6"
print(
    """You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format(
        "Moon", mass_percentage
    )
)

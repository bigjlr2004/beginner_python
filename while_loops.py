# user_input = ""

# while user_input.lower() != "done":
#     user_input = input("Enter a new value, or done when done")


# Create the variable for user input
# user_input = ""
# Create the list to store the values
# inputs = []

# # # The while loop
# # while user_input.lower() != "done":
# #     # Check if there's a value in user_input
# #     if user_input:
# #         # Store the value in the list
# #         inputs.append(user_input)
# #     # Prompt for a new value
# #     user_input = input("Enter a new value, or done when done")


# user_input = ""
# planets = []

# while user_input.lower() != "done":
#     # check if there's a value in user_input
#     if user_input:
#         inputs.append(user_input)
#     user_input = input("Enter a new value, or done when done: ")
# print(inputs)

countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
print("Blast off!! 🚀")

# from time import sleep

# countdown = [4, 3, 2, 1, 0]

# for number in countdown:
#     print(number)
#     sleep(1)  # Wait 1 second
# print("Blast off!! 🚀")

planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]

count = len(planets)
for planet in planets:
    print(f"The {count} planet is ", planets[count - 1])
    count -= 1

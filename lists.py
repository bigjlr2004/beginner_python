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

print("The first planet is", planets[0])
print(planets[1])
print(planets[2])
print(planets[3])
print(planets[4])
print(planets[5])
print(planets[6])
print(planets[7])

planets[3] = "Red Planet"
print("Mars is known as the", planets[3])

print("There are", len(planets), " planets in the solar system.")

planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, " planets in the solar system.")

planets.pop()
print("No there are definitely", len(planets), " planets in the solar system.")

print("The last planet in the solar system is", planets[-1])
print("The first planet in the solar system is", planets[-(len(planets))])
print("The penultimate planet in the solar system is", planets[-2])

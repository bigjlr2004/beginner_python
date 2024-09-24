planet = {"name": "Mars", "moons": 2}

print(planet.get("name"))

print(planet["name"])
print(planet["moons"])

print(f'{planet["name"]} has {planet['moons']} moons.')

planet.update(circumference = {'polar': 6752, 'equatorial': 6792})


print(f'{planet["name"]} has a polar circumference of {planet["circumference"]["polar"]}')
print(f'{planet["name"]} has a equatorial circumference of {planet["circumference"]["equatorial"]}')

planet_moons = {
'mercury': 0,
'venus': 0,
'earth': 1,
'mars': 2,
'jupiter': 79,
'saturn': 82,
'uranus': 27,
'neptune': 14,
'pluto': 5,
'haumea': 2,
'makemake': 1,
'eris': 1
}

for key in planet_moons.keys():
    print(f'{key}: {planet_moons[key]}')

moons = planet_moons.values()
total_planets = len(planet_moons.keys())

for moon in moons:
    print(moon)

print(total_planets)

average_moons = sum(moons)/total_planets
print(f'Average moons: {average_moons}')

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

average = total_moons/total_planets
print(f'Each planet has an average of {round(average)} moons.')

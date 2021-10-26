import ephem
from datetime import datetime, date, time

name_pl=[
	{"Number": "0", "Name": "Mercury"},
	{"Number": "1", "Name": "Venus"},
	{"Number": "2", "Name": "Earth"},
	{"Number": "3", "Name": "Mars"},
	{"Number": "4", "Name": "Jupiter"},
	{"Number": "5", "Name": "Saturn"},
	{"Number": "6", "Name": "Uranus"},
	{"Number": "7", "Name": "Neptune"}
]

print("Hi, input Name of the planet: ")

for nam1 in name_pl:
 	print(nam1.get("Number") + " " + nam1.get("Name"))
	
planet =input("Planet number:")
planet_number = round(int(planet),0)

for planet_name_user in name_pl:
	if round(int(planet_name_user.get("Number")),0) == planet_number:
		print(planet_name_user.get("Name"))


t=datetime.date.today()
print(t)

mars = ephem.Mars('2000/01/01')
constellation = ephem.constellation(mars)
print(constellation)

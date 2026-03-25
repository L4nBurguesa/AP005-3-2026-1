##### Get A Key
# Diccionario edificios
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
print(building_heights["Burj Khalifa"])  # Imprime altura del Burj Khalifa
print(building_heights["Ping An"])       # Imprime altura del Ping An

# Diccionario de signos zodiacales agrupados por elemento string-list
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])          # Imprime signos de tierra
print(zodiac_elements["fire"])           # Imprime signos de fuego

# Verificación si dentro de un diccionario esta una key
key_to_check = "Landmark 81"
if key_to_check in building_heights:
    print(building_heights[key_to_check])

# Agregar nueva key al diccionario de signos
zodiac_elements["energy"] = "Not a Zodiac element"

# validacion de keys
if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])

# Obtener valores de manera segura usando .get()
print(building_heights.get("Shanghai Tower"))  # imprime
print(building_heights.get("My House"))        # imprime vacio

# Diccionario de IDs de usuarios
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder", 1000)      # Devuelve de teraCoder
print(tc_id)
stack_id = user_ids.get("superStackSmash", 100000)  # No existe, devuelve 100000
print(stack_id)

# Diccionario---uso de .pop() para eliminar keys
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(320291, "No Prize"))  # Elimina y muestra "Gift Basket"
print(raffle)
print(raffle.pop(100000, "No Prize"))  # Clave inexistente, devuelve "No Prize"
print(raffle)
print(raffle.pop(872921, "No Prize"))  # Elimina y devuelve "Concert Tickets"
print(raffle)

# Diccionario
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop("stamina grains", 0)  # Suma puntos de salud y elimina item
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)    # No existe, suma 0
print(available_items)  # Muestra items restantes
print(health_points)    # Muestra puntos de salud totales

# Diccionario 
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(list(test_scores))       # Lista de nombres de estudiantes
for student in test_scores.keys():
    print(student)             # imprime nombres

# Diccionarios 
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
users = user_ids.keys()        # Claves de usuarios
lessons = num_exercises.keys() # Claves de ejercicios
print(users)
print(lessons)

# Obtener todos los valores de puntajes y sumatoria de ejercicios
for score_list in test_scores.values():
    print(score_list)           # Muestra solo los puntajes
total_exercises = 0
for exercises in num_exercises.values():
    total_exercises += exercises
print(total_exercises)         # Total de ejercicios

# Diccionario de empresas y su valor en billones
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars. ")

# Diccionario de porcentaje de mujeres por ocupación
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for occupation, percentage in pct_women_in_occupation.items():
    print("Women make up " + str(percentage) + " percent of " + occupation + "s.")
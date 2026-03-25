#asigna variable para dos diccionarios y imprime
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}
print(sensors)
print(num_cameras)

#asigna variable para diccionario string-string y imprime
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
print(translations)

# Verifiying an error:
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
# print(powers)

#diccionario string-lista
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)

#diccionario vacio
my_empty_dictionary = {}
print(my_empty_dictionary)

#diccionario string- int                 
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["cheesecake"] = 8 #agrega key a diccionario menu
print("After", menu)

# reescribe valor del diccionario 
animals_in_zoo = {"dinosaurs": 0}#reescribe 1
animals_in_zoo = {"dinosaurs": 0}#reescribe 2
animals_in_zoo = {"horses": 2}#reescribe 3
print(animals_in_zoo)

# agrega 3 keys al diccionario
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensors)

sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("After", sensors)

#hace lo mismo todo esto utilizando .update
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

# cambia el valor de oatmeal
menu["banana"] = 3
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["oatmeal"] = 5 # lo cambia aqui <----------
print("After", menu)

#diccionariop de oscars
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners)
print()
#agrega keys a diccionario oscars
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After1", oscar_winners)
print()

#cambia el valor de key: best picture por otro
oscar_winners["Best Picture"] = "Moonlight"
print("After2", oscar_winners)

#maneras de estructurar un diccionario parte por parte
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents)#error sale datos confusos

students = {key:value for key, value in zip(names, heights)}#estructura el diccionario con la relacion de zipestudiantes
print(students)#ahora si imprime bien


#pasa lo mismo de arriba pero utiliza otro ejemplo
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks) #no imprime algo <.....

drinks_to_caffeine = {key:value for key, value in zipped_drinks}#Estructura diccionario
print(drinks_to_caffeine)


# misma estructura pero ahora agrega datos al diccionario
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key:value for key, value in zip(songs, playcounts)} #crea diccionario
print(plays)

plays.update({"Purple Haze": 1}) # agrega dato
plays.update({"Respect": 94}) #agrega dato
print("After: ", plays)

# toma como valor de keys un diccionario plays y imprime a la perfeccion 
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
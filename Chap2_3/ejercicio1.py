import csv
from math import sqrt
users = {}
# Abrir el archivo CSV
with open('./Dataset1/BX-Book-Ratings.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    # Iterar a través de los datos
    for row in reader:
        # Obtener los valores de la fila
        user_id = row[0]
        book_id = row[1]
        rating = int(row[2])
        
        # Si el usuario aún no está en el diccionario, crear un nuevo diccionario para él
        if user_id not in users:
            users[user_id] = {}
        
        # Agregar el libro y la puntuación al diccionario del usuario
        users[user_id][book_id] = rating

with open('./Dataset1/BX-Users.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    
    # Crear un diccionario vacío para almacenar los datos
    user_data = {}
    
    # Iterar a través de los datos
    for row in reader:
        # Obtener los valores de la fila
        user_id = row[0]
        location = row[1]
        age = row[2] if row[2] != '\\N' else None
        
        # Dividir la ubicación en acrónimo, ciudad y país
        location_parts = location.split(', ')
        acronym = location_parts[0]
        city = location_parts[1] if len(location_parts) > 1 else None
        country = location_parts[-1] if len(location_parts) > 1 else None
        
        # Agregar los datos del usuario al diccionario
        user_data[user_id] = {
            'acronym': acronym,
            'age': age,
            'city': city,
            'country': country
        }

class Similitud:
    def __init__(self, nombre1, nombre2, metrica):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.metrica = metrica
        
        self.rating1 = users[self.nombre1]
        self.rating2 = users[self.nombre2]
    def manhattan(self): 
        distance = 0 
        common_items = set(self.rating1.keys()) & set(self.rating2.keys())
        if len(common_items) == 0:
            return 0
        for key in common_items: 
            distance += abs(self.rating1[key] - self.rating2[key]) 
        return distance
        
    def euclidiana(self): 
        distance = 0 
        common_items = set(self.rating1.keys()) & set(self.rating2.keys())
        if len(common_items) == 0:
            return 0
        for key in common_items: 
            distance += pow(abs(self.rating1[key] - self.rating2[key]),2) 
        return pow(distance, 1/2)
    def Pearson(self): 
        multi = 0 
        sumrating1 = 0
        sumrating2 = 0
        sqrating1 = 0
        sqrating2 = 0
        distance = 0
        common_items = set(self.rating1.keys()) & set(self.rating2.keys())
        aux = len(common_items)
        if aux == 0:
            return 0
        for key in common_items: 
            multi += self.rating1[key] * self.rating2[key]
            sumrating1 += self.rating1[key]
            sqrating1 += self.rating1[key]**2
            sumrating2 += self.rating2[key]
            sqrating2 += self.rating2[key]**2
        deno = sqrt(sqrating1 - (sumrating1**2)/aux)*sqrt(sqrating2 - (sumrating2**2)/aux)
        if deno == 0:
            return 0
        else: 
            distance = (multi - ((sumrating1 * sumrating2)/ aux)) / deno
            return distance 
    def Cosine(self): 
        common_items = set(self.rating1.keys()) & set(self.rating2.keys())
        print(common_items)
        if len(common_items) == 0:
            return 0
        numerador = sum(self.rating1[item] * self.rating2[item] for item in common_items)
        denominador1 = sum(self.rating1[item]**2 for item in self.rating1.keys())
        denominador2 = sum(self.rating2[item]**2 for item in self.rating2.keys())
        distance = numerador / (sqrt(denominador1) *  sqrt(denominador2))
        return distance
    def calcular_similitud(self):
        if self.metrica == 'manhattan':
            similitud = self.manhattan()
        elif self.metrica == 'euclidiana':
            similitud = self.euclidiana()
        elif self.metrica == 'cosine':
            similitud = self.Cosine()
        elif self.metrica == 'pearson':
            similitud = self.Pearson()
        print(similitud)

name1 = input("Ingrese el nombre de la primera persona: ")
name2 = input("Ingrese el nombre de la segunda persona: ")
metric_type = input("Ingrese el tipo de métrica (manhattan, euclidiana, cosine, pearson): ")
sim = Similitud(name1, name2, metric_type)
sim.calcular_similitud()
# Imprimir el diccionario para el usuario con ID "276725" como ejemplo
# print(users.get('276747', {}))

# Imprimir el diccionario para el usuario con id "1" como ejemplo
# print(user_data.get('5555', {}))
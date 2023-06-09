import csv
from math import sqrt
users = {}

with open('Movie_Ratings.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(reader):
        if i == 0:
            headers = row[1:]
        else:
            movie = row[0]
            for j, rating in enumerate(row[1:]):
                if rating != "":
                    user = headers[j]
                    if user not in users:
                        users[user] = {}
                    users[user][movie] = float(rating)
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
# print(manhattan(users['Heather'], users['Bryan']))
# print(euclidiana(users['Heather'], users['Bryan']))
# print(Pearson(users['Heather'], users['Bryan']))
# print(Cosine(users['Heather'], users['Bryan']))
name1 = input("Ingrese el nombre de la primera persona: ")
name2 = input("Ingrese el nombre de la segunda persona: ")
metric_type = input("Ingrese el tipo de métrica (manhattan, euclidiana, cosine, pearson): ")
sim = Similitud(name1, name2, metric_type)
sim.calcular_similitud()
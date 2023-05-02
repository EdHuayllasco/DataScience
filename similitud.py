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
        commonRatings = False

        for key in self.rating1: 
            if key in self.rating2: 
                distance += abs(self.rating1[key] - self.rating2[key]) 
                commonRatings = True
        if commonRatings: 
                return distance 
        else: 
                return -1
    def euclidiana(self): 
        distance = 0 
        commonRatings = False

        for key in self.rating1: 
            if key in self.rating2: 
                distance += pow(abs(self.rating1[key] - self.rating2[key]),2) 
                commonRatings = True
        if commonRatings: 
                return pow(distance, 1/2)
        else: 
                return -1
    def Pearson(self): 
        multi = 0 
        sumrating1 = 0
        sumrating2 = 0
        sqrating1 = 0
        sqrating2 = 0
        aux = 0
        distance = 0

        for key in self.rating1: 
            if key in self.rating2: 
                multi += self.rating1[key] * self.rating2[key]
                sumrating1 += self.rating1[key]
                sqrating1 += self.rating1[key]**2
                sumrating2 += self.rating2[key]
                sqrating2 += self.rating2[key]**2
                aux += 1
        if aux == 0: 
            return 0
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
        multi = 0 
        sqrating1 = 0
        sqrating2 = 0

        for key in self.rating1: 
            sqrating1 += self.rating1[key]**2
            if key in self.rating2: 
                multi += self.rating1[key] * self.rating2[key]
        for key in self.rating2:
            sqrating2 += self.rating2[key]**2
        distance = multi / (sqrt(sqrating1) *  sqrt(sqrating2))
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
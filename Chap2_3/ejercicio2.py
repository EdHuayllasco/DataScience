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
    def __init__(self, nombre1, metrica):
        self.nombre1 = nombre1
        self.metrica = metrica
    def manhattan(self, rating1, rating2): 
        distance = 0 
        common_items = set(rating1.keys()) & set(rating2.keys())
        if len(common_items) == 0:
            return 0
        for key in common_items: 
            distance += abs(rating1[key] - rating2[key]) 
        return distance
        
    def euclidiana(self, rating1, rating2): 
        distance = 0 
        common_items = set(rating1.keys()) & set(rating2.keys())
        if len(common_items) == 0:
            return 0
        for key in common_items: 
            distance += pow(abs(rating1[key] - rating2[key]),2) 
        return pow(distance, 1/2)
    def Pearson(self, rating1, rating2): 
        multi = 0 
        sumrating1 = 0
        sumrating2 = 0
        sqrating1 = 0
        sqrating2 = 0
        distance = 0
        common_items = set(rating1.keys()) & set(rating2.keys())
        aux = len(common_items)
        if aux == 0:
            return 0
        for key in common_items: 
            multi += rating1[key] * rating2[key]
            sumrating1 += rating1[key]
            sqrating1 += rating1[key]**2
            sumrating2 += rating2[key]
            sqrating2 += rating2[key]**2
        deno = sqrt(sqrating1 - (sumrating1**2)/aux)*sqrt(sqrating2 - (sumrating2**2)/aux)
        if deno == 0:
            return 0
        else: 
            distance = (multi - ((sumrating1 * sumrating2)/ aux)) / deno
            return distance 
    def Cosine(self, rating1, rating2): 
        common_items = set(rating1.keys()) & set(rating2.keys())
        print(common_items)
        if len(common_items) == 0:
            return 0
        numerador = sum(rating1[item] * rating2[item] for item in common_items)
        denominador1 = sum(rating1[item]**2 for item in rating1.keys())
        denominador2 = sum(rating2[item]**2 for item in rating2.keys())
        distance = numerador / (sqrt(denominador1) *  sqrt(denominador2))
        return distance
    def computeNearestMan(self,username, users):
        distances = []
        for user in users:
            if user != username:
                distance = self.manhattan(users[user], users[username])
                distances.append((distance, user))
        distances.sort()
        return distances
    def computeNearestEu(self,username, users):
        distances = []
        for user in users:
            if user != username:
                distance = self.euclidiana(users[user], users[username])
                distances.append((distance, user))
        distances.sort()
        return distances
    def computeNearestPer(self,username, users):
        distances = []
        for user in users:
            if user != username:
                distance = self.Pearson(users[user], users[username])
                distances.append((distance, user))
        distances.sort()
        return distances
    def computeNearestCos(self,username, users):
        distances = []
        for user in users:
            if user != username:
                distance = self.Cosine(users[user], users[username])
                distances.append((distance, user))
        distances.sort()
        return distances
    def calcular_similitud(self):
        if self.metrica == 'manhattan':
            similitud = self.computeNearestMan(self.nombre1, users)[0][1]
        elif self.metrica == 'euclidiana':
            similitud = self.computeNearestEu(self.nombre1, users)[0][1]
        elif self.metrica == 'cosine':
            similitud = self.computeNearestCos(self.nombre1, users)[0][1]
        elif self.metrica == 'pearson':
            similitud = self.computeNearestPer(self.nombre1, users)[0][1]
        print(similitud)
# print(manhattan(users['Heather'], users['Bryan']))
# print(euclidiana(users['Heather'], users['Bryan']))
# print(Pearson(users['Heather'], users['Bryan']))
# print(Cosine(users['Heather'], users['Bryan']))
name1 = input("Ingrese el nombre de la primera persona: ")
metric_type = input("Ingrese el tipo de métrica (manhattan, euclidiana, cosine, pearson): ")
sim = Similitud(name1, metric_type)
sim.calcular_similitud()
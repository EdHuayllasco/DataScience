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
    def manhattan(rating1, rating2): 
        distance = 0 
        commonRatings = False

        for key in rating1: 
            if key in rating2: 
                distance += abs(rating1[key] - rating2[key]) 
                commonRatings = True
        if commonRatings: 
                return distance 
        else: 
                return -1
    def euclidiana(rating1 , rating2): 
        distance = 0 
        commonRatings = False

        for key in rating1: 
            if key in rating2: 
                distance += pow(abs(rating1[key] - rating2[key]),2) 
                commonRatings = True
        if commonRatings: 
                return pow(distance, 1/2)
        else: 
                return -1
    def Pearson(rating1, rating2): 
        multi = 0 
        sumrating1 = 0
        sumrating2 = 0
        sqrating1 = 0
        sqrating2 = 0
        aux = 0
        distance = 0

        for key in rating1: 
            if key in rating2: 
                multi += rating1[key] * rating2[key]
                sumrating1 += rating1[key]
                sqrating1 += rating1[key]**2
                sumrating2 += rating2[key]
                sqrating2 += rating2[key]**2
                aux += 1
        if aux == 0: 
            return 0
        deno = sqrt(sqrating1 - (sumrating1**2)/aux)*sqrt(sqrating2 - (sumrating2**2)/aux)
        if deno == 0:
            return 0
        else: 
            distance = (multi - ((sumrating1 * sumrating2)/ aux)) / deno
            return distance 
    def Cosine(rating1, rating2): 
        common_items = set(rating1.keys()) & set(rating2.keys())
        print(common_items)
        if len(common_items) == 0:
            return 0
        multi = 0 
        sqrating1 = 0
        sqrating2 = 0

        for key in rating1: 
            sqrating1 += rating1[key]**2
            if key in rating2: 
                multi += rating1[key] * rating2[key]
        for key in rating2:
            sqrating2 += rating2[key]**2
        distance = multi / (sqrt(sqrating1) *  sqrt(sqrating2))
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
            similitud = self.computeNearestPer(self.nombre1, users) 
        print(similitud)
# print(manhattan(users['Heather'], users['Bryan']))
# print(euclidiana(users['Heather'], users['Bryan']))
# print(Pearson(users['Heather'], users['Bryan']))
# print(Cosine(users['Heather'], users['Bryan']))
name1 = input("Ingrese el nombre de la primera persona: ")
metric_type = input("Ingrese el tipo de métrica (manhattan, euclidiana, cosine, pearson): ")
sim = Similitud(name1, metric_type)
sim.calcular_similitud()
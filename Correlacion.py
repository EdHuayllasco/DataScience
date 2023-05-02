import csv

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
def euclidiana(rating1, rating2): 
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
print(manhattan(users['Heather'], users['Bryan']))
print(euclidiana(users['Heather'], users['Bryan']))
print(Pearson(users['Heather'], users['Bryan']))
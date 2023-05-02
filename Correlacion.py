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


print(users)
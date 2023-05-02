import csv

# Leemos los datos del archivo CSV
with open('Movie_Ratings.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Convertimos la matriz de datos a numérica
for i in range(1, len(data)):
    for j in range(1, len(data[i])):
        if data[i][j] != '':
            data[i][j] = int(data[i][j])
        else:
            data[i][j] = 0
# Métrica Manhattan
def manhattan(user1, user2):
    distance = 0
    for i in range(1, len(data[user1])):
        if data[user1][i] != 0 and data[user2][i] != 0:
            distance += abs(data[user1][i] - data[user2][i])
    return distance

# Distancia Euclidiana
def euclidean(user1, user2):
    distance = 0
    for i in range(1, len(data[user1])):
        if data[user1][i] != 0 and data[user2][i] != 0:
            distance += (data[user1][i] - data[user2][i]) ** 2
    return distance ** 0.5

# Similitud de Cosenos
def cosine(user1, user2):
    dot_product = 0
    norm_user1 = 0
    norm_user2 = 0
    for i in range(1, len(data[user1])):
        dot_product += data[user1][i] * data[user2][i]
        norm_user1 += data[user1][i] ** 2
        norm_user2 += data[user2][i] ** 2
    return dot_product / ((norm_user1 ** 0.5) * (norm_user2 ** 0.5))

# Coeficiente de Pearson
def pearson(user1, user2):
    n = 0
    sum_user1 = 0
    sum_user2 = 0
    sum_squares_user1 = 0
    sum_squares_user2 = 0
    sum_products = 0
    for i in range(1, len(data[user1])):
        if data[user1][i] != 0 and data[user2][i] != 0:
            n += 1
            sum_user1 += data[user1][i]
            sum_user2 += data[user2][i]
            sum_squares_user1 += data[user1][i] ** 2
            sum_squares_user2 += data[user2][i] ** 2
# Solicitamos los nombres de los usuarios y la métrica a utilizar
user1 = input("Ingresa el nombre del primer usuario: ")
user2 = input("Ingresa el nombre del segundo usuario: ")
metric = input("Ingresa la métrica a utilizar (manhattan, euclidean, cosine, pearson): ")

# Buscamos los índices de los usuarios en la matriz de datos
user1_index = -1
user2_index = -1
for i in range(1, len(data)):
    if data[i][0] == user1:
        user1_index = i
    elif data[i][0] == user2:
        user2_index = i

# Calculamos la distancia/similitud correspondiente utilizando la métrica seleccionada
if metric == 'manhattan':
    result = manhattan(user1_index, user2_index)
    print("La distancia Manhattan entre", user1, "y", user2, "es:", result)
elif metric == 'euclidean':
    result = euclidean(user1_index, user2_index)
    print("La distancia Euclidiana entre", user1, "y", user2, "es:", result)
elif metric == 'cosine':
    result = cosine(user1_index, user2_index)
    print("La similitud de cosenos entre", user1, "y", user2, "es:", result)
elif metric == 'pearson':
    result = pearson(user1_index, user2_index)
    print("El coeficiente de Pearson entre", user1, "y", user2, "es:", result)
else:
    print("La métrica seleccionada no es válida.")
import json

f = open('../data/paginaSiete_order.json')
data = json.load(f)

title = []
for i in range(len(data)):
    title.append(data[i]['titulo'])

# clasificar a todas las listas anidadas de title
title2 = [item for sublist in title for item in sublist]
print(title2)




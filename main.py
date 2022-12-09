items = [
    ["в", 3, 25],  # Винтовка
    ["п", 2, 15],  # Пистолет
    ["б", 2, 15],  # Боекомплект
    ["а", 2, 20],  # Аптечка
    ["н", 1, 15],  # Нож
    ["т", 3, 20],  # Топор
    ["о", 1, 25],  # Оберег
    ["ф", 1, 15],  # Фляжка
    ["д", 1, 10],  # Антидот
    ["к", 2, 20],  # Еда
    ["р", 2, 20],  # Арбалет
    ["и", 1, 5]   # Ингалятор
]  

for item in items:
    size = item[1]
    points = item[2]
    space_points = points / size
    item.append(int(space_points))

start_points = 10  
plus_points = 0  
minus_points = 0  
inventory = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
space_l = 9

while space_l > 0:  

    max_item = [' ', 0, 0, 0]
    for item in items:  
        if item[3] > max_item[3]:
            max_item = item
    items[items.index(max_item)], items[10] = items[10], items[items.index(max_item)]

    if space_l < items[10][1]:  
        items[10][3] = 0
        continue

    for rows in range(3):
        for columns in range(3):

            if items[10][1] == 1:  
                if inventory[rows][columns] == ' ':  
                    inventory[rows][columns] = items[10][0] 
                    space_l -= items[10][1] 
                    plus_points += items[10][2]
                    items[10][1], items[10][2], items[10][3] = 0, 0, 0  
                else:
                    continue

            if items[10][1] == 2: 
                if columns < 2:
                    if inventory[rows][columns] == ' ' and inventory[rows][columns + 1] == ' ':
                        inventory[rows][columns] = items[10][0]
                        inventory[rows][columns + 1] = items[10][0]
                        space_l -= items[10][1]
                        plus_points += items[10][2]
                        items[10][1], items[10][2], items[10][3] = 0, 0, 0
                    else:
                        continue
                else:
                    break

            if items[10][1] == 3: 
                if columns == 0:
                    inventory[rows][columns] = items[10][0]
                    inventory[rows][columns + 1] = items[10][0]
                    space_l -= items[10][1]
                    plus_points += items[10][2]
                    items[10][1], items[10][2], items[10][3] = 0, 0, 0
                else:
                    break

for item in items:  
    minus_points += item[2]

points = start_points + plus_points - minus_points  

for i in range(3): 
    print(inventory[i])
print('Итоговые очки выживания: ', points)

database = []
with open('./status.txt') as file:
    content = file.readlines()
    # print(content[1].strip())
    for each in content:
        updated=each.strip().split(',')
        database.append(updated)
print(database)        
print(database[2][1])
print(database[2:])



    





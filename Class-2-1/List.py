# List, Dictionary, Function

snacks = ["Chips", "Soda", "Cake"]
# print(snacks)

# snacks.append("Cookies")
# print(snacks)

# snacks.remove("Soda")
# print(snacks)

# snacks.sort()
# print(snacks)

# print("middle indexed snake: ", snacks[-2])

# snacks[1] = "Juice"
# print(snacks)

# snacks.insert(1, "Chocolate")
# print(snacks)

# del snacks[3]
# print(snacks)

snacks = sorted(snacks, reverse = False)
print(snacks)

party_bag = [
    ["Chips", "Cookies"],
    ["Cake", "Juice"],
    ["Soda", "Pizza"]
]

for bag in party_bag:
    for item in bag:
        for character in item:
            print(character)
            
table1 = ["Chips", "Juice"]            
table2 = ["Cake", "Cookie"]      

full_table = table1 + table2 #Concatinet
print(full_table)      
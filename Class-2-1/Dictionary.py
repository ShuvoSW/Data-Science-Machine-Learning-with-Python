# Key, Value
# guest = {
#     "name": "Alice",
#     "age": 25,
#     "favourite_snack": "Cake"
# }
# print(guest["name"])
# guest["name"] = "joy"
# print(guest)
# guest.pop("age")
# print(guest)

# for key, val in guest.items():
#     print(key, val)
    
party_guests = {
    "guests1": {"name": "Alice", "favourite_snack": "Cake"},
    "guests2": {"name": "Sunny", "favourite_snack": ["Chips", "Choco"]}
}    
print(party_guests["guests2"]["favourite_snack"][0])
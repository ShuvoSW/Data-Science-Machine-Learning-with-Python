# thisset = {"Apple", "Banana", "Apple", "Grape", True, 1, 2}
# print(thisset)
# thisset.add("orange")
# print(thisset)

# tropical = {"Pineapple", "mango", "papaya"}

# thisset.update(tropical)
# print(thisset)
# print(tropical)

# thisset.remove("papaya")
# print(thisset)

# thisset.discard("Banana")
# print(thisset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "a","c"}
set3 = set1.union(set2)
print(set3)

set3 = set1.intersection(set2)
print(set3)

set4 = set2.difference(set1)
print(set4)
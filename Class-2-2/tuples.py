mytuple = ("apple", "banana", "cherry")
print(mytuple)

print(len(mytuple))
print(mytuple[1])
print(mytuple[-1])
print(mytuple[2:5])

convert_to_list = list(mytuple)
print(convert_to_list)
convert_to_list.append("orange")
convert_to_list[1] = "kiwi"
youtuple = tuple(convert_to_list)
print(youtuple)
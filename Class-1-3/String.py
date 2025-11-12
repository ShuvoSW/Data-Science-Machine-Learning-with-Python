tweet = "hello Earth, Shuvo here reporting form sector 9"
print("Start of tweet : ", tweet[:2])
print("Last of tweet : ", tweet[-3:])
print("Slice middle part : ", tweet[ 3:5])
print("Backwards tweet : ", tweet[::-1])
print("Alien code : ", tweet[::2])

messy = "Visit##Earth!! It's#sooooo!!!green###"
cleaned = messy.replace("!", "").replace("#", "").replace("ssooooo", "so")
print(cleaned.upper())
print(cleaned.count('i'))

planet = "Earth"
activity = "farming"
alien_name = 22.
print(f" Alins {alien_name:.2f}")

tweet =  "Shuvo on the " + planet +  " to " + activity + "ff"
print(tweet)

insult = "You fight like a dairy farmer"
words = insult.split("i")
print("Words in insult:", words)
# #Class
# class Avenger:
#     def fight(self):
#         print("Avengers, Start fighting !!")
 
# #Object       
# ironman = Avenger()    
# Hulk = Avenger()    

# ironman.fight()
# Hulk.fight()


# #Introducing method

# class Avenger:
#     def introduce(self, name):
#         print(f"I am {name} and I protect the workd")
 
# #Object       
# ironman = Avenger()    
# thor = Avenger()    
   

# ironman.introduce("Tony stark")
# thor.introduce("Thor")

#Default constructor
# class Avenger:
#     def __init__(self):
#         print("A new avenger has joined the team")
        
# captain = Avenger()        

# Parameterized constructor

# class Avenger:
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#     def show(self):
#         print(f"{self.name} has power: {self.power}")
   
# input_x = input("Enter val: ")        
# spiderman = Avenger(input_x, "web-slinging")
# spiderman.show()


#Inheritance
class Hero:
    def __init__(self, name):
        self.name =name
        
    def protect(self):
        print("protecting the world")

class IronMan(Hero):
    def fly(self):
        print(f"{self.name}Flying")        
        
tony = IronMan("Ironman")
tony.fly()        
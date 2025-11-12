# Dad Mr. object
# Daughter Multi
# Mother -- Mrs. classy
# Son - naughty Inno

# Single Inheritance
# class Father:
#     def skills(self):
#         print("I csn code in c++")
        
# class Son(Father):
#     pass

# inno = Son()

# inno.skills()        


#Hierarchical inheritance
# class Mom():
#     def cooking(self):
#         print("I can cool deliciouse Briayani")
        
# class Inno(Mom):
#      pass  
 
# class Multi(Mom):
#      pass     
 
# inno = Inno()
# multi = Multi()
 
# inno.cooking()
# multi.cooking()


#Multi level inheritance
# class Grandpa:
#     def advice(self):
#         print("Never ignore bugs")
        
# class Father(Grandpa):
#     def teach(self):
#         print("Practice C++ will make you logical and increase thinking capability")        

# class Son(Father):
#     pass

# multi = Son()
# multi.advice()        
# multi.teach()        


#Multiple inheritance
# class Mother:
#     def discipline(self):
#         print("Go to bed at 10 PM")
        
# class UncleLogic:
#     def math(self):
#         print("Solving equation")        
        
# class Daughter(Mother, UncleLogic):
#     pass

# multi=  Daughter()      
# multi.discipline()
# multi.math()


# method Overloading 
# class ReportCard:
#     def marks(self, math=None, english =None):
#         if math is not None and english is not None:
#             print(f"Math: {math}, English: {english}")
#         elif math is not None:
#             print(f"Math: {math}")    
#         else:
#             print("No mark given")    

# inno_report = ReportCard()
# inno_report.marks(90)
# inno_report.marks(90, 85)


#Method overaiding
# class Parent:
#     def role(self):
#         print("I am the boss")
        
# class Child(Parent):
#     def role(self):
#         print("i run the show now")        
        
# mult = Child()
# mult.role()     

# parent_obj = Parent()
# parent_obj.role()  


# encapsulation |||| parameter , value
# class Family:
#     def __init__(self):
#         self.__secret_find = 500 #Private variable
        
#     def get_fund(self):
#         return self.__secret_find
    
# dad = Family()
# print(dad.get_fund())    


class Role:
    def act(self):
        pass
    
class Cook(Role):
    def act(self):
        print("Cooling Dinner")
        
class Doctor(Role):
    def act(self):
        print("Prescribing medicine")
        
def daily_roles(role):       
    role.act()
    
daily_roles(Cook())    
daily_roles(Doctor())    
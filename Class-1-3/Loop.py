# # For loops
# donuts = ["glazed", "chocolate", "galactic sprinkle", "neutron nut"]
# for donut in donuts:
#     print(donut)
# #While loop]
# angle = 0 
# while angle <= 90:
#     print(angle)
#     angle += 30
# # for range function
# for pod in range(5):
#     print("🧹 Cleaning pod number", pod)    
# for pod in range(1,5):
#     print("🧹 Cleaning pod number", pod)    
# for pod in range(2,5,2):
#     print("🧹 Cleaning pod number", pod)    

# Break & Continue    
protocols = ["ok", "ok", "bad", "ok", "bad", "ok"]

for i, p in enumerate(protocols):
    if p == "bad":
        break
    # print( i, p)    
for i, p in enumerate(protocols):
    if p == "bad":
        continue
    print( i, p)    
    
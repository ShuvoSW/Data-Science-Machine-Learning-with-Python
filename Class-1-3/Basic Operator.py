chocolate = 3
sprinkle = 2
price_choco = 5
price_sprinkle = 6

total_cost = chocolate * price_choco + sprinkle * price_sprinkle
print(total_cost)

tax = total_cost * 0.10
final_cost = total_cost + tax

print("Final cost :", final_cost)

total_slices = 8
aliens = 3

per_slice = total_slices // aliens

print(per_slice)

leftover_slice = total_slices % aliens

print("Leftovers :", leftover_slice)

asteroid_size = [34, 7, 108, 55, 2, 89]

print("smallest :", min(asteroid_size))
print("smallest :", max(asteroid_size)) 


movement = -15  # Robot moved 15 meters backward

distance = abs(movement)
print("🤖 SunnyBot moved", distance, "meters (absolute)")

base = 3
exponent = 2
laser_power = pow(base, exponent)
print(laser_power)
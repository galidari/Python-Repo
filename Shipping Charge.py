#!/usr/bin/python
print("Please enter the total weight of the package you want to ship: ")
number_string = input()
num = float(number_string)
weight = num
# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Your GROUND SHIPPING cost will be: ")
print(cost_ground)

# Ground Shipping Premium
premium_ground_shipping = 125.00
print("Ground Shipping Premium always flat rate of ")
print(premium_ground_shipping)

# Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50 
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.00 
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Your DRONE SHIPPING cost will be: ")
print(cost_drone)

if cost_ground > cost_drone:
  print("Your cheapest shipping charge between ground and drone is: ")
  print(cost_drone)
elif cost_drone > cost_ground:
  print("Your cheapest shipping charge between ground and drone is: ")
  print(cost_ground)


# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
#My Code
print("Processing Started")
for item in inventory:
 stock = inventory[item][0]
 minimum_stock = inventory[item][1]
 restock = inventory[item][2]
 print("Processing", item)
 while stock < minimum_stock:
  stock = stock + restock
  inventory[item][0] = stock
  if stock > discount_threshold and inventory[item][3] == False:
   inventory[item][3] = True
print("Processing Completed", inventory)

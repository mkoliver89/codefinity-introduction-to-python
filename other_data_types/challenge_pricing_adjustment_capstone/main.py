#Grocery Inventory
grocery_inventory = {
"Milk":("Dairy",3.50,8),
"Eggs":("Dairy",5.50,30),
"Bread":("Bakery",2.99,15),
"Apples":("Produce",1.50,50)
}
#Eggs
if grocery_inventory["Eggs"][1] >5:
 grocery_inventory["Eggs"] = ("Dairy",4.50,30)
 print("Eggs are too expensive, reducing the price by $1.")
else:
 print("The price of eggs is reasonable")
#Tomatoes
grocery_inventory["Tomatoes"] = ("Produce",1.20,30)
print("Inventory after adding Tomatoes:", grocery_inventory)
#Milk 
milk_stock = grocery_inventory["Milk"][2]
if milk_stock <10:
 grocery_inventory["Milk"] = ("Dairy",3.50,28)
 print("Milk needs to be restocked. increasing stock by 20 units.")
else:
 print:("Milk has sufficient stock.")
#Apples
if grocery_inventory["Apples"][1] >2:
 del grocery_inventory["Apples"]
print("Updated Inventory:", grocery_inventory)
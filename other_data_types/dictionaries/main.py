#Grocery Inventory
grocery_inventory ={
"Milk":(113,"Dairy"),
"Eggs":(116,"Dairy"),
"Bread":(117,"Bakery"),
"Apples":(141,"Produce")
}
#bread details
bread_details = grocery_inventory ["Bread"]
#addition of cookies
grocery_inventory["Cookies"] = (143,"Bakery")
#egg removal
del grocery_inventory["Eggs"]
#printing
print("Details of Bread:", bread_details)
print("Inventory after adding Cookies:", grocery_inventory)
print("Inventory after removing Eggs:", grocery_inventory)
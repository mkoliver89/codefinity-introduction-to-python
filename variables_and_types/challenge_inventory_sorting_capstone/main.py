# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
candy1 = items[0:9]
candy2 = items[10:20]
dry_goods = items[21:27]
category1 = categories[0:11]
category2 = categories [13:24]
#Price Variables
bubblegum_price = 1.50
chocolate_price = 2
pasta_price = 5.40
#Messages
message1 = f"We have {candy1} for {bubblegum_price} in the {category1}"
message2 = f"We have {candy2} for {chocolate_price} in the {category1}"
message3 = f"We have {dry_goods} for {pasta_price} in the {category2}"
print(message1)
print(message2)
print(message3)

# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []
#My Code
for item in products:
#Variables
 price = products[item][0]
 quanity_sold = products[item][1]
 price = float (price)
 quanity_sold = int (quanity_sold)
 sales = price * quanity_sold
 total_sales_list.append(sales) 
 total_sum =  sum(total_sales_list)
 min_sales =  min(total_sales_list)
 max_sales = max(total_sales_list)
 print(f"Total sales for {item}: ${sales}")
print(f"Total sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")



 
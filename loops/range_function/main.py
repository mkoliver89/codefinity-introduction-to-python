# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#My Code
for i in range(5):
 weekday = weekdays[i]
 promotion = daily_promotions[i]
 print(weekday.lower() + ": Promotion on " + promotion.lower())
prices = [29.99, 45.50, 12.75, 38.20]
discounts = [.10, .20, .15, .05]
for i in range(len(prices)):
 original_price = prices [i]
 discount = discounts [i]
 updated_price = original_price * (1 - discount)
 prices[i] = updated_price
 print(f"Updated price for item {i}: {updated_price:.2f}")
def discounted_price(price, discount):
    discounted_price = price - (price * discount / 100)
    return discounted_price

price =int(input("Enter the Price: "))
discount =int(input("Enter the discount: "))


discounted_price = discounted_price(price, discount)

print("The price after the discount is", discounted_price)

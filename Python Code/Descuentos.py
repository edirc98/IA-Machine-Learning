originalPrice = float(input("Give me the original price: "))
discountPrice = float(input("Give me the price discounted: "))

priceDiscounted = originalPrice - discountPrice
percent  = (priceDiscounted/originalPrice) * 100

print("Amount disconted: " + str(priceDiscounted))
print("Percent: " + str(percent) + "%")
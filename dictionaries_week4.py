def car_listing(car_prices):
  result = ""
  for key,value in car_prices.items():
    result += "{} costs {} dollars".format(key,value) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

currency1_name = input("Input currency1 name: ")
currency2_name = input("Input currency2 name: ")
exchange_rate = float(input("Input exchange rate: "))

currency1 = float(input("Input amount of currency1: "))


currency2 = currency1 * exchange_rate

print (currency1_name, currency1, "=", currency2_name, currency2)
print (currency1, currency1_name,  "=", currency2, currency2_name)

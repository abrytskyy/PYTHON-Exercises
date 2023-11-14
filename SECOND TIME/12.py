good_credit = False

x = 1000000
if good_credit:
    print(x*0.9)
else:
    print(x*0.8)

price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")
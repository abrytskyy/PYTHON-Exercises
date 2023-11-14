#temp<0 Freathing weather
#temp 0-10 Very Cold weather
#temp 10-20 Cold weather
#temp 20-30 Normal in Temp
#temp 30-40 It's hot
#temp >= 40 It's very hot
t = int(input("Input temperature: "))
if t < 0:
    print("Freathing weather")
elif t < 10:
    print("Very Cold weather")
elif t < 20:
    print("Cold weather")
elif t < 30:
    print("Normal in Temp")
elif t < 40:
    print("It's hot")
else:
    print("It's very hot")


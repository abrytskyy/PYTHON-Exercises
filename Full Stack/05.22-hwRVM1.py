minutes = int(input("Input minutes: "))

hours = minutes//60
minutes = minutes % 60

print(hours,":",minutes)
print(f"{hours}:{minutes}")
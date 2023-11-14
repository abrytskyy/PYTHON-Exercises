s = "Python"
s = s.upper()
s = s.lower()
print(s)
b = "abrakadabra"
print(b.count("ra",1, 4))
print(b.find("rak")) # index
print(b.rfind("z"))
#print(b.index("b"))
print(b.replace("a", "t", 2))
print(b.isalpha())
print(b.isdigit())
b = "abc"
print(b.rjust(5, "-"))
print(b.ljust(7, "2"))
print(b.split("b"))
b = "1 7, d, jj, 4 "
print(b.replace(" ", "").split(","))
r = b.split(",")
print(",".join(r))
list1 =["Nazar", "Legeza", "Andrijovych"]
print("-".join(list1))
b = "    H   ellow   "
print(b.strip())
#print(b.rstrip())
#print(b.lstrip())
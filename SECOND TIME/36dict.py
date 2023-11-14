customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True

}
print(customer["name"])
print(customer.get("ages"))
print(customer.get("ages", "False value"))

customer["name"] = "Jack Smith"
print(customer["name"])

customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])

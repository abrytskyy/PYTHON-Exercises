# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet ():
    print("Hi")
    print("by")
    print("welcome")


greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
greet_with_name("Artem")

def greet_with(name1, name2):
    print(f"Hello {name1}")
    print(f"What is it like in {name2}?")
greet_with("Anton", "Lviv")

def greet_with(name3, name4):
    print(f"Hello {name3}")
    print(f"What is it like in {name4}?")
greet_with(name4="Oslo", name3= "Artem")

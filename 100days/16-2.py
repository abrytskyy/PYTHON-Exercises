from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.add_column("Speed",["70", "40", "130"])

table.align = "l"

print (table
       )
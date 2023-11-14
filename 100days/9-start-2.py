#Nesting a list in a Dictionary
#You cant:
travel_log = {
    "France": "Paris", "Lille", "Dijon"
}
#right is to turn into the list:
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
#you can nest list,dictionary in the dictionary:
travel_log = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits":5},
}
#nestet dictionary inside list

travel_log = {
    {"country": "France", "cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
    {"country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits":5},
}
travel_log = [
    {
        "country": "France",
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":5
    },
]
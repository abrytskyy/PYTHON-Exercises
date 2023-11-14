# Дан словарь с информацией о фильмах. Каждый фильм представлен вложенным словарем
# с ключами "название", "режиссер" и "жанр". Найдите фильмы определенного жанра.

#if "Comedy" in ["Comedy", "Fantasy"]:
#    print("yes")


movies = [
    {
        "name": "Ace Ventura",
        "director": "Tom Shadyac",
        "genre": ["Comedy"]
    },
    {
        "name": "The Mask",
        "director": "Chuck Russell",
        "genre": ["Action", "Comedy"]
    },
    {
        "name": "Bruce Almighty",
        "director": "Tom Shadyac",
        "genre": ["Comedy", "Fantasy"]
    }
]
genre = input("Choose from genre action, comedy or fantasy: ")

def get_genre (movies_list):
    new_list = []
    for movie in movies_list:
        if genre in movie["genre"]:
            #return movie
            new_list.append(movie)
    return new_list
print (get_genre(movies))


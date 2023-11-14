list1 = (10,20,30)
print(list1[2])

books = {"title": "Book 1", "text": "This is a book about programming."}

print(books.get("title"))


set1 = {1, 4, 2, 5, 7}
set2 = {7, 4, 8, 1}
set3 = {7, 4,}
print(len(set1 & set2 & set3))


books = [
    {"title": "Book 1", "text": "This is a book about programming."},
    {"title": "Book 2", "text": "The novel tells a story of adventure."},
    {"title": "Book 3", "text": "In this book, you'll find tips for success."}
]

search_words = {"book", "programming"}
sum = 0
for b in books:
    for w in search_words:
        if w in b["text"]:
            sum += 1
            break
print(sum)
#1. Create a list of tasks with categories and statuses. Write a function to count the number
# of unfinished tasks in each category.
tasks = [
    {"description": "Analyze customer survey data to identify preferences", "category": "Work", "status": "Incomplete"},
    {"description": "Optimize online advertising campaigns using data insights", "category": "Work", "status": "Complete"},
    {"description": "Create interactive data dashboards for website traffic", "category": "Work", "status": "Complete"},
    {"description": "Analyze personal investment portfolio performance", "category": "Home", "status": "Incomplete"},
    {"description": "Evaluate social media engagement metrics for marketing", "category": "Work", "status": "Complete"},
    {"description": "Conduct market segmentation analysis for customer targeting", "category": "Work", "status": "Incomplete"},
    {"description": "Prepare data-driven reports for executive decisions", "category": "Work", "status": "Complete"},
    {"description": "Analyze user feedback data to improve product usability", "category": "Work", "status": "Incomplete"},
    {"description": "Analyze personal fitness and health data to track progress", "category": "Home", "status": "Incomplete"},
    {"description": "Organize and analyze recipes and meal planning data", "category": "Home", "status": "Complete"}
]
def number_of_unfinished_tasks_by_category(tasks):
    tasks1 = {}
    for task in tasks:

        if task["category"] in tasks1 and task["status"] == "Incomplete":
            tasks1[task["category"]] += 1
        else:
            tasks1[task["category"]] = 1
    return tasks1
print(number_of_unfinished_tasks_by_category(tasks))



#2. Create a list of books in a library with information about genres and authors. Write a function
# to find the most popular genre.
library = [
    {"title": "Book 1", "author": "Author A", "genre": "Fantasy"},
    {"title": "Book 2", "author": "Author B", "genre": "Science Fiction"},
    {"title": "Book 3", "author": "Author A", "genre": "Mystery"},
    {"title": "Book 4", "author": "Author C", "genre": "Fantasy"}
]
def most_popular_genre(books):
    genre = {}
    for book in books:
        if book["genre"] in genre:
            genre[book["genre"]] += 1
        else:
            genre[book["genre"]] = 1
    return max(genre, key = genre.get)
print(most_popular_genre(library))

#3. Create a list of holidays with information about dates and countries where they are
# celebrated. Write a function to find a holiday in a specific country by date.
holidays = [
    {"date": "2023-01-01", "country": "USA", "name": "New Year's Day"},
    {"date": "2023-05-01", "country": "USA", "name": "Labor Day"},
    {"date": "2023-12-25", "country": "USA", "name": "Christmas"},
    {"date": "2023-01-01", "country": "Canada", "name": "New Year's Day"},
    {"date": "2023-07-01", "country": "Canada", "name": "Canada Day"},
    {"date": "2023-12-25", "country": "Canada", "name": "Christmas"},
]
def find_holiday_in_country(country, date):
    return [holiday for holiday in holidays if holiday["country"] == country and holiday["date"] == date]
print(*find_holiday_in_country("USA", "2023-12-25"))

#just name of holiday:
def find_holiday_in_country(country, date):
    return [holiday["name"] for holiday in holidays if holiday["country"] == country and holiday["date"] == date]
print(*find_holiday_in_country("USA", "2023-12-25"))



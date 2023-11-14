# Create a file containing a list of email addresses. Read the file, find all unique domains, and display them on the screen.

email_addresses = [
    "user1@example.com",
    "user2@example.com",
    "user3@example.com",
    "user4@example.com",
]
file_name = "email_addresses.txt"

def write(data, path):
    try:
        with open(path, 'w') as file:
            for email in data:
                file.write(f"{email}\n")
    except Exception as ex:
        print(ex)
write(email_addresses, file_name)

def read(path):
    try:
        with open(path) as file:
            return file.read()
    except FileNotFoundError as ex:
        print(ex)




# Create a file with book data in the format "title, author, year of publication." Read the file, find all books by a specific author,
# and display them on the screen.


# Create a program for keeping a diary. Implement adding entries with dates to a file and the ability to search for entries by date.
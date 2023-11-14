#Откройте бинарный файл для чтения и выведите его содержимое.
file_path = "binary_file.bin"

try:
    with open(file_path, "rb") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
data = b"Hello, this is binary content."

# Создание и запись данных в бинарный файл
file_path = "binary_data.bin"
with open(file_path, "wb") as file:
    file.write(data)

# Открытие и чтение содержимого бинарного файла
try:
    with open(file_path, "rb") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

#Запишите строку в бинарный файл.

new_text = "This is additional content."
with open(file_path, "ab") as file:
    file.write(new_text.encode("utf-8"))


try:
    with open(file_path, "rb") as file:
        file_content = file.read()
        print(file_content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

#Прочитайте и выведите первые 10 байт из бинарного файла.

try:
    with open(file_path, "rb") as file:
        file_content = file.read(10)
        print(file_content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
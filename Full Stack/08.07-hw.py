###Артём
#Сформируйте множество из символов строки, которые не являются цифрами.
str1 ="kotoryje ne3 javlajutsa 1"
non_digit_set = {i for i in str1 if not i.isdigit()}
print(non_digit_set)

#Создайте множество из длин строк в списке ['яблоко', 'груша', 'апельсин', 'киви'].
str2 = ['яблоко', 'груша', 'апельсин', 'киви']
from_len_set = {len(i) for i in str2}
print(from_len_set)

#Найдите множество всех буквенных символов в строке "Hello, World!" без учета регистра.
str3 = "Hello, World!"
all_alpha = {i for i in str3 if i.isalpha()}
print(all_alpha)
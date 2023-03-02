
import json

# English
en_dict = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}

# Russian
ru_dict = {
    "1": "Один",
    "2": "Два",
    "3": "Три",
    "4": "Четыре",
    "5": "Пять"
}

# Сохраните словари в формате JSON
with open('en_dict.json', 'w') as f:
    json.dump(en_dict, f)

with open('ru_dict.json', 'w') as f:
    json.dump(ru_dict, f)

# Прочитайтаем вводимые пользователем данные
user_input = input("Enter a number: ")

# Перевод
if user_input in en_dict:
    with open('en_dict.json', 'r') as f:
        en_dict = json.load(f)
    print(en_dict[user_input])
elif user_input in ru_dict:
    with open('ru_dict.json', 'r') as f:
        ru_dict = json.load(f)
    print(ru_dict[user_input])
else:
    print("Number not found!")
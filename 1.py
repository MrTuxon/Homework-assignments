import uuid
byte1 = 'А'.encode('utf-8')
byte2 = 'И'.encode('utf-8')
print(byte1, byte2)
test1 = byte1.decode('cp1251')
print(test1)
test2 = byte2.decode('cp1251')
print(test2)

def read_license_file():
    license_dict = {}
    with open(LICENSE_FILE, 'r') as f:
        for line in f:
            name, key = line.strip().split(': ')
            license_dict[name] = key
    return license_dict

def write_license_file(license_dict):
    with open(LICENSE_FILE, 'w') as f:
        for name, key in license_dict.items():
            f.write(f'{name}: {key}\n')

def register_license():
    name = input('Введите ваше имя: ')
    key = str(uuid.uuid4())  # Генерируем уникальный ключ регистрации
    print(f'Ваш ключ регистрации: {key}')
    license_dict[name] = key  # Добавляем новую пару в словарь
    write_license_file(license_dict)

license_dict = read_license_file()
name = input('Введите ваше имя: ')
if name in license_dict:
    key = input('Введите ключ регистрации: ')
    if key == license_dict[name]:
        print('Авторизация успешна!')
    else:
        print('Неверный ключ регистрации.')
else:
    choice = input('У вас нет лицензии. Хотите зарегистрировать программу? (y/n) ')
    if choice == 'y':
        register_license()
    else:
        print('Программа будет закрыта.')
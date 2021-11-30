from datetime import date
d = date.today()
name = input("ВВедите свое имя: ")
age = int(input("Введите свой возраст"))

res = 100 - age + d.year


namef = f'Вас зовут {name}'
agef = f'В {res} то году Вам исполниться 100 лет'

print(namef)
print(agef)
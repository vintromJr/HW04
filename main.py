from datetime import datetime

#Створення класу
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def review(self):
        print('Опис собаки')
        print("Кличка:", self.name)
        print('Порода:', self.breed)
        print('Вік:', str(self.age))

    def action(self):
        now = datetime.now()
        print('Час:', now.strftime("%H:%M:%S"))
        hour = int(now.strftime("%H"))
        if hour > 22 or hour < 7: print("Пора спати")
        elif hour < 8: print("Пора снідати")
        elif hour < 10: print("Пора гуляти")
        elif hour < 12: print("Пора гратись")
        elif hour < 13: print("Пора обідати")
        elif hour < 16: print("Дресура")
        elif hour < 19: print("Пора гуляти")
        elif hour < 20: print("Пора вечеряти")
        else: print("Пора митись, сушитись та розчісувати шерсть")

#Створення екземпляру
data = []
print("Створіть профіль вашого собаки")
while True:
    temp = input("Введіть кличку собаки: ")
    if temp.isalpha():
        data.append(temp)
        break
    else: print("Щось пішло не так!!!")
while True:
    temp = input("Введіть породу собаки: ")
    if temp.isalpha():
        data.append(temp)
        break
    else: print("Щось пішло не так!!!")
while True:
    temp = input("Введіть вік собаки: ")
    if temp.isdigit() or temp[0] == '-' and temp[1:].isdigit():
        if 0 <= int(temp) <= 15:
            data.append(int(temp))
            break
        elif int(temp) < 0: print("Ваш собака ще не народився")
        else: print("Коли ви востаннє бачили свого собаку живим?")
    else: print("Щось пішло не так!!!")
my_dog = Dog(data[0], data[1], data[2])
print("Вітаю! Профіль вашого улюбленця створено")
print()
print('-' * 10)
print()

#Виклик методу review (опис собаки)
my_dog.review()

#Виклик методу action (дія господаря з собакою залежно від реального часу)
my_dog.action()
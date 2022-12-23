"""10. В цехе 7 бригад, имеющих порядковые номера от 1 до 10.
О каждом рабочем цеха известны следующие данные:
номер бригады, фамилия, год рождения.
Данные по бригадам не упорядочены и количество рабочих заранее не известно.
Необходимо выдать справку о самом молодом рабочем в каждой бригаде.
Выполнить сортировку списка."""
import tabulate # pip install tabulate
import pandas #pip install pandas

def spisok(): #список всех рабочих
    print(" Список всех Рабочих:")
    from tabulate import tabulate
    #data = []
    with open('list.txt','r', encoding="utf-8") as f: #открытие файла и добавление формата
        data = [line.split(',') for line in f]
        data.sort(key = lambda x : x[2], reverse=True) #сортировка по годам (от самого молодого до самого старого
        for line in f:
            data.append(list(map(str.strip, line.split(',')))) #сама табуретка
    print(tabulate(data, tablefmt='grid', headers=('Номер Бригады', 'Фамилия', 'Год рождения'))) #формат и что будет написано
    popo()

def popo():
    print("\n" * 5)
    print("Список самых молодых рабочих в каждой бригаде:")
    import pandas as pd  #  pip install pandas
    from tabulate import tabulate
    fn = r'list.txt'

    df = pd.read_csv(fn,encoding="utf-8", header=None, names=['Номер','Фамилия','Год рождения']) #шапка табулейта от панды
    aboba = df.sort_values(['Номер','Год рождения'],ascending=True).groupby('Номер').head(1) #сама сортировка
    print(tabulate(aboba, headers='keys', tablefmt='psql')) #вывод
    print("\n" * 5)
    home()



def add(Nomer=None, Name=None, Year=None): #Страница добавления
    Nomer = input("Введи номер бригады рабочего (от 1 до 7):")
    Name = input("Введи фамилию рабочего:")
    Year = input("Введи год рождения рабочего:")
    list = open("list.txt", "a", encoding="utf-8")                       # Открывает список  и ставит кадировку на рус
    list.write(Nomer+", "+str(Name)+ ", "+str(Year)+"\n")     #записывает  в файл
    print("Рабочий добавлен!")
    print("\n" * 5)
    list.close()                              #сохраняет и закрывает
    home()                                # кидает обратно

def home(): # Главная страница
    print('''Выберите пункт меню:
    1. Показать справку о самом молодом рабочем в каждой бригаде
    2. Добавить рабочего''')
    user_input = input()
    if user_input == '1':
        spisok()
    elif user_input == '2':
        add()
    else:
        print("Ты что-то не так написал")
home()
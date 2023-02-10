https://github.com/VikaRzyankina/Laba-1#Натуральные числа, содержащие не более двух групп из 5 подряд идущих 0.
#Список используемых в числах цифр выводить отдельно прописью.
start_numb = ['1','2','3','4','5','6','7','8','9'] # с чего может начинаться число
num = ['1','2','3','4','5','6','7','8','9','0']# возможные числа после второго по порядку числа
lines = []#строки из файла
numbers = []#числа из файла

def repl(n):
    f = {0:'ноль', 1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять'}
    return f.get(n) #замена из словаря

with open('text.txt') as f: #открытие и чтение файла
    file = f.read()
    for i in file.split():
        lines.append(i)

for line in lines: #поиск чисел в файле и занесение их в отдельный массив(чтобы избежать разделения чисел)
    h = 0
    for i in range(len(line)):
        if h > 0:
            h -= 1
            break
        else:
            if line[i] in start_numb:
                number = line[i]
                h = 1
                while True:
                    try:
                        if line[i + h] in num:
                            number += line[i + h]
                        if line[i + h] not in num:
                            break
                        h += 1
                    except IndexError:
                        break
                numbers.append(number)

if len(numbers) == 0:
    print('В файле нет цифр')
    quit()

uwu = [] # подходящие по условию
for i in numbers:
    kn = 0 #Кол-во нулей
    pn = 0 #кол-во групп нулей
    for j in range(len(i)):
        try:
            if i[j] == '0':
                kn += 1
                if kn == 5 and i[j + 1] != '0':
                    pn += 1
                    kn = 0
                elif kn == 5 and i[j + 1] == '0':
                    break
        except IndexError:
            break
    if pn in [1, 2]:
        uwu.append(i)

if len(uwu) == 0: #если файл без чисел
    print('В файле нет подходящих под условие цифр')
    quit()

for j in uwu: #замена чисел прописью
    exp = []
    for i in j:
        if repl(int(i)) not in exp:
            exp.append(repl(int(i)))
    print(j + ' - ', *exp)

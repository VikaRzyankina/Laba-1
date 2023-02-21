#Натуральные числа, содержащие не более двух групп из 5 подряд идущих 0.
#Список используемых в числах цифр выводить отдельно прописью.
def repl(n):
    f = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return f.get(n)  # замена из словаря
uwu=[]
buffer_len=1 #размер буфера чтения
work_buffer='' #рабочий буфер
work_buffer_len=buffer_len #длина рабочего буфера
with open('text.txt','r') as f: #открываем файл
    buffer=f.read(buffer_len) #читаем первый блок
    if not buffer: #если пуст
        print('Файл пустой')
    while buffer: #пока файл не пуст
        while buffer>='0' and buffer <='9': #обработка текущего блока
            work_buffer+=buffer
            buffer=f.read(buffer_len) #читаем следующий блок
        if work_buffer:
            kn = 0
            pn = 0
            for j in range(len(work_buffer)):
                try:
                    if work_buffer[j] == '0':
                        kn += 1
                        if kn == 5:
                            pn += 1
                            kn = 0
                    elif work_buffer[j] != '0':
                        kn = 0
                except IndexError:
                    break
            if pn in [0, 2]:
                uwu.append(work_buffer)
        work_buffer=''
        buffer=f.read(buffer_len) #читаем очередной блок
if len(uwu) == 0:
    print('В файле нет подходящих под условие чисел')
    quit()
for j in uwu: #замена чисел прописью
    exp = []
    for i in j:
        if repl(int(i)) not in exp:
            exp.append(repl(int(i)))
    print(j + ' - ', *exp)

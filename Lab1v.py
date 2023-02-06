start_numb = ['1','2','3','4','5','6','7','8','9']
num = ['1','2','3','4','5','6','7','8','9','0']
lines = []
numbers = []

def repl(n):
    f = {0:'ноль', 1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять'}
    return f.get(n)

with open('text.txt') as f:
    file = f.read()
    for i in file.split():
        lines.append(i)

for line in lines:
    for i in range(len(line)):
        if line[i] in start_numb:
            number = line[i]
            kn = 0
            pn = 0
            while pn < 3:
                try: #во избежание ошибки чтобы не выйти за пределы файла
                    if line[i + 1] in num:
                        if line[i + 1] == '0':
                            kn += 1
                            if kn == 5 and line[i + 2] != '0':
                                pn += 1
                                kn = 0
                            elif kn == 5 and line[i + 2] == '0':
                                break
                            number += line[i + 1]
                        else:
                            number += line[i + 1]
                    else:
                        break
                    i += 1
                except IndexError:
                    break
            if pn in [1,2]:
                numbers.append(number)

for i in numbers:
    exm = ''
    for j in i:
        if j != '0':
            exm += repl(int(j)) + ' '
    print(i + ' - ' +exm+'ноль')
import random

maya_numbers = [3, 4, 5, 6, 7, 8, 9,
                10, 11, 12, 13, 14, 15,
                16, 17, 18, 19, 20
                ]
print('Привестую тебя странник!')
a = input('Напиши свое имя и судьба выберет тебе число: ')
random_number = random.choice(maya_numbers)
print('Твое число,', a, ',будет: ', random_number)
print('У тебя есть 7 попыток, чтобы подобрать верный пароль!!!')
password = ' '
for i in range(1, 20):
    for j in range(1, 20):
        if random_number % (i+j) == 0 and i != j and i <= j:
            password += str(i) + str(j)
code_maya = int(password[0:len(password)])
for k in range(7):
    your_password = int(input('Ваедите верный пароль:'))
    if your_password == code_maya:
        print('Верно! Проход открыт!')
        break
    else:
        while k == 2:
            assent = input('Привет, я Phyton! Если тебе нужна помощь напиши "Да"!: ')
            if assent == 'Да':
                print('Верный пароль:', password)
            break
        else:
            if k == 6:
                print('Ты использовал(а) все попытки! Тебе больше не выйти, прощай!')
                break
            else:
                print('Попробуй еще')

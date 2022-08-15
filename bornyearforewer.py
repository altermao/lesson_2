#Год рождения А.С.Пушкина
answere=int(input('В каком году родился А.С.Пушкин? : '))
while answere != 1799 :
    print('Неверно')
    answere=int(input('В каком году родился А.С.Пушкин? : '))
while answere == 1799 :
    print('Верно')
    break
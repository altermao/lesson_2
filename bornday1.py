# Год и день рождения А.С.Пушкина (вариант 2: дата рождения - класс 'str')
answere = int(input('В каком году родился А.С.Пушкин? : '))
if answere != 1799 :
    print('Неверный год рождения')
    exit()

if answere == 1799:
   print('Верно')

answere = input('Когда у А.С.Пушкина день рождения ? (в виде "01 января") : ')
if answere != '06 июня' :
    print('Неверный день рождения')

if answere == '06 июня' :
    print('Верно')

exit()
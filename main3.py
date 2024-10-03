first = int(input('Введите цену на первый товар: '))
second = int(input('Введите цену на второй товар: '))
third = int(input('Введите цену на третий товар: '))
total = first + second + third
if total >10000: 
    print ('Итоговая сумма:', total*0.9)
else:
      print ('Итоговая сумма:', total)

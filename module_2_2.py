First_number = int(input('Введите первое число: '))
Second_number = int(input('Введите второе число: '))
Third_number = int(input('Введите третье число: '))
if First_number == Second_number == Third_number :
      print(3)
elif  First_number == Second_number or  Second_number == Third_number or  First_number == Third_number :
      print(2)
else:
      print(0)
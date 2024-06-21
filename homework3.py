task = 'Практическая работа по уроку "Динамическая типизация"'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()
print('Напишите ваше имя:')
name = str(input())
print('Переменная "name" = ', name, type(name))
print('Введите ваш возраст:')
age = input()
age = int(age)
print('Переменная "age" = ', age, type(age))
if age <= 18:
    age = age + 10
    print('А вам когда то будет в переменной "age" = ', age, "лет", type(age))
else:
    age = age - 10
    print('А вам когда то было в переменной "age" = ', age, "лет", type(age))
is_student = True
print('Теперь переменная "age" =', age, type(age))
print('Переменная "is_student" = True =', is_student, type(is_student))
print()
print(thanks)
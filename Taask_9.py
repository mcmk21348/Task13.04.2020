a = str(input('Введи сторку: '))
try:
    if a.rindex('f') <= a.index('f') :
        print(a.index('f'))
    else:
        print(a.index('f'))
        print(a.rindex('f'))
except ValueError:
    print()
age = int(input('how old are you ?'))

if age <=30 :
    if age>=0 and age<=10 :
        print('you are child')
    elif age>11 and age<=19:
        print('you are Boy')
    else :
        print('you are teenager')
else :
    print('you older than 30')
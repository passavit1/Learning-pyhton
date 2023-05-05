import random

number = random.randrange(1,7)
print(number)

i=1

while True :
    A = int(input('what is your number ?'))
    if A==number :
        print('you correct')
        break
    else :
        print('you wrong')
        if A<number :
            print('your number less than random')
        else :
            print('your number more than random')
        i+=1
    if i==4:
        print('game over the random number is ' , number)
        break
    

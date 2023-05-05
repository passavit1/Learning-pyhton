money = int(input('how much money do you have ?'))



if money >= 1000:
    a = money//1000
    money = money%1000
    print('แบง 1000 จำนวน ' , a)
if money >= 500:
    b = money//500
    money = money%500
    print('แบง 500 จำนวน ' , b)
    print(money)
if money >= 100:
    c = money//100
    money = money%100
    print('แบง 100 จำนวน ' , c)
    print(money)


print('ได้แบง 1000 จำนวน' , a , 'ได้แบง 500 จำนวน' , b , 'ได้แบง 100 จำนวน' ,c , 'และเหลือเศษอีก' , money , 'บาท')

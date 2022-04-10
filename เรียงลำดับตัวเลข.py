
number=[]

odd=[] #เลขคี่
even = [] #เลขคู่

while True:
    a=int(input('what is your number ?'))
    if a<0:
        break
    if a%2==0:
        even.append(a)
    else:
        odd.append(a)
    number.append(a)

number.sort()
odd.sort()
even.sort()



print(number)
print('odd' , odd)
print('even' , even)

# print('before' , number)
# number.sort()
# print('after',number)
# number.reverse()
# print('reverst' , number)
# print('min' , min(number))
# print('max' , max(number))
# print('sum' , sum(number))
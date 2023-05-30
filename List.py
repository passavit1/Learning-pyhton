x = 'My name is passavit maicharoen'
myList = x.split(' ')

print(len(myList))
print(myList)

# myList[3] = 'wizat'
# print(myList)

# myList[3:5] = ['GOD']
# print(myList)

# myList.insert(3, 'the')
# print(myList)

# myList.append('of')
# print(myList)

# myList.remove('the')
# print(myList)

# myList.pop(4)
# print(myList)

# myList.pop()
# print(myList)

# newList = [expression for item in iterable if condition == true]
newList = [x for x in myList if 'm' in x]
print('เลือกเฉพาะที่มี m ', newList)

newList = [x for x in myList if 'My' not in x]
print('เลือกทุกตัวยกเวิน my ', newList)

newList = [x.upper() for x in myList]
print('ปรับทุกตัวเป้น uppercase  ', newList)

newList = ['hello' for x in myList]
print('เปลี่ยนทุก index เป็น hello ', newList)

newListOfNumber = [x for x in range(10) if x < 5]
print(newListOfNumber)

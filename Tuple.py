
#reverst tuple เรียงจากหลังมาหน้า
tup=(1,3,5,77,3,2,4)
tup=reversed(tup)
print(type(tup))
print(tuple(tup))

#แปลง tuple => String
# tup = ('k','a','s','v')
# name=''.join(tup)
# print(name)

#สลับ tuple
# x=(50,40)
# y=(99,55)
# x,y=y,x
# print(x)
# print(y)

#นำค่าใน tuple => ตัวแปร
# tup=(10,20,30)
# a,b,c=tup
# print(a)
# print(b)
# print(c)

# tup=(1,2,3,9,5,6,7,4)
# lis=['name' , 'bank']

#การ sort ข้อมูล
# tup=list(tup)
# print(type(tup))
# tup.sort()
# tup=tuple(tup)
# print(tup)
# print(type(tup))


#ค้นหาตามตำแหน่ง
# x=tup.index('d')
# print(x)

#การค้นหาและนับจำนวนสมาชิก
# print(tup.count(3))

#ลบข้อมูลด้านใน
# tup=list(tup)
# print(type(tup))
# tup.pop(3)
# tup=tuple(tup)
# print(tup)
# print(type(tup))

#การลบข้อมูลใน tuple 
# del tup 
# print(tup)

#นำ list มารวมกับ tuple 
# tup=list(tup)
# tup=lis+tup
# tup=tuple(tup)
# print(type(tup))
# print(tup)

#การเข้าถึงข้อมูล
# print(tup[0:3])
# print(tup[-3:-1])

#แปลง tup เป็น list 
# lis=list(tup) #เปลี่ยน tup เป็น lis 
# print('before',tup)
# lis[3] = 'bangkok' #แก้ไขค่า 
# tup=tuple(lis) #เปลี่ยน lis กลับเป็น tuple
# print('after' , tup)

#LOOP
# for item in tup :
#     print(item)

#การตรวจสอบข้อมูล
# if 3 in tup :
#     print('มี 3 ใน Tup')

#การนับสมาชิก
# print(len(tup))

#LOOP FOR
# for item in range(len(tup)):
#     print('round' , tup[item])

#การสร้างและเพิ่มข้อมูล
# name=('pass' , )
# new=('nut',)
# name=name+new
# print(type(name))
# print(name)
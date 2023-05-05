

# BMI = นน (kg) / ส่วนสูง (m) ยกกำลังสอง



weight = int(input('what is your weight (kg) ?'))
height = int(input('what is your height (cm) ?'))

bmi=weight/((height/100)**2)
print('your bmi = ' , bmi)
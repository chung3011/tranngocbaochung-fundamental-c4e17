weight = float(input ("how heavy are you? (kg)\t"))
heightc = float(input ("how tall are you? (cm)\t"))
heightm = heightc / 100
BMI = weight / (heightm * heightm)
if (BMI < 16):
    print ("Severely underweight")
elif (BMI < 18.5 ):
    print ("Underweight")
elif (BMI < 25):
    print ("Normal")
elif (BMI < 30):
    print ("Overweight")
else:
    print ("Obese")

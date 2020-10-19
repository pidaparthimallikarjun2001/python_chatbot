from regular_diet import regular_diet
from gain_weight import gain_weight
from lose_weight import lose_weight
from findBMI import findBMI

"""
This function asks the user his weight and height and it calculates his/her BMI(Body Mass Index). According to that BMI, 
According to that BMI, it suggests the user to take suitable food in order to lose or gain weight
"""

def food():
	try:
		print("please Enter your weight(in kgs) and height(in cm)")
		weight=int(input("Weight:"))
		height=int(input("height:"))
		bmi=findBMI(height, weight)	#calculating BMI
		print("Your Body Mass Index(BMI) is",bmi,"\n")
		if(bmi>=18.5 and bmi<=24.9):				#Ideal BMI lies between 18.5 and 24.9
			print("there is no need to lose or gain weight as your BMI is",bmi,"do follow your regular diet\n")
			regular_diet()
		elif(bmi<18.5):								#BMI < 18.5
			print("your BMI is",bmi,"it would be better to gain weight\n")
			gain_weight()
		else:										#BMI > 24.9
			print("Your BMI is",bmi,"it would be better to lose weight\n")
			lose_weight()
	except Exception as e:
		print(str(e))
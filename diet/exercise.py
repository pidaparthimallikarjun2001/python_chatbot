import webbrowser
import math
from regular_diet import regular_diet
from findBMI import findBMI

"""
This function asks the user his weight and height and it calculates his/her BMI(Body Mass Index). According to that BMI, 
It suggests the user some exercises to gain or lose weight
"""

def exercise():
	try:
		print("A.Regular exercise or B.EXercise to lose weight\n")
		p=input("Mode of Exercise:").upper()
		if(p=="A"):
			regular_diet()
		elif(p=="B"):
			print("please Enter your weight(in kgs) and height(in cm)\n")
			weight=int(input("Weight:"))
			height=int(input("height:"))
			bmi=findBMI(height, weight)		#calculating BMI
			print("Your Body Mass Index(BMI) is",bmi,"\n")
			if(bmi>=18.5 and bmi<=24.9):						#Ideal BMI lies between 18.5 and 24.9
				print("there is no need of loosing weight as your BMI is",bmi,"do regular exercise\n")
				regular_diet()
			elif(bmi<18.5):										#BMI < 18.5
				print("your BMI is",bmi," it would be better to gain weight by eating good protein food and do some push ups\n")
			else:												#BMI > 24.9
				less=bmi-24
				print("To loose your weight you should diet for",math.ceil(less),"weeks\n")
				week=int(input("day of workout:"))//7
				if(week==0):
					print("do basic Exercises like fetching and walking for 45 mins-1 hour a day at evening for morning in open place\n")
				elif(week==1):
					print("do Forword Lunge\n")
					webbrowser.open("https://www.youtube.com/watch?v=QE_hU8XX48I")
				elif(week==2):
					print("do burpee\n")
					webbrowser.open("https://www.youtube.com/watch?v=dZgVxmf6jkA")
				elif(week==3):
					print("do Explosive Lunge\n")
					webbrowser.open("https://www.youtube.com/watch?v=eV_JhAnBj7M")
				elif(week==4):
					print("do Squat\n")
					webbrowser.open("https://www.youtube.com/watch?v=otzWCWpuW-A")
				elif(week==5):
					print("do Double Jump\n")
					webbrowser.open("https://www.youtube.com/watch?v=2wJ_Y7ReY9g")
				elif(week==6):
					print("do Mountain Climbers\n")
					webbrowser.open("https://www.youtube.com/watch?v=nmwgirgXLYM")
				elif(week==7):
					print("do Jump Rope\n")
					webbrowser.open("https://www.youtube.com/watch?v=1BZM2Vre5oc")
				elif(week==8):
					print("do Bodyweight Balance\n")
					webbrowser.open("https://www.youtube.com/watch?v=ydxEUddbZTE")
				elif(week==9):
					print("do Kettlebell Swing\n")
					webbrowser.open("https://www.youtube.com/watch?v=YSxHifyI6s8")
				else:
					print("do Tabata Drill\n")
					webbrowser.open("https://www.youtube.com/watch?v=nDJie_hJlnc")
		else:
				print("choose a valid option")
	except Exception as e:
		print(str(e))

import webbrowser
import math
from mentalhealth import mental_health
from food import food
from exercise import exercise
from regular_diet import regular_diet
from gain_weight import gain_weight
from lose_weight import lose_weight

def start():
	#This function asks for the user what type of fitness he/she wants i.e., Meantal or Physical fitness
	try:
		print("Which type of fitness you want:")
		print("A.Mental fitness		 B.Physical fitness\n")
		x=input("Type of fitness:").upper()
		if(x=="A"):
			print("Mental Fitness\n")
			mental_health()		#calling corresponding function
		elif(x=="B"):
			print("Which form you want the physical fitness:\n")	#If the user chooses physical fitness, the bot asks to choose exercise or foot diet
			print("A.Exercise 	 B.Food Diet\n")
			k=input("Type of physical fitness: ").upper()
			if(k=="A"):
				exercise()	#calling corresponding function
			elif(k=="B"):
				food()	#calling corresponding function
			else:
				print("Please choose A or B\n")
		else:
			print("Choose a valid option")
		print("\n\nThanks for using our service")
	except Exception as e:
		print(str(e))
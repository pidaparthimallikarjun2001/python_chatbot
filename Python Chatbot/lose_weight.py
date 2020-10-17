def lose_weight():	#tells different food items like what to eat when you are in a specific day of your diet plan
	try:
		day=int(input("Enter the date of diet:"))
		if(day%7==0):
			print("\n\nday",day,"\nBreakfast: Sambar with 2 brown rice idlis/ Paneer sandwich with mint chutney.\nLunch: Whole-grain roti with mixed-vegetable curry with one dal.\nDinner: Tofu/chicken curry with mixed vegetables and a fresh spinach salad/chicken gravy with 2 multigrain rotis\n")
		elif(day%7==1):
			print("day",day,"\nBreakfast: Chana dal pancakes with mixed vegetables and a glass of milk/ bread and egg with fruits\nLunch: Chickpea curry with brown rice/ Brown rice with dal\nDinner: Khichdi with sprout salad/Veg paratha with raita\n")
		elif(day%7==2):
			print("day",day,"\nBreakfast: Apple cinnamon porridge/ Vegetable uttapam with sambhar\nLunch: Whole-grain roti with tofu/ non veg and mixed vegetables\nDinner: Palak paneer with brown rice and vegetables/ 2 Multigrain rotis with chicken and curd\n")
		elif(day%7==3):
			print("day",day,"\nBreakfast: Yogurt with sliced fruits and sunflower seeds/ vegetable poha\nLunch: Whole-grain roti with vegetable sabzi/ Dal with veg or non veg sabzi and brown rice\nDinner: Chana masala with basmati rice and green salad/ One bowl of fruits and vegetables with multigrain rotis\n")
		elif(day%7==4):
			print("day",day,"\nBreakfast: Vegetable dalia and a glass of milk/ 3-4 dal paddu with sambar\nLunch: Vegetable sambar with brown rice/ 2 multigrain roti with veg/non veg curry\nDinner: Tofu curry with potatoes and mixed vegetables/ chicken curry with 2 multigrain rotis\n")
		elif(day%7==5):
			print("day",day,"\nBreakfast: Multigrain parathas with avocado and sliced papaya/ dal paratha with mixed vegetables\nLunch: Large salad with rajma curry and quinoa/ one bowl mixed vegetable kadai\nDinner: Lentil pancakes with tofu tikka masala/ green salad with mixed vegetables and multigrain roti\n")
		elif(day%7==6):
			print("day",day,"\nBreakfast: Buckwheat porridge with sliced mango/ fruit salad with a glass of milk\nLunch: Vegetable soup with whole-grain roti/ one bowl millet and dal khichdi with multigrain roti\nDinner: Masala-baked tofu with vegetable curry/ non veg curry (chicken, seafood) with multigrain roti\n")	
	except Exception as e:
		print(str(e))
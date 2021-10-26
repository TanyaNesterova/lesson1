a = input ("Введите ваш возраст: ")
a = round (float(a),0)
def age_1(a):
	if a <= 6:
		print ("вы учитесь в детском саду")
	elif 7 <= a <= 17:
		print ("вы учитесь в школе")
	elif 17 < a <= 24:
		print ("вы учитесь в ВУЗе")
	elif 25 <= a :
		print ("вы работаете")
age_1 (a)
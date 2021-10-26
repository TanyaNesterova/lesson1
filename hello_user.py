def hello_user(answer):
	try:	
		print("Программа: Привет, как дела?")
		answer=input("Пользователь:")
		while True:
			if answer =="хорошо":
				print("Программа: ok")
				break
			else:
				print("Программа: как дела")
				answer=input("Пользователь:")
	except KeyboardInterrupt:
		print("Программа: Пока")

hello_user(" ")
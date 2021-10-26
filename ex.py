catalog_w = {
"Как дела?": "Хорошо!",
"Что делаешь?": "Прогаммирую",
"Как погода": "Дождик!"
}
def ask_user():
	while True:
		ask_user = input("Ваш вопрос Пользователь: ")
		if ask_user in catalog_w:
			print(f"Программа: {catalog_w[ask_user]}")
			break
ask_user( )
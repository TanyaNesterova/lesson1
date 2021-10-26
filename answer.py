answers = {
	"привет": "Привет!",
	"как дела": "Отлично. А у тебя?",
	"Пока": "Еще увидимся!"

}

def get_answer(question, answers):
	return answers.get(question)


def ask_user(answers):
	while True:
		user_input = input("Скажи что-нибудь:")
		answer = get_answer(user_input, answers)
		print(answer)

		if user_input == "Пока":
			print("ну пока")
			break

def exc_q(answers):
	try:
		return ask_user(answers)
	except KeyboardInterrupt:
		print("До встречи")	

if __name__=="__main__":
	exc_q(answers)
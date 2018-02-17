def get_answer(question, answers):
    question = question.lower()
    answer = answers[question]
    return answer

answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

while True:
    question = input('Question? ')
    print(get_answer(question, answers))
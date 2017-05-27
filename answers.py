def get_answer(question):
    answer = {"привет" : "И тебе привет!", "как дела" : "Лучше всех", "пока" : "Увидимся" }
    return str.lower(answer[question.lower()])
question = input()
print(get_answer(question))

# 30. Quiz Database
# Questions are stored inside a JSON file.
# Your program loads questions automatically.
# Practice
#     • JSON
#     • loops
#     • functions
# --------------------------------------------

import json


def load_questions():
    with open("questions.json", "r") as file:
        questions = json.load(file)

    return questions


def ask_question(question):
    print(question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Your answer: ")

    return answer.upper()


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False


def run_quiz(questions):
    score = 0

    for question in questions:
        answer = ask_question(question)

        if check_answer(answer, question["answer"]):
            score += 1
            print("Correct!")

        else:
            print("Wrong!")

    percentage = (score / len(questions)) * 100

    print("\nQuiz Finished!")
    print("Score:", score, "/", len(questions))
    print("Percentage:", percentage, "%")


questions = load_questions()

run_quiz(questions)

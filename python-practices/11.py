# Quiz Game
# Ask
# 10 questions
# Example
# Capital of Germany?

# A Berlin

# B Paris

# C Madrid
# Keep score.
# Show percentage.
# ------------------------

questions = [
  {
    "question": "Capital of France?",
    "options": ["A Paris", "B London", "C Rome"],
    "answer": "A"
  },
  {
    "question": "Largest planet in our solar system?",
    "options": ["A Earth", "B Jupiter", "C Mars"],
    "answer": "B"
  },
  {
    "question": "Who wrote Romeo and Juliet?",
    "options": ["A William Shakespeare", "B Charles Dickens", "C Mark Twain"],
    "answer": "A"
  },
  {
    "question": "What is the chemical symbol for water?",
    "options": ["A O2", "B H2O", "C CO2"],
    "answer": "B"
  },
  {
    "question": "Which continent is Egypt located in?",
    "options": ["A Asia", "B Europe", "C Africa"],
    "answer": "C"
  },
  {
    "question": "How many sides does a triangle have?",
    "options": ["A Three", "B Four", "C Five"],
    "answer": "A"
  },
  {
    "question": "Who painted the Mona Lisa?",
    "options": ["A Pablo Picasso", "B Leonardo da Vinci", "C Vincent van Gogh"],
    "answer": "B"
  },
  {
    "question": "What is the fastest land animal?",
    "options": ["A Cheetah", "B Lion", "C Horse"],
    "answer": "A"
  },
  {
    "question": "Which ocean is the largest?",
    "options": ["A Atlantic Ocean", "B Indian Ocean", "C Pacific Ocean"],
    "answer": "C"
  },
  {
    "question": "What is the boiling point of water at sea level?",
    "options": ["A 50°C", "B 100°C", "C 150°C"],
    "answer": "B"
  }
]

score = 0

for question in questions:

    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    user_answer = input("Your answer: ")
    user_answer = user_answer.upper()

    if user_answer == question["answer"]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")


percentage = (score / len(questions)) * 100

print("\nQuiz Finished!")
print("Score:", score, "/", len(questions))
print("Percentage:", percentage, "%")
from quizclass import *
quiz = Quiz()

quiz.read_questions("questions.txt")
quiz.runQuiz()
print(f"the score is :{quiz.score}")

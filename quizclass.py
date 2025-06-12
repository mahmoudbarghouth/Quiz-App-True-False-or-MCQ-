from questionclass import *

class Quiz:
     def __init__(self):
         self.questions = []
         self.score = 0

     def read_questions(self,filename):

        with open(filename,"r") as file:
            for line in file:
                parts=line.strip().split(';')
                if len(parts) == 3:
                    text=parts[0]
                    choices=parts[1].split(',')
                    answer=parts[2]
                    self.questions.append(Question(text,choices,answer))
        print(self.questions[0].text)

     def runQuiz(self):
         for i, question in enumerate(self.questions):
             print(f'Q({i + 1}) {question.text}')
             for g, choice in enumerate(question.choices):
                 print(f'{chr(97 + g)}) {choice}')

             while True:
                 answer = input('Please enter your answer (a/b/c/...): ').lower()
                 if len(answer) == 1 and 'a' <= answer < chr(97 + len(question.choices)):
                     break
                 else:
                     print("❌ Invalid input! Try again.")

             if question.choices[ord(answer) - 97] == question.answer:
                 self.score += 1
                 print("✅")
             else:
                 print("❌")

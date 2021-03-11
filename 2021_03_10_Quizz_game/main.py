from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_q = Question(text, answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")
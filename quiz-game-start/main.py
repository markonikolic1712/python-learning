from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []
quiz_brain = QuizBrain(questions_bank)

for question in question_data:
    questions_bank.append(Question(question.get("text"), question.get("answer")))

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
    print(quiz_brain.still_has_questions())

print(f"You've completed the quiz.")
print(f"Your final score was: {quiz_brain.score}/{len(quiz_brain.question_list)}.")
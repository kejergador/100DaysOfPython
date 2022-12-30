from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []


for question in question_data:
    text_bank = question["question"]
    answer_bank = question["correct_answer"]
    new_question = Question(text_bank, answer_bank)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

quiz.completed_quiz()

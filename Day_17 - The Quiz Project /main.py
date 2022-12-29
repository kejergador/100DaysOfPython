from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []


for question in question_data:
    text_bank = question["text"]
    answer_bank = question["answer"]
    new_question = Question(text_bank, answer_bank)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz.still_has_questions()

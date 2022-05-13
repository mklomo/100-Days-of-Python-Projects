from question_model import Question
from quiz_brain import QuizBrain

# Creating a question bank

questions = Question()

quiz = QuizBrain(question_dict=questions.get_question_bank())

more_questions = quiz.still_has_question()

while more_questions:
    # Ask the next  question
    answer_provided, right_answer = quiz.next_question()
    # Check if the answer is correct
    is_right = quiz.check_answer(user_answer=answer_provided, correct_answer=right_answer)
    
    # Check for more questions
    more_questions = quiz.still_has_question()
    
    # if user is right and no more questions
    if is_right and not more_questions:
        break
    
    # If user is right and there are more questions, ask another question
    elif is_right and more_questions:
        continue
    
    # If user is wrong 
    elif not is_right:
        break
        

print("You've completed the quiz")

# Get the total score
quiz.get_total_score()

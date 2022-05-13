# TODO :1 : Ask the Questions

# TODO :2 : Check if the answer is correct

# TODO :3 : Checking if we're at the end of the quiz


class QuizBrain:
    
    def __init__(self, question_dict, score=0, question_number = 1):
        self._question_dict = question_dict
        self._score = score
        self._question_number = question_number


    def still_has_question(self):
        # Check if it is the last question
        return self._question_number < len(self._question_dict)


    def next_question(self):
        question_item = self._question_dict[self._question_number]
        question_text = question_item[f"Question_{self._question_number}"]
        question_answer = question_item[f"Answer_{self._question_number}"]
        user_answer = input(f"Q.{self._question_number} {question_text} (True or False)? \n")
        return user_answer, question_answer


    def check_answer(self, user_answer, correct_answer):
        
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self._score += 1
            # Move to the next question
            self._question_number += 1
            print(f"Your current score is: {self._score}/{list(self._question_dict)[-1]}")
            # Should we continue to next question?
            return True

        else:
            print("That's wrong!")
            print(f"Your current score is: {self._score}/{list(self._question_dict)[-1]}")
            print(f"The correct answer is {correct_answer}\n")
            # Should we continue to next question?
            return False
            

    def get_total_score(self):
        print(f"Your final score is {self._score}/{list(self._question_dict)[-1]}")

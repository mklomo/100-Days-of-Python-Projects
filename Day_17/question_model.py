import json

import requests



class Question:
    
    URI = "https://opentdb.com/api.php?amount=15&type=boolean"
    
    OPENT_DB = requests.get(URI)
    
    QUESTION_DATA = OPENT_DB.json()['results']
    
    
    def __init__(self):
        """Initializes the class"""
        self._question_bank = {}
        
        for i in range(len(Question.QUESTION_DATA)):
            q_num = i + 1
            self._question_bank[q_num] = {f"Question_{q_num}": Question.QUESTION_DATA[i]['question'],
                                          f"Answer_{q_num}": Question.QUESTION_DATA[i]['correct_answer']}
            
    def get_question_bank(self):
        return self._question_bank
            


from typing import List
from collections.abc import Iterable


# a question has a unique id, a number of options, and a category
class Question(object):
    def __init__(self, option_num:int, weight:float = 1) -> None:
        self.option_num = option_num
        self.weight = weight

    def __str__(self) -> str:
        return f"""问题共{self.option_num}个选项, 权重为{self.weight}"""

    __repr__ = __str__

# a questionnaire is a list of questions
class Questionaire(object):
    # pattern is a
    def __init__(self, questions:List[Question]) -> None:
        self.questions = questions

    def __len__(self) -> int:
        return len(self.questions)
    
    def scale_by_max(self, maximum:int = 100):
        for question in self.questions:
            question.weight = maximum / self.__len__() * question.weight

    def __str__(self) -> str:
        return f"""这是一个{self.__len__()}个问题的问题集"""

    __repr__ = __str__


class Player(object):
    def __init__(self, name, gender:int, city:str = "杭州"):
        self.name = name
        """ 0: male , 1: female"""
        self.gender = gender
        self.city = city


    def __str__(self) -> str:
        self.gender_text = "男" if self.gender == 0 else "女"
        return f"""{self.name}, 性别 {self.gender_text}"""

    __repr__ = __str__

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.gender == other.gender

class AnswerSheet(object):
    def __init__(self, player:Player, questionnaire:Questionaire, answers:List[int] ) -> None:
        self.player = player
        self.questionnaire = questionnaire
        self.answers = answers

    def __str__(self) -> str:
        return self.player

    __repr__ = __str__


    def __iter__(self):
        return self

    def matching_score(self, other, mode:int = 0) -> float:
        # if self.questionnaire != other.questionnaire:
        #     raise ValueError("questionaire does not match")

        total_distance = 0
        question_num = len(self.answers)

        for i in range(question_num):
            option_num = self.questionnaire.questions[i].option_num
            weight = self.questionnaire.questions[i].weight
            
            total_distance += abs(self.answers[i] - other.answers[i]) / option_num * weight
        
        return round(100 - total_distance,2)



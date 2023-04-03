# -*-coding:utf-8 -*-
#!/usr/bin/env python3
import io
import sys
from typing import List
import pandas as pd
import rules


# 腾讯问卷csv
class TXQuestionnaire(object):
    def __init__(
            self, 
            questionnaire: rules.Questionaire, 
            nickname_column:int = 11, 
            gender_column:int = 12, 
            question_columns:List[int] = [13,14,15,16,17,18,19,20,21,22], 
            starting_line = 2) -> None:
        
        self.questionnaire = questionnaire
        self.starting_line = starting_line
        self.nickname_column = nickname_column
        self.gender_column = gender_column
        self.question_columns = question_columns

    def read_lines(self, dataframe:pd.DataFrame, questionnaire:rules.Questionaire) -> List[rules.AnswerSheet]:
        answersheets = []
        for line in range(len(dataframe)):
            new_player = rules.Player(dataframe.iloc[line, self.nickname_column], int(dataframe.iloc[line, self.gender_column]) - 1)
            new_answers = []
            for column in self.question_columns:
                new_answers.append(dataframe.iloc[line, column])
            answersheets.append(rules.AnswerSheet(new_player, questionnaire, new_answers))

        return answersheets





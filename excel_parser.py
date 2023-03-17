# -*-coding:utf-8 -*-
#!/usr/bin/env python3
import io
import sys
from typing import List
import pandas as pd
import rules


# 腾讯问卷csv
class TXQuestionnaire(object):
    def __init__(self, questionnaire: rules.Questionaire, starting_line = 2):
        self.questionnaire = questionnaire
        self.starting_line = starting_line
        self.colomns = [13,14,15,16,17,18,19,20,21,22]

    def read_lines(self, dataframe:pd.DataFrame, questionnaire:rules.Questionaire) -> List[rules.AnswerSheet]:
        answersheets = []
        for line in range(len(dataframe)):
            new_player = rules.Player(dataframe.iloc[line, 11], int(dataframe.iloc[line, 12]) - 1)
            new_answers = []
            for colomn in self.colomns:
                new_answers.append(dataframe.iloc[line, colomn])
            answersheets.append(rules.AnswerSheet(new_player, questionnaire, new_answers))

        return answersheets

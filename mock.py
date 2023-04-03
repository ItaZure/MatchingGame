import random
from typing import List
import algorithm

import rules
# generate a list of players
def generate_players(num:int) -> List[rules.Player]:
    player_list = []
    for i in range(num):
        player_list.append(rules.Player("Mock Player" + str(i), random.randint(0,1)) )
    return player_list

def generate_questionnaire(total_num:int, option_num:int, weight:float = 1) -> rules.Questionaire:
    question_list = []
    for i in range(total_num):
        question_list.append(rules.Question(option_num, weight))

    return rules.Questionaire(question_list)

def generate_answer_sheet(player:rules.Player, questionnaire:rules.Questionaire) -> rules.AnswerSheet:
    answer = []
    for question in questionnaire.questions:
        answer.append(random.randint(0,question.option_num - 1))
    return rules.AnswerSheet(player, questionnaire, answer)


if __name__ == "__main__":
    mock_players = generate_players(20)
    mock_questionnaire = generate_questionnaire(10, 5)
    mock_questionnaire.scale_by_max(100)
    answersheet_list = [generate_answer_sheet(player, mock_questionnaire) for player in mock_players]

    all_pair = algorithm.Pairs(answersheet_list)

    # print(all_pair)
    pair_1 = algorithm.PairsForOne(answersheet_list, answersheet_list[2])
    pair_1.sort_by_score()
    pair_1.only_hexo()
    print(all_pair.top_pairs())


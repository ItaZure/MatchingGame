import rules
from typing import List
import pandas as pd

# Pairs is a list
# any element is a dict of ((player_1, player_2), score)
class Pairs(object):
    def __init__(self, answersheets:List[rules.AnswerSheet]) -> None:
        player_number = len(answersheets)

        all_pairs = []
        
        for i in range(player_number):
            for j in range(i + 1, player_number):
                new_pair = ((answersheets[i].player, answersheets[j].player), answersheets[i].matching_score(answersheets[j]) )
                all_pairs.append(new_pair)

        self.pairs = all_pairs
        
        self.male_num = 0
        self.female_num = 0
        for answersheet in answersheets:
            if answersheet.player.gender == 0:
                self.male_num += 1
            else:
                self.female_num += 1

    def __str__(self) -> str:
        return str(self.pairs)

    def sort_by_score(self) -> None:
        self.pairs.sort(key = lambda x: x[1], reverse = True)
    
    # mode: 0 - hexo, 1 - homo
    def filter_by_gender(self, mode:int = 0) -> List[tuple]:
        filtered_pairs = []

        for pair in self.pairs:
            if pair[0][0].gender ^ pair[0][1].gender:
                if mode == 0:
                    filtered_pairs.append(pair)
                else:
                    filtered_pairs.append(pair) 

        return filtered_pairs
            

    def dataframe(self, two_name = True, show_rel_rank = 0) -> pd.DataFrame:
        df = pd.DataFrame(self.pairs, columns = ["pair", "score"])
        df["玩家1"] = df["pair"].apply(lambda x: x[0].name)
        df["玩家2"] = df["pair"].apply(lambda x: x[1].name)
        df["默契分"] = df["score"].apply(lambda x: round(x))

        return pd.DataFrame(df, columns = ["玩家1", "玩家2", "默契分"])

    # return the rank of pair (player_1, player_2) in the list
    def show_rank(self, player_1:rules.Player, player_2:rules.Player) -> int:
        self.sort_by_score()

        try:
            return self.pairs.index((player_1.name, player_2.name)) + 1
        except:
            return self.pairs.index((player_2.name, player_1.name)) + 1
    
    def only_hexo(self):
        self.pairs = list(filter(lambda pair: pair[0][0].gender != pair[0][1].gender, self.pairs))

    # a single player cannot appears twice
    def top_pairs(self) -> List[tuple]:
        self.only_hexo()
        self.sort_by_score()

        top_pairs = []
        del_players = []
        while(self.female_num >0 and self.male_num > 0):
            pair = self.pairs.pop(0)
            if pair[0][0].name not in del_players and pair[0][1].name not in del_players:
                top_pairs.append(pair)
                del_players.append(pair[0][0].name)
                del_players.append(pair[0][1].name)
                self.male_num -= 1
                self.female_num -= 1
    
        return top_pairs

        
        


class PairsForOne(Pairs):
    def __init__(self, answersheets:List[rules.AnswerSheet], spec:rules.AnswerSheet) -> None:
        super().__init__(answersheets)
        self.owner = spec.player

        player_num = len(answersheets)
        self.pairs = []

        for i in range(player_num):
            if answersheets[i].player != self.owner:
                self.pairs.append(((self.owner, answersheets[i].player), spec.matching_score(answersheets[i])))

    def filter_by_player(self, pair_list:List[tuple], player_name:str) -> List[tuple]:
        return list(filter(lambda x: player_name in x[0], pair_list))

    def transform_to_df(self, two_name = True, show_rel_rank = 0) -> pd.DataFrame:
        pass

    # return the rank of pair (player_1, player_2) in the list
    def show_rank(self, player_1:rules.Player, player_2:rules.Player) -> int:
        self.sort_by_score()

        try:
            return self.pairs.index((player_1.name, player_2.name)) + 1
        except:
            return self.pairs.index((player_2.name, player_1.name)) + 1
        
    def top_pairs(self, number:int) -> List[tuple]:
        self.sort_by_score()
        return self.pairs[:number]


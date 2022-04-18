import random as rand

class set():
    def __init__(self, card_list, name):
        self.card_list = card_list
        self.name = name

    def pick_card(self):
        'picks a card based on the current weightings of each card within a set'
        weight_list = []
        for each in self.card_list:
            weight_list.append(each.weight)
        return rand.choice(self.card_list,weights=weight_list)
    
    def question_builder(self,answer_num):
        'builds a question of "answer_num" possibilities, returns in format question,correct ans, answer possibility list'
        temp_cardlist = self.card_list
        selected_card = self.pick_card
        temp_cardlist.remove(selected_card)
        answer_list = []
        for i in range(answer_num-1):
            answer_list.append(rand.choice(temp_cardlist))
            temp_cardlist.pop(answer_list[i])
        answer_list.append(selected_card.answer)
        rand.shuffle(answer_list)
        return selected_card.question, selected_card.answer, answer_list, selected_card
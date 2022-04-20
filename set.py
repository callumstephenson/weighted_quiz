import random as rand

class set():
    def __init__(self, card_list, name):
        self.card_list = card_list
        self.name = name

    def __repr__(self):
        d = "The card list is " + str(self.card_list) + "\n"
        d += "The name of the set is " + str(self.name)
    
    def pick_card(self):
        'picks a card based on the current weightings of each card within a set'
        weight_list = []
        for each in self.card_list:
            weight_list.append(each.weight)
        weight_list = tuple(weight_list)
        return rand.choices(self.card_list,weights=weight_list)[0]
    
    def question_builder(self,answer_num):
        'builds a question of "answer_num" possibilities, returns in format question,correct ans, answer possibility list'
        temp_cardlist = self.card_list
        selected_card = self.pick_card()
        temp_cardlist.remove(selected_card)
        answer_list = []
        for i in range(answer_num-1):
            rand.shuffle(temp_cardlist)
            answer_list.append(temp_cardlist.pop().answer)
        answer_list.append(selected_card.answer)
        rand.shuffle(answer_list)
        return selected_card.question, selected_card.answer, answer_list, selected_card
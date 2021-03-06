class card():
    def __init__(self,question,answer,weight=1):
        self.question = question
        self.answer = answer
        self.weight = weight
        self.inRotation = True
    
    def __repr__(self):
        d = "The question is " + str(self.question) +"\n"
        d += "The answer is " + str(self.answer) +"\n"
        d += "The current weight is " + str(self.weight) +"\n"
        d += "Current card in rotation? " + str(self.inRotation)
        return d

    def updateWeight(self,time,time_elapsed,ansCorrect=False):
        'updates the weight of the card object based on if the answer is correct/incorrect'
        if ansCorrect:
            self.weight = self.weight*(0.75+0.25*(time_elapsed/time))
            self.updateRotation()
        else:
            self.weight = self.weight*(1.25+0.25*(time_elapsed/time))

    def updateRotation(self):
        "updates the card's 'inRotation' attribute based on current weight, a weight lower than 0.4 results in False"
        if self.weight < 0.4:
            self.inRotation = False
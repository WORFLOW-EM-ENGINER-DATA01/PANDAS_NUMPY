
class Card:
    def __init__(self, card):
        self.color = card[0]
        pattern = {'J': 11, 'Q': 12, 'K' : 13, 'A' : 1}

        if card[1] in pattern.keys():
            self.value = pattern[card[1]]
        else:
            self.value = int(card[1])

        
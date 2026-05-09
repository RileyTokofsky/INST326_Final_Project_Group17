from abc import ABC, abstractmethod

class Bet(ABC):
    """
    done by: Riley Tokofsky
    """
    def __init__(self, value):
        self.value = value
        self.result = None

    @abstractmethod
    def resolve(self, outcome):
        pass

    @abstractmethod
    def payout(self):
        pass

    def __str__(self):
        return f"Bet: ${self.value}, Result: {self.result}"


class StandardBet(Bet):
    def resolve(self, outcome):
        self.result = outcome

    def payout(self):
        if self.result == "blackjack":
            return int(self.value * 2.5)
        if self.result == "win":
            return self.value * 2
        if self.result == "push":
            return self.value
        return 0
    
class Pairs(Bet):
    def __init__(self, value, type):
        super().__init__(value)
        self.type = type
        
    def resolve(self, outcome):
        self.result = outcome

    def payout(self):
        if self.result == "win" and self.type == "pp":
            return int(self.value * 7)
        if self.result == "win" and self.type == "mp":
            return int(self.value * 13)
        if self.result == "win" and self.type == "cp":
            return int(self.value * 31)
        else:
            return 0
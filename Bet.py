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
        """
        Purpose: constructor for pair bet class
        Arguments: value as how much you want to bet, type as the type of pair
            bet
        Returns: none
        Author: Ama
        """
        super().__init__(value)
        self.type = type
        
    def resolve(self, outcome):
        """
        Purpose: sets result instance var to the decided outcome
        Arguments: outcome as the calculated outcome of a pair bet
        Returns: none
        Author: Ama
        """
        self.result = outcome

    def payout(self):
        """
        Purpose: pays out winnings to pair betters
        Arguments: none
        Returns: pay out depending on whether you won or lost
        Author: Ama
        """
        if self.result == "win" and self.type == "pp":
            return int(self.value * 31)
        if self.result == "win" and self.type == "mp":
            return int(self.value * 6)
        if self.result == "win" and self.type == "cp":
            return int(self.value * 11)
        else:
            return 0
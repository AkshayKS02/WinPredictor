class WinStats:
    def __init__(self,results):
        self.results=results
    
    def get_total_matches(self):
        return len(self.results)
    
    def get_total_wins(self):
        wins=0
        for res in self.results:
            if res=="W" or res=="w":
                wins+=1
        return wins
    
    def get_total_losses(self):
        losses=0
        for res in self.results:
            if res=="L" or res=="l":
                losses+=1
        return losses
    
    def get_win_rate(self):
        numMatch=self.get_total_matches()
        numWins=self.get_total_wins()
        return float(numWins/numMatch)
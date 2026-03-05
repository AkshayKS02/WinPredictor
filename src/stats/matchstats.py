class MatchStats:
    def __init__(self,score):
        self.score=score

    def get_number_matches(self):
        matches=len(self.score)
        if matches==0:
            raise RuntimeError("List is empty")
        else:
            return matches
    
    def get_total_runs(self):
        sum=0
        for num in self.score:
            sum+=num
        return sum
    
    def get_average_score(self):
        sum=self.get_total_runs()
        matches=self.get_number_matches()
        return float(sum/matches)
    
    def get_highest_score(self):
        return max(self.score)
    
    def get_lowest_score(self):
        return min(self.score)
    
    def get_score_range(self):
        max=self.get_highest_score()
        min=self.get_lowest_score()
        return [min,max]
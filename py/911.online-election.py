#
# @lc app=leetcode id=911 lang=python3
#
# [911] Online Election
#

# @lc code=start
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        votes = collections.defaultdict(int)
        winner = 0
        self.winners = [None] * len(times)
        self.times = times
        for i, person in enumerate(persons):
            votes[person] += 1 
            if votes[person] >= votes[winner]:
                winner = person
            self.winners[i] = winner
    
    def q(self, t: int) -> int:
        return self.winners[bisect.bisect(self.times, t) - 1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

# @lc code=end


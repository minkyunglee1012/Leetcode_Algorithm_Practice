class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        
        team_list = []
        output = 0
        for i in range(len(skill)//2):
            team_list.append(skill[i]+skill[len(skill)-1-i])
            output += skill[i] * skill[len(skill)-1-i]
            
        if len(set(team_list)) != 1:
            return -1
        return output
        
        
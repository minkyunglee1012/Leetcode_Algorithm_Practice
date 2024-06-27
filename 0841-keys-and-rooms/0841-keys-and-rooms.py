class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        l = []
        l.extend(rooms[0])
        
        for i in l:
            for j in rooms[i]:
                if j not in l:
                    l.append(j)
        
        for i in range(1, len(rooms)):
            if i not in l:
                return False
        return True
  
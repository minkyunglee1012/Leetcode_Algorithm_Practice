class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        # row for문 순회하면서 1이 몇개 인지 각각 카운트에서 리스트에 저장
        # 리스트에서 인덱스와 그 값 리턴
        
        mat_one = []
        
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count +=1
            mat_one.append(count)
            
            
        answer = [mat_one.index(max(mat_one)), mat_one[mat_one.index(max(mat_one))]]
        
        return answer
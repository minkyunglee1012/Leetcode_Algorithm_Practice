class Solution:
    def greatestLetter(self, s: str) -> str:
        upper_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_letter = "abcdefghijklmnopqrstuvwxyz"
        
        upper_list = []
        lower_list = []
        
        for i in range(len(s)):
            if s[i] in upper_letter:
                upper_list.append(s[i])
            else:
                lower_list.append(s[i])

                
        output = []
        
        for i in range(len(upper_list)):
            if lower_letter[upper_letter.index(upper_list[i])] in lower_list:
                output.append(upper_list[i])
                
        output = sorted(output)
        print(output)
        if output:
            return output[-1]
        else:
            return ""
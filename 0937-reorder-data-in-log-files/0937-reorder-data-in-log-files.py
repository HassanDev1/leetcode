class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        dig = []
        letter = []
        
        for log in logs:
            if log.split(" ")[1].isdigit():
                dig.append(log)
            else:
                letter.append(log)
                
        letter.sort(key=lambda x:(x.split(" ")[1:],x.split(" ")[0]))
        
        return letter+dig
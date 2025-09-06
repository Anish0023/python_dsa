class Solution(object):
    def findleastrepeatingcharacter(self, n):
        mp  = {}
        n_str = str(n)
        for ch in n_str:
            if ch in mp:
                mp[ch] += 1
            else:
                mp[ch] = 1
        min_count = float('inf')
        #if multiple digit have same frequency then return the smallest digit
        idx = 0
    
        for k,v in mp.items():
            if v < min_count:
                min_count = v
                if v == min_count:
                    if int(k) < int(idx):
                        idx = k
                else:           
                    idx = k
        return int(idx)
        
if __name__ == "__main__":
    n = 2
    print(Solution().findleastrepeatingcharacter(n))
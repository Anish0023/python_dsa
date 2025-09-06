class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        # try to create sorted dic
        res = ' '
        a = s.split()
        ans = []
        mp = {}
        for word in a:
            mp[word[-1]] = word[:-1]
        #sorting the dictionary keys
        for k in sorted(mp):
            ans.append(mp[k])
        return res.join(ans)
if __name__ == "__main__":
    s = "is2 sentence4 This1 a3"
    print(Solution().sortSentence(s))
    s1 = "Myself2 Me1 I4 and3"
    print(Solution().sortSentence(s1))
'''
Here sort by removing the last character from each word and sorting it according to it.
'''
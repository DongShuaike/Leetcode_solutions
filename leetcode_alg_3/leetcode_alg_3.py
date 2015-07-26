#Given a string, find the length of the longest substring without repeating characters. 
#For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
#For "bbbbb" the longest substring is "b", with the length of 1.

class Solution:
    #@param {string} s
    #@return {integer}
    def lengthOfLongestSubstring(self,s):
        l=r=0
        maxval=0
        #list=[chr(i) for i in range(97,123)]
        #dic=dict().fromkeys(list,0)
        dic={}
        for r in range(0,len(s)):
            dic[s[r]]=0
        for r in range(0,len(s)):
            #if not dic.has_key(s[r]):
            #else:
                #dic.pop(s[l])
            while dic[s[r]]==1:
                dic[s[l]]=0
                l+=1
            dic[s[r]]=1
            maxval=max(maxval,r-l+1)

        return maxval

if __name__=="__main__":
    s = Solution()
    print s.lengthOfLongestSubstring('eee')
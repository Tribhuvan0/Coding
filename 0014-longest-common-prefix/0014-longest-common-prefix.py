class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stri = ""
        #if there would be any other world with not same prefix the first or 
        #last word would be displaced, if the word is smaller than first word
        #it will get first position otherwise last
        sorted_list = sorted(strs)
        first_word = sorted_list[0]
        last_word = sorted_list[-1]
        
        for i in range(min(len(first_word), len(last_word))):
            if first_word[i] != last_word[i]:
                return stri
            stri += first_word[i]
        return stri
        
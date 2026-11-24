class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        vowels = set("aeiou")
        count = 0
        for w in words[left:right + 1]:
            if w[0] in vowels and w[-1] in vowels:
                count += 1
        return count



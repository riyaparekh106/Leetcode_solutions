class Solution(object):
    def isPalindrome(self, s):
        s = re.sub("[^a-z0-9]",'',s.lower())
        if s == ''.join(reversed(s)):
            return True
        return False;
class Solution():
    def _reverse(self,string):
        rev = ""
        string = str(string)
        for i in range(len(string)):
            rev += string[len(string)-1-i]
        return rev

    def isPalindrome(self,string):
        if self._reverse(string) == string:
            return "true"
        else:
            return "false"

string = input()
print(Solution().isPalindrome(string))
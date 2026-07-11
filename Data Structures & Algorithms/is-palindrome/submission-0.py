class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str="".join(char for char in s if char.isalnum())

        new=clean_str[::-1]
        print(new)
        print(clean_str)
        if new.lower()==clean_str.lower():
            return True

        return False
        
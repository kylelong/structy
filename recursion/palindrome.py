import string
def isPalindrome(s: str) -> bool:
    def clean(s):
        return "".join([c for c in s.lower() if c.isalnum()])
    
    s = clean(s)

    def is_palindrome(left, right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return is_palindrome(left + 1, right - 1)
    
    return is_palindrome(0, len(s) - 1)
assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("ravens football") == False
assert isPalindrome("racecar") == True
assert isPalindrome("Was it a car or a cat I saw?") == True
assert isPalindrome("Do geese see God?") == True
assert isPalindrome("Never odd or even") == True
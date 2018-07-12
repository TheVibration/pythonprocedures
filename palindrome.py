# A palindrome is a word that reads
# the same way forward and backwards
# so for ex. radar is a palindrome.
# This procedure is going to use recursion
# to test to see if a string is a palindrome.
# A boolean will be returned on whether
# word is a palindrome or not.

def ispalindrome(word):
    if word == '':
        return True
    else:
        if word[0] != word[-1]:
            return False
        else:
            if ispalindrome(word[1:-1]):
                return True
            else:
                return False

# Test
#print(ispalindrome("radar"))
#print(ispalindrome("bob"))
#print(ispalindrome("hello"))
#print(ispalindrome("aabbcdcdbbaa"))

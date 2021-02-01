# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]

# Driver code
s =str(input("Enter any word you can possibly think of: "))
ans = isPalindrome(s)

if ans:
    print("This is a palindrome!")
else:
    print("This is NOT a palindrome!")

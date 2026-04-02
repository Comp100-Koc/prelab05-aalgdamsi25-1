def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    max_palindrome=''
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i:j]==s[i:j][::-1]:
                if len(s[i:j])>len(max_palindrome):
                    max_palindrome= s[i:j]
                
    if len(max_palindrome)!=1:
        return max_palindrome
    else:
        return ''

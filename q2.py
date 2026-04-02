def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    found=''
    for i in range(len(s)):
        if found and s[i] == found[-1]:
            found=found[:-1]
        else:
            found+=s[i]
            
    return found


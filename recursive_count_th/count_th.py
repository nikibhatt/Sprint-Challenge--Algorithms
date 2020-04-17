'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):


    if (len(word) == 1 or len(word) == 0):
        return 0
    else:
        first_letter = word[0]
        second_letter = word[1]
        if (first_letter == 't' and second_letter == 'h'):
            return count_th(word[1:]) + 1
        return count_th(word[1:])



#word = "abcthxyzth"
#print(count_th(word))

'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if (len(word) == 1 or len(word) == 0):
        count = 0
        return count

    first_letter = word[0]
    second_letter = word[1]

    if (first_letter == 't' and second_letter =='h'):
        count += 1
        return count
    else:
        return count

    count = count_th(work[1:])


word = "abcthxyz"
print(count_th(word))

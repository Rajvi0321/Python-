def most_frequent(word):
    ansdict = dict()
    
    for ch in word:
        if ch in word:
            ansdict[ch] = 0
    for ch in word:
        if ch in list(ansdict.keys()):
            ansdict[ch] += 1
    return ansdict

user_in = input("\nEnter your word: ")
ansdict=most_frequent(user_in)
sort_dict = sorted(ansdict.items(), key=lambda x: x[1], reverse=True)
print(sort_dict)
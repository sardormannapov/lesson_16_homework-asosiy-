word1 = "Nope"
word2 = "Note"

def comparison(w1, w2):
    result = set(w2).issuperset(set(w1))
    return result

print(comparison(w1=word1, w2=word2))
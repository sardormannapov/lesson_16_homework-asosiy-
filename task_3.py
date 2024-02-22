word = "hello world"
word2 = ""

def duplicate(w, w2):
    for alp in w:
        w2 += alp*2
    return w2

print(duplicate(w=word, w2=word2))
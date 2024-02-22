def sortirovka(word):
    lst = list(word)
    srt = sorted(lst)
    str = "".join(srt)
    return str

print(sortirovka(word="hello"))
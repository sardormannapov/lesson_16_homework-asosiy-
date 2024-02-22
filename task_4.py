string = "eDaBiT"
result = []

def up(str, rezultat):
    for word in str:
        if word == word.upper():
            result.append(string.index(word))

    return rezultat

print(up(str=string, rezultat=result))
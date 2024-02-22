string = "Consecutive"

def calculate(str):
    word = str.casefold()
    for alp in word:
        if word.count(alp) == 1:
            return True

        else:
            return False


print(calculate(str=string))
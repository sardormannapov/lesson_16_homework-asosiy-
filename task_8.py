def sortirovks(word):
    if sorted(word) == list(word):
        return True
    else:
        return False

print(sortirovks(word="edabit"))
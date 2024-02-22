string = "I have never seen thin person drinking Diet Coke"
vowels = "aouie"
result = ""

def remove_vowels(str, vw, rezultat):
    for alp in str:
        if alp not in vw:
            rezultat += alp
    return rezultat

print(remove_vowels(str=string, vw=vowels, rezultat=result))
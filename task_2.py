count_character = ["###", "###", "###"]
result = 0

def calculate_count(string, rezultat):
    for cnt in string:
        count = count_character.count(cnt)
        rezultat += count
    return rezultat


print(calculate_count(string=count_character, rezultat=result))
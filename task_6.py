name = ["Adam", "Sarah", "Malcolm"]
lst = []

def first_index(lstt, result):
    for nm in lstt:
        lst.append(nm[0])
        lst.sort()
        result = "".join(lst)
    return result

print(first_index(lstt=name, result=lst))
def solution_asc(dic):
    return sorted(dic.items())


def solution_desc(dic):
    return list(reversed(sorted(dic.items())))

dic = {1: 20, 3: 40, 4: 30, 2: 10, 0: 8}
print solution_asc (dic)
print solution_desc(dic)

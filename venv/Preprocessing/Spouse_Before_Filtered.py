newFile = open('../Data/Spouse/Spouse_Before_Filtered.txt', 'w', encoding="utf-8")

Directions = False

with open('../Data/Spouse/Spouse_Clean.txt', encoding="utf-8") as f:
    for c in f.read():
        if Directions is False and c == '(':
            Directions = True
        elif Directions is True and c == ')':
            Directions = False
            continue

        if not Directions:
            newFile.write(c)

        if Directions:
            pass

try:
    lines = []
    with open(r"E:\python\works\01 - lessions\חודש 03.2025\‏‏16.03.2025\לימוד על קבצים\lior.txt", 'r') as file:
        for line in file:
            currentline = line.strip()
            lines.append(currentline)
        print(lines)
        
except Exception as err:
    print(err)


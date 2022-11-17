# -- coding: utf-8 --
file = open("Galushka.P.A_Y223_vvod.txt", "r")
mas = []
while True:
    x = file.readline().strip()
    if (x == ""):
        break
    mas.append(str(x))

end = []

for i in range(len(mas)):
    end.append([])
    for j in mas[i]:
        end[i].append(int(j))

for i in range(len(end)):
    end[i].sort()
    mx = min(end[i]);
    print(mx)
    for j in range(len(end[i])):
        if (mx % 2 == 0) and (mx == end[i][j]):
            end[i][j] = 0
            break
        elif (mx % 2 != 0) and (mx == end[i][j]):
            end[i][j] = 1
            break
print("\n", end)
with open("Galushka.P.A_Y223_vivod.txt", "w") as file:
    for i in range(len(end)):
        for j in range(len(end[i])):
            file.write(str(end[i][j]))
        file.write("\n")
# -- coding: utf-8 --
def function():
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

    print("\n", end)
    with open("Galushka.P.A_Y223_vivod.txt", "w") as file:
        for i in range(len(end)):
            for j in range(len(end[i])):
                file.write(str(end[i][j]))
            file.write("\n")
function()
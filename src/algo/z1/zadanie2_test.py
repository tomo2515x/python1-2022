import os
import matplotlib.pyplot as plt
dane = [
    5, 0.7,
    10, 0.75,
    100, 2.4,
    200, 4.9,
    400, 11,
    800, 29,
    1600, 86,
    3200, 224,
    6400, 497,
    12800, 1]

# zadanie -- wszystkie elementy na parzystych elementach --> do listy "x", pozostae do listy "y"

x, y = [], []

for i in dane:
    if dane.index(i) % 2 == 0: 
        x.append(i)
    else:
        y.append(i)
os.system("cls")
print(f"x={x} \ny={y}")

plt.plot(x,y)
plt.xlabel("Rozmiar danych")
plt.ylabel("Czas wykonania (usec)")
plt.show()



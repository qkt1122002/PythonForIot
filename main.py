import matplotlib.pyplot as plt
# import numpy as np

X = [0,3,5]
Y = [3,-4,8]

plt.subplot(2, 2, 1)
plt.plot(X, Y, marker='o')
plt.title('Do thi')
plt.xlabel('Truc X')
plt.ylabel('Truc Y')

# Ve do thi duong thang y = 2x + 2
# Trong doan [-10, 10]
x = []
y =[]
i = -5
while(i <= 5):
    x.append(i)
    i = i + 0.01
for a in x:
    s = 2*a*a + 3 * a - 1
    y.append(s)

plt.subplot(2, 2, 2)
plt.plot(x, y)

plt.title("do thi", loc='right')
plt.xlabel("Truc x")
plt.ylabel("Truc y")
plt.grid()
plt.show()
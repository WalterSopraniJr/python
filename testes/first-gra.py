from random import randrange, seed

seed(11)
randrange(0,11)

notas_matematica = []

for notas in range(8):
  notas_matematica.append(randrange(0,11))

print(notas_matematica)

len(notas_matematica)


import matplotlib.pyplot as plt

x = list(range(1,9))
y = notas_matematica
plt.plot(x, y, marker='o')
plt.title('Notas de Matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()
import matplotlib.pyplot as plt

p=[]
for N in range(1,51):
    nP=1.0
    for i in range(N):
        nP *= (365-i)/365
    p.append(1-nP)

plt.plot(p)
plt.show()
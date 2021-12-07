import matplotlib.pyplot as plt
import numpy

yal_price = [23.5, 24.0, 24.0, 24.5]
svin_price = [24.5, 26.0, 26.3, 26.5]
salo_price = [14.5, 14.6, 14.8, 15.0]

plt.plot(yal_price,label = "Яловичина", linewidth=5)
plt.plot(svin_price,label = "Свинина", linewidth=4)
plt.plot(salo_price,label = "Сало", linewidth=3)
plt.xlabel("На число мсяця")
plt.ylabel("Ціна")
plt.title('Графiк за Вересень')
plt.legend()
plt.grid(True)
plt.xticks(numpy.arange(4),(2,10,14,24))
plt.show()
def showplot2():
    plt.show()
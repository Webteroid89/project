import matplotlib.pyplot as plt
import numpy

yal_price = [25.5,23.5,30.8,23.7]
svin_price = [25.0,25.5,25.5,25.7]
salo_price = [14.5,14.5,14.5,14.5]

plt.plot(yal_price,label = "Яловичина", linewidth=5)
plt.plot(svin_price,label = "Свинина", linewidth=4)
plt.plot(salo_price,label = "Сало", linewidth=3)
plt.xlabel("На число мсяця")
plt.ylabel("Ціна")
plt.title('Графiк за Серпень')
plt.legend()
plt.grid(True)
plt.xticks(numpy.arange(4),(2,10,14,24))
plt.show()
def showplot1():
    plt.show()

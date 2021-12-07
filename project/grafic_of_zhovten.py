import matplotlib.pyplot as plt
import numpy

yal_price = [25.0, 25.0, 25.5, 25.5]
svin_price = [26.6, 26.8, 27.0, 27.4]
salo_price = [15.5, 15.5, 15.6, 16.0]


plt.plot(yal_price,label = "Яловичина", linewidth=5)
plt.plot(svin_price,label = "Свинина", linewidth=4)
plt.plot(salo_price,label = "Сало", linewidth=3)
plt.xlabel("На число мсяця")
plt.ylabel("Ціна")
plt.title('Графiк за Жовтень')
plt.legend()
plt.grid(True)
plt.xticks(numpy.arange(4),(2,10,14,24))
plt.show()
def showplot3():
    plt.show()
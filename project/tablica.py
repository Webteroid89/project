from tabulate import tabulate
dt = [
    ["Яловичина",25.5,23.5,30.8,23.7,'Серпень',25.88,25.50,1.01],
    ["Свинина",25.0,25.5,25.5,25.7,"Серпень",25.43,26.50,0.96],
    ["Cало",14.4,14.5,14.5,14.5,"Серпень",14.48,15.00,0.97],
    ["Яловичина",23.5,24.0,24.0,24.5,"Вересень",24.00,25.50,0.94],
    ["Свинина",25.5,26.0,26.3,26.6,"Вересень",26.08,26.50,0.98],
    ["Сало",14.5,14.6,14.8,15.0,"Вересень",14.73,15.00,0.98],
    ["Яловичина",25.0,25.0,25.5,25.5,"Жовтень",25.25,25.50,0.99],
    ["Свинина",26.6,26.8,27.0,27.4,"Жовтень",26.95,26.50,1.02],
    ["Сало",15.5,15.5,15.6,16.0,"Жовтень",15.65,15.00,1.04]]
tabl = ['Назва товару','На 2 число місяца','На 10 число місяця','На 14 число місяця','На 24 число місяця','Місяць','Середня ринкова ціна за місяць','Роздрібнка ціна,грн','Рівень зміни цін']
print (tabulate(dt,tabl,tablefmt="pipe"))
def opentable():
    print('\nАналіз')
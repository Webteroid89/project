import json


nounlist1 = [["Nazva tovary","Na druhe chyslo misyatsya", "Na desyate chyslo misyatsya", "Na chotyrnadtsyate chyslo misyatsya", "Na dvadtsyat chetverte chyslo misyatsya", "Misyats"],
    ['Yalovichina',25.5,23.5,30.8,23.7,'Serpen'],
    ["Svinina",25.0,25.5,25.5,25.7,"Serpen"],
    ["Salo",14.4,14.5,14.5,14.5,"Serpen"],
    ["Yalovichina",23.5,24.0,24.0,24.5,"Veresen"],
    ["Svinina",25.5,26.0,26.3,26.6,"Veresen"],
    ["Salo",14.5,14.6,14.8,15.0,"Veresen"],
    ["Yalovichina",25.0,25.0,25.5,25.5,"Zhovten"],
    ["Svinina",26.6,26.8,27.0,27.4,"Zhovten"],
    ["Salo",15.5,15.5,15.6,16.0,"Zhovten"]]

price = {'Price': nounlist1}

with open('price_json.json', 'w') as f:
    json.dump(price, f)


def ToJson1():
    with open('price_json.json') as f:
        print(f.read())

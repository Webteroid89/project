import json

nounlist2 = [
               ["Kod","Tovar","Rozdribna cina"],
               [10,"Yalovichina",25],
               [20,"Svinina",26],
               [30,"Salo",15]]

price = {'Tovar': nounlist2}

with open('tovar_json.json', 'w') as f:
    json.dump(price, f)


def ToJson2():
    with open('tovar_json.json') as f:
        print(f.read())
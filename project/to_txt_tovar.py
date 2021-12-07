import json

nounlist2 = [
               ["Kod","Tovar","Rozdribna cina"],
               [10,"Yalovichina",25],
               [20,"Svinina",26],
               [30,"Salo",15]]

json_obj = json.dumps(nounlist2, indent= 2)

with open("tovar.txt", "w") as f:
    f.write(json_obj)
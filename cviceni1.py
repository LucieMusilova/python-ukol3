import json

with open('body.json', mode="r", encoding='utf-8') as file: 
   body = json.load(file)
print(body)

for jmeno, pocet_bodu in body.items():
    if pocet_bodu >= 60:
        body[jmeno] = "Pass"
    else:
        body[jmeno] = "Fail"

with open('prospech.json', mode='w', encoding='utf-8') as file:
    json.dump(body, file, ensure_ascii=False)

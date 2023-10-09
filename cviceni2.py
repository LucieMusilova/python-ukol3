import json

with open('body.json', mode="r", encoding='utf-8') as file: 
   body = json.load(file)

with open('bonusy.json', mode="r", encoding='utf-8') as file: 
   bonusove_body = json.load(file)

vysledne_body = {}

for jmeno, pocet_bodu in body.items():
    vysledne_body[jmeno] = pocet_bodu

for jmeno, pocet_bodu in bonusove_body.items():
    if jmeno in vysledne_body:
        vysledne_body[jmeno] += pocet_bodu

for jmeno, pocet_bodu in vysledne_body.items():
    if pocet_bodu >= 90:
        vysledne_body[jmeno] = "A"
    elif pocet_bodu <= 89 and pocet_bodu >= 70:
        vysledne_body[jmeno] = "B"
    elif pocet_bodu <= 69 and pocet_bodu >= 50:
        vysledne_body[jmeno] = "C"
    elif pocet_bodu <= 49 and pocet_bodu >= 30:
        vysledne_body[jmeno] = "D"
    elif pocet_bodu <= 29:
        vysledne_body[jmeno] = "E"

with open('znamky.json', mode='w', encoding='utf-8') as file:
    json.dump(vysledne_body, file, ensure_ascii=False)




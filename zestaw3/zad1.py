import json
from textwrap import indent

with open("tramwaje.json", 'r', encoding='utf-8') as read_file:
    data = json.load(read_file)

better_data = {}
wszystkie_przystanki = {}

for i in range(len(data['linia'])):
    przystanki = list()
    if 'przystanek' in data['linia'][i]:
        ilosc_przystankow = len(data['linia'][i]['przystanek'])
        for j in range(ilosc_przystankow):
            nazwa = data['linia'][i]['przystanek'][j]['name']
            bez_numerkow = nazwa[:-3]
            przystanki.append(bez_numerkow)
            wszystkie_przystanki[bez_numerkow] = True

    better_data[int(data['linia'][i]['name'])] = przystanki

with open('tramwaje_out.json', 'w', encoding="utf-8") as file:
    json.dump(better_data, file, ensure_ascii=False, indent=2)

for linia in sorted(better_data, key = lambda i: better_data[i], reverse=True):
    print("linia " + '{: >2}'.format(linia) + ": " + '{: >2}'.format(len(better_data[linia])) + " przystankow")

print()
for przystanek in wszystkie_przystanki:
    print(przystanek)
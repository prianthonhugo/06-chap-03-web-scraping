import bs4
import requests

url = 'https://www.jadwalsholat.org/adzan/monthly.php?id=208'
contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, "html.parser")
data = response.find_all('tr', 'table-row-striped active')
data = data[0]
# print(data)

sholat = {}
# for d in data:
#     print(d)
i = 0

for d in data:
    if i == 5:
        sholat['Imsyak'] = d.get_text()
    elif i == 6:
        sholat['Shubuh'] = d.get_text()
    elif i == 7:
        sholat['Terbit'] = d.get_text()
    elif i == 8:
        sholat['Dhuha'] = d.get_text()
    elif i == 9:
        sholat['Dhuhur'] = d.get_text()
    elif i == 10:
        sholat['Ashr'] = d.get_text()
    elif i == 11:
        sholat['Maghrib'] = d.get_text()
    elif i == 12:
        sholat['Isya'] = d.get_text()
    i += 1

print(sholat)

print(f'Waktu Sholat Ashr adalah: {sholat['Ashr']}')
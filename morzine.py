# import requests

# url = "https://ski-resorts-and-conditions.p.rapidapi.com/v1/resort/portes-du-soleil"

# headers = {
# 	"X-RapidAPI-Key": "5dacc0e086mshf2c6575d2a2dc18p132160jsne77dc6d78e91",
# 	"X-RapidAPI-Host": "ski-resorts-and-conditions.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response.json())


# import requests

# url = "https://ski-resort-api.p.rapidapi.com/resort-list/country/france"

# headers = {
# 	"X-RapidAPI-Key": "5dacc0e086mshf2c6575d2a2dc18p132160jsne77dc6d78e91",
# 	"X-RapidAPI-Host": "ski-resort-api.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response.json())

# import requests

# url = "https://ski-resorts-and-conditions.p.rapidapi.com/v1/resort"

# headers = {
# 	"X-RapidAPI-Key": "5dacc0e086mshf2c6575d2a2dc18p132160jsne77dc6d78e91",
# 	"X-RapidAPI-Host": "ski-resorts-and-conditions.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response.json())

a = {'data': {'slug': 'morzine', 'name': 'Morzine', 'country': 'FR', 'region': 'ARA', 'href': 'https://en.morzine-avoriaz.com/ski-lift-opening.html', 'units': 'metric', 'location': {'latitude': 46.1789, 'longitude': 6.7089}, 'lifts': {'status': {'TPH PRODAINS 3S': 'closed', 'TD6 GRANDES COMBES': 'closed', 'TD6 LAC-INTRETS': 'closed', 'TD6 STADE': 'closed', 'TSK ARARE 2': 'closed', 'TSK ARARE1': 'closed', 'TSK PRODAINS': 'closed', 'TD4 CHOUCAS': 'closed', 'TD6 FORNET': 'closed', 'TS3 CUBORE': 'closed', 'TSK CHAVANETTE 1': 'closed', 'TSK CHAVANETTE 2': 'closed', 'TLC ARDENT': 'closed', 'TD4 LINDARETS': 'closed', 'TD4 MOSSETTES': 'closed', 'TD6 BROCHAUX': 'closed', 'TD6 CASES': 'closed', 'TD6 CHAUX FLEURIE': 'closed', 'TD6 LECHERE': 'closed', 'TD6 PROLAYS': 'closed', 'TSK BARMETTES': 'closed', 'TS3 PLATEAU': 'closed', 'TS6 TOUR': 'closed', 'TSK CHAPELLE': 'closed', 'TSK DES TRASHERS': 'closed', 'TSK DROMONTS 1': 'closed', 'TSK DROMONTS 2': 'closed', 'TSK ECOLES 1': 'closed', 'TSK ECOLES 2': 'closed', 'TLC SUPER': 'closed', 'TD4 ZORE': 'closed', 'TD6 PROCLOU': 'closed', 'TD6 SERAUSSAIX': 'closed', 'TSK BARON': 'closed'}, 'stats': {'open': 0, 'hold': 0, 'scheduled': 0, 'closed': 34, 'percentage': {'open': 0, 'hold': 0, 'scheduled': 0, 'closed': 100}}}}}

# print(a['data']['lifts'])
lifts = []
for i in a['data']['lifts']['status']:
    print(i)
    lifts.append(i)

print(lifts)
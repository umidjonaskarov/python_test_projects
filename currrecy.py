import requests

api_url = 'http://data.fixer.io/api/latest'
client_key = '06c143598fc4f79c00be2f6febfe424a'

currency = input('Enter currency code: ')
currency_2 = input('Enter base currency code: ')

params = {'access_key': client_key, 'symbols': currency}
get_data = requests.get(api_url, params=params)
data = get_data.json()
success = data['success']
timestamp = data['timestamp']
base = data['base']
date = data['date']
rates = data['rates']

print(success)
print(timestamp)
print(base)
print(date)
print(rates)

print(data)

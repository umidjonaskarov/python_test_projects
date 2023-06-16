import requests

params = {
    'access_key' : 'bef12957a226dc92b1c8974a33200daf',
}

city = input('Enter city name: ')
specific_date = input('Enter specific date:')
units = input('Enter m for celcius and s for Fahrenheit: ')

params['query'] = city
params['date'] = specific_date
params['units'] = units

api_result = requests.get('http://api.weatherstack.com/current', params=params)
api_response = api_result.json()

if 'current' in api_response:
    weather_data = api_response['current']
    temperature = weather_data['temperature']
    weather_description = weather_data['weather_descriptions'][0]
    humidity = weather_data['humidity']
    wind_speed = weather_data['wind_speed']

    print(f"Weather in {city} on {specific_date}:")
    print(f"Temperature: {temperature} {units.upper()}")
    print(f"Description: {weather_description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} km/h")
else:
    print("No weather data found for the specified parameters.")
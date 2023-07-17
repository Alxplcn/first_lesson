import requests

url = 'https://wttr.in/Череповец?MmnqT&lang=ru'
response = requests.get(url)
try:
  response.raise_for_status()
  print(response.text)
except requests.exceptions.HTTPError:
  print('Ошибка')

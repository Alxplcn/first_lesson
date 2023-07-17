import requests

def get_weather_from_certain_location(location: str) -> str:
  """Функция принимает наименование локации, по которой нужно получить погоду, и возвращает 
  полученный от сервера результат. В случае, если сервер вернул ошибку, возвращается слово
  "Ошибка"
  """
  base_url = 'https://wttr.in/'
  response = requests.get(base_url+location)
  try:
    response.raise_for_status()
  except requests.exceptions.HTTPError:
    return 'Ошибка'
  return response.text
  
print(get_weather_from_certain_location('london'))
print(get_weather_from_certain_location('svo'))
print(get_weather_from_certain_location('Череповец'))

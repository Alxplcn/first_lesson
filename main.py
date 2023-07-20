import requests


def get_weather(location: str) -> str:
    """Функция принимает наименование локации, по которой нужно получить погоду, и возвращает
    полученный от сервера результат. В случае, если сервер вернул ошибку, возвращается слово
    "Ошибка"
    """
    base_url = 'https://wttr.in/'
    response = requests.get(f"{base_url} {location}")
    return response.text


def main():
    # Шаг 3
    payload = {'nTqu': '',
               'lang': 'en'}
    url = 'https://wttr.in/san%20francisco'
    response = requests.get(url, params=payload)
    try:
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError:
        print('Ошибка на шаге 3')

    # Шаг 4
    locations = ['london', 'svo', 'Череповец']
    for location in locations:
        try:
            print(get_weather(location))
        except requests.exceptions.HTTPError:
            print('Ошибка на шаге 4')

    # Шаг 5
    payload = {'MmnqT': '',
               'lang': 'ru'}
    url = 'https://wttr.in/Череповец'
    response = requests.get(url, params=payload)
    try:
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError:
        print('Ошибка на шаге 5')


if __name__ == '__main__':
    main()

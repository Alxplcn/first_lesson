import requests
import os


def get_weather(location: str, payload: dict) -> str:
    """Функция принимает наименование локации, по которой нужно получить погоду, и возвращает
    полученный от сервера результат. В случае, если сервер вернул ошибку, возвращается слово
    "Ошибка"
    """
    base_url = 'https://wttr.in/'
    response = requests.get(f"{base_url} {location}", params=payload)
    response.raise_for_status()
    return response.text


def main():
    os.system('color')
    payload = {'MmnqT': '',
               'lang': 'ru'}

    locations = ['london', 'svo', 'Череповец']
    for location in locations:
        print(get_weather(location, payload))
    input("Нажмите любую клавишу для выхода ")


if __name__ == '__main__':
    main()

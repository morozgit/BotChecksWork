import requests


def main():
    headers = {
        'Authorization': 'Token b59cc5445ea444f525c516c39cab691038092c94'
    }
    url = 'https://dvmn.org/api/long_polling/'
    while (True):
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        print(response.json())


if __name__ == '__main__':
    main()

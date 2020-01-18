import requests

TOKEN = 'xxxxxxxxxxxxxxxxxx'


def send_message(text, chat_id):
    url = 'https://api.tekegram.org/bot{0}/sendMessage'.format(TOKEN)
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=data)
    print('\n>>>> RESPONSE: ' + response.content)

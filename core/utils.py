import requests

TOKEN = '1006254076:AAEVeYezbRPzFF4FRptN_TnDrt7dDRZUMHc'


def send_message(text, chat_id):
    url = 'https://api.tekegram.org/bot{0}/sendMessage'.format(TOKEN)
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=data)
    print('\n>>>> RESPONSE: ' + response.content)

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from core.utils import send_message
import requests
import json
# Create your views here.


@csrf_exempt
def event(requests):
    print('\n MEUS REQUESTS: ' + str(requests))
    json_list = json.loads(requests.body)
    print('\nJson List:' + str(json_list))
    chat_id = json_list['message']['chat']['id']
    print('\n>>>> Chat ID: ' + str(chat_id))
    send_message('I AM ALIVE MOTHAFOCKA', chat_id)
    return HttpResponse()
    # return JsonResponse({'status': 'true', 'message': 'Worked modafoca'})
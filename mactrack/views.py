from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
import urllib3
import requests
import datetime
import json
import os

# Create your views here.
# Default Index View
def index(request):
    return render(request, 'index.html')

def macTracker(request):
    mac_add = request.GET.get('mac')
    target_date = request.GET.get('date')
    mac_ad = mac_add.replace('%3A',':')
    if target_date != "":
        date = target_date
    else:
        now = datetime.datetime.now()
        date = now.strftime("%Y/%m/%d")
    #date = "2017/06/06"
    safeurl = open("static/api/url")
    preurl = safeurl.read()
    url = preurl+mac_ad
    querystring = { "date":date }
    safeauth = open("static/api/auth")
    safetoke = open("static/api/toke")
    headers = {
        'authorization': safeauth.read(),
        'cache-control': "no-cache",
        'postman-token': safetoke.read()
   }
    array = requests.request("GET", url, headers=headers, params=querystring, verify=False)
    #array.json()
    jsondata = array.json()
    
    return render(request, 'macTrack.html', {"jsondata": jsondata})

def mac_input(request):
    safeurl1 = open("static/api/url1")
    preurl1 = safeurl1.read()
    #preurl = preurl+"/api/location/v2/clients"
    safeauth1 = open("static/api/auth1")
    safetoke1 = open("static/api/toke1")
    headers1 = {
        'authorization': safeauth1.read(),
        'cache-control': "no-cache",
        'postman-token': safetoke1.read()
   }
    array1 = requests.request("GET", preurl1, headers=headers1, verify=False)
    
    jsondata1 = array1.json()
    
    return render(request, 'mac_input.html', {"jsondata1": jsondata1})
from django.shortcuts import render
from decouple import config
import requests
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
from xml.etree import ElementTree

# Create your views here.

def main(request):
    return render(request, 'medignore/main.html')

def temp(request):
    return render(request, 'medignore/temp.html')

def search(request):
    return render(request, 'medignore/search.html')

def result(request):
    param = request.GET.get('param') # search.html 에서 GET으로 받은 쿼리들 밑에 넣어줘야함

    serviceKey = config('DATA_API_SERVICEKEY')
    # url = 'http://apis.data.go.kr/1470000/DURPrdlstInfoService/getPwnmTabooInfoList'
    # params = {
    #     'serviceKey' : serviceKey,
    #     'typeName' : '임부금기',
    #     'ingrCode':'A005138',
    #     'itemName' : '세레콕시브', 
    #     'pageNo' : '1', 
    #     'numOfRows' : '3',
    #     }
    # print(requests.get(url,params=params).url)
    # response = requests.get(url, params=params)
    # print(response.text)

    API_Key = unquote(serviceKey)
    url = 'http://apis.data.go.kr/1470000/DURPrdlstInfoService/getPwnmTabooInfoList'
    queryParams = '?' + urlencode(
        {
            quote_plus('serviceKey') : API_Key,
            quote_plus('typeName'): '임부금기',
            quote_plus('ingrCode'): param, # 코드: A005138
            # quote_plus('itemName') : '세레콕시브', 
            # quote_plus('pageNo') : '1',
            # quote_plus('numOfRows') : '3',
            }
    )

    req = Request(url+queryParams)
    req.get_method = lambda : 'GET'
    response_body = urlopen(req).read().decode('utf-8')
    print(response_body)

    print("###############################")

    root = ElementTree.fromstring(response_body)
    # for content in root.iter("./PROHBT_CONTENT"):
    #     print(content.text)
    data = root.find('body').find('items').find('item').find('PROHBT_CONTENT').text
    print(data)

    return render(request, 'medignore/result.html',{'param':data})

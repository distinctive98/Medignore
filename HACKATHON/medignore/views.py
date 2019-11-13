from django.shortcuts import render
from decouple import config
import requests
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

# Create your views here.

def main(request):
    return render(request, 'medignore/main.html')

def temp(request):
    return render(request, 'medignore/temp.html')

#의약품 낱알식별정보 서비스
def service(request):
    #param = request.GET.get('param')
    serviceKey = config('DATA_API_SERVICEKEY')

    API_KEY = unquote(serviceKey)
    url = 'http://apis.data.go.kr/1470000/MdcinGrnIdntfcInfoService/getMdcinGrnIdntfcInfoList'
    queryParams = '?' + urlencode(
        {
            quote_plus('ServiceKey') : API_KEY,
            quote_plus('item_name'): '디카맥스1000정',
            #quote_plus('edi_code'): '664600460', 
        }
    )

    request_body = Request(url+queryParams)
    request_body.get_method = lambda : 'GET'
    response_body = urlopen(request_body).read().decode('utf-8')

    print(response_body)

    return render(request, 'medignore/service.html',{'res':response_body})

from django.shortcuts import render
from decouple import config
import requests
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
from xml.etree import ElementTree
import openpyxl

# Create your views here.

def main(request):
    return render(request, 'medignore/main.html')

def temp(request):
    return render(request, 'medignore/temp.html')

def search(request):
    return render(request, 'medignore/search.html')

# def result(request):
#     param = request.GET.get('param') # search.html 에서 GET으로 받은 쿼리들 밑에 넣어줘야함

#     serviceKey = config('DATA_API_SERVICEKEY')
#     # url = 'http://apis.data.go.kr/1470000/DURPrdlstInfoService/getPwnmTabooInfoList'
#     # params = {
#     #     'serviceKey' : serviceKey,
#     #     'typeName' : '임부금기',
#     #     'ingrCode':'A005138',
#     #     'itemName' : '세레콕시브', 
#     #     'pageNo' : '1', 
#     #     'numOfRows' : '3',
#     #     }
#     # print(requests.get(url,params=params).url)
#     # response = requests.get(url, params=params)
#     # print(response.text)

#     API_Key = unquote(serviceKey)
#     url = 'http://apis.data.go.kr/1470000/DURPrdlstInfoService/getPwnmTabooInfoList'
#     queryParams = '?' + urlencode(
#         {
#             quote_plus('serviceKey') : API_Key,
#             quote_plus('typeName'): '임부금기',
#             #quote_plus('ingrCode'): param, # 코드: A005138
#             quote_plus('itemName'): param,

#             # quote_plus('itemName') : '세레콕시브', 
#             # quote_plus('pageNo') : '1',
#             # quote_plus('numOfRows') : '3',
#             }
#     )

#     req = Request(url+queryParams)
#     req.get_method = lambda : 'GET'
#     response_body = urlopen(req).read().decode('utf-8')
#     print(response_body)

#     print("###############################")

#     root = ElementTree.fromstring(response_body)
#     # for content in root.iter("./PROHBT_CONTENT"):
#     #     print(content.text)
#     data = root.find('body').find('items').find('item').find('PROHBT_CONTENT').text
#     print(data)

#     return render(request, 'medignore/result.html',{'param':data})


def result(request):
    param = request.GET.get('param') # search.html 에서 GET으로 받은 쿼리들 밑에 넣어줘야함
    # param이 보험코드면 1. 품목 목록에서 이름 뽑아오고 2. 이름으로 임부 주의사항 뽑기
    import openpyxl
 
    # 엑셀파일 열기
    wb = openpyxl.load_workbook('product_detail.xlsx')
    
    # 현재 Active Sheet 얻기
    ws = wb.active
    # ws = wb.get_sheet_by_name("Sheet1")
    
    # 국영수 점수를 읽기
    for r in ws.rows:
        row_index = r[0].row   # 행 인덱스
        kor = r[1].value
        eng = r[2].value
        math = r[3].value
        sum = kor + eng + math
    
        # 합계 쓰기
        ws.cell(row=row_index, column=5).value = sum
    
        print(kor, eng, math, sum)
    
    # 엑셀 파일 저장
    wb.save("score2.xlsx")
    wb.close()
    
    return render(request, 'medignore/result.html',{'param':data})

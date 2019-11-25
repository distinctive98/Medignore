import json

#임부금기 : 1, 노인주의 : 2, 연령대주의 : 3

def durProhibit(durList, sign) :
    with open('./static/medignore/json/durProhibit' + sign + '.json', encoding="utf-8") as data_file :
        data = json.load(data_file)

    field = data['FIELD']
    durList_len = len(durList)
    field_len = len(field)
    result = []
    for i in range(durList_len) :
        check = False
        for j in range(field_len) :
            if field[j]['Item'] == durList[i] :
                result.append(field[j]['Prohibit'])
                check = True
                break
        if not check :
            result.append('이상없음')

    for i in range(len(result)) :
        print(result[i])
   

durList = ['원포팜주사액(네포팜염산염)', '라이트네포팜주(네포팜염산염)', '이상한약', '로이나제주(엘아스파라기나제)']
durProhibit(durList, '1')

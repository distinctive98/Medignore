import json

#임부금기 : 1, 노인주의 : 2, 연령대주의 : 3
def durProhibit(durList, sign) :
    path = 'medignore/static/medignore/json/durProhibit' + sign + '.json'
    with open(path, encoding="utf-8") as data_file :
        data = json.load(data_file)

    field = data['FIELD']
    durList_len = len(durList)
    field_len = len(field)
    result = []
    for i in range(durList_len) :
        check = False
        for j in range(field_len) :
            if durList[i] in field[j]['Item'] :
                result.append(field[j]['Prohibit'])
                check = True
                break
        if not check :
            result.append('이상없음')

    return result

    #for i in range(len(result)) :
    #    print(result[i])
   
def getDurItems(codeList) :
    path = 'medignore/static/medignore/json/durItems.json'
    with open(path, encoding="utf-8") as data_file :
        data = json.load(data_file)

    field = data['FIELD']
    codeList_len = len(codeList)
    field_len = len(field)
    result = []

    for i in range(codeList_len) :
        for j in range(field_len) :
            if codeList[i] in field[j]['Code'] :
                result.append(field[j]['Item'])
                break
    
    return result


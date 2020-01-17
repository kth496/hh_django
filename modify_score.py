# 주어진 item 데이터의 각 row마다 score를 계산해서 추가하는 코드
import json
import pathlib
path = 'C:\\Users\\김태홍\\Desktop\\django-template-master\\myapp\\item\\fixtures\\'


file = pathlib.Path(path+'modi-items-data.json')
file_text = file.read_text(encoding='utf-8')
json_data = json.loads(file_text)

ingred_table = pathlib.Path(path+'modi-ingred-data.json')
ingred_table_text = ingred_table.read_text(encoding='utf-8')
ingred_json_data = json.loads(ingred_table_text)

"""
{'model': 'item.item', 'fields': {'id': 1, 'imageId': 'a18de8cd-c730-4f36-b16f-665cca908c11', 'name': '리더스 링클 콜라
겐 마스크', 'price': '520', 'gender': 'female', 'category': 'suncare', 'ingredients': 'executrix,provision,multimedia,destruction,screw', 'monthlySales': 5196}}
(virtual-venv)
"""
result = []

skinType = ['oily', 'dry', 'sensitive']

for e in json_data:
    newData = e
    newData['fields']['oilyScore'] = 0
    newData['fields']['dryScore'] = 0
    newData['fields']['sensitiveScore'] = 0
    stringOfCurrentItemIngredients = e['fields']['ingredients']
    ListOfIngredients = stringOfCurrentItemIngredients.split(',')
    
    for ingredInfo in ingred_json_data:
        curData = ingredInfo['fields']
        if (curData['name'] in ListOfIngredients):
            for _type in skinType:
                if(curData[_type] == "O"):
                    newData['fields'][_type+'Score'] += 1
                elif(curData[_type] == "X"):
                    newData['fields'][_type+'Score'] -= 1

    result.append(newData)


with open(path+'scored-items-data.json', 'w', encoding='utf-8') as make_file:
    json.dump(result, make_file, indent="\t")

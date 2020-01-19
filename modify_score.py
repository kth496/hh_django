# 주어진 item 데이터의 각 row마다 score를 계산해서 추가하는 코드
# 각 제품의 ingredients 필드를 스플릿하여 각 성분에 관한 정보를 성분정보 json파일에서 읽어온다.
# 읽어온 정보를 바탕으로 해당 제품의 oily, dry, sensitive 점수를 요구사항에 맞게 계산해서 새로운 키-값으로 추가한다.
# 점수계산이 완료된 데이터를 DB에 저장해서 사용한다.

import json
import pathlib
path = 'C:\\Users\\김태홍\\Desktop\\django-template-master\\myapp\\item\\fixtures\\'

# 제품정보를 저장한 파일을 읽어와서 item_json_data로 저장
file = pathlib.Path(path+'modi-items-data.json')
file_text = file.read_text(encoding='utf-8')
item_json_data = json.loads(file_text)

# 성분에 관한 정보를 저장한 파일을 읽어와서 ingred_json_data로 저장
ingred_table = pathlib.Path(path+'modi-ingred-data.json')
ingred_table_text = ingred_table.read_text(encoding='utf-8')
ingred_json_data = json.loads(ingred_table_text)

# 새로 구성한 모든 정보를 담을 result 배열 선언
result = []

skinType = ['oily', 'dry', 'sensitive']

# 요구사항에서 제시한 규칙에 맞게 점수를 계산하는 코드
# <성분이름>Score 형태로 모든 점수를 계산한다.
# 예를들어, oily에 관한 점수는 oilyScore로 저장된다.
for e in item_json_data:
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

# 완성된 리스트를 저장한다.
with open(path+'scored-items-data.json', 'w', encoding='utf-8') as make_file:
    json.dump(result, make_file, indent="\t")

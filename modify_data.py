# 주어진 json 데이터를 manage.py loaddata로 불러올 수 있도록 변형하는 코드

import json
import pathlib
path = 'C:\\Users\\김태홍\\Desktop\\django-template-master\\myapp\\item\\fixtures\\'

# items 데이터를 변형
file = pathlib.Path(path+'item-data.json')
file_text = file.read_text(encoding='utf-8')
json_data = json.loads(file_text)

result = []
for e in json_data:
    new_data = {"model": "item.item", "fields": e}
    result.append(new_data)

with open(path+'modi-items-data.json', 'w', encoding='utf-8') as make_file:
    json.dump(result, make_file, indent="\t")

# ingredients 데이터를 변형
file = pathlib.Path(path+'ingred-data.json')
file_text = file.read_text(encoding='utf-8')
json_data = json.loads(file_text)

result = []
for e in json_data:
    new_data = {"model": "item.ingredients", "fields": e}
    result.append(new_data)

with open(path+'modi-ingred-data.json', 'w', encoding='utf-8') as make_file:
    json.dump(result, make_file, indent="\t")

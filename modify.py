import json
import pathlib
path = 'C:\\Users\\김태홍\\Desktop\\django-template-master\\myapp\\item\\fixtures\\'

# items-data.json
# file = pathlib.Path(path+'item-data.json')
# file_text = file.read_text(encoding='utf-8')
# json_data = json.loads(file_text)

# result = []
# for e in json_data:
#     new_data = {"model": "item.item", "fields": e}
#     result.append(new_data)

# with open(path+'modi-items-data.json', 'w', encoding='utf-8') as make_file:
#     json.dump(result, make_file, indent="\t")

# ingred-data.json
file = pathlib.Path(path+'ingred-data.json')
file_text = file.read_text(encoding='utf-8')
json_data = json.loads(file_text)

result = []
for e in json_data:
    new_data = {"model": "item.ingredients", "fields": e}
    result.append(new_data)

with open(path+'modi-ingred-data.json', 'w', encoding='utf-8') as make_file:
    json.dump(result, make_file, indent="\t")

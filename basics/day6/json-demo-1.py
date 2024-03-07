import json
rd = json.load(open('./emp.json'))
for rec in rd:
    print(type(rec))
    print(rec)

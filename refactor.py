import json

with open('target.json', 'r') as f:
    obj = json.load(f)

    real_content = next(iter(obj['content']))
    print(json.dumps(real_content, indent=2))

    for key, value in obj['content'][real_content].items():
        obj['content'][key] = value

    obj['content'].pop(real_content, None)

with open('target.json', 'w+') as f:
    f.write(json.dumps(obj, indent=4))
    f.flush()
    f.close()

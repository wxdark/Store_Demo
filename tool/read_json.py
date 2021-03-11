import json


def read_json(filename):
    filepath = "../data/" + filename
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == '__main__':
    result = read_json("data.json").values()
    arr = []
    for i in result:
        arr.append((i.get("username"), i.get("password"), i.get("verify_code"), i.get("result")))
    print(arr)

import sys

keep_number = [{}]
dic = {}
while True:
    try:
        line = sys.stdin.readline().rstrip('\n')
        if line == "{":
            keep_number.append({})
        elif line == "}":
            now_dic = keep_number.pop()
            for k, v in now_dic.items():
                if v is None:
                    del dic[k]
                else:
                    dic[k] = v
        else:
            first, second = line.split("=")
            if second.lstrip('-').isnumeric():
                if first not in keep_number[-1]:
                    keep_number[-1][first] = dic.get(first, None)
                dic[first] = int(second)
            else:
                if first not in keep_number[-1]:
                    keep_number[-1][first] = dic.get(first, None)
                value = dic.get(second, 0)
                dic[first] = value
                print(value)
    except:
        break
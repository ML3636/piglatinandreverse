def reverseLookUp(dictionary, value):
    list = []
    for key in dictionary.keys():
        if value == dictionary[key]:
            list.append(key)
    return list

NList = {"one":2, "two":1, "three":3, "four":4, "five":2}

value = int(input())

result = reverseLookUp(NList, value)

print(result)
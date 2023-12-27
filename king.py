def element(array, x, y, string)
    conversionrate = 0
    newArray = []
    for i in string:
        if(int(i) * 2 == i * 2):
            conversionrate = i
        else:
            continue
    for i in array:
        array.remove(i)
        newArray.append(i * conversionrate)
    return newArray

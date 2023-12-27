def conversionelement(array, conversion1, conversion2, conversionrate, array, functionlayout)
    arrayconversionrate = []
    symbolconversionrate = []
    newArray = []
    sum = 0
    for i in string:
        try:
            i = int(i)
        except ValueError:
            symbolconversionrate.append(i)
        
        for item in newArray:
            for i in range(len(arrayconversionrate)):
                if(symbolconversionrate[i] == "+"):
                    newArray.remove(item)
                    item = item + arrayconversionrate[i]
                    newArray.append(item)
                 if(symbolconversionrate[i] == "-"):
                     newArray.remove(item)
                     item = item - arrayconversionrate[i]
                     newArray.append(item)
                 if(symbolconversionrate[i] == conversion1):
                     newArray.remove(item)
                     item = item * arrayconversionrate[i]
                     newArray.append(item) 

        for item in newArray:
            sum += item
    return str(newArray) + "Finished Calculation" + "Total amount of" + conversion2 + "  is" + sum


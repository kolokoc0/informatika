def sort_emotions(arr, order):
    array  = [ ':D', ':)', ':|', ':(', 'T_T' ]
    newarr = []
    poc = 0
    for i in range(len(array)):
        for index,word in enumerate(arr):
            if array[i] == word:
                for a in range(arr.count(array[i])):
                    val = arr.pop(index)
                    newarr.append(val)
    if order == True:
        return newarr[::]
    else:
        return newarr
print(sort_emotions([ 'T_T', ':D', ':(', ':(' ], True), [ ':D', ':(', ':(', 'T_T' ])
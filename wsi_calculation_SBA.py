import numpy as np

# calculating the WSI of each SBA
# array1 is the local water availability data
# array2 is the upstream water availability data
# array3 is the upstream withdrawal data

def cal(array1, array2, array3):
    for i in range(0, 12):
        if array2[i] > array3[i]:
            array1[i] = array1[i] + array2[i] - array3[i]
    return array1
wsi = cal(availability1, availability2, withdrawal2) / withdrawal1


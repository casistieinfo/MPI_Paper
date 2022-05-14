from random import shuffle
import time
from sorting_techniques import pysort

sortObj = pysort.Sorting()


def create_array(arr,x):
    for i in range(x):
        arr.append(i)
    shuffle(arr)


def sort():
    array = []
    x=[100,1000,5000,10000]
    for z in x:
        create_array(array,z)
        timee(array,z,sorts)


def timee(array,x,sorts):
    for y in sorts:
        tot = 0
        for i in range(5):
            arr = array.copy()

            st = time.time()
            if y == sortObj.quickSort:
                y(arr,0,99)
            else:
                y(arr)
            time.sleep(1)
            et = time.time()
            elapsed_time = et - st - 1
            tot +=elapsed_time

        print('bubble: (',x,',', tot, ') seconds')


sorts = [sortObj.bubbleSort, sortObj.selectionSort, sortObj.quickSort, sortObj.insertionSort, sortObj.mergeSort,
             sortObj.heapSort, sortObj.radixSort]

sort()




#
#
#
# bubble = sortObj.bubbleSort(array)
# select = sortObj.selectionSort(array)
# #quick = sortObj.quickSort(array, 1, 100)
# insertion = sortResult = sortObj.insertionSort(array)
# merge = sortObj.mergeSort(array)
# heap = sortObj.heapSort(array)
# #radix = sortObj.radixSort(array)
#


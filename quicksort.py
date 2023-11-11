#Rachael Mallinson
#Quicksort Implementation

#Partition function------------------------------------------------------
def _partition(arr, low, high):
    """ Partition Function to take part in quicksort Algorithm
    Atributes:
        l: counts the number of items in the array that are less than the pivot element(p)
        p: the pivot point- integer item in the array that we place in its correct place within the array by comparing 
    :param arr: the array we are sorting
    :param low: lower index number, the start of the smaller portion of the array we are sorting
    :param high: higher index number, the end of the smaller portion of the array we are sorting
    :return: the index of the position where partition is completed
    """
    l = low - 1;
    p = arr[high];
    for i in range(low, high):
        if (arr[i] <= p):
            l = l + 1;
            arr[i], arr[l] = arr[l], arr[i];
    arr[l + 1], arr[high] = arr[high], arr[l + 1];
    return l + 1;
 

#QuickSort function-----------------------------------------------------
def _quicksort(arr, low, high):
    """ Quicksort Function to perform quicksort and its subsequent recursive calls on smaller portions of the array
    :param arr: the array we are sorting
    :param low: lower index number, the start of the smaller portion of the array we are sorting
    :param high: higher index number, the end of the smaller portion of the array we are sorting
    """
    if (low < high): 
        #only recursive call if our low and high haven't met, which means there is more to sort
        r = _partition(arr, low, high);
        _quicksort(arr, low, r - 1);
        _quicksort(arr, r + 1, high);


#Wrapper function-------------------------------------------------------
def _quicksortWrapper(arr):
    """ Quicksort Function wrapper for a cleaner start to the _quicksort function.

    :param arr: The array to sort
    """
    #START QUICKSORT
    _quicksort(arr, 0, len(arr)-1);


#Section to call functions ----------------------------------------------
while True:
    given = input("Please provide several numbers separated by spaces below.\n");
    #remove the white space and check if there are anything but numbers in it
    noSpace = given.replace(" ", "");
    if noSpace.isnumeric():
        break;
    else:
        print("Input not valid. Please try again.");

#take in input and create array from given input
elements = given.split( );
numElements = len(elements);
arr = [0] * numElements;

for i in range(0, numElements):
    arr[i] = int(elements[i]);

#Provide that we built the given array correctly, and then show that we sort it
print("Given: ", arr);
_quicksortWrapper(arr); #call to quicksort
print("Sorted:", arr);

print("--End--");

 ## END OF FILE ##
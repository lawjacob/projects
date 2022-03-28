import timeit
def swap_list(list, p1, p2):
    list[p1], list[p2] = list[p2], list[p1]
    return (list)

time_consumed = 0.0
start = 0.0
#bubble sorting O(n^2) & Ω(n)
def bub(list):
    start = timeit.timeit()
    if_sort = False
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list = swap_list(list, j, j + 1)
                if_sort = True
        if if_sort == False:
            return(list)
    return (list)
    
#selection sort O(n^2) & Ω(n^2)
def sel(list):
    start = timeit.timeit()
    min_po = 0
    for i in range(len(list)):
        min_po = i
        for j in range(i, len(list)):
            if list[j] < list[min_po]:
                list[j], list[min_po] = list[min_po], list[j]
    return list

#insertion sort O(n^2) & Ω(n)
def ins(list):
    start = timeit.timeit()
    for i in range(1,len(list)):
        cursor = i
        value = list[cursor]
        while cursor > 0 and list[cursor - 1] > value:
            list[cursor] = list[cursor - 1]
            cursor = cursor - 1
        list[cursor] = value
    return list

#merge sort O(nlog(n)) & Ω(nlog(n))
def merge_sort(list):
    start = timeit.timeit()
#base case
    if len(list) == 1:
        return list

#slicing list & recursion
    mid = round(len(list) / 2)
    left_half = list[:mid]
    right_half = list[mid:]
    merge_sort(left_half)
    merge_sort(right_half)

#merge
    left_po = 0
    right_po = 0
    list_po = 0
    while (left_po < len(left_half)) and (right_po < len(right_half)):
        if left_half[left_po] < right_half[right_po]:
            list[list_po] = left_half[left_po]
            left_po += 1
        else:
            list[list_po] = right_half[right_po]
            right_po += 1
        list_po += 1

    #if right end, all value left on left stores at lsit
    for po in range(left_po, len(left_half)):
        list[list_po] = left_half[po]
        list_po += 1

    #if left end, all value left on right stores at lsit
    for po in range(right_po, len(right_half)):
        list[list_po] = right_half[po]
        list_po += 1

raw_list = [260, 202, 312, 650, 929, 610, 433, 883, 41, 476, 751, 696, 905, 178, 756, 538, 768, 692, 155, 457, 762, 52, 554, 863, 275, 694, 870, 253, 625, 403, 946, 638, 472, 940, 547, 294, 975, 313, 220, 920, 227, 164, 225, 280, 641, 91, 118, 209, 807, 722]
merge_sort(raw_list)
print("which sorting algorithm do you want to use?")
print("1. bubble sort")
print("2. selection sort")
print("3. insertion sort")
print("4. merge sort")
choice = int(input("Your choice: "))
match choice:
    case "1":bub(raw_list)
    case "2":sel(raw_list)
    case "3":ins(raw_list)
    case "4":merge_sort(raw_list)

end = timeit.timeit()
print(raw_list)
print("Time consumed to run this algorithm: " + str(end - start))
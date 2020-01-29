def quick_sort(old_list, left, right):
    # print(left,right)
    if left > right:
        return
    key = old_list[left]
    min = left
    max = right

    while left < right:
        while left <= right and old_list[right] >= key:
                right -= 1

        while left < right and old_list[left] <= key:
                left += 1


        if left < right:
            old_list[left], old_list[right] = old_list[right], old_list[left]


        else:
            old_list[min] = old_list[left]
            old_list[left] = key



    quick_sort(old_list, min, left-1)
    quick_sort(old_list, left + 1, max)

    return old_list



def quick_sort():
    pass

if __name__ == '__main__':
    old_list= [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    print(quick_sort(old_list,0,9))



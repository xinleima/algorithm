import copy
# def quick_sort(old_list, left, right):
#     # print(left,right)
#     if left > right:
#         return
#     key = old_list[left]
#     min = left
#     max = right
#
#     while left < right:
#         while left <= right and old_list[right] >= key:
#                 right -= 1
#
#         while left < right and old_list[left] <= key:
#                 left += 1
#
#
#         if left < right:
#             old_list[left], old_list[right] = old_list[right], old_list[left]
#
#
#         else:
#             old_list[min] = old_list[left]
#             old_list[left] = key
#
#
#
#     quick_sort(old_list, min, left-1)
#     quick_sort(old_list, left + 1, max)
#
#     return old_list


def quick_sort(s1,left,right):
    print(left,right)
    if left == right:
        return
    else:
        basic = s1[left]
        pos_left = left
        pos_right = right
        while pos_left < pos_right:

            while pos_right >= left and pos_left < pos_right:
                if s1[pos_right] < basic:
                    s1[pos_left] = s1[pos_right]
                    break
                pos_right -= 1

            while pos_left <= right and pos_left < pos_right:
                if s1[pos_left] > basic:
                    s1[pos_right] = s1[pos_left]
                    break
                pos_left += 1

            if pos_left == pos_right:
                s1[pos_right] = basic
                print(pos_right)
                print(s1)

        quick_sort(s1, left, max(pos_right-1,left))
        quick_sort(s1, min(pos_right+1,right), right)

    return s1


def merge_sort(s1, left, right):
    if left == right:
        return [s1[left]]
    else:
        mid = int((left+right)/2)
        s2 = merge_sort(s1, left, mid)
        s3 = merge_sort(s1, mid+1, right)
        return merge(s2,s3)


def merge(s1,s2):
    i = j = 0
    s3 = []
    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            s3.append(s1[i])
            i += 1
        else:
            s3.append(s2[j])
            j += 1
    if i < len(s1):
        s3 = s3 + copy.deepcopy([s1[x] for x in range(i,len(s1))])
    if j < len(s2):
        s3 = s3 + copy.deepcopy([s2[x] for x in range(j,len(s2))])
    return s3


def heap_init(s1):
    start = int(len(s1)/2)-1
    while start >= 0:
        print(start)
        adjust_heap(s1, start, len(s1)-1)
        start -= 1
    return s1


def adjust_heap(s1,begin,end):
    current = begin
    tmp = s1[current]
    left = current * 2 + 1
    right = left + 1
    max_pos = left

    while left <= end:

        if right <= end and s1[left] < s1[right]:
            max_pos = right

        if tmp < s1[max_pos]:
            s1[current] = s1[max_pos]
            current = max_pos
            left = current * 2 + 1
            right = left + 1
            max_pos = left

        else:
            break

    s1[current] = tmp


def heap_sort(s1):
    s1 = heap_init(s1)
    i = len(s1)-1

    while i >=1:
        s1[i], s1[0] = s1[0], s1[i]
        adjust_heap(s1,0,i-1)
        print(s1)
        i -=1
    return s1

if __name__ == '__main__':
    old_list= [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    #
    # print(quick_sort(old_list,0,9))

    # s1 = [4,5,7,8]
    # s2 = [1,2,3,6]
    print(heap_sort(old_list))




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

            if pos_left >= pos_right:
                s1[pos_right] = basic
                print(pos_right)
                print(s1)

        quick_sort(s1, left, max(pos_right-1,left))
        quick_sort(s1, min(pos_right+1,right), right)

    return s1




if __name__ == '__main__':
    old_list= [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]

    print(quick_sort(old_list,0,9))



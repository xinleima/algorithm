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
import math


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


# 已知s1[begin]的左子树和右子树都满足最大堆，那么调节节点s1[begin]，将以s1[begin]为根节点的二叉树调整为最大堆。
def adjust_heap(s1,begin,end):
    #current 可以看做是 tmp 这个数 这轮准备摆放的位置。
    #如果tmp大于 current这个位置的左右子树，那tmp可以放在current这个位置，不然的话把左右子树的较大值放在current这个位置，预计把tmp放在较大值的左右子树位置
    current = begin
    tmp = s1[current]
    left = current * 2 + 1
    right = left + 1
    #先假设左节点的值比右节点大，因为有可能不存在右节点
    max_pos = left

    #如果左子树已经超过数组边界，证明current必定在树的叶子节点，就不必再担心tmp是否大于左右子树了
    while left <= end:

        #可能存在只存在左节点，没有右节点的情况，所以要判断是否存在右节点
        if right <= end and s1[left] < s1[right]:
            max_pos = right

        #如果tmp小于左右节点
        if tmp < s1[max_pos]:
            #把current的位置换给左右节点较大值
            s1[current] = s1[max_pos]
            #这样左右节点较大的位置就空出来了可以放置current,但是不能直接放置,因为可能左右节点大于tmp,需要进入下一轮循环判断
            current = max_pos
            left = current * 2 + 1
            right = left + 1
            max_pos = left

        #如果tmp值比左右节点都大，证明已经为tmp找到合适的位置
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


def insertion_sort(s1):
    for i in range(1,len(s1)):
        tmp = s1[i]
        for j in range(0,i):
            if s1[i]< s1[j]:
                for m in range(i,j,-1):
                    s1[m]=s1[m-1]
                s1[j] = tmp

    return s1


def bubble_sort(s1):
    for i in range(len(s1)-1,0,-1):
        for j in range(0,i):
            if s1[j]>s1[j+1]:
                s1[j],s1[j+1] = s1[j+1],s1[j]
    return s1


def shell_sort(s1):
    gap = int(len(s1)/2)
    while gap > 0:
        print(gap)
        for i in range(0, gap):
            for j in range(i + gap, len(s1), gap):
                tmp = s1[j]
                for m in range(i, j, gap):
                    if s1[j] < s1[m]:
                        for n in range(j, m, -gap):
                            s1[n] = s1[n - gap]

                        s1[m] = tmp
                    print(s1)
        gap = int(gap/2)
    return s1


def selection_sort(s1):
    for i in range(len(s1)-1,0,-1):
        max_pos = 0
        for j in range(1,i):
            if s1[j] > s1[max_pos]:
                max_pos = j
        s1[max_pos],s1[i] = s1[i],s1[max_pos]
    return s1


def countsort(s1):
    min = 0
    max = 0
    for i in range(len(s1)):
        if s1[i]>max:
            max = s1[i]
        if s1[i]<min:
            min = s1[i]

    a_len = max - min + 1
    a = [0] * a_len
    s2 = []
    for i in range(len(s1)):
        index = s1[i] - min
        a[index] += 1
    for i in range(a_len):
        s2 = s2 + [i+min]*a[i]
    return s2


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self, init_list=[]):
        self.head = None
        if len(init_list)>0:
            last_node = Node(init_list[0])
            self.head = last_node
            for i in range(1, len(init_list)):
                current_node = Node(init_list[i])
                last_node.next = current_node
                last_node = current_node
        return self.head

    def insert(self,value):
        insert_node = Node(value)
        flag = False
        if self.head == None:
            self.head =  insert_node

        elif value <self.head.value:
            insert_node.next = self.head
            self.head = insert_node
        else:
            last_node =  self.head
            cur_node = self.head.next
            while cur_node != None:
                if value < cur_node.value:
                    last_node.next = insert_node
                    insert_node.next = cur_node
                    flag = True
                    break
                else:
                    last_node = cur_node
                    cur_node = cur_node.next
            if flag == False:
                last_node.next = insert_node

        return self.head


    def get_list(self):
        s = []
        cur_node = self.head
        while cur_node != None:
            s.append(cur_node.value)
            last_node = cur_node
            cur_node  =  cur_node.next
        return s


def bucket_sort(s1):
    min = 0
    max = 0
    for i in range(len(s1)):
        if s1[i] > max:
            max = s1[i]
        if s1[i] < min:
            min = s1[i]

    total_bucket_num = 5
    one_bucket_range = (max - min + 1) / total_bucket_num

    a = []
    for i in range(total_bucket_num):
        linkedlist = LinkedList([])
        a.append(linkedlist)

    for i in range(len(s1)):
        current_num = int((s1[i]-min)/one_bucket_range)
        print(s1[i],current_num,i)
        a[current_num].insert(s1[i])

    b = []
    for i in range(total_bucket_num):
        b = b + a[i].get_list()

    return b


def radix_sort(s1):
    max_digit_num = 0
    for i in range(len(s1)):
        if  max_digit_num < (len(str(s1[i]))):
            max_digit_num = len(str(s1[i]))


    for i in range(0, max_digit_num):
        bucket_list = [[] for i in range(10)]
        for j in range(len(s1)):
            cur_bucket_num = int(s1[j]/(10**i))%10
            bucket_list[cur_bucket_num].append(s1[j])

        s1 = []
        for m in range(len(bucket_list)):
            s1 = s1 + bucket_list[m]

    return s1


if __name__ == '__main__':
    old_list= [6, 1, 2, 7, 9, 3, 4, 5, 10, 8, 0]
    A = [-1, 2, 0, 4, 3, 6, 5, 8, -2, 1, 3, 0, 3, 6, 5, 2]
    a = [63, 157, 189, 51, 101, 47, 141, 121, 157, 156, 194, 117, 98, 139, 67, 133, 181, 13, 28, 109]
    #
    # print(quick_sort(old_list,0,9))

    # s1 = [4,5,7,8]
    # s2 = [1,2,3,6]
    # print(heap_sort(old_list))
    # print(insertion_sort(old_list))
    # # print(bubble_sort(old_list))
    # print(selection_sort(old_list))
    # print(shell_sort(old_list))
    # print(countsort(A))
    # print(bucket_sort(a))
    print(radix_sort(a))




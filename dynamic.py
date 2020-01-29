import copy
def select_coin(coin_value_list, total_coin_value):
    min_coin_num = [0]
    select_coin_list = []
    for current_total_coin_value in range(1,total_coin_value+1):
        min_coin_num.append(float("inf"))
        for current_coin_value in coin_value_list:
            if current_coin_value <= current_total_coin_value and min_coin_num[current_total_coin_value - current_coin_value ]+1 < min_coin_num[current_total_coin_value]:
                min_coin_num[current_total_coin_value] = min_coin_num[current_total_coin_value - current_coin_value ]+ 1
                select_coin_list.append(current_coin_value)

    return select_coin_list


def bag(item_weight_list, item_value_list, max_weight):
    total_item_number = len(item_weight_list)
    bag_item_number_weight = []
    bag_item_number_weight_item = []
    bag_item_number_weight.append([0] * (max_weight+1))
    bag_item_number_weight_item.append([[]] * (max_weight+1))

    for current_item_number in range(1, total_item_number+1):
        print("current_item_number:",current_item_number)
        bag_item_number_weight.append(copy.deepcopy(bag_item_number_weight[current_item_number-1]))
        bag_item_number_weight_item.append(copy.deepcopy(bag_item_number_weight_item[current_item_number-1]))

        w = item_weight_list[current_item_number - 1]
        v = item_value_list[current_item_number - 1]


        for current_max_wight in range(1, max_weight+1):
            if w <= current_max_wight and bag_item_number_weight[current_item_number-1][current_max_wight-w]+v>bag_item_number_weight[current_item_number][current_max_wight]:
                bag_item_number_weight[current_item_number][current_max_wight] = bag_item_number_weight[current_item_number-1][current_max_wight-w]+v
                bag_item_number_weight_item[current_item_number][current_max_wight] = copy.deepcopy(bag_item_number_weight_item[current_item_number - 1][current_max_wight-w])
                bag_item_number_weight_item[current_item_number][current_max_wight].append(current_item_number)

    return bag_item_number_weight[total_item_number][max_weight],bag_item_number_weight_item[current_item_number][current_max_wight]


def LIS(old_list):
    lis_list = []
    lis_list.append(1)
    list_len = len(old_list)
    for i in range(1,list_len):
        lis_list.append(1)
        for j in range(0,i):
            if old_list[i] >= old_list[j] and lis_list[j] + 1 > lis_list[i]:
                lis_list[i] = lis_list[j] + 1
    lis_max = max(lis_list)
    return lis_max


t

if __name__ == '__main__':
    # coin_value_list = [1, 3, 5]
    # total_coin_value = 11
    # print(select_coin(coin_value_list, total_coin_value))

    # item_weight_list = [2, 2, 6, 5, 4]
    # item_value_list = [6, 3, 5, 4, 6]
    # max_weight = 10
    # print(bag(item_weight_list, item_value_list, max_weight))

    old_list = [2, 1, 5, 3, 6, 4, 8, 9, 7]
    print(LIS(old_list))

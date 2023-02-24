def find_sub_list_for_sum_target_0(array_1d: list, target: float):
    """
    self_realization
    matrix: 一维数组
    target: 目标值
    """
    if len(array_1d) == 0:
        return 0
    if len(array_1d) == 1:
        return 1 if array_1d[0] == target else 0
    count = 0
    length = len(array_1d)
    sum = 0
    for i in range(length):
        sum += array_1d[i]
        if sum == target:
            count += 1
    return count + find_sub_list_for_sum_target_0(array_1d[1:], target)


def find_sub_list_for_sum_target_1(array_1d: list, target: float):
    length = len(array_1d)
    pre_sum = [0]
    count = 0
    for i in range(length):
        pre_sum.append(0)
        pre_sum[i+1] = pre_sum[i] + array_1d[i]
    for i in range(length):
        for j in range(i+1, length+1):
            if (pre_sum[j] - pre_sum[i]) == target:
                count += 1
    return count


def find_sub_list_for_sum_target(array_1d: list, target: float):
    pre_sum = 0
    count = 0
    temp_dict = dict()
    for item in array_1d:
        if pre_sum in temp_dict:
            temp_dict[pre_sum] += 1
        else:
            temp_dict[pre_sum] = 1
        pre_sum += item
        if (pre_sum - target) in temp_dict:
            count += temp_dict[pre_sum - target]
    return count


def count_sub_matrix_for_sum_target(matrix: list, target: float):
    """
    matrix: 一个 m * n 维的矩阵，在此以 list 数据结构来存储
    target: 目标值
    """
    if not list:
        return
    row_length = len(matrix)
    column_length = len(matrix[0]) if isinstance(matrix[0], list) else 1
    count = 0
    for i in range(row_length):
        sum_target_list = list()
        for j in range(i, row_length):
            for k in range(column_length):
                if j == i:
                    sum_target_list.append(matrix[j][k])
                else:
                    sum_target_list[k] += matrix[j][k]
            count += find_sub_list_for_sum_target(sum_target_list, target)
    return count


matrix_1 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
result_1 = count_sub_matrix_for_sum_target(matrix_1, 0)
print(result_1)

matrix_2 = [[1, -1], [-1, 1], [0, 0]]
result_2 = count_sub_matrix_for_sum_target(matrix_2, 0)
print(result_2)

matrix_3 = [[904]]
result_3 = count_sub_matrix_for_sum_target(matrix_3, 0)
print(result_3)

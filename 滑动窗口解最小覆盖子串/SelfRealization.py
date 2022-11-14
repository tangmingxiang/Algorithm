import math


def sliding_window(source, target):
    """
    这种实现并没有让窗口滑起来，这算是一种迭代实现
    :param source: 源字符串
    :param target: 目标字符串
    :return: 返回源字符串中包含目标字符串所有字符的最小子串，若不存在满足这样条件的子串，则返回空字符串
    举例： source："ADOBECODEBANC"  target："ABC"  则返回 “BANC“
    """
    # window_size 代表当前窗口大小，初始为目标字符串的大小
    target_length = len(target)
    # 源字符串长度
    source_length = len(source)
    if target_length > source_length:
        return ''
    source_i = 0
    result = ''
    while source_i < source_length:
        if source[source_i] in target:
            window_start = source_i
            window_end = window_start + target_length
            while window_end <= source_length:
                if window_end < window_start + target_length:
                    window_end = window_start + target_length
                    if window_end > source_length:
                        break
                temp_str = source[window_start:window_end]
                if target_in_source(temp_str, target):
                    result = temp_str
                    break
                else:
                    while (source[window_end] == source[window_start] or source[window_start] not in target) \
                            and window_start <= window_end:
                        window_start += 1
                    window_end += 1
            source_i = window_end
            if result:
                break
        else:
            source_i += 1
    if target_length < (source_length - source_i - 1):
        sub_source = source[source_i+1:]
        sub_result = sliding_window(sub_source, target)
        if sub_result and (len(sub_result) < len(result)):
            result = sub_result
    return result


def target_in_source(source, target):
    """判断target中所有的字符是否都存在于source中"""
    flag = True
    for item in target:
        if item not in source:
            flag = False
            break
    return flag


print(sliding_window("ADOBECODEBANC", "ABC"))
print(sliding_window('AAAAAAAAAAAAAAAAB', 'AB'))
print(sliding_window('AAAAAAAAABBAAAAAAAB', 'ABB'))

print("-" * 100)


def sliding_window_2(source, target):
    """滑动窗口"""
    if len(source) < len(target):
        return ''
    count = len(target)
    target_dict = dict(zip(target, [0] * count))
    for char in target:
        target_dict[char] += 1
    source_length = len(source)
    left = 0
    right = 0
    start_str = 0
    window_size = -1
    while right < source_length:
        if source[right] in target_dict:
            if target_dict[source[right]] > 0:
                count -= 1
            target_dict[source[right]] -= 1
        while count == 0:
            if source[left] in target_dict:
                if target_dict[source[left]] == 0:
                    count += 1
                target_dict[source[left]] += 1
                if window_size == -1 or window_size > right - left + 1:
                    start_str = left
                    window_size = right - left + 1
            left += 1
        right += 1
    if window_size == -1:
        return ''
    return source[start_str:start_str+window_size]


print(sliding_window_2("ADOBECODEBANC", "ABC"))
print(sliding_window_2('AAAAAAAAAAAAAAAAB', 'AB'))
print(sliding_window_2('AAAAAAAAABBAAAAAAAB', 'ABB'))

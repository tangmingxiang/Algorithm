def sliding_window(source, target):
    """
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
                temp_str = source[window_start:window_end]
                if target_in_source(temp_str, target):
                    result = temp_str
                    break
                else:
                    if source[window_end] == source[window_start]:
                        window_start += 1
                        while source[window_start] not in target:
                            window_start += 1
                    window_end += 1
            source_i = window_end
            if result:
                break
        else:
            source_i += 1
    if source_i < (source_length - target_length):
        sub_source = source[source_i:]
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
    return  flag


print(sliding_window("ADOBECODEBANC", "ABC"))

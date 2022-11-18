def self_realization(begin_word, end_word, word_list):
    """
    :param begin_word: 开始字符串
    :param end_word: 结束字符串
    :param word_list: 字符串列表
    :return: 开始字符串每次改变一个字符，则至少需要多少次，可以由开始字符串转变为结束字符串，要求所有改变过程中的字符串包含于字符串列表中
             若无法转换成功，则返回 0
    """
    if end_word not in word_list:
        return 0
    ergodic_list = [begin_word]
    count = 0
    visited = [begin_word]
    while ergodic_list:
        temp_str = ergodic_list.pop()
        count += 1
        for item in word_list:
            if item in visited:
                continue
            if difference_one_char(temp_str, item):
                if item == end_word:
                    count += 1
                    return count
                ergodic_list.append(item)
                visited.append(item)

    return 0


def difference_one_char(source, target):
    """判断 source 与 target 之间是否长度相等且只差一个字母"""
    if len(source) != len(target):
        return False
    count = 0
    for i in range(len(source)):
        if source[i] == target[i]:
            continue
        if count != 0:
            return False
        count += 1
    if count == 1:
        return True
    return False


print(self_realization('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(self_realization('hit', 'cii', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(self_realization('hit', 'cii', ['hit', 'dct', 'd2g', 'l1t', 'log', 'cii']))
print(self_realization('hit', 'cii', ['hit', 'hct', 'hci', 'hii', 'cii', 'cii']))

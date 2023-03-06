#Question 1
def find_max(numbers):
    numbers = sorted(numbers, reverse=True)
    return numbers[0]

def find_position(numbers, target):
    if target in numbers:
        for idx in range(len(numbers)):
            if numbers[idx] == target:
                return idx
    else:
        return -1

print(find_max([1, 2, 4, 5]) ); # should print 5
print(find_max([5, 2, 7, 1, 6]) ); # should print 7
print(find_position([5, 2, 7, 1, 6], 5)) # should print 0
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1

#Question 2
def count(input):
    count_dic={}
    for idx in range(len(input)):
        count_dic.update({input[idx]: input.count(input[idx])})
    return count_dic

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}

def group_by_key(input):
    group_dic = {}
    for idx in input:
        group_dic[idx["key"]] = group_dic.get(idx["key"], 0) + idx["value"]
    return group_dic

input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2},
{'key': 'a', 'value': 3},
{'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
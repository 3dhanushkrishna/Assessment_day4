# import json as j
# data = '{"dha":"nus","hku":"mar"}'
# jsondata = j.loads(data)
# print(jsondata)

list1 = [2,4,5,6,5,34,65,84,33,44,23,12,65,89,99,55]
evenlist = list(filter(lambda x:(x %2 == 0), list1))
print(sorted(evenlist))

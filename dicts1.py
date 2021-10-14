#dict1 = {"a": 1}
#if "b" in dict1:
#    print(dict1["b"])
#else:
#    print(0)
#print(dict1.get("a", 7))

#list1 = [10, 3, 5, 4]
#print(sorted(list1))

from operator import itemgetter
#import operator

list2 = [{"a": 5}, {"a": 1}, {"a": 3}]
print(sorted(list2, key=itemgetter("a"), reverse=True))
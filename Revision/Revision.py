my_list = [1, 2, 3]
my_list.append(4)
my_list.extend([5, 6])
my_list.insert(2, 7)
my_list.remove(3)
popped_value = my_list.pop()
index = my_list.index(2)
count = my_list.count(5)
my_list.sort()
my_list.reverse()
#######################################################
my_tuple = (1, 2, 3, 2, 4, 2)
count = my_tuple.count(2)
index = my_tuple.index(4)
######################################################
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
my_set.discard(3)
popped_value = my_set.pop()
my_set.clear()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_difference_set = set1.symmetric_difference(set2)
#######################################################
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
value = my_dict.get('b')
my_dict.update({'d': 4})
popped_value = my_dict.pop('a')
popped_item = my_dict.popitem()
my_dict.clear()
####################################################
from collections import deque
my_deque = deque([1, 2, 3])
my_deque.append(4)
my_deque.appendleft(0)
popped_value = my_deque.pop()
popped_left_value = my_deque.popleft()
my_deque.extend([5, 6])
my_deque.extendleft([-1, 0])
my_deque.rotate(2)
##############################################
from queue import Queue
my_queue = Queue()
my_queue.put(1)
my_queue.put(2)
item = my_queue.get()
size = my_queue.qsize()
is_empty = my_queue.empty()
is_full = my_queue.full()

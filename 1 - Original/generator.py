import sys

my_generator = (i for i in range(100000) if i % 2 == 0)
# for _ in my_generator:
#    print(_)

print(sys.getsizeof(my_generator))

my_list = [i for i in range(100000) if i % 2 == 0]
# print(my_list)

print(sys.getsizeof(my_list))

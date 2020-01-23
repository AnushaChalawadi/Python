'''Given an integer, n, and n space-separated integers as input,
create a tuple,t , of those n integers. Then compute and print the result of .
hash(t)
'''
'''
Tuple : A tuple is a collection which is ordered and unchangeable
'''

if __name__ == '__main__':
    n= int(input())
    integer_list=map(int,input().split())
    print(hash(tuple(integer_list)))

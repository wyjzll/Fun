1:
>>> A = {'a': 1, 'b': 2, 'c': 3}
>>> B = {'b': 4, 'c': 6, 'd': 8}
>>> for key,value in B.items():
...     if key in A:
...         A[key] += value
...     else:
...         A[key] = value
>>> dict(sorted(A.items(), key=lambda d:d[1]))
{'a': 1, 'b': 6, 'd': 8, 'c': 9}

2:
  
>>> A = {'a': 1, 'b': 2, 'c': 3}
>>> B = {'b': 4, 'c': 6, 'd': 8}
>>> C = {}
>>> for key in list(set(A) | set(B)):
...     if A.get(key) and B.get(key):
...         C.update({key: A.get(key) + B.get(key)})
...     else:
...         C.update({key: A.get(key) or B.get(key)})
>>> C
{'c': 9, 'd': 8, 'a': 1, 'b': 6}

3:

  >>> A = {'a': 1, 'b': 2, 'c': 3}
>>> B = {'b': 4, 'c': 6, 'd': 8}
>>> def dict_union(d1, d2):
...     keys = d1.keys() | d2.keys()
...     temp = {}
...     for key in keys:
...         temp[key] = sum([d.get(key,0) for d in (d1, d2)])
...     return temp
>>> C = dict_union(A, B)
>>> C
{'d': 8, 'a': 1, 'b': 6, 'c': 9}

4:
>>> A = {'a': 1, 'b': 2, 'c': 3}
>>> B = {'b': 4, 'c': 6, 'd': 8}
>>> C = {}
>>> for key1 in A:
...     for key2 in B:
...         if key1 in B:
...             C[key1] = A[key1] + B[key1]
...         else:
...             C[key1] = A[key1]
...             if key2 not in A:
...                 C[key2] = B[key2]
>>> C
{'a': 1, 'd': 8, 'b': 6, 'c': 9}

5:
>>> A = {'a': 1, 'b': 2, 'c': 3}
>>> B = {'b': 4, 'c': 6, 'd': 8}
>>> C = {}
>>> for key in A:
...     if B.get(key):
...         C[key] = A[key] + B[key]
...     else:
...         C[key] = A[key]
>>> for key in B:
...     if not A.get(key):
...         C[key] = B[key]
>>> C
{'a': 1, 'b': 6, 'c': 9, 'd': 8}
————————————————
版权声明：本文为CSDN博主「杰瑞26」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Jerry_1126/article/details/86378259

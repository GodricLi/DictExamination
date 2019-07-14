# _*_ coding=utf-8 _*_

# 1.按照字典内部的年龄排序
d = [
    {'name': 'alex', 'age': 22},
    {'name': 'rain', 'age': 25},
    {'name': 'ric', 'age': 18}
]

print(sorted(d, key=lambda x: x['age']))

# 2.合并字典
a = {"A": 1, "B": 2}
b = {"C": 2, "D": 4}
a.update(b)
print(a)
print({**a, **b})

# 3.使用生成式的方式写一个字典，调换字典的key和value
dic = {'a': 1, 'b': 2}
print({v: k for k, v in dic.items()})
print(dict(zip(dic.values(), dic.keys())))

# 4.把两个元祖变为一个字典
t1 = (1, 2)
t2 = ('a', 'b')
print(dict(zip(t1, t2)))

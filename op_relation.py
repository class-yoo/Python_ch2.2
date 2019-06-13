# 객체의 대소의 비교

print(1 > 3)
print(2 > 4)

print(6 == 9)
print(6 != 9)


# 복합관계
a = 6
print(0 < a and a < 10)
print(0 < a < 10)

#수치형 이외의 객체비교

print('abcd' > 'abd')
print((1, 2, 4) < (1, 3, 1))
print([1, 3, 2] < [1, 2, 0])

#error
print(([1, 3, 2] < [1, 2, 0]))
# print([1, 3, 2] < license((1, 2, 0)))

# 동질성 비교 == 동일성비교 : is
a = 10
b = 20
c = a
d = 10
print( a== b)
print(a is b)
print(a is c)
print(a == b)
print(a == d)
print(a is d)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)
print(l1 is l2)

# 논리의 계산 순서
print([] or 'logical')
print('logical' or 'operator')
print('' or 'operator')
print('' and 'operator')
print('ok')


def f():
    print('exception!!!!!')


# if 1 + 2 < 10:
# f()
1+2 < 10 and f();
